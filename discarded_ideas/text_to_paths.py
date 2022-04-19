#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ABOUT THIS SCRIPT:

Convert all text fields to paths (work in progress)

############################

LICENSE:
Public domain
"""

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
   
def main():
    """This is a documentation string. Write a description of what your code
    does here. You should generally put documentation strings ("docstrings")
    on all your Python functions."""
    #########################
    #  YOUR CODE GOES HERE  #
    #########################
    #scribus.getAllObjects()
    textList = ['SampleText1', 'SampleText2']

    scribus.setRedraw(False)

    for t in textList:
        scribus.traceText(t)
    scribus.docChanged(True)
    scribus.setRedraw(True)

if __name__ == '__main__':
    if scribus.haveDoc() > 0:
        main()
    else:
        scribus.messageBox("Text to path", "You need to have a document open <i>before</i> you can run this script successfully.", scribus.ICON_INFORMATION)
