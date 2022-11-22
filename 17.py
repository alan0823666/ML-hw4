from liblinearutil  import *

X_train = []
Y_train = []

fp = open('train.txt', "r")
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
    X_train.append(tmp_list)
    Y_train.append(label)
    line = fp.readline()
 
fp.close()

model_17A = train(Y_train, X_train, '-s 0 -c 5000 -e 0.000001')
predict(Y_train, X_train, model_17A,"")
print("17A")

model_17B = train(Y_train, X_train, '-s 0 -c 50 -e 0.000001')
predict(Y_train, X_train, model_17B,"")
print("17B")

model_17C = train(Y_train, X_train, '-s 0 -c 0.5 -e 0.000001')
predict(Y_train, X_train, model_17C,"")
print("17C")

model_17D = train(Y_train, X_train, '-s 0 -c 0.005 -e 0.000001')
predict(Y_train, X_train, model_17D,"")
print("17D")

model_17E = train(Y_train, X_train, '-s 0 -c 0.00005 -e 0.000001')
predict(Y_train, X_train, model_17E,"")
print("17E")
