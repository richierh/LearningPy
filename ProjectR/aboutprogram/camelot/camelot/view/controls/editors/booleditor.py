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

from ....core.qt import QtGui, QtCore, Qt, QtWidgets
from .customeditor import AbstractCustomEditor
from camelot.core import constants
from camelot.core.utils import ugettext

class BoolEditor(QtWidgets.QCheckBox, AbstractCustomEditor):
    """Widget for editing a boolean field"""

    editingFinished = QtCore.qt_signal()
    
    def __init__(self,
                 parent=None,
                 minimum=constants.camelot_minint,
                 maximum=constants.camelot_maxint,
                 nullable=True,
                 field_name = 'boolean',
                 **kwargs):
        QtWidgets.QCheckBox.__init__(self, parent)
        AbstractCustomEditor.__init__(self)
        self.setObjectName( field_name )
        self._nullable = nullable
        self.clicked.connect( self._state_changed )

    def set_value(self, value):
        value = AbstractCustomEditor.set_value(self, value)
        if value:
            self.setCheckState(Qt.Checked)
        else:
            self.setCheckState(Qt.Unchecked)

    def get_value(self):
        value_loading = AbstractCustomEditor.get_value(self)
        if value_loading is not None:
            return value_loading
        state = self.checkState()
        if state==Qt.Unchecked:
            return False
        return True

    def set_field_attributes( self, editable = True, **kwargs ):
        AbstractCustomEditor.set_field_attributes( self, **kwargs )
        self.setDisabled( not editable )
        
    @QtCore.qt_slot( bool )
    def _state_changed(self, value=None):
        if not self.hasFocus():
            """
            Mac OS X's behaviour is not to move focus to a checkbox when it's
            state is changed. Therefore, the text_input_editing_finished method
            will not be called on a TextLineEditor when a checkbox is clicked
            after a text line has been changed, thus leading to a loss of the
            changes made in the text line. This issue is resolved by forcing
            the focus to the checkbox here.
            """
            self.setFocus()
        self.editingFinished.emit()

    def sizeHint(self):
        size = QtWidgets.QComboBox().sizeHint()
        return size

class TextBoolEditor(QtWidgets.QLabel, AbstractCustomEditor):
    """
    :Parameter:
        color_yes: string
            text-color of the True representation
        color_no: string
            text-color of the False representation
    """
    editingFinished = QtCore.qt_signal()
    
    def __init__(self,
                 parent=None,
                 yes="Yes",
                 no="No",
                 color_yes=None,
                 color_no=None,
                 **kwargs):
        QtWidgets.QLabel.__init__(self, parent)
        AbstractCustomEditor.__init__(self)
        self.setEnabled(False)
        self.yes = ugettext(yes)
        self.no = ugettext(no)
        self.color_yes = color_yes
        self.color_no = color_no

    def set_value(self, value):
        value = AbstractCustomEditor.set_value(self, value)
        if value:
            self.setText(self.yes)
            if self.color_yes:
                selfpalette = self.palette()
                selfpalette.setColor(QtGui.QPalette.WindowText, self.color_yes)
                self.setPalette(selfpalette)
        else:
            self.setText(self.no)
            if self.color_no:
                selfpalette = self.palette()
                selfpalette.setColor(QtGui.QPalette.WindowText, self.color_no)
                self.setPalette(selfpalette)


