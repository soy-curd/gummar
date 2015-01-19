#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import novel
import random

def main():
  #sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
  #sys.stdin = codecs.getreader('utf_8')(sys.stdin)
  print("python encoding :", sys.getdefaultencoding())

  string = "私は家を出た。外は晴れていた。公園に向かって歩いていくと、犬が猫を連れて散歩していた。"
  window = 10    #animal window
  avl = evalAnimalValue(string, window)
  printList(avl)

def evalAnimalValue(string, window):

  #add buf to string
  st = (window - 1) * "." + string + (window - 1) * "."

  #make animal list
  animalList = [st[i:i+window] for i in range(len(st))]

  #evaluate animal value
  animalValue = [countAnimal(x) for x in animalList]

  return animalValue

def countAnimal(string):

  #define animal set
  animal = {"犬", "猫", "鼠", "ねこ", "山猫", "栗", "馬", "きのこ", "山羊", "蟻", "蜂", "どんぐり", "鮭"}
  av = 0    #animal value
  for v in [string.count(x) for x in animal]:
    av += v

  return av

def countAnimalInWords(wordList):
    baseline = 50
    cost = 100

    #リストの要素を一個ずつずらしたリストを作成
    wordList2 = ["*"] + wordList
    wordList3 = ["*"] + wordList2
    wordList4 = ["*"] + wordList3
    wordList5 = ["*"] + wordList4
    wordList6 = ["*"] + wordList5
    wordList7 = ["*"] + wordList6
    wordList8 = ["*"] + wordList7
    wordList9 = ["*"] + wordList8
    wordList10 = ["*"] + wordList9

    evalWordList = []

    #zipで大きさを揃えたwordListに対して各々の先頭単語を連結して動物価を算出
    for i , x in enumerate(zip(wordList, wordList2, wordList3, wordList4, wordList5, wordList6, wordList7, wordList8, wordList9, wordList10)):
        string = ""
        for y in x:
            string += y

        evalWordList.append([wordList[i], str(cost * countAnimal(string) + random.randrange(baseline))])

    return evalWordList

def printList(list):
  for x in list:
    print("*" + "***" * x )

#output pretty print
def pp(obj):
  pp = pprint.PrettyPrinter(indent=4, width=160)
  str = pp.pformat(obj)
  return re.sub(r"\\u([0-9a-f]{4})", lambda x: unichr(int("0x"+x.group(1),16)), str)

if __name__=="__main__":
  main()
