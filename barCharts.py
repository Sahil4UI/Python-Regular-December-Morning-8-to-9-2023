import matplotlib.pyplot as plt

x = [2,4,6,8,10]
y = [3,5,9,2,4]

x2=[3,5,7,9,11]
y2=[5,8,6,1,2]

plt.bar(x,y,label="Bar1",color="b")
plt.bar(x2,y2,label="Bar2",color="r")
plt.xlabel("X- axis")
plt.ylabel("Y- axis")
plt.title("X vs Y Chart")
plt.legend()
plt.show()