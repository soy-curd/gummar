#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from bs4 import BeautifulSoup

def main():
  try:
    shift2utf("yamaneko.html")
  except:
    pass

  html = readFile("yamaneko.html")

  str = soupHtml(html)
  print(str)

def soupHtml(html):
  soup = BeautifulSoup(html)
  tag = soup.div

  #ここでルビをreplaceする必要がある。
  while(soup.ruby):
    tag.ruby.replace_with(tag.ruby.rb.string)
  while(soup.br):
    soup.br.decompose()
  while(soup.strong):
    soup.strong.decompose()

  str = ""
  for x in tag.div.contents:
    str = str + x

  while(tag.div):
    tag.div.replace_with(str)

  str = ""
  for x in tag.contents:
    str = str + x

  return str

def readFile(filename):
  with open(filename, 'r', encoding='utf-8') as f:
    str = f.read()
  return str

def shift2utf(filename):
  try:
    f = open(filename, 'r', encoding='shift-jis')
    str = f.read()
    f.close()

  except IOError:
    raise
  except TypeError:
    print("You maybe do this script by python2.x.")
    raise
  except UnicodeDecodeError:
    print("This file maybe utf-8 or EUC.")
    raise

  with open(filename, 'w', encoding='utf-8') as f:#default encoding is utf-8
    f.write(str)

  print("str type: ", type(str))

if __name__=="__main__":
  main()
