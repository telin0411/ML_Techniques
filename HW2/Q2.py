import sys
import math
import numpy as np
from scipy import optimize
import pylab as pl

def sign(x):
    if x > 0:
        return 1
    else:
        return -1

def Transform(x):
    x1 = x[0]
    x2 = x[1]
    phi = []
    phi1 = x2 ** 2 - 2 * x1 + 3
    phi2 = x1 ** 2 - 2 * x2 - 3
    phi = [phi1, phi2]
    return phi
    
def Check(X, Y, plane):
    for i in range(len(X)):
        if sign(plane[0] * X[i][0] + plane[1] * X[i][1] + plane[2]) == Y[i]:
            pass
        else:
            return False
    return True
    
def dist(X, plane):
    val = 0
    for i in range(len(X)):
        tmp = abs(plane[0] * X[i][0] + plane[1] * X[i][1] + plane[2])
        tmp = tmp / math.sqrt(plane[0] ** 2 + plane[1] ** 2)
        val += tmp
    return val
    
X = np.array([[1, 0],
             [0, 1],
             [0, -1],
             [-1, 0],
             [0, 2],
             [0, -2],
             [-2, 0]])
             
Y = np.array([-1, -1, -1, 1, 1, 1, 1])

X = np.array([[0, 0],
              [2, 2],
              [2, 0],
              [3, 0]])

y = [-1, -1, 1, 1]
Y = np.array([[-1, -1, 1, 1]])

Q_T = np.dot(X, np.transpose(X))
Y_D = np.dot(np.transpose(Y), Y)
dim = 4
s = (dim,dim)
Q_D = np.zeros(s)
for i in range(dim):
    for j in range(dim):
        Q_D[i][j] = Q_T[i][j] * Y_D[i][j]
print Q_T 
print Y_D
print Q_D
A1 = []
A1.append(y)
A1.append([-1 * b for b in y])
col = 0
I = []
for i in range(dim):
    tmp = [0 for row in range(dim)]
    tmp[i] = 1
    col += 1
    I.append(tmp)
A_D = np.array(A1 + I)
print A_D

H = Q_D
c = np.array([-1.])
c0 = 0
A = A_D
b = np.array([0.])
x0 = np.random.randn(dim)

def objective(x,sign=1.):
    return sign*(0.5*np.dot(x.T,np.dot(H,x))+ np.dot(c,x) + c0)
def jacobian(x,sign=1.):
    return sign*(np.dot(x.T,H) + c)
cons = ({'type':'ineq', 'fun':lambda x: b - np.dot(A,x)})

def solve():
    res_cons = optimize.minimize(objective,x0,jac=jacobian,constraints=cons,
        method='SLSQP',options={'disp':False})

    res_uncons = optimize.minimize(objective,x0,jac=jacobian,
        method='SLSQP',options={'disp':False})

    print '\nConstrained:'
    print res_cons

    print '\nUnconstrained:'
    print res_uncons

solve()

"""
X = []
Y = []
X.append([1, 0])
Y.append(-1)
X.append([0, 1])
Y.append(-1)
X.append([0, -1])
Y.append(-1)
X.append([-1, 0])
Y.append(1)
X.append([0, 2])
Y.append(1)
X.append([0, -2])
Y.append(1)
X.append([-2, 0])
Y.append(1)

Z = []
for each in X:
    Z.append(Transform(each))

plane1 = [1., 1., -4.5]
plane2 = [1., -1., -4.5]
plane3 = [1., 0., -4.5]
plane4 = [0., 1., -4.5]

print Check(Z, Y, plane4)
"""
