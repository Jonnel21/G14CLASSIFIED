from __future__ import division, print_function, unicode_literals

from pyglet import font
from pyglet.app import exit

from cocos.director import director
from cocos.menu import Menu, MenuItem, fixedPositionMenuLayout
from cocos.menu import shake, shake_back
from cocos.scene import Scene
from cocos.layer import ColorLayer

# This code is so you can run the samples without installing the package
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
#

testinfo = "s, q"
tags = "menu, layout_strategy, fixedPositionMenuLayout"


class MainMenu(Menu):
    def __init__(self):
        super(MainMenu, self).__init__("COOL GAME")
        items = [
            ( MenuItem('New Game', self.on_quit ) ),
            ( MenuItem('Load', self.on_quit ) ),
            ( MenuItem('Settings', self.on_quit ) ),
            ( MenuItem('High Scores', self.on_quit ) ),
        ]
        self.create_menu(items, selected_effect=shake(),
                          unselected_effect=shake_back(),
                          layout_strategy=fixedPositionMenuLayout(
                            [(450, 300), (130, 200), (200, 100), (400, 50)]))

    def on_quit(self):
        exit()


class BackgroundMenu(ColorLayer):
    def __init__(self):
        super(BackgroundMenu, self).__init__(64, 64, 224, 225)


def main():
    font.add_directory('.')
    director.init(resizable=True)

    # set Scene to a variable
    scene1 = Scene(MainMenu())
    # add ColorLayer to scene variable
    scene1.add(BackgroundMenu())
    # run scene1 variable
    director.run(scene1)


if __name__ == '__main__':
    main()
