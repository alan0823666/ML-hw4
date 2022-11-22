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

model_16A = train(Y_test, X_test, '-s 0 -c 5000 -e 0.000001')
predict(Y_test, X_test, model_16A,"")
print("16A")

model_16B = train(Y_test, X_test, '-s 0 -c 50 -e 0.000001')
predict(Y_test, X_test, model_16B,"")
print("16B")

model_16C = train(Y_test, X_test, '-s 0 -c 0.5 -e 0.000001')
predict(Y_test, X_test, model_16C,"")
print("16C")

model_16D = train(Y_test, X_test, '-s 0 -c 0.005 -e 0.000001')
predict(Y_test, X_test, model_16D,"")
print("16D")

model_16E = train(Y_test, X_test, '-s 0 -c 0.00005 -e 0.000001')
predict(Y_test, X_test, model_16E,"")
print("16E")
