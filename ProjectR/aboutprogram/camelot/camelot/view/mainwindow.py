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

import logging
logger = logging.getLogger('camelot.view.mainwindow')

from ..core.qt import Qt, QtWidgets, QtCore, py_to_variant, variant_to_py

from camelot.view.controls.busy_widget import BusyWidget
from camelot.view.controls.section_widget import NavigationPane

from camelot.core.utils import ugettext as _

class MainWindow(QtWidgets.QMainWindow):
    """Main window of a Desktop Camelot application
    
    :param gui_context: an :class:`camelot.admin.action.application_action.ApplicationActionGuiContext`
        object
    :param parent: a :class:`QtWidgets.QWidget` object or :class:`None` 
    
    """

    def __init__(self, gui_context, parent=None):
        from .workspace import DesktopWorkspace
        logger.debug('initializing main window')
        QtWidgets.QMainWindow.__init__(self, parent)

        self.toolbars = []
        self.nav_pane = None
        self.app_admin = gui_context.admin.get_application_admin()
        
        logger.debug('setting up workspace')
        self.gui_context = gui_context
        self.workspace = DesktopWorkspace( self.app_admin, self )
        self.gui_context.workspace = self.workspace

        logger.debug('setting child windows dictionary')

        logger.debug('setting central widget to our workspace')
        self.setCentralWidget( self.workspace )

        self.workspace.change_view_mode_signal.connect( self.change_view_mode )
        self.workspace.last_view_closed_signal.connect( self.unmaximize_view )
        self.workspace.view_activated_signal.connect( self.view_activated )

        logger.debug('reading saved settings')
        self.read_settings()

        logger.debug('initialization complete')
        
    @QtCore.qt_slot()
    def unmaximize_view( self ):
        """Show the navigation pane and the menu bar if they exist """
        if self.navpane:
            self.navpane.show()
        if self.menuBar():
            self.menuBar().show()

    @QtCore.qt_slot()
    def change_view_mode( self ):
        """Switch between hidden or shown menubar and navigation pane"""
        if self.menuBar().isHidden():
            if self.navpane:
                self.navpane.show()
            self.menuBar().show()
        else:
            if self.navpane:
                self.navpane.hide()
            self.menuBar().hide()

    def read_settings( self ):
        """Restore the geometry of the main window to its last saved state"""
        settings = QtCore.QSettings()
        geometry = variant_to_py( settings.value('geometry') )
        if geometry:
            self.restoreGeometry( geometry )

    def write_settings(self):
        """Store the current geometry of the main window"""
        logger.debug('writing application settings')
        settings = QtCore.QSettings()
        settings.setValue('geometry', py_to_variant(self.saveGeometry()))
        logger.debug('settings written')

    @QtCore.qt_slot( object )
    def set_main_menu( self, main_menu ):
        """Set the main menu
        :param main_menu: a list of :class:`camelot.admin.menu.Menu` objects,
            as returned by the :meth:`camelot.admin.application_admin.ApplicationAdmin.get_main_menu`
            method.
        """
        from camelot.view.controls.action_widget import ActionAction
        if main_menu == None:
            return
        menu_bar = self.menuBar()
        for menu in main_menu:
            menu_bar.addMenu( menu.render( self.gui_context, menu_bar ) )
        for qaction in menu_bar.findChildren( ActionAction ):
            qaction.triggered.connect( self.action_triggered )

    def get_gui_context( self ):
        """Get the :class:`GuiContext` of the active view in the mainwindow,
        or the :class:`GuiContext` of the application.

        :return: a :class:`camelot.admin.action.base.GuiContext`
        """
        active_view = self.gui_context.workspace.active_view()
        if active_view:
            return active_view.gui_context
        return self.gui_context
        
    @QtCore.qt_slot( object, object )
    def set_toolbar_actions( self, toolbar_area, toolbar_actions ):
        """Set the toolbar for a specific area
        :param toolbar_area: the area on which to put the toolbar, from
            :class:`Qt.LeftToolBarArea` through :class:`Qt.BottomToolBarArea`
        :param toolbar_actions: a list of :class:`camelot.admin.action..base.Action` objects,
            as returned by the :meth:`camelot.admin.application_admin.ApplicationAdmin.get_toolbar_actions`
            method.
        """
        from camelot.view.controls.action_widget import ActionAction
        if toolbar_actions != None:
            #
            # gather menu bar actions to prevent duplication of QActions
            #
            qactions = dict()
            menu_bar = self.menuBar()
            if menu_bar:
                for qaction in menu_bar.findChildren( ActionAction ):
                    qactions[qaction.action] = qaction
            toolbar = QtWidgets.QToolBar( _('Toolbar') )
            self.addToolBar( toolbar_area, toolbar )
            toolbar.setObjectName( 'MainWindowToolBar_%i'%toolbar_area )
            toolbar.setMovable( False )
            toolbar.setFloatable( False )
            for action in toolbar_actions:
                qaction = qactions.get( action, None )
                if qaction != None:
                    # the action already exists in the menu
                    toolbar.addAction( qaction )
                if qaction == None:
                    rendered = action.render( self.gui_context, toolbar )
                    # both QWidgets and QActions can be put in a toolbar
                    if isinstance(rendered, QtWidgets.QWidget):
                        toolbar.addWidget(rendered)
                    elif isinstance(rendered, QtWidgets.QAction):
                        rendered.triggered.connect( self.action_triggered )
                        toolbar.addAction( rendered )
            self.toolbars.append( toolbar )
            toolbar.addWidget( BusyWidget() )

    @QtCore.qt_slot( object )
    def set_hidden_actions( self, hidden_actions ):
        from camelot.view.controls.action_widget import ActionAction
        for action in hidden_actions:
            action_action = ActionAction( action, self.gui_context, self )
            action_action.triggered.connect( self.action_triggered )
            self.addAction( action_action )
        
    @QtCore.qt_slot()
    def view_activated( self ):
        """Update the state of the actions when the active tab in the
        desktop widget has changed"""
        from camelot.view.model_thread import post
        from camelot.view.controls.action_widget import ActionAction
        gui_context = self.get_gui_context()
        model_context = gui_context.create_model_context()
        for toolbar in self.toolbars:
            for qaction in toolbar.actions():
                if isinstance( qaction, ActionAction ):
                    post( qaction.action.get_state,
                          qaction.set_state,
                          args = ( model_context, ) )
        menu_bar = self.menuBar()
        if menu_bar:
            for qaction in menu_bar.findChildren( ActionAction ):
                post( qaction.action.get_state,
                      qaction.set_state,
                      args = ( model_context, ) )
        
    @QtCore.qt_slot( bool )
    def action_triggered( self, _checked = False ):
        """Execute an action that was triggered somewhere in the main window,
        such as the toolbar or the main menu"""
        action_action = self.sender()
        gui_context = self.get_gui_context()
        action_action.action.gui_run( gui_context )
        
    @QtCore.qt_slot( object )
    def set_sections( self, sections ):
        """Set the sections of the navigation pane
        :param main_menu: a list of :class:`camelot.admin.section.Section` objects,
            as returned by the :meth:`camelot.admin.application_admin.ApplicationAdmin.get_sections`
            method.
        """
        if sections != None:
            self.navpane = NavigationPane(
                workspace=self.workspace,
                parent=self
            )
            self.addDockWidget( Qt.LeftDockWidgetArea, self.navpane )
            self.navpane.set_sections(sections)
        else:
            self.navpane = None

    def closeEvent( self, event ):
        from camelot.view.model_thread import get_model_thread
        model_thread = get_model_thread()
        self.workspace.close_all_views()
        self.write_settings()
        logger.info( 'closing mainwindow' )
        model_thread.stop()
        super( MainWindow, self ).closeEvent( event )
        QtCore.QCoreApplication.exit(0)

