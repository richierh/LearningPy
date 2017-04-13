#  ============================================================================
#
#  Copyright (C) 2007-2016 Conceptive Engineering bvba.
#  www.conceptive.be / info@conceptive.be
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met:
#      * Redistributions of source code must retain the above copyright
#        notice, this list of conditions and the following disclaimer.
#      * Redistributions in binary form must reproduce the above copyright
#        notice, this list of conditions and the following disclaimer in the
#        documentation and/or other materials provided with the distribution.
#      * Neither the name of Conceptive Engineering nor the
#        names of its contributors may be used to endorse or promote products
#        derived from this software without specific prior written permission.
#  
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#  ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#  WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#  DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
#  DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#  (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
#  ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
#  ============================================================================

"""Functions and classes to use a progress dialog in combination with
a model thread"""

import logging

from camelot.core.utils import ugettext
from camelot.view.art import Icon

import six

from ...core.qt import QtGui, QtCore, QtWidgets, Qt, q_string, py_to_variant

LOGGER = logging.getLogger( 'camelot.view.controls.progress_dialog' )

class ProgressDialog(QtWidgets.QProgressDialog):
    """
A Progress Dialog, used during the :meth:`gui_run` of an action.

.. image:: /_static/controls/progress_dialog.png
    """

    progress_icon = Icon('tango/32x32/actions/appointment-new.png')

    def __init__(self, name, icon=progress_icon):
        QtWidgets.QProgressDialog.__init__( self, q_string(u''), q_string(u''), 0, 0 )
        label = QtWidgets.QLabel( six.text_type(name) )
        progress_bar = QtWidgets.QProgressBar()
        progress_bar.setObjectName('progress_bar')
        cancel_button = QtWidgets.QPushButton( ugettext('Cancel') )
        cancel_button.setObjectName( 'cancel' )
        ok_button = QtWidgets.QPushButton( ugettext('OK') )
        ok_button.setObjectName( 'ok' )
        ok_button.clicked.connect( self.accept )
        ok_button.hide()
        copy_button = QtWidgets.QPushButton( ugettext('Copy') )
        copy_button.setObjectName( 'copy' )
        copy_button.clicked.connect( self.copy_clicked )
        copy_button.hide()
        copy_button.setToolTip(ugettext('Copy details to clipboard'))
        self.setBar( progress_bar )
        self.setLabel( label )
        self.setCancelButton( cancel_button )
        self._window_title = ugettext('Please wait')
        self.setWindowTitle(self._window_title)
        # use a list view to display details, for performance reasons,
        # since this widget will not freeze in case the list of details
        # becomes long
        details = QtWidgets.QListView( parent = self )
        details.setObjectName( 'details' )
        details.hide()
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget( label )
        layout.addWidget( progress_bar )
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.setDirection( QtWidgets.QBoxLayout.RightToLeft )
        button_layout.addWidget( ok_button )
        button_layout.addWidget( cancel_button )
        button_layout.addWidget( copy_button )
        button_layout.addStretch()
        layout.addWidget( details )
        layout.addLayout( button_layout )
        self.setLayout( layout )
        # show immediately, to prevent a pop up before another window
        # opened in an action_step
        self.show() 
        #QtCore.QTimer.singleShot( 1000, self.show )

    @property
    def title(self):
        return self._window_title

    @title.setter
    def title(self, value):
        self._window_title = value
        self.setWindowTitle(value)

    # This method is overwritten,to undo the overwrite of this method
    # in QProgressDialog, as the QProgressDialog then manually relayouts
    # the dialog instead of using the normal layouts
    def resizeEvent(self, event):
        return QtWidgets.QWidget.resizeEvent(self, event)

    @QtCore.qt_slot(bool)
    def copy_clicked(self, checked):
        details = self.findChild( QtWidgets.QListView, 'details' )
        if details is None:
            return
        model = details.model()
        if model is not None:
            text = u'\n'.join([six.text_type(s) for s in model.stringList()])
            QtWidgets.QApplication.clipboard().setText(text)

    def add_detail( self, text ):
        """Add detail text to the list of details in the progress dialog
        :param text: a string
        """
        details = self.findChild( QtWidgets.QListView, 'details' )
        copy_button = self.findChild( QtWidgets.QPushButton, 'copy' )
        if copy_button is not None:
            copy_button.show()
        if details is not None:
            # a standarditem model is used, in the ideal case, the item
            # model with the real data should live in the model thread, and
            # this should only be a proxy
            if details.isHidden():
                model = QtGui.QStringListModel( parent = self )
                details.setModel( model )
                details.show()
            model = details.model()
            model.insertRow(model.rowCount())
            model.setData(model.index(model.rowCount()-1, 0),
                          py_to_variant(text),
                          Qt.DisplayRole)

    def clear_details( self ):
        """Clear the detail text"""
        details = self.findChild( QtWidgets.QListView, 'details' )
        if details is not None:
            details.hide()

    def enlarge(self):
        """ Increase the size of the dialog window """
        desktop = QtWidgets.QApplication.desktop()
        geo = desktop.availableGeometry(self)
        self.resize(geo.width() * 0.75, geo.height() * 0.75)
        frame = self.frameGeometry()
        frame.moveCenter(geo.center())
        self.move(frame.topLeft())

    def set_ok_hidden( self, hidden = True ):
        ok_button = self.findChild( QtWidgets.QPushButton, 'ok' )
        progress_bar = self.findChild(QtWidgets.QProgressBar, 'progress_bar')
        if ok_button:
            ok_button.setHidden( hidden )
            progress_bar.setHidden(not hidden)
            self.setWindowTitle(self.title if hidden else ugettext('Completed'))

    def set_cancel_hidden( self, hidden = True ):
        cancel_button = self.findChild( QtWidgets.QPushButton, 'cancel' )
        if cancel_button:
            cancel_button.setHidden( hidden )


class SplashProgress( QtWidgets.QSplashScreen ):
    """
    Wrapper around :class:`QtWidgets.QSplashScreen` to make it behave as if
    it were a progress dialog, this allows reuse of the progress related
    action steps within a splash screen.
    """
    # don't let splash screen stay on top, this might hinder
    # registration wizards or others that wait for user input
    # while camelot is starting up  

    def __init__( self, pixmap ):
        super( SplashProgress, self ).__init__(pixmap)
        # allow the splash screen to keep the application alive, even
        # if the last dialog was closed
        layout = QtWidgets.QVBoxLayout()
        progress_bar = QtWidgets.QProgressBar(parent=self)
        progress_bar.setObjectName('progress_bar')
        layout.addStretch(1)
        layout.addWidget(progress_bar)
        self.setAttribute(Qt.WA_QuitOnClose)
        self.setWindowTitle(' ')
        # support transparency
        if pixmap.mask(): self.setMask(pixmap.mask())
        self.setLayout(layout)

    def setMaximum( self, maximum ):
        progress_bar = self.findChild(QtWidgets.QProgressBar, 'progress_bar')
        progress_bar.setMaximum(maximum)

    def setValue( self, value ):
        progress_bar = self.findChild(QtWidgets.QProgressBar, 'progress_bar')
        progress_bar.setValue(value)

    def setLabelText( self, text ):
        progress_bar = self.findChild(QtWidgets.QProgressBar, 'progress_bar')
        progress_bar.setFormat(text)

    def wasCanceled( self ):
        return False

    def clear_details( self ):
        pass

    def add_detail( self, text ):
        self.setLabelText(text)

    def set_cancel_hidden( self, hidden = True ):
        pass

    def set_ok_hidden( self, hidden = True ):
        pass

    def exec_(self):
        pass

