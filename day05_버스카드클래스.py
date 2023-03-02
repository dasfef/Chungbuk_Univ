class BusCard :
    def __init__(self) :
        self.__balance = 0

    def withDraw(self, amount) :
        self.__balance -= amount
        return self.__balance

    def deposit(self, amount) :
        self.__balance += amount
        return self.__balance


def main() :
    fCharge = int(input("충전금액 입력 : "))
    bus = BusCard()
    bus.deposit(fCharge)

    count = 0
    while True:
        getIn = str(input("☞ 승차 하시겠습니까?(Y/N) : "))
        if ((getIn == str("Y")) or (getIn == str("y"))) :
            count += 1
            print("\n<< %d 회 탑승 >>" % count)
            change = bus.withDraw(1200)
            print("『 잔액 』 : %d" % change)
            print("")
            if (change < 1200):
                print("=== 잔액이 부족합니다 ===")
                break
        elif ((getIn == str("N")) or (getIn == str("n"))):
            print("\n=== 승차 의사 없음 ===")
            print("\n『 잔액 』 : %d" % change)
            print("남은 탑승가능 횟수 : %d\n" % (change // 1200))
            choice()
            break
        else :
            print("\n▣ Y 혹은 N 으로 답변해주세요 ▣\n")
            continue

def choice() :
    choice = int(input("1) 재시작\n2) 프로그램 종료 : "))
    if choice == 1 :
        main()
    else : pass
    
main()
print("=== 프로그램 종료 ===")
