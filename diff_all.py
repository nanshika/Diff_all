#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python diff_all.py ori1.txt ori2.txt
from optparse import OptionParser

def diff_all(input1, input2, output):
    # 改行位置は気にせず、2つのファイルのdiffを取る
    
    f_in1 = open(input1,'r')
    f_in2 = open(input2,'r')
    f_out = open(output,'w')
    
    in1 = {}
    in2 = {}
    
    for l in f_in1:
        in1.get(l.rstrip())
        in1[l.rstrip()] = 0
    
    for l in f_in2:
        in2.get(l.rstrip())
        in2[l.rstrip()] = 0
    
    f_out.write('===ここから1ファイル目にのみ存在==='+'\n')
    print('===ここから1ファイル目にのみ存在===')
    for key in in1:
        if not key in in2 and len(key) > 0:
            print(key)
            f_out.write(key+'\n')
    
    f_out.write('===ここから2ファイル目にのみ存在==='+'\n')
    print('===ここから2ファイル目にのみ存在===')
    for key in in2:
        if not key in in1 and len(key) > 0:
            print(key)
            f_out.write(key+'\n')
    
    f_out.write('===終了==='+'\n')
    print('===終了===')
    

if __name__ == '__main__':
    usage = "%prog <input_file1> <input_file2> [<output_file>] \n"
    parser = OptionParser(usage=usage)
    (options, args) = parser.parse_args()
    
    if len(args) == 2:
        # 出力ファイルの指定がない場合
        args.append(args[0][0:-4]+'_diff-all.txt')
    
    if len(args) != 3:
        # 引数に過不足がある場合の対処
        parser.error("Check the usage and arguments!")
    
    diff_all(args[0], args[1], args[2])

