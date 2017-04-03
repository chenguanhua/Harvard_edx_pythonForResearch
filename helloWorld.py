import random
print(random.choice([2,44,55,66]))
print((1,2,3)[-0:0] )
x=(1,2,3)
print(x.count(3))
print(range(10))
print("125,000".isdigit())

x={1,2,3}
y={2,3,4}
print(y-x&y)
print({1,2} in {1,2,3})

x=3
y=x
y-=1
print(x)
print(y)

#week2
import numpy as np
a = np.array([1,2])
b = np.array([3,4,5])
#a + b

a = np.array([1,2])
b = np.array([3,4,5])
print(b[a])
c = b[1:]
print(b[a] is c)
print(b[a] == c)

x=20
print(not np.any([x%i == 0 for i in range(2, x)]))

#matplotlib
import matplotlib.pyplot as plt
#plt.plot([0,1,4,9,16])
#plt.show()

x=np.logspace(0,1,10)
y=x**2
#plt.loglog(x,y,"bo-")
#plt.show()

print(x)
print(sum(random.choice(range(10)) for i in range(10)))
print(sum(random.sample(range(10),10)))
print(random.choice(list((1,2,3,4))))


print(np.sum(np.random.randint(1,7,(100,10)), axis=0))

#random walk
X_0=np.array([[0],[0]])
delta_X=np.random.normal(0,1,(2,500000))
X=np.concatenate((X_0,np.cumsum(delta_X,axis=1)),axis=1)
plt.plot(X[0],X[1],"ro-")
plt.show()



















