#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def replaceBr(text):
    return text.replace('<br>', '\n')

if __name__ == '__main__':
    for line in sys.stdin:
        print(replaceBr(line), end='')
