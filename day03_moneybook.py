import os
import time
import csv

now = time.localtime(time.time())
fName = "C:\\Users\\User\Desktop\Money_Book.csv"
header = ["년 월 일", "시간", "내용", "입금", "출금", "잔액"]
bill = 0

with open(fName, 'w', newline="") as Writer :
    csvWriter = csv.writer(Writer)
    csvWriter.writerow(header)

    while True :
        now = time.localtime(time.time())

        account = input("\n▣전표 선택\n① 입금 / ② 출금 (1,2)\n[ 종료 : q ] :")

        nDate = ("%d-%d-%d" % (now.tm_year, now.tm_mon, now.tm_mday))
        nTime = ("%02d:%02d:%02d" % (now.tm_hour, now.tm_min, now.tm_sec))

        if (account == str(1)) or (account == '입금') :
            contents = input("입금 내용(ex.용돈, 알바비 ...) : ")
            inValue = int(input("금액을 입력해주세요 : "))
            outValue = 0
            bill += inValue
            
            addList = [nDate, nTime, contents, inValue, outValue, bill]

            csvWriter.writerow(addList)

        elif (account == str(2)) or (account == '출금') :
            contents = input("출금 내용 : ")
            outValue = int(input("금액을 입력해주세요 : "))
            inValue = 0
            bill -= outValue
            
            addList = [nDate, nTime, contents, inValue, outValue, bill]

            csvWriter.writerow(addList)

        else :
            break

        
