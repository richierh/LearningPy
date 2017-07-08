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

import six

from ....core.qt import QtGui, QtCore, Qt, QtWidgets
from camelot.core.utils import ugettext as _
from camelot.view.controls.editors import CustomEditor
from camelot.view.controls.editors.customeditor import ValueLoading
from camelot.view.controls.editors.integereditor import CustomDoubleSpinBox

class MonthsEditor(CustomEditor):
    """MonthsEditor

    composite months and years editor
    """

    def __init__(self, parent=None, editable=True, field_name='months', **kw):
        CustomEditor.__init__(self, parent)
        self.setSizePolicy( QtGui.QSizePolicy.Preferred,
                            QtGui.QSizePolicy.Fixed )        
        self.setObjectName( field_name )
        self.years_spinbox = CustomDoubleSpinBox()
        self.months_spinbox = CustomDoubleSpinBox()
        self.years_spinbox.setRange(-1, 10000)
        self.months_spinbox.setRange(-1, 12)
        self.years_spinbox.setSuffix(_(' years'))
        self.months_spinbox.setSuffix(_(' months'))
        
        self.years_spinbox.setDecimals(0)
        self.years_spinbox.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
        self.years_spinbox.setSingleStep(1)
        
        self.months_spinbox.setDecimals(0)
        self.months_spinbox.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
        self.months_spinbox.setSingleStep(1)

        self.years_spinbox.editingFinished.connect( self._spinbox_editing_finished )
        self.months_spinbox.editingFinished.connect( self._spinbox_editing_finished )
        
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.years_spinbox)
        layout.addWidget(self.months_spinbox)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

    @QtCore.qt_slot()
    def _spinbox_editing_finished(self):
        self.editingFinished.emit()
        
    def set_field_attributes(self, **kwargs):
        super(MonthsEditor, self).set_field_attributes(**kwargs)
        self.set_enabled(kwargs.get('editable', False))
        self.set_background_color(kwargs.get('background_color', None))
        self.years_spinbox.setToolTip(six.text_type(kwargs.get('tooltip') or ''))

    def set_enabled(self, editable=True):
        self.years_spinbox.setReadOnly(not editable)
        self.years_spinbox.setEnabled(editable)
        self.months_spinbox.setReadOnly(not editable)
        self.months_spinbox.setEnabled(editable)
        if not editable:
            self.years_spinbox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
            self.months_spinbox.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        else:
            self.years_spinbox.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
            self.months_spinbox.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)

    def set_value(self, value):
        # will set privates value_is_none and _value_loading
        value = CustomEditor.set_value(self, value)
        if value is None:
            self.years_spinbox.setValue(self.years_spinbox.minimum())
            self.months_spinbox.setValue(self.months_spinbox.minimum())
        else:
            # value comes as a months total
            years, months = divmod( value, 12 )
            self.years_spinbox.setValue(years)
            self.months_spinbox.setValue(months)

    def get_value(self):
        if CustomEditor.get_value(self) is ValueLoading:
            return ValueLoading
        self.years_spinbox.interpretText()
        years = int(self.years_spinbox.value())
        self.months_spinbox.interpretText()
        months = int(self.months_spinbox.value())
        years_is_none = (years == self.years_spinbox.minimum())
        months_is_none = (months == self.months_spinbox.minimum())
        if years_is_none and months_is_none:
            return None
        if years_is_none:
            years = 0
        if months_is_none:
            months = 0
        return (years * 12) + months

