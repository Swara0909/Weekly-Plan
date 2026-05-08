import numpy as np

# Simple dataset
X = np.array([1, 2, 3, 4, 5], dtype=float)
Y = np.array([2, 4, 6, 8, 10], dtype=float)

# Initial weight and bias
w = 0.0
b = 0.0
n = len(X)
# Hyperparameters
learning_rate = 0.01
epochs = 5


# Batch Gradient Descent
for epoch in range(epochs):

    # Forward pass
    y_pred = w * X + b

    # Compute gradients using ALL samples
    dw = (-2/n) * np.sum(X * (Y - y_pred))
    db = (-2/n) * np.sum(Y - y_pred)

    # Update parameters ONCE
    w = w - learning_rate * dw
    b = b - learning_rate * db

    # Loss
    loss = np.mean((Y - y_pred) ** 2)

    print(f"Epoch {epoch+1}: Loss={loss:.4f}, w={w:.4f}, b={b:.4f}")

# Stochastic Gradient Descent
for epoch in range(epochs):

    for i in range(len(X)):

        x = X[i]
        y = Y[i]

        # Prediction for ONE sample
        y_pred = w * x + b

        # Gradients for ONE sample
        dw = -2 * x * (y - y_pred)
        db = -2 * (y - y_pred)

        # Update after EVERY sample
        w = w - learning_rate * dw
        b = b - learning_rate * db

    # Total loss
    total_pred = w * X + b
    loss = np.mean((Y - total_pred) ** 2)

    print(f"Epoch {epoch+1}: Loss={loss:.4f}, w={w:.4f}, b={b:.4f}")


