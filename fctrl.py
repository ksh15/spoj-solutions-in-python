#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def easy_way():
  """ See http://www.swageroo.com/wordpress/spoj-problem-11-factorial-fctrl/
  for explanation.
  """

  t =  int(sys.stdin.readline())

  for i in range(0, t):
    n = int(sys.stdin.readline())
    x = 0 # solution

    while (n):
      n = n / 5
      x = x + n

    print x


if __name__ == '__main__':
  easy_way()
