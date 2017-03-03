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

from ....core.utils import ugettext
from ....core.qt import QtGui, QtCore, QtWidgets, Qt
from .customeditor import CustomEditor

class ColorEditor(CustomEditor):
    """
    This editor alows the user to select a color.  When the selected color is
    completely transparent, the value of the editor will be None.
    """

    def __init__(self, parent=None, editable=True, field_name='color', **kwargs):
        CustomEditor.__init__(self, parent)
        self.setSizePolicy( QtGui.QSizePolicy.Preferred,
                            QtGui.QSizePolicy.Fixed )        
        self.setObjectName( field_name )
        layout = QtWidgets.QVBoxLayout(self)
        layout.setSpacing(0)
        layout.setContentsMargins( 0, 0, 0, 0)
        self.color_button = QtWidgets.QPushButton(parent)
        self.color_button.setMaximumSize(QtCore.QSize(20, 20))
        layout.addWidget(self.color_button)
        if editable:
            self.color_button.clicked.connect(self.buttonClicked)
        self.setLayout(layout)
        self._color = None

    def get_value(self):
        color = self.getColor()
        if color:
            value = (color.red(), color.green(), color.blue(), color.alpha())
        else:
            value = None
        return CustomEditor.get_value(self) or value

    def set_value(self, value):
        value = CustomEditor.set_value(self, value)
        if value:
            color = QtGui.QColor()
            color.setRgb(*value)
            self.setColor(color)
        else:
            self.setColor(value)

    def getColor(self):
        return self._color

    def set_enabled(self, editable=True):
        self.color_button.setEnabled(editable)

    def setColor(self, color):
        pixmap = QtGui.QPixmap(16, 16)
        if color is not None:
            pixmap.fill(color)
        else:
            pixmap.fill(Qt.transparent)
        self.color_button.setIcon(QtGui.QIcon(pixmap))
        self._color = color

    def buttonClicked(self, raised):
        options = QtGui.QColorDialog.ShowAlphaChannel
        if self._color is None:
            color = Qt.white
        else:
            color = self._color
        color = QtGui.QColorDialog.getColor(
            color, self.parent(), ugettext('Select Color'),
            options,
        )
        if color.isValid():
            # transparant colors become None
            if color.alpha() == 0:
                self.setColor(None)
            else:
                self.setColor(color)
        self.editingFinished.emit()





