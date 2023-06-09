#gradient descent algorithm

import numpy as np

# declare target function
def target(x,y):
    return x - y +(2*(x**2))+(2*x*y)+(y**2)

# function for partial derivatives of target function 
def partial_dev_res_x(x,y):
    return 1+(4*x)+(2*y)
def partial_dev_res_y(x,y):
    return -1+(2*x)+(2*y)

#initialise parameters 
x=0
y=0
learning_rate=0.01

for i in range(1000):
#     update values of x,y
    x = x - learning_rate*(partial_dev_res_x(x,y))
    y = y - learning_rate*(partial_dev_res_y(x,y))
    

print("point of optima: ",x,y)
print("value of partial derivative res to x: ",partial_dev_res_x(x,y))
print("value of partial derivative res to y: ",partial_dev_res_y(x,y))
print("functional value: ",target(x,y))
