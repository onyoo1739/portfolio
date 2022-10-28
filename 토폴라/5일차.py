pw=input('패스워드를 입력하시오.')
if len(pw) > 5 and len(pw) < 17 :
    for x in pw:
        if not x.isalpha() and not  x.isnumeric():
            print('숫자와 영문자를 모두 넣어야합니다.')
            print('%s는 조건에 부합하지 않습니다.'%pw)
               
        else :
            for x in pw:
                if x.isalpha():
                    if x.isupper():
                        if x.slower():
                            print('%s는 조건을 충족합니다.' %pw)
                        else:
                            print('대문자 혹은 소문자를 하나이상 포함하여야 합니다.')
                            print('%s는 조건에 부합하지 않습니다 '%pw)



else :
    print('패스워드는 6글자 이상, 16글자 이하여야합니다.')
    print('%s는 조건에 부합하지 않습니다.'%pw)