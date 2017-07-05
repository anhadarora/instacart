import numpy as np
import operator
from numpy import genfromtxt
test = genfromtxt('/Users/anhad/Desktop/new.csv', delimiter=',')
number_of_entries = test.shape[0] - 1
columns = 21
MATx = np.empty(shape=[0, columns])

def number_to_row(argument):
    switcher = {
        1: [test[i][1],1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        2: [test[i][1],0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        3: [test[i][1],0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        4: [test[i][1],0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        5: [test[i][1],0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        6: [test[i][1],0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        7: [test[i][1],0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
        8: [test[i][1],0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
        9: [test[i][1],0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
        10: [test[i][1],0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
        11: [test[i][1],0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
        12: [test[i][1],0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
        13: [test[i][1],0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
        14: [test[i][1],0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
        15: [test[i][1],0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
        16: [test[i][1],0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
        17: [test[i][1],0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
        18: [test[i][1],0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
        19: [test[i][1],0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
        20: [test[i][1],0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    }
    return switcher.get(argument, [test[i][1],0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

for i in range (50000):
    app = number_to_row(test[i][0])
    print app
    MATx = np.append(MATx, [app], axis=0)

print MATx

temp=0
# SUM = np.zeros((columns,))
temp_array=np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
j=0
k=0
# RESx = np.empty(shape=[0, columns])
result_array=np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
## x is the np.array which is input
temp=x[0][0]

new_number_of_entries = MATx.shape[0]

for j in range(new_number_of_entries):
    if (MATx[j][0]==temp):
        temp_array = np.add(temp_array,MATx[j])
            temp = MATx[j][0]
    else:
        np.put(temp_array,0,temp)
        #result_array=np.append(result_array,temp_array)
        result_array=np.insert(result_array,k,temp_array)
        k=k+21
        temp_array=np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    temp_array=np.add(temp_array,MATx[j])
        temp=MATx[j][0]
np.put(temp_array,0,temp)
#result_array=np.append(result_array,temp_array)
result_array=np.insert(result_array,k,temp_array)
print result_array

# def add_weights(lista,listb):
#     SUM = np.array([a+b for a,b in zip(lista,listb)])
#     SUM[0] = listb[0]
#
#     return (SUM)

#
# RESx = np.empty(shape=[0, columns])
# SUM = np.zeros((columns,))
# new_number_of_entries = (MATx.shape[0]) - 1
# for j in range (new_number_of_entries):
#
#     order_current = MATx[j][:]
#     order_id = order_current[0]
#
#     order_next = MATx[j+1][:]
#     order_id_next = order_next[0]
#
#     if order_id_next:
#         if (order_id == order_id_next):
#             SUM = add_weights(SUM,order_next)
#             j = j + 1
#         else:
#             print SUM
#             RESx = np.append(RESx, [SUM], axis=0)
#
# RESx = np.append(RESx, [SUM], axis=0)
# line = RESx.astype(int)
# print line
# np.savetxt("/Users/anhad/Desktop/order_vs_department.csv", line, delimiter=",")