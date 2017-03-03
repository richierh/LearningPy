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

from ....core.qt import QtCore, QtWidgets
from .wideeditor import WideEditor
from .customeditor import AbstractCustomEditor


class TextEditEditor(QtWidgets.QTextEdit, AbstractCustomEditor, WideEditor):

    editingFinished = QtCore.qt_signal()

    def __init__(self,
                 parent,
                 length=20,
                 editable=True,
                 field_name='text',
                 **kwargs):
        QtWidgets.QTextEdit.__init__(self, parent)
        self.setObjectName(field_name)
        AbstractCustomEditor.__init__(self)
        self.setReadOnly(not editable)

    def set_value(self, value):
        value = AbstractCustomEditor.set_value(self, value)
        if value is not None:
            self.setText(six.text_type(value))
        else:
            self.setText('')
        return value

    def get_value(self):
        val = AbstractCustomEditor.get_value(self)
        if val is not None:  # we need to distinguish between None
            return val       # and other falsy values
        return six.text_type(self.toPlainText())

    def set_enabled(self, editable=True):
        self.setEnabled(editable)

