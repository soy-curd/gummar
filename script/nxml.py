#!/usr/bin/python3
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as etree

def main():
  print("hello gummar.")
  xml = createXml(["surface", "feature"], [["spam", "noun"], ["python", "lang"]])
  print(xml)

def createXml(tag, data):
  # tag = [tag1, tag2, ... tagn]
  # data = [[data1, data2, ... tadan], ... ]

  feed = etree.Element("novel")
  print(feed)
  for x in data:
    c = etree.SubElement(feed, "word")
    for i , y in enumerate(x):
      cc = etree.SubElement(c, tag[i])
      print(y)
      cc.text = y

#  print(etree.tostring(feed))
  return feed

def writeXml(filename, feed):
  etree.ElementTree(feed).write(filename, encoding='utf-8', xml_declaration=True)

if __name__ == "__main__":
  main()
