import numpy as np
from scipy.integrate import odeint
importmatplotlib as plt

def model(y, t):
  k = 0.3
  dydt = -k * y
  return dydt

y0 = 5

t = np.linspace(0, 20, 1000)

y = odeint(model, y0, t)
plt.plot(t, y)
plt.xlabel('time')
plt.ylabel('y(t)')
