ftr = open('hw3_train.dat', 'r')
fotr = open('hw3_train.txt', 'w')
for each in ftr:
    s = each.split(" ")
    f1 = float(s[0])
    f2 = float(s[1])
    la = int(s[2])
    if la == -1:
        la = 0
    fotr.write(str(la) + " " + "1:" + str(f1) + " " + "2:" + str(f2) + "\n")
ftr.close
fotr.close

fte = open('hw3_test.dat', 'r')
fote = open('hw3_test.txt', 'w')
for each in fte:
    s = each.split(" ")
    f1 = float(s[0])
    f2 = float(s[1])
    la = int(s[2])
    if la == -1:
        la = 0    
    fote.write(str(la) + " " + "1:" + str(f1) + " " + "2:" + str(f2) + "\n")