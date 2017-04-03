import string
alphabet=string.ascii_letters

sentence = 'Jim quickly realized that the beautiful gowns are expensive'

def counter(input_string):
    count_letters = {}
    for letter in input_string:
        if letter in count_letters:
            count_letters[letter]+=1
        else:
            count_letters[letter]=1
    return count_letters

test=counter(sentence)

a=max(test,key=lambda i:test[i])
print(a)

#2a
import math
print(math.pi/4)

import random

random.seed(1) # This line fixes the value called by your function,
               # and is used for answer-checking.

def rand():
   # define `rand` here!
    return random.uniform(-1,1)

print(rand())

def distance(x, y):
    return math.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)

print(distance((0,0),(1,1)))

random.seed(1)


def in_circle(x, origin=[0] * 2):
    if distance(x,origin)<1:
        return True
    else:
        return False

print(in_circle((1,1)))

R = 10000
x = []
inside = []
for i in range(R):
    point = [rand(), rand()]
    x.append(point)
    inside.append(in_circle(point))

print(sum(inside)/R)
print(abs(sum(inside)/R-math.pi/4))
#print(math.pi/4)

#3a
random.seed(1)

def moving_window_average(x, n_neighbors=1):
    n = len(x)
    width = n_neighbors*2 + 1
    x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors
    # To complete the function,
    # return a list of the mean of values from i to i+width for all values i from 0 to n-1.
    target=[]
    for i in range(n_neighbors,len(x)-n_neighbors):
        temp=x[i]
        for j in range(1,n_neighbors+1):
            temp+=x[i-j]
            temp+=x[i+j]
        target.append(temp/(n_neighbors*2+1))
    return target

x=[0,10,5,3,1,5]
print(moving_window_average(x, 1))

#3b
random.seed(1)
x=[random.uniform(0,1) for i in range(0,1000)]
Y=[x]
for i in range(1,10):
    Y.append(moving_window_average(x,i))

#3c
ranges=[max(singleList)-min(singleList) for singleList in Y]
print(ranges)













