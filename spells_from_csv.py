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
import csv
import re

#get the cvs data
def getCSVdata():
    """opens a csv file, reads it in and returns a 2 dimensional list with the data"""
    csvfile = scribus.fileDialog("spells_from_csv :: open file", "*.csv")
    #temp for development
    #csvfile = r"c:\Users\wikto\Desktop\spell_cards\bard_sample_scribus.csv"

    if csvfile != "":
        try:
            reader = csv.reader(open(csvfile, "r", encoding="UTF-8"),delimiter=';')
            datalist=[]
            for row in reader:
                rowlist=[]
                for col in row:
                    rowlist.append(col)
                datalist.append(rowlist)
            return datalist
        except Exception as e:
            scribus.messageBox("spells_from_csv", "Could not open file %s"%e)
    else:
        return []


def getDataInformation(list):
    """takes a 2 dimensional list object and returns the numbers of rows and cols"""
    datainfo = dict()
    datainfo["rowcount"]=len(list)
    datainfo["colcount"]= len(list[0])
    return datainfo


def replaceText(newText, object):
    scribus.selectText (0,-1, object)
    scribus.deleteText(object)
    scribus.insertText(newText, 0 ,object)


def fillTemplate(header, spellData): #...templateName?
    for i in range(0,len(header)):
        replaceText(spellData[i], header[i])

def toFilename(fileName):
    return re.sub('[^A-Za-z0-9_\-]+', '_', fileName)

def findAll(text, tag):
    out = []
    pos = text.find(tag)
    while pos != -1:
      out.append(pos)
      pos = text.find(tag, pos+1)
    return out

def handleTag(startTag, endTag, style, frame='Desc'):
    scribus.selectText(0,0,frame)
    text=scribus.getAllText(frame)

    starts = findAll(text,startTag)
    ends = findAll(text, endTag)

    for i in range (0,len(starts)):
        scribus.selectText(starts[i], ends[i]-starts[i], frame)
        scribus.setCharacterStyle(style, frame)

    temp1 = [(x,len(startTag)) for x in starts]
    temp2 = [(x,len(endTag)) for x in ends]

    toRemove = temp1+temp2
    toRemove.sort(reverse=True)

    scribus.selectText(0,0,frame)
    for (st,ln) in toRemove:
        scribus.selectText(st, ln, frame)
        scribus.deleteText(frame)


def handleBold():
    handleTag(u'<b>', u'</b>', "Boldlol")


def handleItalics():
    handleTag(u'<i>', u'</i>', "Italico")


def handleDurationOverflow():
    if len(scribus.getAllText("Duration")) > 28:
        scribus.setCharacterStyle("Spell proprty - fit", "Duration")


def replaceBr(text):
    return text.replace(u'<br>', u'\n')


def handleBr():
    frame='Desc'
    scribus.selectText(0,0,frame)
    text=scribus.getAllText(frame)
    replaceText(replaceBr(text), frame)


def main(argv):
    """This is a documentation string. Write a description of what your code
    does here. You should generally put documentation strings ("docstrings")
    on all your Python functions."""
    #########################
    #  YOUR CODE GOES HERE  #
    #########################

    if not scribus.haveDoc() > 0:
        scribus.messageBox("spells_from_csv", "No opened document.\nPlease open the template you want to fill first.")
        sys.exit()

    data = getCSVdata()
    header = data[0]
    spells = data[1:]

    # consistency check
    if len(header) != len(spells[0]):
        scribus.messageBox("spells_from_csv", "Header has different number of entries than data row.")
        sys.exit()
    
    # i=0
    # scribus.progressTotal(len(spells))
    # scribus.setRedraw(False)
    for row in spells:
        # this is tiresome
        # scribus.openDoc(r"c:\Users\wikto\Desktop\spell_cards\template_comp.sla")
        fillTemplate(header, row)
        handleBr()
        handleBold()
        handleItalics()
        handleDurationOverflow()
        scribus.saveDocAs(r"c:\Users\wikto\Desktop\spell_cards\staging\\" + toFilename(row[1]) + ".sla")
        # scribus.closeDoc()
        # i=i+1
        # scribus.progressSet(1)
        #reset style changes
        scribus.setCharacterStyle("Spell property", "Duration")
    
    scribus.progressReset()
    scribus.statusMessage("Done")
    # scribus.setRedraw(True)

def main_wrapper(argv):
    """The main_wrapper() function disables redrawing, sets a sensible generic
    status bar message, and optionally sets up the progress bar. It then runs
    the main() function. Once everything finishes it cleans up after the main()
    function, making sure everything is sane before the script terminates."""
    try:
        scribus.statusMessage("Importing .csv...")
        scribus.progressReset()
        main(argv)
    finally:
        # Exit neatly even if the script terminated with an exception,
        # so we leave the progress bar and status bar blank and make sure
        # drawing is enabled.
        # if scribus.haveDoc() > 0:
        #     scribus.setRedraw(True)
        scribus.statusMessage("")
        # scribus.progressReset()
        #reset style changes
        if scribus.haveDoc() > 0:
            scribus.setCharacterStyle("Spell property", "Duration")

# This code detects if the script is being run as a script, or imported as a module.
# It only runs main() if being run as a script. This permits you to import your script
# and control it manually for debugging.
if __name__ == '__main__':
    main_wrapper(sys.argv)
