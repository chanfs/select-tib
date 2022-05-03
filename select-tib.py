#!/usr/bin/python3
import sys,re

file1 = open(sys.argv[1],'r')
#lines = file1.readlines()
#tib = re.findall(\p{Tibetan}, lines)

#for line in lines:
for line in file1:
    # for each line in the file, a list will be returned. This list exist only during the loop
    tib = re.findall(r'[\u0f00-\u0fff]+', line)
    #if the line is empty, do not print
    if tib != []:
        #if the line is '༔', do not print
      if tib != ['༔']:
        #print(tib)
        # using list comprehension
        listToStr = ' '.join(map(str, tib))
        #listToStr = listToStr.replace('\n', ' ').replace('\r', '')
#        listToStr = listToStr.replace('\r\n', ' ')
        #listToStr_r = re.sub("\n", "A", listToStr,re.M)
        # print without newline, python 3
        print(listToStr, end =" ")
    #elif tib != ['༔']:
     # print(tib)
#print(tib)
    #tib = re.sub(r'^\u0f14', "", listToStr)
    # using list comprehension
#    listToStr = ' '.join(map(str, tib))
#    tib1 = re.sub(r'^\u0f14', "", tib)
    #listToStr_no = re.sub(r'^\s*$',"", listToStr_out, re.MULTILINE)
#    listToStr.split('\n')
#    tib1 = [line for line in listToStr.split('\n') if line.strip()]
#    listToStr1 = ' '.join(map(str, tib1))
#    print(listToStr1)
    #print(listToStr_out.rstrip("\n"))
    #removedWhitespce = re.sub(r'^\s*$', '', listToStr_out)
    #print(removedWhitespce)

