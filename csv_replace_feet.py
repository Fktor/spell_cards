#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys


def squaresFromFeet(feet):
    return round(feet/5.0)


def metersFromSquares(meters):
    return meters*1.5


expressionsToReplace= [
    re.compile('([0-9]+)(.)feet'),
    re.compile('([0-9]+)(.)foot')
    ]

def replaceImperial(text):
    for exp in expressionsToReplace:
        match = exp.search(text)
        while match:
            sq = squaresFromFeet(float(match.group(1)))
            met = metersFromSquares(sq)
            if met <= 0:
                metString=match.group(1) + 'ft<!!>'
            else:
                if round(met) == met:
                    metString='{0:.0f}'.format(met)
                else:
                    metString='{0:.1f}'.format(met)
            if match.group(2) == '-':
                unitString = 'meter'
            else:
                unitString = 'meters'
            newExpression = '{0}{1}{2}({3:.0f}sq)'.format(metString, match.group(2), unitString, sq)
            text = text[:match.start()] + newExpression + text[match.end():]
            match = exp.search(text)
    return text

if __name__ == '__main__':
    for line in sys.stdin:
        print(replaceImperial(line), end='')
