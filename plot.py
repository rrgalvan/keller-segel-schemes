# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""





import matplotlib.pylab as plt

filename = 'plot.txt'
with open(filename) as f:
    lines = f.readlines()
    x = [line.split()[0] for line in lines]
    y = [line.split()[1] for line in lines]
    plt.plot(x, y, c='blue', linewidth=5)
    plt.title("Max(u)")
    plt.show() 
