import matplotlib.pyplot as plt
import numpy as np

# 创建 x 值范围，例如 -10 到 10 之间的一组值
x = np.linspace(-2, 4, 100)  # 生成100个均匀分布的点

# 計算 y 值，即 x 的平方
y = x**2

# 创建图形
plt.plot(x, y, label='y = x^2', color='blue')
plt.scatter(2, 4, color='red', label='Point (2, 4)')
# 添加轴标签和图例
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# 显示图形
plt.title('y = x^2')
plt.grid(True) #顯示格線
plt.show()