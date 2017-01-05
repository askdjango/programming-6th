fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
fruits.count('tangerine')
fruits.index('banana')
fruits.index('banana', 4)  # Find next banana starting a position 4
fruits.reverse()
fruits.append('grape')
fruits.sort()
fruits.pop()

vec = [-4, -2, 0, 2, 4]
[x*2 for x in vec]
[x for x in vec if x >= 0]
[abs(x) for x in vec]
[(x, x**2) for x in range(6)]
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]

string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
non_null

for j in [2,3,4,5,6,7,8,9]:
    print ('-----{}단-----'.format(j))
    for i in [1,2,3,4,5,6,7,8,9]:
        print('{}*{]={}'.format(j,i, j*i))

for j in [2,3,4,5,6,7,8,9]:
    print ('-----{}단-----'.format(j))
    for i in [1,2,3,4,5,6,7,8,9]:
        print("{}*{}={}".format(j, i, j * i))

numbers=[1,3,5,7,9]
numbers[0]=10
numbers



'''slice'''
a=[1,2,3,4,5,6]
a[0:100]
# [1,2,3,4,5,6] .... no need for terminal number


for i in range(2,10,2):
    for j in range(2,10,2):
        print(i*j)

numbers=[1,2,3,4,5,6,7,8,9]
for i in numbers[2::3]:
    for j in numbers[2::3]:
        print ('{}*{}={}'.format(i,j,i*j))



'''list comprehension/summation'''
numbers1=[1,3,5,7]
numbers2=[2,4,6,8]
print ([i+j for (i.j) in zip(numbers1,numbers2)])


'''tuple & sumation'''
number=(1+3) #this is summation
number=(1+3,) #this is tuple
(3+6,)*5 #(9,9,9,9,9)

numbers=(2)
#라고 하고
for i in numbers:
    print(i**2)
#를 쓰면 에러가 뜬다. 왜? ㅡ그냥 integers는 순회할 수 없기 때문이다. 그래서
numbers=(2,)
#를 쓰면 numbers의 type는 tuple로 바뀐다.

'''packing && unpacking'''
x,y=1,2

temp =x
x=y
y=temp

#but python is so simple

x,y = y,x

(x,y)=(y,x)

x=1
y=2
mytuple=(x,y)
(y,x)=mytuple

print (mytuple)
a,b,c, *dummy = (1,2,3,4,5,6,7)
print (type(dummy))
'''set
순서를 보장해 주지 않음. 하지만 중복 되는 것 자동으로 제거 가능'''

'''dictionary
도 키와 밸류를 뽑는 순서가 완전히 랜덤임.'''

dict_values={'blue':10,'yellow':3,'red':7}
 #but there is method that can import key and dict_values
#that is .items()
for (key, value) in dict_values.items():
    print (key,value)
dict_values={'blue':10,'yellow':3,'red':7}
for (key, value) in dict_values.items():
    print (key,value)

for key in dict_values:
    value=dict_values[key]
    print (key, value)

 10 in dict_values.values()
 #이건 딕셔너리가 값 위주가 아니라 키 위주이기 때문에 값을 갖고 뭔갈 찾을 수 있는지 알아보기 위한 예시.

for key in dict_values.keys():
    print (key)

'''조건문 if'''

if number < 0:
    print('음수입니다.')
elif number ==0:
    print('0입니다.')
elif number < 10:
    print ('일의 자리수')

'''generator of python'''

from itertools import count
for i in count(1):
    print i

#generator라는 개념인데, 만들자 마자 바로 출고하는 개념이라고 함.