def sign(x):
    if x > 0:
        return 1.0
    else:
        return -1.0

fi = open('out', 'r')
fo = open('test_libsvm1.txt', 'r')
test = []
tested = []
for each in fi:
    tested.append(sign(float(each)))
for each in fo:
    info = each.split(" ")
    label = float(info[0])
    test.append(label)
#print test
#print tested
cnt = 0.0
for i in range(len(test)):
    if test[i] != tested[i]:
        cnt += 1.0
print cnt / 400.0