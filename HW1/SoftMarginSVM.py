# Soft-Margin SVMs Q15~
import sys

num = int(sys.argv[1])

train_data = open('train.txt', 'r')
tr = []
for each in train_data:
    stripped = each.split("\n")[0]
    details = stripped.split(" ")
    label = float(details[3])
    value1 = float(details[6])
    value2 = float(details[8])
    tmp = [label, value1, value2]
    tr.append(tmp)
train_data.close    

train_data_out = open('train_libsvm'+str(num)+'.txt', 'w')
for data in tr:
    if data[0] != num:
        labeled = 1
    else:
        labeled = 0
    #labeled = int(data[0])        
    dataStr = str(labeled) + " " + "1:" + str(data[1]) + " 2:" + str(data[2]) + "\n"
    train_data_out.write(dataStr)
train_data_out.close
print "LIBSVM training data done!"

test_data = open('test.txt', 'r')
te = []
for each in test_data:
    stripped = each.split("\n")[0]
    details = stripped.split(" ")
    label = float(details[3])
    value1 = float(details[6])
    value2 = float(details[8])
    tmp = [label, value1, value2]
    te.append(tmp)
test_data.close    

test_data_out = open('test_libsvm'+str(num)+'.txt', 'w')
for data in te:
    if data[0] != num:
        labeled = 1
    else:
        labeled = 0
    #labeled = int(data[0])
    dataStr = str(labeled) + " " + "1:" + str(data[1]) + " 2:" + str(data[2]) + "\n"
    test_data_out.write(dataStr)
test_data_out.close
print "LIBSVM testing data done!"