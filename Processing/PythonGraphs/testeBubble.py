import matplotlib.pyplot as plt
import plotly.plotly as py

bubbles_mpl = plt.figure()

# doubling the width of markers
x = [0,2,4,6,8,10]
y = [0]*len(x)
s = [20*4**n for n in range(len(x))]
plt.scatter(x,y,s=s)

plot_url = py.plot_mpl(bubbles_mpl, filename='mpl-bubbles')