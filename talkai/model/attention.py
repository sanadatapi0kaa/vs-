# 単語同士の関係性を計算するpython

"""

1. Q = X @ Wq
2. K = X @ Wk
3. V = X @ Wv

4. scores = Q @ K^T
5. scores /= √d
6. weights = softmax(scores)
7. output = weights @ V

X.shape = (seq_len, d_model)
Wq.shape = (d_model, d_k)
Wk.shape = (d_model, d_k)
Wv.shape = (d_model, d_v)
Q.shape = (seq_len, d_k)
K.shape = (seq_len, d_k)
V.shape = (seq_len, d_v)

Wq = np.random.randn(token_dim, d_k) / np.sqrt(token_dim)
Wk = np.random.randn(token_dim, d_k) / np.sqrt(token_dim)
Wv = np.random.randn(token_dim, d_v) / np.sqrt(token_dim)
Wo = np.random.randn(token_dim, token_dim) / np.sqrt(token_dim)

np.save("../data/Wq.npy", Wq)
np.save("../data/Wk.npy", Wk)
np.save("../data/Wv.npy", Wv)
np.save("../data/Wo.npy", Wo)
"""
import numpy as np

token_dim = 8

d_k = 4
d_v = 4



Wq = np.load("../data/Wq.npy")
Wk = np.load("../data/Wk.npy")
Wv = np.load("../data/Wv.npy")
Wo = np.load("../data/Wo.npy")

def softmax(array):
    rows = range(len(array))
    cols = range(len(array[0]))
    answer = np.zeros_like(array)

    for i in rows:
        max_val = max(array[i])
        exp_sum = 0
        exp_vals = []
        for j in cols:
            val = np.exp(array[i][j] - max_val)
            exp_vals.append(val)
            exp_sum += val
        for j in cols:
            answer[i][j] = exp_vals[j] / exp_sum
    return answer

def MakeScores(X):
    
    Q = X @ Wq
    print(Q)
    K = X @ Wk
    V = X @ Wv

    """
    scores = Q @ K.T
    scores /= np.sqrt(d_k)
    weights = softmax(scores)
    output = weights @ V
    return output
    """

    Q1 = Q[:, :4]
    Q2 = Q[:, 4:]
    K1 = K[:, :4]
    K2 = K[:, 4:]
    V1 = V[:, :4]
    V2 = V[:, 4:]
    print(Q1.shape, Q2.shape,K2.shape,V2.shape)
    head1 = softmax(Q1 @ K1.T / np.sqrt(d_k)) @ V1
    head2 = softmax(Q2 @ K2.T / np.sqrt(d_k)) @ V2
    H = np.concatenate([head1, head2], axis = 1)
    print(head2.shape, Wo.shape)
    output = H @ Wo
    return output
