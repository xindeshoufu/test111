import matplotlib.pyplot as plt

# 生成数据
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# 绘制图表
plt.plot(x, y)
plt.xlabel("X轴")
plt.ylabel("Y轴")
plt.title("示例图表")
plt.savefig("chart.png")  # 保存为图片
print("图表已生成！")