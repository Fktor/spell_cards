#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys

splitRegEx = re.compile('^([^;]*;[^;]+;[^;]+;[^;]+;[^;]+;[^;]+;[^;]+;)" *\(([^\)]*)\)(.*)')
materialLine = 'Level;Name;School;Casting_time;Range;Components;Duration;Materials;Desc;Class'
noMaterialLine = 'Level;Name;School;Casting_time;Range;Components;Duration;Desc;Class'

if __name__ == '__main__':
    materialComponentSpells = []
    noMaterialComponentSpells = []
    for line in sys.stdin:
        m = splitRegEx.match(line) 
        if m:
            materialComponentSpells.append('{0}"{1}";"{2}'.format(m.group(1), m.group(2), m.group(3)))
        else:
            noMaterialComponentSpells.append (line)

    print(materialLine)
    for l in materialComponentSpells:
        print(l)
    print(noMaterialLine)
    for l in noMaterialComponentSpells:
        print(l, end='')
