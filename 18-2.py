from liblinearutil  import *

X_test = []
Y_test = []

fp = open('test.txt', "r")
line = fp.readline()

while line:
    L = line.split()
    x = []
    for i in range(6):
        k = L[i]
        x.append(float(k))
    label = L[6]
    label = int(label)
    tmp_list = []
    tmp_list.append(1.0)
    for i in range(6):
        tmp_list.append(x[i])
    for i in range(6):
        for k in range(6):
            if(k >= i):
                tmp_list.append(x[i]*x[k])
    X_test.append(tmp_list)
    Y_test.append(label)
    line = fp.readline()
 
fp.close()

model_18B = load_model('model_18B.model')
predict(Y_test, X_test, model_18B, "" )