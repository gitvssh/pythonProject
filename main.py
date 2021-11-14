
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

tClass = 10
b = "a"


# print(a, b)


def abc(t=3, d=5):
    print(t)
    print(d)


class testClass:
    def testClass(self):
        pass

    def __init__(self, attr1="basic1", attr2="basic2"):
        self.attr2 = attr2
        self.attr1 = attr1
        print("initiating")

    def print(self, msg="basic"):
        print("print msg : ", msg)
        print("my attr is ", self.attr1, ",", self.attr2)

    def set1(self, attr1):
        self.attr1 = attr1

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


z = np.linspace(-1, 1, 100)
w = np.sqrt(1-z**2)
print(w)
x = np.linspace(0, 2, 100)
plt.figure()
plt.plot(x)

