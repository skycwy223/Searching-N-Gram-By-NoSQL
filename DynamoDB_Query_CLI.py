#!/usr/bin/python
# -*- coding: utf-8 -*-
execfile('20101703.conf')
from sys import stdin, stdout
from boto.dynamodb2.table import Table
from boto.dynamodb2.exceptions import ItemNotFound
myTable = Table("sp20101703_proj6")    # DynamoDB의 테이블 이름

while True:
    line = stdin.readline().strip()     # 한줄 씩 입력받는다.
    if line == "":      # 빈줄이면 종료
        break

    wordList = line.split()     # 단어를 빈칸으로 자름
    if len(wordList) != 2:      # 두 단어로 되어 있지 않으면 에러
        stdout.write("You must type 2 words\n")
        continue

    pair = wordList[0] + " " + wordList[1]
    try:
        item = myTable.get_item(words = pair)   # DB에서 검사
    except ItemNotFound:
        stdout.write("0\n")                     # 없으면 0 출력
        continue

    stdout.write(str(item['count'])+"\n")      # count 출력
