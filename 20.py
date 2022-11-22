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
fp.close()

Fold_X = []
Fold_Y = []

for T in range(5):
    T_tmp = []
    Y_tmp = []
    for i in range(40):
        T_tmp.append(X_train[T*40 + i])
        Y_tmp.append(Y_train[T*40 + i])
    Fold_X.append(T_tmp)
    Fold_Y.append(Y_tmp)

Xno0 = Fold_X[1] + Fold_X[2] + Fold_X[3] + Fold_X[4]
Xno1 = Fold_X[0] + Fold_X[2] + Fold_X[3] + Fold_X[4]
Xno2 = Fold_X[1] + Fold_X[0] + Fold_X[3] + Fold_X[4]
Xno3 = Fold_X[1] + Fold_X[2] + Fold_X[0] + Fold_X[4]
Xno4 = Fold_X[1] + Fold_X[2] + Fold_X[3] + Fold_X[0]

Yno0 = Fold_Y[1] + Fold_Y[2] + Fold_Y[3] + Fold_Y[4]
Yno1 = Fold_Y[0] + Fold_Y[2] + Fold_Y[3] + Fold_Y[4]
Yno2 = Fold_Y[1] + Fold_Y[0] + Fold_Y[3] + Fold_Y[4]
Yno3 = Fold_Y[1] + Fold_Y[2] + Fold_Y[0] + Fold_Y[4]
Yno4 = Fold_Y[1] + Fold_Y[2] + Fold_Y[3] + Fold_Y[0]

model_20A = train(Yno0, Xno0, '-s 0 -c 5000 -e 0.000001')
predict(Fold_Y[0], Fold_X[0], model_20A,"")
print("20A")

model_20B = train(Yno1, Xno1, '-s 0 -c 50 -e 0.000001')
predict(Fold_Y[1], Fold_X[1], model_20B,"")
print("20B")

model_20C = train(Yno2, Xno2, '-s 0 -c 0.5 -e 0.000001')
predict(Fold_Y[2], Fold_X[2], model_20C,"")
print("20C")

model_20D = train(Yno3, Xno3, '-s 0 -c 0.005 -e 0.000001')
predict(Fold_Y[3], Fold_X[3], model_20D,"")
print("20D")

model_20E = train(Yno4, Xno4, '-s 0 -c 0.00005 -e 0.000001')
predict(Fold_Y[4], Fold_X[4], model_20E,"")
print("20E")

