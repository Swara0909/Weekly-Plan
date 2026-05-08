import numpy as np

X = np.array([1,2,3,4,5], dtype=float)
Y = np.array([2,4,6,8,10], dtype=float)

w = 0.0
b = 0.0

learning_rate = 0.01
epochs = 5
batch_size = 2

n = len(X)

for epoch in range(epochs):

    for i in range(0, n, batch_size):

        # Create mini-batch
        X_batch = X[i:i+batch_size]
        Y_batch = Y[i:i+batch_size]

        # Predictions
        y_pred = w * X_batch + b

        # Batch size
        m = len(X_batch)

        # Gradients for mini-batch
        dw = (-2/m) * np.sum(X_batch * (Y_batch - y_pred))
        db = (-2/m) * np.sum(Y_batch - y_pred)

        # Update parameters
        w = w - learning_rate * dw
        b = b - learning_rate * db

    # Total loss
    total_pred = w * X + b
    loss = np.mean((Y - total_pred) ** 2)

    print(f"Epoch {epoch+1}: Loss={loss:.4f}, w={w:.4f}, b={b:.4f}")