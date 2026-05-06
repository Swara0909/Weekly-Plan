w = 0
lr = 0.1

for i in range(25):
    grad = 2 * (w - 5)   # derivative
    w = w - lr * grad
    print(i, w)