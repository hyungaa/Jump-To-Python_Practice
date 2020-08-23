# 문자열 포매팅
print("[문자열 포매팅]")
print("I eat %d apples." % 3)
print("I eat %s apples." % "five")

print("*"*30)

number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days." % (number, day))

print("Error is %d%%." % 98) # %표현방법

print("%10s" % "hi") #10개 문자열 오른쪽 정렬

print("%-10s" % "hi") #10개 문자열 왼쪽 정렬

print("%0.4f" % 3.42134234)
print("%10.4f" % 3.42134234)

print("*"*30)

#format함수를 이용한 문자열 포맷팅
print("I eat {0} apples".format(3))
print("I eat {0} apples".format("five"))

number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days.".format(number, day))

print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3))

print("{0:<10}".format("hi")) #왼쪽 정렬
print("{0:>10}".format("hi")) #오른쪽 정렬
print("{0:^10}".format("hi")) #가운데 정렬
print("{0:=^10}".format("hi"))
#공백문자 채우기
print("{0:!<10}".format("hi"))

y = 3.42134234
print("{0:0.4f}".format(y))
print("{0:10.4f}".format(y))
print("{{ and }}".format())

age = 30
print(f'나는 내년이면 {age+1}살이 된다.')

d = {'name':'홍길동', 'age':30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')

print(f'{"hi":<10}')  # 왼쪽 정렬
print(f'{"hi":>10}')  # 오른쪽 정렬
print(f'{"hi":^10}') # 가운데 정렬

# 문자열 함수
print("\n", "="*30)
print("\n[문자열 함수]")
a = "hobby"
print(a.count('b'))
a = "Python is the best choice"
print(a.find('b'))
print(a.find('k')) #문자열 없을때

a = "Life is too short"
print(a.index('t'))

print(",".join('abcd')) #문자열 삽입
print(",".join(['a', 'b', 'c', 'd']))

# For 문 사용
print("\n", "="*30)
print("\n[For 문 사용]")
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
  print(first + last)

# for 반복문
family = ['mother', 'father', 'gentleman', 'sexy lady']
for x in family:
    print('%s %s' % (x, len(x)))    # x 와 x의 길이를 출력하라. 

# for문을 이용한 구구단 출력
for i in range(2,10):        # ①번 for문
    for j in range(1, 10):   # ②번 for문
        print(i*j, end=" ")   # 매개변수 end를 넣어준 이유는 그 줄에 계속 출력하기 위해
    print('')                 # 2단, 3단 등을 구분하기 위해 다음 줄에 출력  

# For 문 사용
print("\n", "="*30)
print("\n[For 문 사용]]")
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
  print(first + last)

# while 반복문
num = 1
while num <= 100:
    print(num)
    num = num + 1