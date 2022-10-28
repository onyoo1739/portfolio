'''2.
cafe = {'아메리카노' : 1900, '카페모카' : 3300, '에스프레소'  : 1900, '카페라뗴' : 2500, '카푸치노' : 2500, '바닐라라떼' : 2900}
a= input('메뉴를 입력하세요')
if a in cafe :
    print(cafe[a])
if a =='끝':
    print('종료합니다.')

4.
di={}
a= int(input('정수 N을 입력하시오'))
for b in range (1, a+1):
    di[b] = b**2
print(di)
'''
5.
di={}
li = ['Bob', 'Jeffrey', 'Tony', 'Casandra', 'Alex', 'Sophie', 'Tony', 'Sola', 'Merry', 'Bob']

for name in li :
    di[name] = li.count(name)
print(di)
a=0

튜플 -> 리스트 변경 -> 리스트에 값 추가 -> 리스트를 튜플로
set -> add, update, remove
& 세트이름.intersection(세트이름2) 교집합
|(shift \), untion 합집합
-, differnce() 차집
