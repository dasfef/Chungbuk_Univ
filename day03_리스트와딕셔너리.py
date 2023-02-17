# ========= List =========
##myList = ["우유", "사과", "두부", "소고기" ]
##
##for k in range(len(myList)) :
##    print(myList[k])
# --------------------------


##myList = ["우유", "사과", "두부", "소고기" ]
##myList[1] = "커피"
##
##print(myList)
# --------------------------


##myList= []
##
##myList.append("마가렛")
##myList.append("촉촉")
##myList.append("카스타드")
##myList.append("후레쉬부에리")
##
##print(myList)
# --------------------------


# ★ 0부터 시작하는 짝수 List 100개에 입력 ★
##myList = []
##value = 0
##
##for k in range(101) :
##    myList.append(value)
##    value += 2
##
##print(myList)
# --------------------------


# ★ 난수 리스트에 넣기 ★
##import random
##
##myList = []
##
##for k in range(100) :
##    number = random.randint(1, 100)
##    myList.append(number)
##
##print(myList)
# --------------------------


# ★ insert 활용하여 리스트 중간에 삽입하기 ★
##myList = ["우유", "사과", "두부", "소고기"]
##myList.insert(1, "커피")
##print(myList)
# --------------------------


# ★ remove, pop 활용하여 리스트 특정내용 삭제하기 ★
##myList = ["우유", "사과", "두부", "소고기"]
##myList.remove("소고기")
##print(myList)

##myList = ["우유", "사과", "두부", "소고기"]
##myList.pop(1)
##print(myList)

##myList = ["우유", "사과", "두부", "소고기"]
##
##if "소고기" in myList :
##    k = myList.index("소고기")
##
##print(k)


##myList = ["우유", "두부"]
##yourList = ["두부", "소고기"]
##sum = myList + yourList
##
##print(sum)


##myList = ["우유", "두부"]
##print(myList * 2)


# ★ 통계치 구하기 ★
##import statistics
##
##sample = [2, 3, 3, 4, 5, 5, 5, 5, 6, 6, 6, 7]
##
##print(f"입력 리스트 = {sample}")
##print(f"평균 = {statistics.mean(sample)}")
##print(f"중간값 = {statistics.median(sample)}")
##print(f"최빈값 = {statistics.mode(sample)}")
##print(f"표준편차 = {statistics.stdev(sample)}")
# --------------------------


# ★ 2차원 리스트 ★
##dogNames = []
##while True :
##    name = input("강아지 이름 입력 :")
##    if name == '' :
##        break
##    dogNames.append(name)
##
##print("\n『 강아지 이름 』")
##for name in dogNames :
##    print(name, end = " ")



# ★ 튜플 ★
##tp1 = (70)
##tp2 = 70
##tp3 = (1, 2, 3, 4)
##tp4 = 1, 2, 3, 4
##
##print(tp1, tp2, tp3, tp4)


# ★ 딕셔너리 ★
##singer = {}
##
##singer['이름'] = '트와이스'
##singer['구성원 수'] = 9
##singer['데뷔'] = '서바이벌 식스틴'
##singer['대표곡'] = 'SIGNAL'
##
##singer['이름'] = ['BTS', 'TWICE']
##
##print(singer.get('BTS'))
##
##print(singer.keys())
##print(singer.values())
##
##for k in singer.keys() :
##    print("%s : %s" %(k, singer[k]))



# ★ 리스트 종합실습 ★
##names = ["최연웅", "견병욱", "이동욱", "신희성", "연정수", "정소진",\
##         "김현지", "황재원", "박종민", "국유채"]
##
##while True :
##    search = input("이름을 입력하세요 : ")
##    if search in names :
##        print(f"\n{search}과(와) 저는 친구입니다\n")
##    elif search == '종료' :
##        break
##    else :
##        print("\n저와 친구가 아닙니다.")
##        print("친구를 찾아보세요\n")
