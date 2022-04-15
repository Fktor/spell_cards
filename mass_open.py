#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ABOUT THIS SCRIPT:
todo
############################

LICENSE:

public domain
"""

#will use current pdf export settings
#draws on curve
#scribus.createPathText(0,0,'SampleText1','BezierTest')

#from __future__ import division
import sys

try:
    # Please do not use 'from scribus import *' . If you must use a 'from import',
    # Do so _after_ the 'import scribus' and only import the names you need, such
    # as commonly used constants.
    import scribus
except ImportError as err:
    print ("This Python script is written for the Scribus scripting interface.")
    print ("It can only be run from within Scribus.")
    sys.exit(1)

#########################
# YOUR IMPORTS GO HERE  #
#########################
import os

def main(argv):
    """This is a documentation string. Write a description of what your code
    does here. You should generally put documentation strings ("docstrings")
    on all your Python functions."""
    #########################
    #  YOUR CODE GOES HERE  #
    #########################
    
    # if not scribus.haveDoc() > 0: #do we have a doc?
    #     scribus.messageBox("spells_from_csv", "No opened document.\nPlease open one first.")
    #     sys.exit()

    baseDir = r'c:\Users\wikto\Desktop\spell_cards\staging'

    files = [ i for i in os.listdir(baseDir) if not os.path.isfile(i)]

    for f in files:
        scribus.openDoc(os.path.join (baseDir,f))

if __name__ == '__main__':
    main(sys.argv)
