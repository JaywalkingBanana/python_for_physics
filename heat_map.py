%matplotlib inline 
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interactive
import seaborn as sb

x = np.linspace(0, 10, 100)
y = np.linspace(0, 10, 100)

x, y = np.meshgrid(x, y)

def f(A, B, C, D):
    return D * np.sin(C * np.sqrt(A ** 2 + B ** 2))

def plotting(C, D):
    z = f(x, y, C, D)
    ax = sb.heatmap(z, xticklabels = 10, yticklabels = 10, cmap ='rainbow', vmin = -5, vmax = 5)
    ax.invert_yaxis()
    
interactive_plot = interactive(plotting, C = (0, 10, 1), D = (1, 5, 1))
