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

"""Convenience functions and classes to present views to the user"""

import six

import logging
logger = logging.getLogger('camelot.view.workspace')

from ..core import constants
from ..core.qt import QtCore, QtGui, QtWidgets, Qt
from camelot.admin.action import ApplicationActionGuiContext
from camelot.core.utils import ugettext as _
from camelot.view.model_thread import object_thread, post
from camelot.view.controls.action_widget import ( ActionLabel, 
                                                  HOVER_ANIMATION_DISTANCE,
                                                  NOTIFICATION_ANIMATION_DISTANCE )
from .controls.view import AbstractView

class DesktopBackground(AbstractView):
    """
    A custom background widget for the desktop. This widget is contained
    by the first tab ('Start' tab) of the desktop workspace.
    """
    
    def __init__(self, gui_context):
        super(DesktopBackground, self).__init__()
        self.gui_context = gui_context
        mainLayout = QtWidgets.QVBoxLayout()
        
        actionButtonsLayout = QtGui.QGridLayout()
        actionButtonsLayout.setObjectName('actionButtonsLayout')
        actionButtonsLayout.setContentsMargins(200, 20, 200, 20)
        
        actionButtonInfoWidget = ActionButtonInfoWidget()
        actionButtonInfoWidget.setObjectName('actionButtonInfoWidget')
                
        mainLayout.addWidget(actionButtonInfoWidget, 0, Qt.AlignCenter)
        mainLayout.addLayout(actionButtonsLayout)
        
        self.setLayout(mainLayout)
        
        # Set a white background color
        palette = self.palette()
        self.setAutoFillBackground(True)
        palette.setBrush(QtGui.QPalette.Window, Qt.white)
        self.setPalette(palette)

    def set_actions(self, actions):
        """
        :param actions: a list of Actions
        """
        #
        # Remove old actions
        #
        for actionButton in self.findChildren(ActionLabel):
            actionButton.deleteLater()
        
        # Make sure that the action buttons aren't visually split
        # up in two rows when there are e.g. only 3 of them.
        # So:
        #  <= 3 action buttons: 1 row and 1, 2 or 3 columns;
        #  >= 4 action buttons: 2 rows and 2, 3, 4 or 5 columns.
        actionButtonsLayoutMaxItemsPerRowCount = max((len(actions) + 1) / 2, 3)
        
        actionButtonsLayout = self.findChild(QtGui.QGridLayout, 'actionButtonsLayout')
        if actionButtonsLayout is not None:
            for position in range(0, min( len(actions), actionButtonsLayoutMaxItemsPerRowCount) ):
                action = actions[position]
                actionButton = action.render( self.gui_context, self )
                actionButton.entered.connect(self.onActionButtonEntered)
                actionButton.left.connect(self.onActionButtonLeft)
                actionButton.setInteractive(True)
                actionButtonsLayout.addWidget(ActionButtonContainer(actionButton), 0, position, Qt.AlignCenter)

            for position in range(actionButtonsLayoutMaxItemsPerRowCount, len(actions)):
                action = actions[position]
                actionButton = action.render( self.gui_context, self )
                actionButton.entered.connect(self.onActionButtonEntered)
                actionButton.left.connect(self.onActionButtonLeft)
                actionButton.setInteractive(True)
                actionButtonsLayout.addWidget(ActionButtonContainer(actionButton), 1, position % actionButtonsLayoutMaxItemsPerRowCount, Qt.AlignCenter)
            
    @QtCore.qt_slot()
    def onActionButtonEntered(self):
        actionButton = self.sender()
        actionButtonInfoWidget = self.findChild(QtWidgets.QWidget, 'actionButtonInfoWidget')
        if actionButtonInfoWidget is not None:
            # @todo : get state should be called with a model context as first
            #         argument
            post( actionButton.action.get_state,
                  actionButtonInfoWidget.setInfoFromState,
                  args = (None,) )
       
    @QtCore.qt_slot()
    def onActionButtonLeft(self):
        actionButtonInfoWidget = self.findChild(QtWidgets.QWidget, 'actionButtonInfoWidget')
        if actionButtonInfoWidget is not None:
            actionButtonInfoWidget.resetInfo()
        
    # This custom event handler makes sure that the action buttons aren't
    # drawn in the wrong position on this widget after the screen has been
    # e.g. maximized or resized by using the window handles.
    
    def resizeEvent(self, event):
        for actionButton in self.findChildren(ActionLabel):
            actionButton.resetLayout()

        event.ignore()

    # This slot is called after the navpane's animation has finished. During 
    # this sliding animation, all action buttons are linearly moved to the right,
    # giving the user a small window in which he or she may cause visual problems
    # by already hovering the action buttons. This switch assures that the user 
    # cannot perform mouse interaction with the action buttons until they're
    # static.
    @QtCore.qt_slot()
    def makeInteractive(self, interactive=True):
        for actionButton in self.findChildren(ActionLabel):
            actionButton.setInteractive(interactive)
            
    def refresh(self):
        pass

