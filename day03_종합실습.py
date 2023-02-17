import os
import time
import csv

now = time.localtime(time.time())
fName = "Money Book.csv"
Header = ["년/월/일", "시간", "내용", "입금", "출금", "잔액"]
bill = 0

file = open(fName, 'w', newline='')

global csvWriter
csvWriter = csv.writer(file)
csvWriter.writerow(Header)
##file.close()


def Process() :
    file = open(fName, 'a', newline = '')
    now = time.localtime(time.time())
    
    global csvWriter, purpose, mPurpose, putin, putout, bill
    nYear = ("%d-%d-%d" % (now.tm_year, now.tm_mon, now.tm_mday))
    nTime = ("%02d-%02d-%02d" % (now.tm_hour, now.tm_min, now.tm_sec))
    contents = mPurpose
    accountIn = putin
    accountOut = putout
    bill = (bill + accountIn) - accountOut
    dataList = [nYear, nTime, contents, accountIn, accountOut, bill]
    
    csvWriter.writerow(dataList)
    file.close()

def addProcess() :
    global csvWriter, purpose, mPurpose, putin, putout, bill
    


def Main() :
    while True :
        global purpose, mPurpose
        purpose = str(input("1. 전표 내용\n① 입금, ② 출금 : "))
        mPurpose = input("2. 출처를 적어주세요 : ")

        if (purpose == str(1)) or (purpose == "입금") :
            global putin, putout
            putin = int(input("입금 금액을 입력해주세요(없으면 공백) : "))
            putout = 0
            Process()

        elif purpose == '' :
            break
        
        else :
##            global putin, putout
            putin = 0
            putout = int(input("출금 금액을 입력해주세요(없으면 공백) : "))
            Process()

    

Main()
