import numpy as np

array = np.array([[56, 0, 4.4, 68],
                 [1.2, 104, 52, 8],
                 [1.8, 135, 99, 0.9]])

# print(array)
cal1 = array.sum(axis=0)
print(cal1)
cal2 = array.sum(axis=1)
print(cal2)
percentage = 100*array/cal1.reshape(1, 4)
print(percentage)