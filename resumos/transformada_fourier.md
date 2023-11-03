## Transformada de Fourier

### What is it?
Given a signal, which is composed by a number of different signals, it is possible to read the frequency, and see in a more clean way using DFT.

![fourier-transform](images/fourier-transform.png)

### Exemplos
$$

$$

```python
def DFT_v1(x):
    N = len(x)

    X = np.zeros(N)
    n = np.arange(N)

    for k in np.arange(N):
        # n, k = 0, 1, ..., N - 1
        w_k = np.exp(-1j* (2 * np.pi / N) * n * k) 
        # @ - operação matricial
        X[k] += w_k.T @ x
    
    return X
```

