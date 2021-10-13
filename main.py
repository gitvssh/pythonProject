# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# python 주석
"""
이건 주석블럭
"""
a = 5000 % 3
print("a : ")
print(a)

b = 20
c = a / b
print(c)

print(type(10))

# 20210909 List
squares = [1, 4, 9, 16, 25]
print(squares[0])
print(squares[-3:])  # 리스트 뒤로꺼내기 역방향으로 진행
print(squares[:])
print("역방향 ")
print(squares[-2])
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

watch = 100000
book = 30000

print(watch + book)
f = 40

test_list = ['one','two','three']
for i in test_list:
    print(i)



def abc(f):
    c = 10
    d = 20
    print(c + d + f)


abc(50)


class Human:
    def walk(self):
        print("he's animal, such a animal")

    def run(self):
        print("run")


class Cat:
    def walk(self):
        print("cat cat cat")

    def cry(self):
        print("meow")


hum = Human()
hum.walk()
hum.run()

cat = Cat()
cat.walk()
cat.cry()


g = a ** b
print(g)

#help("modules")

dct = dict(a=[1,2],b=[4,5])
key = 'c'
try:
    print(dct[key])
except:
    print("Key %s is missing. Add it with empty value" % key)
    dct['c'] = [4,5,6]

a = range(1,10)

print(a)

class CatCat:
    def meow(self):
        print("meow")
    def eat(self):
        print("nyam")

catcat = CatCat()

catcat.meow()
catcat.eat()
#list
listType = [1,2,3]
#tuple
tupleType = (1,2,3)
#dictionaly
dicType = {'dad':'homer','mom':'marge','size':6}

print(dicType['dad'])
print(listType)

lista = [1,2,3]
tuplea = (1,2,3)
dicttionarya = {'1':'b','2':'c'}


for l in lista:
    print(l)
    print("파이썬")


print(lista)
print(tuplea)
print(dicttionarya['1'])
# import numpy as np

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
