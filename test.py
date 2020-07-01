print("hi")
"""라인전솔킬당하는 애송이는 삭제해라"""
a = 3
b = 4
a + b
a * b
a / b
a ** b
7 % 3
3 % 7
7 // 4

say = '"python is very easy." he says.'

ap = '''
life is long
be gentle young friend
'''
print(ap)

head = "Python"
tail = " is fun"
head + tail

a = "python"
a * 2

print("=" * 50)
print("My Program")
print("=" * 50)

a = "Life is too long"
len(a)

a = "Life is too short, You need Python"
a[12]
a[-1]
a[-0]

b = a[0] + a[1] + a[2] + a[3]
b
a[0:4]
a[0:3]

0 <= a < 3
a[0:5]

a[12:17]
a[5:7]

a[19:]
a[:]

a[19:-7]

a = "20010331Rainy"
date = a[:8]
weather = a[8:]
date
weather

year = a[:4]
day = a[4:8]
weather = a[8:]

year
day
weather

a = "pithon"
a[1]

a[1] = 'y'

a[:1]
a[2:]
a[:1] + 'y' + a[2:]

"현재 온도는 %d도입니다" % 3

number = 5

"현재 온도는 %d도입니다" % number

number = 10
 day = "three"
 "I ate %d apples. so I was sick for %s days." % (number, day)
'I ate 10 apples. so I was sick for three days.'

"%10s" % "hi"
"%0.4f" % 3.42134234

"I eat {0} apples" .format(3)

number = 3
"i eat {0} apples" .format(number)
"i ate {0} apples. so i was sick for {1} days.".format(10,20)

"{0:<10}".format("hi")

"{0:^10}".format("hi")

"{0:=^10}".format("hi")
"{0:!<10}".format("good")

y = 3.42134234
"{0:0.4f}".format(y)

"{0:10.4f}".format(y)

"{{and}}".format()

name = '홍길동'
age = 30
f'나의 이름은{name}입니다. 나이는 {age}입니다'

f'나는 내년이면 {age+1}살이 된다.'

d = {'name' : '홍길동' , 'age' : 30}
f'나의 이름은{d["name"]}입니다. 나이는 {d["age"]}입니다.'

f'{"hi":<10}'

y = 3.4123123124
f'{y:0.4f}'
f'{y:10.4f}'

f'{{and}}'

a = "hobby"
a.count('b')

a = "python is the best choice"
a.find('b')
a.find('k')

a = "Life is too short"
a.index('t')
a.index('k')

",".join('abcd')
"m".join(['a', 'b', 'c', 'd'])

a = 'hi'
a.upper()

a = 'HI'
a.lower()

a = '    hi'
a.lstrip()

a = '    hi    '
a.rstrip()
a.strip()

a = 'life is too short'
a.replace('life', 'your leg')

a.split()
b = 'a:b:c:d'
b.split(':')

odd = [1,3,5,7,9]
리스트명 = [요소1,요소2,요소3,...]

a = []
b = [1,2,3]
c = ['Life','is','too','short']
d = [1,2,'life','is']
e = [1,2,['life','is']]

a = [1,2,3]
a
a[0]

a[0] + a[2]
a[-1]

a = [1,2,3,['a','b','c']]
a[-1]

a[-1][0]
a[3][1]
a[3][2]
a = [1,2,['a','b',['Life','is']]]
a[2][2][0]

a = [1,2,3,4,5]
a[0:2]

a = '12345'
a[0:2]

a = [1,2,3,4,5]
b = a[:2]
c = a[2:]
b
c

a = [1,2,3]
b = [4,5,6]
a + b

a * 3

len(a)

a = [1,2,3]
a[2] = 4
a

del a[1]

a = [1,2,3,4,5]
del a[2:]
a

a = [1,2,3]
a.append(4)
a

a.append([5,6])
a

a = [1,4,3,2]
a.sort()
a

a = ['a','c','b']
a.sort()
a

a = ['a','c','b']
a.reverse()
a

a = [1,2,3]
a.index(1)

a = [1,2,3]
a.remove(1)
a

a = [1,2,3]
a.insert(0,55)
a

a = [1,2,3]
a.pop()
a

a = [1,2,3,1]
a.count(1)

a = [1,2,3]
a.extend([4,5])
a

