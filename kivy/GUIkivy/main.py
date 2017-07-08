#!usr/bin/env python
# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.widget import Widget


class PongGame(App):
    def __init__(self,*args):
        super(PongGame,self).__init__()
        self.pong = Widget()
        




if __name__ == '__main__':
    l =  App()
    PongGame().run()
