# ======= FILE ========
# ★ file write ★
##outFile = open("data.txt", "w")
##
##while True :
##    outStr = input("내용 입력 : ")
##    if outStr != "" :
##        outFile.writelines(outStr + "\n")
##    else :
##        break
##
##outFile.close()
##print("파일 생성 완료")
#------------------------



# ★ file read ★
##inFile = open("data.txt", "r")

# == 1번 방식 ==
##inStr = inFile.readline()
##print(inStr)
##
##inStr = inFile.readline()
##print(inStr)

# == 2번 방식 ==
##while True :
##    inStr = inFile.readline()
##    if inStr == "" :
##        break
##    print(inStr)

# == 3번 방식 ==
##inStr = inFile.readline()
##print(inStr)
##for k in inStr :
##    print(k)

##inFile.close()


# ★ os path 활용 ★
# :: 파일이 경로에 있는지 확인 후 파일 열기
##import os
##
##inFile = None
##fName, inList, inStr = "", [], ""
##
##fName = input("파일명 입력 : ")
##
##if os.path.exists(fName) :
##    inFile = open(fName, "r")
##
##    inList = inFile.readlines()
##    for inStr in inList :
##        print(inStr, end="")
##
##    inFile.close()
##else :
##    print("%s 파일은 없는 파일입니다" %fName)


# :: 파일 복사하기
##import os
##
##inFile, outFile = None, None
##inFileName, outFileName = "", ""
##inList, inStr = [], ""
##
##inFileName = input("입력 파일명 : ")
##outFileName = input("출력 파일명 : ")
##
##if os.path.exists(inFileName) :
##    inFile = open(inFileName, "r")
##    outFile = open(outFileName, "w")
##
##    inList = inFile.readlines()
##    for inStr in inList :
##        outFile.writelines(inStr)
##
##    inFile.close()
##    outFile.close()
##    print("%s -> %s" % (inFileName, outFileName))
##
##else :
##    print("%s 파일이 없습니다" % (inFileName))


# :: 파일 삭제하기
##import os
##
##delFile = input("삭제할 파일명 : ")
##
##if os.path.exists(delFile) :
##    os.remove(delFile)
##    print("%s 파일을 삭제했습니다" % delFile)
##
##else :
##    print("%s 파일이 존재하지 않습니다" % delFile)


# :: 로그 파일 생성
##import os
##import time
##
##now = time.localtime(time.time())
##file_name = ("%d-%d-%d.dat" % (now.tm_year, now.tm_mon, now.tm_mday))
##
##if os.path.exists(file_name) :
##    with open(file_name, 'a') as wrFile :
##        wrFile.writelines("%d:%d:%d\n" %(now.tm_hour, now.tm_min, now.tm_sec))
##        wrFile.writelines("이미 생성중입니다"+"\n")
##        wrFile.close()
##        print("파일에 추가 하였습니다")
##
##else :
##    with open(file_name, 'w') as wrFile :
##        wrFile.writelines("%d:%d:%d\n" %(now.tm_hour, now.tm_min, now.tm_sec))
##        wrFile.writelines("새로 파일을 생성합니다" + "\n")
##        wrFile.close()
##        print("새로 파일을 생성하였습니다")


# :: 품격있는 로그 파일
##import os
##import time
##
##now = time.localtime(time.time())
##fname = ("%d-%d-%d.dat" % (now.tm_year, now.tm_mon, now.tm_mday))
##
##if os.path.exists(fname) :
##    with open(fname, 'a') as LogData :
##        print(fname + " : appending")
##        for k in range(10) :
##            nTime = ("%02d:%02d:%02d" % (now.tm_hour, now.tm_min, now.tm_sec))
##            nText = ("%d:Process" % k)
##            LogData.write(nTime + " , " + nText + "\n")
##            print("%d Processing" % k)
##            time.sleep(1)
##            now = time.localtime(time.time())
##
##else :
##    with open(fname, 'w') as LogData :
##        LogData.write("  Time  :  Data " + "\n")
##        print(fname + " : creating")
##        for k in range(10) :
##            nTime = ("%02d:%02d:%02d" % (now.tm_hour, now.tm_min, now.tm_sec))
##            nText = ("%d:Process" % k)
##            LogData.write(nTime + " , " + nText + "\n")
##            print("%d Processing" % k)
##            time.sleep(1)
##            now = time.localtime(time.time())


# ★ CSV 파일 이용하기 ★
import os
import time
import random
import csv

now = time.localtime(time.time())
fname = ("K%d-%d-%d.csv" % (now.tm_year, now.tm_mon, now.tm_mday))
cHeader = ["Time", "Temperature", "Humidity"]

with open(fname, 'w', newline = "") as LogFile :
    csvWriter = csv.writer(LogFile)
    csvWriter.writerow(cHeader)

    for k in range(10) :
        nTime = ("%02d:%02d:%02d" % (now.tm_hour, now.tm_min, now.tm_sec))
        nTemp = random.randrange(0, 30)
        nHumi = random.randrange(0, 80)
        dataList = [nTime, nTemp, nHumi]

        csvWriter.writerow(dataList)

        print("%d Processing" % (k+1))
        time.sleep(1)
        now = time.localtime(time.time())

print("Finished")
