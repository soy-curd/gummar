#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
This script is gummar_test.
'''

import unittest
import gummar
import file

class TestGummar(unittest.TestCase):
  def setUp(self):
    pass

  def test_shift2utf_None(self):
    #self.assertRaises(TypeError, file.utf2shift(None))
    # -> The  sentence is not true,
    #because the function raise error before evaluate.
    self.assertRaises(TypeError, file.utf2shift, (None))

  def test_shift2utf_hoge(self):
    # There is no "hoge.file".
    self.assertRaises(IOError, file.utf2shift, ("hoge.file"))

if __name__ == "__main__":
  unittest.main()
