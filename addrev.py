#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def main():
  n = int(sys.stdin.readline())

  for i in range(0, n):
    a, b = sys.stdin.readline().strip().split(' ')
    c = int(a[::-1]) + int(b[::-1])
    print int(c.__repr__()[::-1])


if __name__ == '__main__':
  main()