class ActionButtonContainer(QtWidgets.QWidget):
    def __init__(self, actionButton, parent = None):
        super(ActionButtonContainer, self).__init__(parent)
        
        mainLayout = QtWidgets.QHBoxLayout()
        # Set some margins to avoid the ActionButton being visually clipped
        # when performing the hoverAnimation.
        mainLayout.setContentsMargins(2*NOTIFICATION_ANIMATION_DISTANCE,
                                      2*HOVER_ANIMATION_DISTANCE,
                                      2*NOTIFICATION_ANIMATION_DISTANCE,
                                      2*HOVER_ANIMATION_DISTANCE)
        mainLayout.addWidget(actionButton)
        self.setLayout(mainLayout)
        
    def mousePressEvent(self, event):
        # Send this event to the ActionButton that is contained by this widget.
        self.layout().itemAt(0).widget().onContainerMousePressEvent(event)
            
class ActionButtonInfoWidget(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super(ActionButtonInfoWidget, self).__init__(parent)
        
        mainLayout = QtWidgets.QHBoxLayout()
        
        font = self.font()
        font.setPointSize(14)
        
        actionNameLabel = QtWidgets.QLabel()
        actionNameLabel.setFont(font)
        actionNameLabel.setFixedSize(250, 50)
        actionNameLabel.setAlignment(Qt.AlignCenter)
        actionNameLabel.setObjectName('actionNameLabel')
        
        actionDescriptionLabel = QtWidgets.QLabel()
        actionDescriptionLabel.setFixedSize(250, 200)
        actionDescriptionLabel.setObjectName('actionDescriptionLabel')

        mainLayout.addWidget(actionNameLabel, 0, Qt.AlignVCenter)
        mainLayout.addWidget(actionDescriptionLabel)

        self.setLayout(mainLayout)

    @QtCore.qt_slot( object )
    def setInfoFromState(self, state):
        actionNameLabel = self.findChild(QtWidgets.QLabel, 'actionNameLabel')
        if actionNameLabel is not None:
            actionNameLabel.setText( six.text_type( state.verbose_name ) )
        
        actionDescriptionLabel = self.findChild(QtWidgets.QLabel, 'actionDescriptionLabel')
        if actionDescriptionLabel is not None:
            tooltip = six.text_type( state.tooltip or '' )
            actionDescriptionLabel.setText(tooltip)
            if tooltip:
                # Do not use show() or hide() in this case, since it will
                # cause the actionButtons to be drawn on the wrong position.
                # Instead, just set the width of the widget to either 0 or 250.
                actionDescriptionLabel.setFixedWidth(250)
            else:
                actionDescriptionLabel.setFixedWidth(0)
            
    def resetInfo(self):
        actionNameLabel = self.findChild(QtWidgets.QLabel, 'actionNameLabel')
        if actionNameLabel is not None:
            actionNameLabel.setText('')
        
        actionDescriptionLabel = self.findChild(QtWidgets.QLabel, 'actionDescriptionLabel')
        if actionDescriptionLabel is not None:
            actionDescriptionLabel.setText('')
    
class DesktopTabbar(QtWidgets.QTabBar):

    change_view_mode_signal = QtCore.qt_signal()
    
    def mouseDoubleClickEvent(self, event):
        self.change_view_mode_signal.emit()
        event.accept()
        
    def tabSizeHint(self, index):
        originalSizeHint = super(DesktopTabbar, self).tabSizeHint(index)
        minimumWidth = max(160, originalSizeHint.width())
        
        return QtCore.QSize(minimumWidth, originalSizeHint.height())

class DesktopWorkspace(QtWidgets.QWidget):
    """
    A tab based workspace that can be used by views to display themselves.
    
    In essence this is a wrapper around QTabWidget to do some initial setup
    and provide it with a background widget.
    This was originallly implemented using the QMdiArea, but the QMdiArea has 
    too many drawbacks, like not being able to add close buttons to the tabs
    in a decent way.

    .. attribute:: background

    The widget class to be used as the view for the uncloseable 'Start' tab.
    """

    view_activated_signal = QtCore.qt_signal(QtWidgets.QWidget)
    change_view_mode_signal = QtCore.qt_signal()
    last_view_closed_signal = QtCore.qt_signal()

    def __init__(self, app_admin, parent):
        super(DesktopWorkspace, self).__init__(parent)
        self.gui_context = ApplicationActionGuiContext()
        self.gui_context.admin = app_admin
        self.gui_context.workspace = self
        self._app_admin = app_admin
        
        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Setup the tab widget
        self._tab_widget = QtWidgets.QTabWidget( self )
        tab_bar = DesktopTabbar(self._tab_widget)
        tab_bar.setToolTip(_('Double click to (un)maximize'))
        tab_bar.change_view_mode_signal.connect(self._change_view_mode)
        self._tab_widget.setTabBar(tab_bar)
        self._tab_widget.setDocumentMode(True)
        self._tab_widget.setTabsClosable(True)
        self._tab_widget.tabCloseRequested.connect(self._tab_close_request)
        self._tab_widget.currentChanged.connect(self._tab_changed)
        layout.addWidget(self._tab_widget)
        self.setLayout(layout)

    @QtCore.qt_slot()
    def _change_view_mode(self):
        self.change_view_mode_signal.emit()
        
    @QtCore.qt_slot(int)
    def _tab_close_request(self, index):
        """
        Handle the request for the removal of a tab at index.
        
        Note that only at-runtime added tabs are being closed, implying
        the immortality of the 'Start' tab.
        """
        view = self._tab_widget.widget(index)
        if view is not None:
            # it's not enough to simply remove the tab, because this
            # would keep the underlying view widget alive
            view.deleteLater()
            self._tab_widget.removeTab(index)

    @QtCore.qt_slot(int)
    def _tab_changed(self, _index):
        """
        The active tab has changed, emit the view_activated signal.
        """
        self.view_activated_signal.emit(self.active_view())

    def active_view(self):
        """
        :return: The currently active view or None in case of the 'Start' tab.
        """
        i = self._tab_widget.currentIndex()
        return self._tab_widget.widget(i)

    @QtCore.qt_slot(six.text_type)
    def change_title(self, new_title):
        """
        Slot to be called when the tile of a view needs to change.
        """
        sender = self.sender()
        if sender is not None:
            index = self._tab_widget.indexOf(sender)
            self._tab_widget.setTabText(index, new_title)
                
    @QtCore.qt_slot(QtGui.QIcon)
    def change_icon(self, new_icon):
        """
        Slot to be called when the icon of a view needs to change.
        """
        sender = self.sender()
        if sender is not None:
            index = self._tab_widget.indexOf(sender)
            self._tab_widget.setTabIcon(index, new_icon)

    def set_view(self, view, icon = None, title = '...'):
        """
        Remove the currently active view and replace it with a new view.
        """
        index = self._tab_widget.currentIndex()
        current_view = self._tab_widget.widget(index)
        if (current_view is None) or (current_view.close() == False):
            self.add_view(view, icon, title)
        else:
            self._tab_close_request(index)
            view.title_changed_signal.connect(self.change_title)
            view.icon_changed_signal.connect(self.change_icon)
            if icon:
                index = self._tab_widget.insertTab(index, view, icon, title)
            else:
                index = self._tab_widget.insertTab(index, view, title)
            self._tab_widget.setCurrentIndex(index)

    def add_view(self, view, icon = None, title = '...'):
        """
        Add a Widget implementing AbstractView to the workspace.
        """
        assert object_thread(self)
        view.title_changed_signal.connect(self.change_title)
        view.icon_changed_signal.connect(self.change_icon)
        if icon:
            index = self._tab_widget.addTab(view, icon, title)
        else:
            index = self._tab_widget.addTab(view, title)
        self._tab_widget.setCurrentIndex(index)

    def refresh(self):
        """Refresh all views on the desktop"""
        for i in range( self._tab_widget.count() ):
            self._tab_widget.widget(i).refresh()
            
    def close_all_views(self):
        """
        Remove all views, except the 'Start' tab, from the workspace.
        """
        # NOTE: will call removeTab until tab widget is cleared
        # but removeTab does not really delete the page objects
        #self._tab_widget.clear()
        max_index = self._tab_widget.count()
        
        while max_index > 0:
            self._tab_widget.tabCloseRequested.emit(max_index)
            max_index -= 1

top_level_windows = []

def apply_form_state(view, parent, state):
    #
    # position the new window in the center of the same screen
    # as the parent
    #
    screen = QtWidgets.QApplication.desktop().screenNumber(parent)
    geometry = QtWidgets.QApplication.desktop().availableGeometry(screen)
    if state == constants.MAXIMIZED:
        view.setWindowState(QtCore.Qt.WindowMaximized)
    elif state == constants.MINIMIZED:
        view.setWindowState(QtCore.Qt.WindowMinimized)
    elif state == constants.RIGHT:
        geometry.setLeft(geometry.center().x())
        view.resize(geometry.width(), geometry.height())
        view.move(geometry.topLeft())
    elif state == constants.LEFT:
        geometry.setRight(geometry.center().x())
        view.resize(geometry.width(), geometry.height())
        view.move(geometry.topLeft())
    else:
        point = QtCore.QPoint(geometry.x() + geometry.width()/2,
                              geometry.y() + geometry.height()/2)
        point = QtCore.QPoint(point.x()-view.width()/2,
                              point.y()-view.height()/2)
        view.move(point)

def show_top_level(view, parent, state=None):
    """Show a widget as a top level window.  If a parent window is given, the new
    window will have the same modality as the parent.
    
    :param view: the widget extend AbstractView
    :param parent: the widget with regard to which the top level
        window will be placed.
    :param state: the state of the form, 'maximized', or 'left' or 'right', ...
     """
    from camelot.view.register import register
    #
    # Register the view with reference to itself.  This will keep
    # the Python object alive as long as the Qt object is not
    # destroyed.  Hence Python will not trigger the deletion of the
    # view as long as the window is not closed
    #
    register( view, view )
    #
    # set the parent to None to avoid the window being destructed
    # once the parent gets destructed
    #
    view.setParent( None )
    view.setWindowFlags(QtCore.Qt.Window)
    #
    # Make the window title blank to prevent the something
    # like main.py or pythonw being displayed
    #
    view.setWindowTitle( u' ' )
    view.title_changed_signal.connect( view.setWindowTitle )
    view.icon_changed_signal.connect( view.setWindowIcon )
    view.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    apply_form_state(view, parent, state)

    if parent is not None:
        view.setWindowModality(parent.windowModality())
    view.show()



