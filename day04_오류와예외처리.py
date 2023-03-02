##inputValue = input("정수 입력 : ")
##
##if inputValue.isdigit():
##    numberValue = int(inputValue)
##
##    print("입력 + 100 = ", numberValue+100)
##else:
##    print("숫자가 아닙니다")


##inputValue = input("정수 입력 : ")
##
##try :
##     numberValue = int(inputValue)
##
##except :
##    print("오류 발생")
##
##else :
##    print("입력 + 100 = ", numberValue + 100)
##
##finally :
##    print("프로그램이 완료되었습니다")


##try :
##    file = open("test.txt","r")
##    file.close()
##
##except Exception as e:
##    print(e)
##
##print("파일 액세스 완료")


##def three_multiple():
##    try :
##        x = int(input("3의 배수를 입력하세요 : "))
##        if x % 3 != 0 :
##            raise Exception("error : 3의 배수가 아닙니다")
##        print(x)
##    except Exception as e:
##        print("예외 발생", e)
##        raise
##
##try :
##    three_multiple()
##except Exception as e:
##    print("모듈 / 함수에서 예외가 발생", e)
##    
##
##try:
##    three_multiple()
##except Exception as e:
##    print("예외가 발생했습니다\n",e)


##class Counter() :
##    def __init__(self) :
##        self.count = 0
##        
##    def reset(self) :
##        self.count = 0
##
##    def increment(self) :
##        self.count += 1
##
##    def get(self) :
##        return self.count
##
##cnt1 = Counter()
##cnt2 = Counter()
##
##cnt1.reset()
##cnt2.reset()
##
##cnt1.increment()
##print("Counter 1 Value : ",cnt1.get())


##class Student :
##    def __init__(self, name = None, age = 0):
##        self.__name = name
##        self.__age = age
##
##    def getAge(self) :
##        return self.__age
##
##    def getName(self) :
##        return self.__name
##
##    def setAge(self, age) :
##        self.__age = age
##
##    def setName(self, name) :
##        self.__name = name
##
##obj = Student("Hong", 20)
##print(obj.getName())
##print(obj.getAge())
##
##obj.setAge(32)
##obj.setName("Choi")
##
##print(obj.getName())
##print(obj.getAge())


##import math
##
##class Circle :
##    def __init__(self, radius = 1.0) :
##        self.__radius = radius
##
##    def setRadius(self, r) :
##        self.__radius = r
##
##    def getRadius(self) :
##        return self.__radius
##
##    def calcArea(self) :
##        area = math.pi * self.__radius * self.__radius
##        return area
##
##    def calcCircum(self) :
##        circum = 2.0 * math.pi * self.__radius
##        return circum
##
##c1 = Circle(10)
##
##
##print("원의 반지름 = ",c1.getRadius())
##print("원의 넓이 = ",c1.calcArea())
##print("원의 둘레 = ", c1.calcCircum())
    

##class BankAccount:
##    def __init__(self) :
##        self.__balance = 0
##
##    def withDraw(self, amount) :
##        self.__balance -= amount
##        print("출금 : %d 잔액 : %d" % (amount, self.__balance))
##        return self.__balance
##
##    def deposit(self, amount) :
##        self.__balance += amount
##        print("입금 : %d 잔액 : %d" % (amount, self.__balance))
##        return self.__balance
##
##a = BankAccount()
##a.deposit(100)
##a.withDraw(10)


##class Cat :
##    def __init__(self, name, age):
##        self.__name = name
##        self.__age = age
##
##    def setName(self, name) :
##        self.__name = name
##
##    def setAge(self, age) :
##        self.__age = age
##
##    def getName(self) :
##        return self.__name
##
##    def getAge(self) :
##        return self.__age
##
##missy = Cat("Missy", 3)
##lucky = Cat("Lucky", 5)
##
##print(missy.getName())
##print(missy.getAge())
##
##print(lucky.getName())
##print(lucky.getAge())
##
##missy.setName("missy2")
##print(missy.getName(), missy.getAge())


##class Box :
##    def __init__(self, width = 0, length = 0, height = 0) :
##        self.__width = width
##        self.__length = length
##        self.__height = height
##
##    def setWidth(self, width):
##        self.__width = width
##
##    def setLength(self, length) :
##        self.__length = length
##
##    def setHeight(self, height) :
##        self.__height = height
##
##    def getVolume(self) :
##        return self.__width * self.__length * self.__height
##
##    def __str__(self) :
##        return "(%d, %d, %d)" % (self.__width, self.__length, self.__height)
##
##box = Box(100, 100, 100)
##print(box)
##print("상자의 부피는 ", box.getVolume())


##class BankAccount:
##    def __init__(self) :
##        self.__balance = 0
##
##    def withDraw(self, amount) :
##        self.__balance -= amount
##        print("출금 : %d 잔액 : %d" % (amount, self.__balance))
##        return self.__balance
##
##    def deposit(self, amount) :
##        self.__balance += amount
##        print("입금 : %d 잔액 : %d" % (amount, self.__balance))
##        return self.__balance
##
##a = BankAccount()
##a.deposit(100)
##a.withDraw(10)


##class BusCard :
##    def __init__(self) :
##        self.__balance = 0
##
##    def withDraw(self, amount) :
##        self.__balance -= amount
##        return self.__balance
##
##    def deposit(self, amount) :
##        self.__balance += amount
##        return self.__balance
##
##
##def main() :
##    fCharge = int(input("충전금액 입력 : "))
##    bus = BusCard()
##    bus.deposit(fCharge)
##
##    count = 0
##    while True:
##        getIn = str(input("☞ 승차 하시겠습니까?(Y/N) : "))
##        if ((getIn == str("Y")) or (getIn == str("y"))) :
##            count += 1
##            print("\n<< %d 회 탑승 >>" % count)
##            change = bus.withDraw(1200)
##            print("『 잔액 』 : %d" % change)
##            print("")
##            if (change < 1200):
##                print("=== 잔액이 부족합니다 ===")
##                break
##        elif ((getIn == str("N")) or (getIn == str("n"))):
##            print("\n=== 승차 의사 없음 ===")
##            print("\n『 잔액 』 : %d" % change)
##            print("남은 탑승가능 횟수 : %d\n" % (change // 1200))
##            choice()
##            break
##        else :
##            print("\n▣ Y 혹은 N 으로 답변해주세요 ▣\n")
##            continue
##
##def choice() :
##    choice = int(input("1) 재시작\n2) 프로그램 종료 : "))
##    if choice == 1 :
##        main()
##    else : pass
##    
##main()
##print("=== 프로그램 종료 ===")
    


