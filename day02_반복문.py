# ======== 반복문 ========

##for k in [1,2,3,4,5] :
##    print(f"k = {k} 방문을 환영합니다.")
#--------------------------

##for k in ['하나', '둘', '셋'] :
##    print(f"k = {k} 방문을 환영합니다.", end=" ")
#--------------------------

##for k in ['하나', '둘', '셋'] :
##    print(f"k = {k} 방문을 환영합니다.", end="\t")
#--------------------------

##for k in "abcdef" :
##    print(k, end = " ")
#--------------------------

##for k in range(3) :
##    print(f"변수 k의 값 = {k}")
#--------------------------

##sum = 0
##
##for k in range(1, 10001, 1) :
##    sum = sum + k
##
##print("1 ~ 100 sum = %d" %sum)
#--------------------------

##sum = 0
##start = int(input("시작 값 : "))
##end = int(input("종료 값 : "))
##
##for k in range(start, end + 1, 1) :
##    sum = sum + k
##
##print("%d ~ %d sum = %d" %(start, end, sum))
#--------------------------


# ★ 구구단 ★
##dan = int(input("단을 입력하세요 : "))
##
##for k in range(1, 10) :
##    print("%d x %d = %d" %(dan, k, dan * k))
#--------------------------


##for k in range(1, 10) :
##    for m in range(11, 20) :
##        print(k, m)
##    print("")
#--------------------------

##for dan in range(2, 10) :
##    print("----- %d단 -----" %(dan))
##
##    for k in range(1, 10) :
##        print("%d x %d = %d" %(dan, k, dan * k))
##    print("----------------")
#--------------------------


##for k in range(1, 10) :
##    for dan in range(2, 10) :
##        print(f"{dan} x {k} = {dan * k}".center(10), end = " | ")
##    print("")
#--------------------------


##k = 0
##while k < 5 :
##    print("%d번이 호출되었습니다" %k)
##    k = k + 1
#--------------------------

##sum = 0
##k = 1
##
##while k <= 100 :
##    sum += k
##    k += 1
##print(f"1 ~ 100 까지의 합 : {sum}")
#--------------------------


# ★ 1 ~ 100 사이의 모든 3의 배수의 합 구하기 ★

# ▣ while 문 활용 
##a = 0
##sum = 0
##
##while a <= 100 :
##    a += 1
##    if (a % 3) == 0 :
##        sum += a
##        
##print(f"1부터 100 사이의 모든 3의 배수의 합은 {sum}입니다.")



# ▣ for 문 활용
##a = 0
##sum = 0
##
##for k in range(101) :
##    a += 1
##    if (k % 3) == 0 :
##        sum += k
##
##print("1부터 100 사이의 모든 3의 배수의 합은 %d입니다" %sum)
##print("1부터 100 사이의 모든 3의 배수의 합은 {a}입니다".format(a = sum))


# ★ 사용자의 암호 입력 후 암호가 맞는지 확인하기 ★
##pw = ""
##
##while True :
##    pw = str(input("ID 입력 : "))
##    if pw == str(0) :
##        break
##print("로그인 성공")



# ========= Sentinel 사용 ==========
# ★ 성적을 입력받고, 입력에 -1로 입력되면 평균 구하고 종료하기 ★

##int(input("성적 입력 : "))


# ★ 무한 반복 ★



# ========= 함수 =========
# ★ 매개변수 ★
##def get_sum(start, end) :
##    sum = 0
##    for k in range(start, end + 1) :
##        sum += k
##    return sum
##
##print(get_sum(1, 100))


# ★ 반환값 ★
##def calculate_area(radius) :
##    area = 3.14 * radius ** 2
##    return area
##
##c_area = calculate_area(5.0)
##print(c_area)
# ----------------------------


##def add(a, b) :
##    return a + b
##
##x = 3
##y = 4
##c = add(x, y)
##print(x, y, "a : %d + b : %d = %d" %(x, y, c))
# ----------------------------


##def calc(v1, v2, op) :
##    if op == "+" :
##        result = v1 + v2
##    elif op == "-" :
##        result = v1 - v2
##    elif op == "*" :
##        result = v1 * v2
##    elif op == "/" :
##        result = v1 / v2
##    else :
##        result= 0
##    return result
##
##var1 = int(input("첫 번째 수를 입력하세요 : "))
##oper = input("계산을 입력하세요(+, -, *, /) : ")
##var2 = int(input("두 번째 수를 입력하세요 : "))
##
##res = calc(var1, var2, oper)
##print(f"\n계산결과 : {var1} {oper} {var2} = {res}")
# ----------------------------




