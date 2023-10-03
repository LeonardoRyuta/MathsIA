import matplotlib.pyplot as plt

x_axis_graph1 = [0]
y_axis_graph1 = [2.2]

x_axis_graph2 = [0]
y_axis_graph2 = [2.2]

x_axis_graph3 = [0, 0.07 ,0.10, 0.13, 0.17, 0.20, 0.27, 0.30, 0.33, 0.37, 0.43, 0.47, 0.50, 0.53, 0.60, 0.63, 0.67]
y_axis_graph3 = [2.2, 2.19, 2.16, 2.13, 2.03, 1.96, 1.87, 1.79, 1.57, 1.44, 1.29, 1.15, 0.82, 0.62, 0.42, 0.18, 0.00]

x_axis_graph4 = [0]
y_axis_graph4 = [2.2]

def graph1():
    dvdt = -9.81
    h = 0.01
    counter = 0

    while True:
        if counter == 100:
            break

        t = x_axis_graph1[counter]
        d = y_axis_graph1[counter]

        newT = t + h
        newD = d + h * (dvdt * t)

        if newD < 0:
            newD = 0

        x_axis_graph1.append(newT)
        y_axis_graph1.append(newD)

        counter += 1
    
    plt.plot(x_axis_graph1, y_axis_graph1, label='h = 0.01')


def graph2():
    dvdt = -9.81
    h = 0.001
    counter = 0

    while True:
        if counter == 1000:
            break

        t = x_axis_graph2[counter]
        d = y_axis_graph2[counter]

        newT = t + h
        newD = d + h * (dvdt * t)

        if newD < 0:
            newD = 0

        x_axis_graph2.append(newT)
        y_axis_graph2.append(newD)

        counter += 1
    
    plt.plot(x_axis_graph2, y_axis_graph2, label='h = 0.001')

def graph3():
    for i in range(100):
        time = x_axis_graph4[i]

        newTime = time + 0.01
        newHeight = (0.5 * (-9.81 * time ** 2))+2.2

        if newHeight < 0:
            newHeight = 0

        x_axis_graph4.append(newTime)
        y_axis_graph4.append(newHeight)
    plt.plot(x_axis_graph4, y_axis_graph4, label='h = theoretical')

graph1()
graph2()
graph3()

plt.plot(x_axis_graph3, y_axis_graph3, label='experiment')

plt.xlabel('time (s)')
plt.ylabel('height (m)')
plt.legend()
plt.show()