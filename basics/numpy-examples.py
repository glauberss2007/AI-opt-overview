import numpy as np

ages = np.array([10,15,20,18])
scores = np.array([9,8,5,7])

## Conditions directly
print(scores[scores > 8])

## multidimensional array
salary = np.array([[1000,1200,1300],[800,900,950],[2000,2100,2110]])
print(salary[0,2])

## Others
y = np.cos(1)
x = np.inf

matriz = np.zeros([4,3])
matriz_2 = np.ones([3,2])
