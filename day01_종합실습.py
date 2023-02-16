age = int(input("나이를 입력해주세요 : "))

if age >= 20 :
    gender = str(input("성별을 선택해주세요(남/여) : "))
    if gender == '남' :
        ex = 'Blue Bike'
    elif gender == '여' :
        ex = 'Red Bike'
    else :
        print('올바른 성별을 선택해주세요')
        errrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr
        
        
    time = int(input("대여할 시간을 설정해주세요(1시간 단위) : "))
    cost = int(input("금액을 투입해주세요(시간당 5000원) : "))
    print(f"\n[ 아래 내역을 확인해주세요 ] \n나이 : {age} \n색깔 : {ex} \n거스름 돈 : {cost-(time * 5000)}")
    
else :
    print('대여할 수 있는 연령이 아닙니다')





