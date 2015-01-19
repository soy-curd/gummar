#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import random
import file
import novel
import nxml
import animal

def main():
  print(os.getcwd())

  #convert shift-jis to utf-8
  try:
    file.shift2utf("yamaneko.html")
  except:
    pass

  html = file.readFile("yamaneko.html")
  htmlstr = file.soupHtml(html)

  parsedStr = novel.parseNovel(htmlstr)
  listedNovel = novel.listNovel(parsedStr)
  print(listedNovel)

  wList = []
  for x in listedNovel:
      wList.append(x[0])

  evalWordList = animal.countAnimalInWords(wList)

  feed = nxml.createXml(["surface", "feature"], evalWordList)
  nxml.writeXml("./html/xml/novel.xml", feed)

if __name__ == "__main__":
  main()
