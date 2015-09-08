#w = [0.008914413333815244, -0.2817683396140053]
"""
w = [-0.22320634133926537, -0.3282900961146526]
fi = open('train_libsvm0.txt', 'r')
err = 0
cnt = 0.
for each in fi:
    cnt += 1.
    info = each.split(' ')
    value = float(info[0])
    if value == 1.:
        label = 1.
    else:
        label = -1.
    feat1 = float(info[1].split(':')[1])
    feat2 = float(info[2].split(':')[1])
    score = w[0] * feat1 + w[1] * feat2
    if label * score < 0:
        err += 1
        print [label, feat1, feat2]  
print "Error Count = ", err  
print "Error Rate = ", (cnt - err) / cnt
"""
w = []
fi = open('trained_libsvm0.txt', 'r')
for each in fi:
    info = each.split(' ')
    alpha = float(info[0])
    feat1 = float(info[1].split(':')[1])
    feat2 = float(info[2].split(':')[1])
    score = [alpha * feat1, alpha * feat2]
    w.append(score)

w0 = 0.
w1 = 0.
for each in w:
    w0 += each[0]
    w1 += each[1]
print w0, w1