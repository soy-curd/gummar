#!/usr/bin/python3
# -*- coding: utf-8 -*-

import MeCab
import re

def main():
  print("文学フリマ参加サークル一覧")

  #ファイル読み込み
  str = openFile("./txt/bunfuri.txt")

  #改行とタブでデータを分割
  splitedStr = str.split("\n")
  tabSplitedStr = []
  for x in splitedStr:
    tabSplitedStr.append(x.split("\t"))

  #Mecabで形態素解析
  lWords = []
  for x in tabSplitedStr:
    if len(x) >= 2:
      for y in listString(parseString(x[2])):
        lWords.append(y)

  lSurface = [x[0] for x in lWords]

  #ソートして頻度分布を取得
  Dic = {key: lSurface.count(key) for key in set(lSurface)}
  hist = [[k, v] for k, v in sorted(Dic.items(), key=lambda x:x[1], reverse=True)]

  #整形して表示
  print("|単語|出現回数|\n|----|----|")
  for x in hist:
    if x[1] > 1:
      print("|" + x[0] + "|" +  "*" * x[1] + "|")


def listString(parsedString):
  print(parsedString)
  rows = [row.split('\t') for row in parsedString.split('\n')
    if row != '' and row != 'EOS' and not("記号" in row)]
  return rows

def parseString(string):
  mecab = MeCab.Tagger("-Ochasen")
  parsedStr = mecab.parse(string)
  return parsedStr

def openFile(filename):
  try:
    f = open(filename, 'r', encoding='utf-8')
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

  print("str type: ", type(str))

  return str

if __name__ == "__main__":
  main()
