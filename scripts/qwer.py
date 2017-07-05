import numpy as np
import operator

#a = np.array([1, 2, 3, 4])
#b = np.array([4, 2, 2, 4])
#c = np.array([1, 2, 3, 4])
#x=np.array_equal(a[1], b[1])
#print x
temp=0
temp_array=np.array([0,0,0,0,0,0,0,0])
i=0
j=0
result_array=np.array([0,0,0,0,0,0,0,0])
x = np.array([[2,1,0,0,0,0,0,0], [2,0,1,0,0,0,0,0],[2,0,0, 1,0,0,0,0,],[2,0,0,0,1,0,0,0],[2,0,0,0,0,1,0,0 ],[2,0,0,0,0,0, 1,0],[2,0,0,0,0,0,0 ,1],[3,1,0,0,0,0,0,0],[3,0,1,0,0,0,0,0 ],[3,0,0,1,0,0,0,0],[4,1,0,0,0,0,0,0], [4,0,1,0,0,0,0,0]])
array_rows= x.shape[0]
temp=x[0][0]
for i in range(array_rows):
   if (x[i][0]==temp):
	temp_array=np.add(temp_array,x[i])
        temp=x[i][0]
   else:
        np.put(temp_array,0,temp)
        #result_array=np.append(result_array,temp_array)
        result_array=np.insert(result_array,j,temp_array)
        j=j+8
        temp_array=np.array([0,0,0,0,0,0,0,0])
	temp_array=np.add(temp_array,x[i])
        temp=x[i][0]
np.put(temp_array,0,temp)
#result_array=np.append(result_array,temp_array)
result_array=np.insert(result_array,j,temp_array)
 
print result_array 
