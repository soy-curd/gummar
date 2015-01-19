#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import MeCab
import sys
import codecs
import re, pprint
import nltk
from nltk.corpus.reader import *
from nltk.corpus.reader.util import *
from nltk.text import Text


def main():
  #sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
  #sys.stdin = codecs.getreader('utf_8')(sys.stdin)
  print("python encoding :", sys.getdefaultencoding())

  novel = "ぐんまちゃんが走っている姿を見たのは、後にも先にもあの一度きりだ。 ぐんまちゃんはリヤドから帰ってきたばかりで、毛並みも悪く、本当に疲れて見えた。 皇居へのあいさつも辞退し、一晩中、ホテルでぐったりとしているようだった。 無論、一緒にいてあげられるあの娘はもういない。 誰かがぐんまちゃんを励まさなければならなかった。 私はホテルのフロントから、ぐんまちゃんの部屋に電話をかけた。 十回ほど呼び出し音が鳴ったが、ぐんまちゃんは電話を取らない。 半日後、私は再びぐんまちゃんを呼び出したが、 結局ぐんまちゃんは電話に出ることはなかった。 後でわかったことだが、 そのときにはもうぐんまちゃんは高崎に帰っていたのだった。 翌日youtubeに投稿された動画に、ぐんまちゃんは映っていた。 競馬場、他にも並み居るサラブレッドが雄々しく立ち並ぶ中、ぐんまちゃんは発馬機の奥にその姿を見せた。 ゲートの向こうに緑の帽子が見え隠れしている。 山盛りの人参が待つゴールを意識しているのだろうか。 しかし、芝の状態は悪くない、呼吸も落ち着いている。 ぐんまちゃんの目は輝いていた。 私はこのレースのぐんまちゃんの勝利を確信した。 ゲートが開き、そして、一頭のポニーが飛び出した。"

  parsedNovel = parseNovel(novel)
  listedNovel = listNovel(parsedNovel)
  print(pp(listedNovel))

  wordsDic = countWords(listedNovel)
  #print(wordsDic)
  sortedList = sortDicValue(wordsDic)
  print(pp(sortedList))

def sortDicValue(Dic):
  return [[k, v] for k, v in sorted(Dic.items(), key=lambda x:x[1], reverse=True)]

#return dictionary of count of words
def countWords(lWords):
  #abstract surface of word
  lSurface = [x[0] for x in lWords]
  return {key: lSurface.count(key) for key in set(lSurface)}

#output pretty print
def pp(obj):
  pp = pprint.PrettyPrinter(indent=4, width=160)
  str = pp.pformat(obj)
  return re.sub(r"\\u([0-9a-f]{4})", lambda x: unichr(int("0x"+x.group(1),16)), str)

#change Novel to GIF
def visualizeNovel(nobel):
  pass

#tfidf

def listNovel(parsedNovel):
    rows = [row.split('\t') for row in parsedNovel.split('\n') if row != '' and row != 'EOS']
    return rows
    #[row[0] for row in rows if row[1].split(',')[0]=='名詞']

def parseNovel(novel):
  #select tagger
  mecab = MeCab.Tagger("-Ochasen")
  parsedNovel = mecab.parse(novel)
  return parsedNovel

if __name__=="__main__":
  main()
