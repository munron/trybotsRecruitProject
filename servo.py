# -*- coding: utf-8 -*-
import json
import sys

text = open('setting.txt').read()
arg=sys.argv

print text
print arg
print u'引数 '+str(len(arg))
parameter=json.loads(text)
print " "


if arg[1]=="-forward" :
  print parameter['dive_head']
  print parameter['dive_tail']
  print parameter['dive_foot']



if arg[1]=="-left" :
  print parameter['left_head']
  print parameter['left_tail']
  print parameter['left_foot']


if arg[1]=="-dive" :
  print parameter['dive_head']
  print parameter['dive_tail']
  print parameter['dive_foot']

if arg[1]=="-right" :
  print parameter['right_head']
  print parameter['right_tail']
  print parameter['right_foot']


