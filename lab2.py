import matplotlib.pyplot as plt

def FindXY(y_min, y_medium):
    b1 = 2 * y_min
    b2 = -y_medium

    x = (b1 - b2) / ((y_min / 10) + (y_medium / 10))
    y = (-y_min / 10) * x + b1
    return [x, y]

def Superpoz(i,y_medium, y_min, V_x, V_y):
    XY = FindXY(y_min, y_medium)
    x = XY[0]
    y = XY[1]

    F1X=5
    F2X=40/3
    F3X=(40+x)/3
    F4X=70/3

    FX=[F1X,F2X,F3X,F4X]

    F1Y=y_min/2
    F2Y=y_min/3
    F3Y=(y_medium+y)/3
    F4Y=y_medium/3

    FY = [F1Y,F2Y,F3Y,F4Y]

    S1 = y_min * 10
    S2 = y_min * 10 / 2
    S3 = (y_medium * (20 - x)) - (((20 - x) * (y_medium - y)) / 2) - (((20 - x) * y) / 2)
    S4 = y_medium * 10 / 2

    S=[S1,S2,S3,S4]

    Xct=(F1X*S1+F2X*S2+F3X*S3+F4X*S4)/(S1+S2+S3+S4)
    Yct=(F1Y*S1+F2Y*S2+F3Y*S3+F4Y*S4)/(S1+S2+S3+S4)

    return V_x.append(Xct), V_y.append(Yct)


def FunctionModification(i, y_medium, y_min, X):
    Y1 = [y_min, y_min, 0, 0]
    Y2 = [0, 0, y_medium, 0]

    plt.plot(X, Y1, 'o-r', alpha=0.7, lw=5, mec='b', mew=2, ms=10)
    plt.plot(X, Y2, 'o-r', alpha=0.7, lw=5, mec='b', mew=2, ms=10)
    plt.show()

def FunctionPrinadlejnosty(i, t, X, y_min, y_medium):
    Y1 = T_min(t)
    Y2 = T_max(t)

    y_min = Y1[2]
    y_medium = Y2[2]

    plt.plot(X,Y1, 'o-r', alpha=0.7, lw=5, mec='b', mew=2, ms=10)
    plt.plot(X, Y2, 'o-r', alpha=0.7, lw=5, mec='b', mew=2, ms=10)
    plt.show()

    return y_min,y_medium
    # DrawChart(i, X, Y)
    # DrawTitle(i, t)
    # DrawComment(i, t, y_min, y_sredniy, '.fun_pr')

def T_min(t):
    y = -(t / 10) + 2
    Y = [1, 1, y, 0]
    return Y

def T_max(t):
    y = (t / 10) - 1
    y1 = -(t / 10) + 3
    Y = [0, 0, y, y1]
    return Y


myId = 3
X = [0, 10, 20, 30]
t = 12 + 0.5 * myId
y_min = 1
y_medium = 1

V_y=[]
V_x=[]


for i in range(4):
    a = FunctionPrinadlejnosty(i,t,X, y_min, y_medium)
    y_min = a[0]
    y_medium = a[1]
    FunctionModification(i, y_medium, y_min, X)
    Superpoz(i,y_medium, y_min, V_x, V_y)
    t = t + 0.3
    print(t)

plt.plot(V_x, V_y, 'o-r', alpha=0.7, lw=5, mec='b', mew=2, ms=10)
plt.show()
