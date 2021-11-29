import numpy as np

arr1 = np.random.rand(3, 13)
print(arr1)

print("x")
print(arr1[:,0])
print("x")

result = arr1
# result = (arr1 - np.min(arr1))/np.ptp(arr1)
# print(result)

for x in range(13):
  #print(arr1[x])
  result[:,x] = (arr1[:,x] - np.min(arr1[:,x]))/np.ptp(arr1[:,x])

print(result)

