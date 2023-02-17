# ======== 함수 및 모듈활용 =========
# ★ 난수발생 ★
##import random
##
##def getNumber() :
##    return random.randrange(1, 100)
##
##for k in range(0, 20) :
##    num = getNumber()
##    print(num)
# ----------------------


# ★ 랜덤숫자 맞히기 ★
##import random
##
##x = random.randrange(1, 100)
##cnt = 0
##
##while True :
##    cnt += 1
##    value = int(input("숫자 입력 : "))
##    if value > x :
##        print("정답보다 큰 수입니다.\n")
##    elif value < x :
##        print("정답보다 작은 수입니다.\n")
##    else :
##        print("\n★ 축하합니다 ★\n== 정답입니다 ==")
##        print(f"[ 시도횟수 : {cnt} ]")
##        break
# ----------------------


# ★ time module ★
import time

for _ in range(10) :
    now = time.localtime()
    print("%d-%d-%d %d:%d:%d" %(now.tm_year, now.tm_mon, now.tm_mday,
                                now.tm_hour, now.tm_min, now.tm_sec))
    time.sleep(1)
