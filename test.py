#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    print 'try...'
    r = 10 / 1
    print 'result:', r
except ZeroDivisionError, e:
    print 'except:', e
finally:
    print 'finally...'
print 'END'
