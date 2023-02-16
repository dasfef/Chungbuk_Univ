# ============== find ===============
##ss = '파이썬 공부는 즐겁습니다. 물론 모든 공부가 다 재미있지는 않죠'
##print(ss.count('공부'))
##print(ss.find('공부'), ss.rfind('공부'), ss.find('공부', 5), ss.find('없다'))
##print(ss.index('공부'), ss.rindex('공부'), ss.index('공부', 5))
##print(ss.startswith('파이썬'), ss.startswith('파이썬', 10), ss.endswith('^^'))
##print(ss.replace('파이썬', 'Python'))

# ============== split ==============
##ss = 'Python을 열심히 공부 중'
##print(ss.split())
##ss = '하나:둘:셋'
##print(ss.split(':'))
##ss = 'Python, comma, join'
##print(ss.split(','))


# ============== 문자 정렬 ==============
##ss = '파이썬'
##print(ss.center(10))
##print(ss.center(10, '-'))
##print(ss.ljust(10))
##print(ss.rjust(10))
##print(ss.zfill(10))


# ============== 문자열 속성 파악 =============
##isdigit()
##isalpha()
##isalnum()


# ============= 문자열 길이 ==============
##print(len('파이썬'))


# ============= f 문자열(*파이썬에서만 가능) =============
##price = 10000
##count = 3
##product = "coffee"
##
##print(f"상품 {product} {count}개의 가격은 {count*price}원입니다.")


# ============= 문자 슬라이스 =============
##s = "Monty Python"
##print(s[6:10])
##print(s[3:6])
##print(s[0:5])
##print(s[-6:-1])


# ============= 이름 및 문자 슬라이스 응용 ============
##a = input("이름의 첫 번째 글자를 입력하시오: ")
##b = input("이름의 두 번째 글자를 입력하시오: ")
##c = input("이름의 세 번째 글자를 입력하시오: ")
##
##print(f"\n영어 이니셜은 {a[0]}{b[0]}{c[0]} 입니다.")
##
##name = input("\n이름 : ")
##name_split = name.split(" ")
##
##x = name_split[0]
##y = name_split[1]
##z = name_split[2]
##initial = x + y + z
##print("\n영어 이니셜은", initial, "입니다.")


# ============ 기본 조건문 =============
##a = 90
##
##if a < 100 :
##    print("a가 100 보다 작습니다")
##
##print("프로그램 끝")
#---------------------

##a = int(input("정수를 입력하세요 : "))
##
##if a < 100 :
##    print("a의 값은 %d 이고" %a)
##    print("100보다 작습니다")
##
##else :
##    print("입력된 값은")
##    print("100보다 큰 값입니다")

##print("프로그램 끝")
#---------------------

##a = int(input("정수를 입력하세요 : "))
##print("입력한 숫자 : %d" %a)
##
##if a % 2 :
##    print("홀수입니다")
##else :
##    print("짝수입니다")
##
##print("프로그램 끝")
#---------------------

##a = int(input("정수를 입력하세요 : "))
##print("입력한 숫자 : %d" %a)
##
##if a > 50 :
##    if a < 100 :
##        print("50보다 크고 100보다 작은 수 입니다")
##    else :
##        print("100보다 큰 수 입니다")
##else :
##    print("50보다 작은 수 입니다")
##print("프로그램 끝")
#---------------------

##score = int(input("정수를 입력하세요 : "))
##print("입력한 숫자 : %d" %score)
##
##if score > 90 :
##    print("A")
##elif 90 > score >= 80 :
##    print("B")
##elif 80 > score >= 70 :
##    print("C")
##elif 70 > score >= 60 :
##    print("D")
##else :
##    print("F")
##print("학점 입니다")
#---------------------

##weight = int(input("무게 입력 [kg] : "))
##
##if 20 < weight :
##    print("무거움")
##elif 20 >= weight > 5 :
##    print("적당")
##elif 5 >= weight :
##    print("가벼움")
#---------------------


##print("안녕하세요? 두근두근 영화관입니다")
##age = int(input("나이를 입력하세요 : "))
##
##if age >= 19 :
##    print("이 영화를 보실 수 있습니다")
##else :
##    print("이 영화를 보실 수 없습니다")
#---------------------


# =============== 논리연산자 ==============
##age = int(input("나이 : "))
##height = int(input("키(cm) : "))
##
##if age >= 10 and  height >= 165 :
##    print("놀이기구를 탈 수 있습니다")
##
##else :
##    print("놀이기구 탑승이 불가합니다")
#---------------------


##number = int(input("input Number [num < 10] : "))
##
##if number == 0\
##   or number == 2\
##   or number == 4\
##   or number == 6\
##   or number == 8 :
##    print("Even Number")
##else :
##    print("Odd Number")
#---------------------


# ============= 윤년문제 =============
##year = int(input("연도를 입력하세요 : "))
##
##if (year % 4 == 0) or (year % 400 == 0) and (year % 100 != 0) :
##    print("%d 년은 윤년입니다."% year)
##else :
##    print("%d 년은 윤년이 아니네요." % year)


##year = int(input("연도를 입력하세요 : "))
##
##if (year % 4 == 0) \
##   and (year % 100 != 0) \
##   or (year % 400 == 0) :
##    print("%d년은 윤년입니다" %year)
##
##else :
##    print("%d년은 윤년이 아닙니다" %year)    


# ======== 삼항 연산자 =======
##score = int(input("점수 : "))
##
##
##result = '합격' if score >= 60 else '불합격'
##print(result)


# ======== 로그인 프로그램 ========
id = str(input("아이디를 입력하세요 : "))

if id == 'ilovepython' :
    pw = str(input("비밀번호를 입력하세요 : "))
    if pw == '1234' :
        print('환영합니다')
    else :
        print('잘못된 비밀번호입니다')
else :
    print('잘못된 아이디입니다')
