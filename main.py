
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
# See PyCharm help at https://www.jetbrains.com/help/pycharm/\
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

score = pd.read_csv("E:/R/wd/score.csv")
print(score.head())
print(score.shape)

type(score)

score["total"] = score["midterm"] + score["final"]
print(score.head(3))
print(score['total'].mean())
print(score['total'].std())
print(score['total'].median())
print(score['total'].quantile(0.75))

print("----------------------")
import collections as cl
cl.Counter(score['gender'])
cols = ['midterm', 'final', 'total']
# score2 = score[cols]
score2 = score.iloc[:, 2:5]
print(score2.head(3))
print(score2.describe())

scDf = score2.describe()

print(type(scDf))
print(scDf.iloc[1:2, :])
print("=================")
print(scDf.loc['count'])
print("=================")
from scipy.stats import skew
print(skew(score2))

gstat = score.groupby("gender")['total'].describe()
print(gstat)
print(gstat["mean"])
print(gstat["std"])
print(gstat["25%"])

gstat_total = score.groupby("gender")['total']
gResult = gstat_total.agg(['size', 'mean', 'std', 'min', 'max'])
print(gResult)
print("===========")
print(gResult.loc['f'])

import researchpy as rp

print(rp.summary_cont(score['total']))
print(rp.summary_cont(score.groupby("gender")['total']))

import stemgraphic
# stemgraphic.stem_graphic(score.total, scale=10)

import matplotlib.pyplot as plt

import seaborn as sns
sns.set(style='whitegrid')
# sns.boxplot(x="total", data=score)
# sns.boxplot(y="total", data=score)
# scorebox = sns.boxplot(x="gender", y="total", data=score)
# plt.hist(score["total"])
fTotal = score.loc[score.gender == 'f', 'total']
mTotal = score.loc[score.gender == 'm', 'total']
args = dict(alpha=0.5, bins=10)
# plt.hist(fTotal, **args, color='b', label='female')
# plt.hist(mTotal, **args, color='r', label='male')
# plt.gca().set(title="Frequency Histogram of Score.total", ylabel='Frequency')
# plt.legend()


enqete = pd.read_csv("E:/R/wd/enqete.csv")
grade_q1 = pd.crosstab(index=enqete["grade"], columns=enqete["q1"])
grade_q1.index = ["1", "2", "3", "4"]
print(grade_q1)

from scipy.stats import chi2_contingency
print(chi2_contingency(grade_q1))

enqete_table = pd.crosstab(index=enqete["grade"], colnames=["Grade"], columns="count")
enqete_table.index = ["Gr1", "gr2", "Gr3", "Gr4"]
# plt.bar(enqete_table.index, enqete_table["count"])

# plt.pie(enqete_table["count"], labels=enqete_table.index)
grade_q1.plot.bar(stacked=True)
plt.legend(title='Question1')
plt.show()
