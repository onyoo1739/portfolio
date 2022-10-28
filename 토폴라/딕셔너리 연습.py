'''
trans={}
trans['ocean']='ship'
trans['desert']='camel'
trans['mountain']='cablecar'
print(trans)

2.
trans.pop('ocean')
print(trans)
3.
print(trans['desert'])
print(trans['mountain'])

4.
print('ocean' in trans)

5.
icecream = {
    "메로나": 600, 
    "돼지바": 700, 
    "브라보": 1800, 
    "월드콘": 1500, 
    "투게더": 4500} 
b=0
print(type(a))
for a in icecream:
    b += icecream[a]
print(b)

6.
coffee = {
    "아메리카노": 1900, 
    "카페모카": 3300, 
    "에스프레소": 1900, 
    "카페라떼": 2500, 
    "카푸치노": 2500, 
    "바닐라라떼": 2900}
print (max(coffee.values()))

7.
products = {
    "지도":7000, 
    "나침반":3000, 
    "망원경":10000, 
    "물통":4000, 
    "껌":1000}
for a in products :
    products[a] = int((products[a])*1.1)
    
print(products)
'''

8.
products = {
    '지도':4, 
    '나침반':2, 
    '망원경':1, 
    '물통':2, 
    '껌':1}
a= input('물건을 입력하시오.')

while a in products:
    products[a] = products[a]-1
    if not a in products :
        break
    if products[a] == 0:
        del products[a]
    print(products)
    a= input('물건을 입력하시오.')


