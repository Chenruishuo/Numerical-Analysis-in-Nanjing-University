import numpy as np
import matplotlib.pyplot as plt

def fft(x):
    N = len(x)
    if N == 1:
        return x
    even = fft(x[0::2])
    odd = fft(x[1::2])
    freq = np.zeros(N, dtype=complex)
    for k in range(N//2):
        t = np.exp(-2j * np.pi * k / N) * odd[k]
        freq[k] = even[k] + t
        freq[k + N//2] = even[k] - t
    return freq

def ifft(x):
    N = len(x)
    if N == 1:
        return x
    even = ifft(x[0::2])
    odd = ifft(x[1::2])
    time = np.zeros(N, dtype=complex)
    for k in range(N//2):
        t = np.exp(2j * np.pi * k / N) * odd[k]
        time[k] = even[k] + t
        time[k + N//2] = even[k] - t
    return time

N = 1024
t = np.linspace(0, 1, N)
x = np.sin(2 * np.pi * 50 * t) + np.sin(2 * np.pi * 120 * t)
X = fft(x)

X_mag = np.abs(X)
X_mag[X_mag < 100] = 0
X2 = X_mag * np.exp(1j * np.angle(X))

x2 = np.real(ifft(X2)/N)

plt.figure(figsize=(12, 5))
plt.subplot(121)
plt.plot(t, x, label='Original')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.subplot(122)
plt.plot(t, x2, label='Compressed')
plt.xlabel('Omiga')
plt.ylabel('Amplitude')
plt.legend()
plt.show()
