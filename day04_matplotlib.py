import matplotlib.pyplot as plt
import numpy as np
import random
import keyboard

# === 그래프 그리기 ===
##plt.plot([1, 2, 3, 4], [1, 4, 9, 6], 'r*')  x축, y축, 스타일
##plt.axis([0, 6, 0, 15]) xmin, xmax, ymin, ymax
##plt.grid(True)

# === 멀티 그래프 ===
##t = np.arange(0., 5., 0.2)
##plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
##plt.show()

# === 1차 함수 ===
##plt.title('plot')
##y = [k for k in range(20, 100, 3)]
##x = [k for k in range(len(y))]
##plt.plot(x, y)
##plt.grid(True)
##plt.show()

# === Sin() graph ===
##plt.title('Sin Plot')
##plt.grid(True)
##plt.ion()
##
##x = np.linspace(0, 4*np.pi, 200)
##y = np.sin(x)
##
##plt.plot(x, y, 'c--')
##plt.show()


# === 랜덤 그래프 ===
plt.title('Live Random Plot')
plt.grid(True)
plt.ion()

x = []
y = []
k = 0

while True :
    k += 1
    x.append(k)
    y.append(random.randrange(0, 10))

    plt.plot(x, y, 'c-')
    plt.show()
    plt.pause(0.00001)              # 10 마이크로 sec 만큼 쉬도록

    if keyboard.is_pressed("esc") :
        break
