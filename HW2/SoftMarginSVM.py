# Soft-Margin SVMs Q15~
import sys

num = int(sys.argv[1])

train_data = open('hw2_lssvm_all.dat', 'r')
tr = []
for each in train_data:
    stripped = each.split("\n")[0]
    details = stripped.split(" ")
    label = float(details[-1])
    tmp = [label] + details[1:-1]
    tr.append(tmp)
train_data.close    

train_data_out = open('train_libsvm'+str(num)+'.txt', 'w')
for data in tr:
    if data[0] != num:
        labeled = -1
    else:
        labeled = 1
    #labeled = int(data[0])        
    dataStr = str(labeled) + " "
    for i in range(1, len(data)):
        dataStr += (str(i) + ":" + str(data[i]) + " ")
    dataStr += "\n"
    train_data_out.write(dataStr)
train_data_out.close
print "LIBSVM training data done!"


test_data = open('hw2_lssvm_test.dat', 'r')
te = []
for each in test_data:
    stripped = each.split("\n")[0]
    details = stripped.split(" ")
    label = float(details[-1])
    tmp = [label] + details[1:-1]
    te.append(tmp)
test_data.close    

test_data_out = open('test_libsvm'+str(num)+'.txt', 'w')
for data in te:
    if data[0] != num:
        labeled = -1
    else:
        labeled = 1
    #labeled = int(data[0])        
    dataStr = str(labeled) + " "
    for i in range(1, len(data)):
        dataStr += (str(i) + ":" + str(data[i]) + " ")
    dataStr += "\n"
    test_data_out.write(dataStr)
test_data_out.close
print "LIBSVM testing data done!"