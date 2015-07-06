#!/usr/bin/python
# -*- coding: utf-8 -*-
# 설정 파일
execfile('20101703.conf')

from boto.s3.connection import S3Connection
myBucket = S3Connection().get_bucket('sgcs15spproj6tokyo') # s3의 bucket가져오기

from boto.dynamodb2.table import Table
myTable = Table('sp20101703_proj6')    # dynamoDB의 Table 가져오기

for anyObject in myBucket.list():
    if 'output/part-' in anyObject.key:     # sgcs15spproj6tokyo 버켓의 output폴더에 들어가 part-로 시작하는 파일들을 가져옴
        content = myBucket.get_key(anyObject.key).get_contents_as_string()  # 내용 읽어서 words, count를 키-벨류로 테이블에 저장
        for line in content.split('\n'):    # 각 라인 별로 자름
            if line == "":          #  빈줄이면 종료
                break
            words, count = line.split('\t') # 탭으로 워드, 카운트 구분
            myTable.put_item(data={
                'words':words,
                'count':count
                })

