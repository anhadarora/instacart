import numpy as np
import csv

raw_data = csv.reader(open('/Users/anhad/Desktop/new.csv', 'r'))
raw_data.next()
processed_data = np.zeros((1,22), dtype = 'uint32')

output = csv.writer(open('/Users/anhad/Desktop/orders_processed.csv','w'), delimiter=',')
output.writerow(['ORDER_ID', '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21'])


i = -1
curr_oid = 0

for row in raw_data:
    if curr_oid != int(float(row[1])):

        if i >= 0:
            print (processed_data[i])
            output.writerow(processed_data[i])

        i += 1
        curr_oid = int(float(row[1]))

        processed_data = np.vstack((processed_data, np.zeros(22, dtype='uint32')))
        processed_data[i][0] = int(float(row[1]))

    if row[0] != '':
        processed_data[i][int(float(row[0]))] += 1

output.writerow(processed_data[i])
