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
import re


def exportPdf(fileName):
    pdf = scribus.PDFfile()
    pdf.file = (r"c:\Users\wikto\Desktop\spell_cards\output\\"+ fileName + ".pdf")
    pdf.save()


def main(argv):
    """This is a documentation string. Write a description of what your code
    does here. You should generally put documentation strings ("docstrings")
    on all your Python functions."""
    #########################
    #  YOUR CODE GOES HERE  #
    #########################

    # careful! DOES NOT SAVE DOCS

    while scribus.haveDoc() > 0:
        (baseName, _) = os.path.splitext(os.path.basename(scribus.getDocName()))
        exportPdf(baseName)
        scribus.closeDoc()


if __name__ == '__main__':
    main(sys.argv)
