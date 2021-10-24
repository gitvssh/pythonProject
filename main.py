# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


"""
python 주석
변수 할당
함수 선언
클래스 선언
파이선 자료구조
  리스트
  튜플
  딕셔너리
조건문
  for
  while
  if
예외처리
"""
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
# help("modules")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

a = 10
b = "a"


# print(a, b)


def abc(t=3, d=5):
    print(t)
    print(d)


# abc(1, 2)
# abc()

import numpy as np
import pandas as pd

xm = np.array(range(1, 13)).reshape(2, 6)
print(xm)
xm2 = np.insert(xm, 2, np.array([10, 20]), axis=1)
print(xm2)


def mywage(workingHours):
    print("Working hours is ",workingHours," Hours")
    normalHour = 40
    pay = 1
    overtimePay = 0.5
    salary = workingHours * pay
    if workingHours > normalHour:
        print("this week is overwork!")
        additionalPay = (workingHours - normalHour) * overtimePay
        print("overhour : ",(workingHours - normalHour),"add pay : ",additionalPay)
        salary = salary + additionalPay
    print("Total salary : ",salary," won")
    print()


mywage(26)
mywage(50)
mywage(80)

class example:
    def __init__(self,name):
        self.name = name
    def a(self):
        print("Hello ",self.name," !")
    def b(self):
        print("Good-bye ",self.name," !")
