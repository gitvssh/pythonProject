"""
import numpy as np
import matplotlib.pyplot as plt


plt.ioff()
x = np.linspace(0, 10, 50)
sinus = np.sin(x)
cosinus = np.cos(x)
plt.plot(x, sinus, '-b', x, sinus, 'ob', x, cosinus, '-r', x, cosinus, 'or')
plt.xlabel('this is x!')
plt.ylabel('this is y!')
plt.title('My First Plot')
plt.show()


plt.ioff()
x = np.linspace(0, 10, 50)
sinus = np.sin(x)
cosinus = np.cos(x)
plt.plot(x, sinus, label='sinus', color='blue', linestyle='--', linewidth=2)
plt.plot(x, cosinus, label='cosinus', color='red', linestyle='-', linewidth=2)
plt.legend()
plt.show()


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://raw.github.com/neurospin/pystatsml/master/datasets/salary_table.csv'
salary = pd.read_csv(url)
salary.head()
df=salary
colors = colors_edu = {'bachelor':'r', 'Master':'g', 'Ph.D':'blue'}
plt.scatter(df['experience'], df['salary'], c=df['education'].apply(lambda x:colors[x]), s=100)
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
x=np.random.randn(100)
y=np.random.randn(100)

plt.plot(y, 'b:')
plt.title('Green Solid Line')
plt.title('Blue Dotted Line')
plt.ioff()
plt.figure()
plt.plot(y, 'g-')
plt.title('Green Solid Line')
plt.show()

plt.ion()
plt.figure()
h=plt.plot(y, 'g-')
plt.getp(h)
plt.setp(h, 'color', 'red')

plt.figure()
plt.plot(y, alpha=0.5, ls='-.', lw=3, marker='o', mec='red', mew=2, mfc='blue', ms=10)


#x, x^2, x^3 그래프 그리고 수식 라벨달기
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

plt.ioff()
x = np.linspace(0, 2, 100)
plt.figure()
plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')
plt.xlim(-0.25, 2.25)
plt.xlim(-0.25, 2.25)
plt.yticks([0, 1, 2, 4, 8])
plt.xlabel('x label')
plt.ylabel('y label')
plt.legend()
plt.grid(True)
plt.text(1.6, 7, r'$y=x^3$')
plt.text(1.9, 4.5, r'$y=x^2$')
plt.text(1.9, 1.4, r'$y=x$')

plt.title("Simple Polynomials")
plt.show()


#R ggplot 형식으로 그래프 그리기
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

plt.style.available
plt.style.use('ggplot')

plt.ion()

x = np.linspace(0, 2, 100)
plt.figure()
plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')
plt.xlim(-0.25, 2.25)
plt.yticks([0, 1, 2, 4, 8])
plt.xlabel('x label')
plt.ylabel('y label')
plt.legend()
plt.grid(True)
plt.text(1.6, 7, r'$y=x^3$')
plt.text(1.9, 4.5, r'$y=x^2$')
plt.text(1.9, 1.4, r'$y=x^3$')

plt.title("Simple Polynomials")
plt.show()


#서브플롯 그리기

plt.ioff()

plt.figure(1)
plt.subplot(211)
plt.plot([1, 2, 3])
plt.subplot(212)
plt.plot([4, 5, 6])

plt.figure(2)
plt.subplot(211)
plt.title('Test 1, 2, 3')

"""

import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")

iris=sns.load_dataset("iris")
iris.columns
iris.columns = ['sl', 'sw', 'pl', 'pw', 'sp']
iris.head()

g = sns.FacetGrid(iris, col="sp")
g = g.map(plt.hist, "sl")

sns.catplot(x="sp", y="sl", kind="boxen", data=iris)

sns.jointplot(x='sw', y='sl', data=iris, kind='kde', space=0, color='g')

g = sns.PairGrid(iris, hue='sp')
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)
g.map_diag(sns.kdeplot, lw=3, legend=False)

sns.lmplot(x='sw', y='sl', data=iris)
sns.lmplot(x='sw', y='sl', hue='sp', data=iris)

