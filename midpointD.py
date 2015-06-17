#!/usr/bin/python
# -*- coding: utf-8 -*-

##############################################################################
# #
# By cadian42
# #
##############################################################################

import pyglet
from pyglet import window
import random
from argparse import ArgumentParser

class Window(pyglet.window.Window):

    def __init__(self, smoothness):

        window.Window.__init__(self, 1200, 500)
        #points initiaux
        self.points = [(0, 250), (1200, 250)]

        self.currentIteration = 0
        self.currentDisplacement = 100
        self.smoothness = -1 * smoothness

    #affiche la courbe
    def draw(self):
        self.clear()
        pyglet.gl.glColor4f(1., 1., 1., 1.)
        for i in range(len(self.points)-1):
           pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2i', (self.points[i][0], self.points[i][1], self.points[i+1][0], self.points[i+1][1])))

    #calcule le midpoint pour tout le tableau
    def iterate(self):
        for i in range(len(self.points)-1):
            newX = int((self.points[i*2][0] + self.points[(i*2)+1][0])/2)
            newY = int((self.points[i*2][1] + self.points[(i*2)+1][1])/2 + (random.random()-0.5)*2*self.currentDisplacement)
            self.points.insert((i*2)+1,(newX, newY))
        self.currentIteration += 1
        self.currentDisplacement *= pow(2, self.smoothness)

    #lance l'affichage et itère le bon nombre de fois
    def loop(self, numberOfIteration):
        while not self.has_exit:
            self.dispatch_events()

            if self.currentIteration < numberOfIteration:
                self.iterate()

            self.draw()
            #update la fenêtre
            self.flip()


def main():
    parser = ArgumentParser()
    parser.add_argument("-s", action="store", dest="smoothness", default=0.7)
    parser.add_argument("-n", action="store", dest="numberOfIteration", default=7)
    args = parser.parse_args()

    myWin = Window(float (args.smoothness))
    myWin.loop(int (args.numberOfIteration))


if __name__ == '__main__':
    main()
