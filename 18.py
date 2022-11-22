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
X_120 = []
Y_120 = []
for i in range(120):
    X_120.append(X_train[i])
    Y_120.append(Y_train[i])
X_80 = []
Y_80 = []
for i in range(80):
    X_80.append(X_train[120+i])
    Y_80.append(Y_train[120+i])

model_18A = train(Y_120, X_120, '-s 0 -c 5000 -e 0.000001')
predict(Y_80, X_80, model_18A,"")
print("18A")

model_18B = train(Y_120, X_120, '-s 0 -c 50 -e 0.000001')
predict(Y_80, X_80, model_18B,"")
print("18B")

model_18C = train(Y_120, X_120, '-s 0 -c 0.5 -e 0.000001')
predict(Y_80, X_80, model_18C,"")
print("18C")

model_18D = train(Y_120, X_120, '-s 0 -c 0.005 -e 0.000001')
predict(Y_80, X_80, model_18D,"")
print("18D")

model_18E = train(Y_120, X_120, '-s 0 -c 0.00005 -e 0.000001')
predict(Y_80, X_80, model_18E,"")
print("18E")

save_model('model_18B.model',model_18B)