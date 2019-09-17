Title: Pythonメモ
Date: 2019-07-08
Category: Python
Tags: Python, Programming, memo
Slug: python_memo
Authors: Naoto Yamaguchi
Summary: pythonメモ
Status: draft

### Matplotlibで複数(2つ)のグラフを描画 (draw multiple graphs using matplotlib)

[[Python]Matplotlibで複数のグラフを描画する方法](https://qiita.com/supersaiakujin/items/543053ca4610437112df)
```
import matplotlib.pyplot as plt
import numpy as np

# create a sample data
t = np.linspace(-np.pi, np.pi, 1000)
x1 = np.sin(2*t)
x2 = np.cos(2*t)

fig, (axL, axR) = plt.subplots(ncols=2, figsize=(10,4))

axL.plot(t, x1, linewidth=2)
axL.set_title('sin')
axL.set_xlabel('t')
axL.set_ylabel('x')
axL.set_xlim(-np.pi, np.pi)
axL.grid(True)

axR.plot(t, x2, linewidth=2)
axR.set_title('cos')
axR.set_xlabel('t')
axR.set_ylabel('x')
axR.set_xlim(-np.pi, np.pi)
axR.grid(True)

fig.show()

```