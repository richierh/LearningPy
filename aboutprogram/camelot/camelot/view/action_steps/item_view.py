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

"""
Various ``ActionStep`` subclasses that manipulate the `item_view` of 
the `ListActionGuiContext`.
"""

from sqlalchemy.orm import Query

from ...admin.action.base import ActionStep
from ...core.qt import Qt
from ...view.proxy.collection_proxy import CollectionProxy
from ...view.proxy.queryproxy import QueryTableProxy
from ..workspace import show_top_level


class Sort( ActionStep ):
    
    def __init__( self, column, order = Qt.AscendingOrder ):
        """Sort the items in the item view ( list, table or tree )
        
        :param column: the index of the column on which to sort
        :param order: a :class:`Qt.SortOrder`
        """
        self.column = column
        self.order = order
        
    def gui_run( self, gui_context ):
        if gui_context.item_view != None:
            model = gui_context.item_view.model()
            model.sort( self.column, self.order )

class UpdateTableView( ActionStep ):
    """Change the admin and or value of an existing table view
    
    :param admin: an `camelot.admin.object_admin.ObjectAdmin` instance
    :param value: a list of objects or a query
    
    """

    def __init__( self, admin, value ):
        self.admin = admin
        self.value = value
        self.title = admin.get_verbose_name_plural()
        if isinstance(value, list):
            self.proxy = CollectionProxy
        elif isinstance(value, Query):
            self.proxy = QueryTableProxy
        else:
            raise Exception('Unhandled value type : {0}'.format(type(value)))
        self.filters = admin.get_filters()
        self.list_actions = admin.get_list_actions()
        self.columns = self.admin.get_columns()
    
    def update_table_view(self, table_view):
        table_view.set_admin(self.admin)
        model = table_view.get_model()
        model.set_columns(self.columns)
        table_view.set_columns(self.columns)
        # filters can have default values, so they need to be set before
        # the value is set
        table_view.set_filters(self.filters)
        table_view.set_value(self.value)
        table_view.set_list_actions(self.list_actions)

    def gui_run(self, gui_context):
        self.update_table_view(gui_context.view)
        gui_context.view.change_title(self.title)

class OpenTableView( UpdateTableView ):
    """Open a new table view in the workspace.
    
    :param admin: an `camelot.admin.object_admin.ObjectAdmin` instance
    :param value: a list of objects or a query

    .. attribute:: title
        the title of the the new view
        
    .. attribute:: subclasses
        a tree of subclasses to be displayed on the left of the

    .. attribute:: new_tab
        open the view in a new tab instead of the current tab
        
    """
    
    def __init__( self, admin, value ):
        super(OpenTableView, self).__init__(admin, value)
        self.subclasses = admin.get_subclass_tree()
        self.search_text = ''
        self.new_tab = False

    def render(self, gui_context):
        from camelot.view.controls.tableview import TableView
        table_view = TableView(gui_context, 
                               self.admin, 
                               self.search_text,
                               proxy = self.proxy)
        table_view.set_subclass_tree(self.subclasses)
        self.update_table_view(table_view)
        return table_view
        
    def gui_run( self, gui_context ):
        table_view = self.render(gui_context)
        if gui_context.workspace is not None:
            if self.new_tab == True:
                gui_context.workspace.add_view(table_view)
            else:
                gui_context.workspace.set_view(table_view)
        else:
            show_top_level(table_view, None)
        table_view.change_title(self.title)
        table_view.setFocus(Qt.PopupFocusReason)


class ClearSelection(ActionStep):
    """Deselect all selected items."""

    def gui_run(self, gui_context):
        if gui_context.item_view is not None:
            gui_context.item_view.clearSelection()

