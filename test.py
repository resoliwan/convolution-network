# pad
import numpy as np
np.random.seed(1)

X = [[11,12], [21,22]]
X = np.pad(X, ((1,1), (0,0)), 'constant')
X

X = [[11,12], [21,22]]
X = np.pad(X, ((0,0), (1,1)), 'constant')
X

X = [[11,12], [21,22]]
X = np.pad(X, ((1,1), (1,1)), 'constant')
X

X = np.array([[11, 12, 13], [21, 22, 23], [31, 32, 33]])
X[0:2, 0:2]

a_slice_prev = np.array([[11, 12, 13], [21, 22, 23], [31, 32, 33]])
W = np.array([[-1, 0, 1],[-1, 0, 1],[-1, 0, 1]])
b = 10
np.sum(a_slice_prev * W) + b


# def conv_forward(A_prev, W, b, hparameters):
A_prev = np.array([
    [#M[0]
      [[11, 11], [12, 12], [13, 13]], #H[0], #W[0], #C[0]
      [[21, 21], [22, 22], [23, 23]], #H[0], #W[0], #C[0]
      [[31, 31], [32, 32], [33, 33]], #H[0], #W[0], #C[0]
    ]
])
#(1, 3, 3, 2)
(m, n_H_prev, n_W_prev, n_C_prev) = A_prev.shape
A_prev.shape

# Retrieve dimensions from W's shape (≈1 line)
(f, f, n_C_prev, n_C) = None

# Retrieve information from "hparameters" (≈2 lines)
stride = None
pad = None

# Compute the dimensions of the CONV output volume using the formula given above. Hint: use int() to floor. (≈2 lines)
n_H = None
n_W = None

# Initialize the output volume Z with zeros. (≈1 line)
Z = None
