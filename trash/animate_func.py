import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as py
from matplotlib import animation

x = np.random.rand(10)
y = np.random.rand(10)

# animation line plot example

fig = py.figure(4)
ax = py.axes(xlim=(0, 1), ylim=(0, 1))
line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    line.set_data(x[:i], y[:i])
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=len(x)+1,
                               interval=200, blit=False)
anim.save('test1.gif')
plt.show()
