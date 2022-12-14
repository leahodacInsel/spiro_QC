import xml.etree.ElementTree as ET
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Data path and name
# path = 'L:\KKM_LuFu\OfficeData\Biomedical Engineers\Lea\project QC\SentrySuite\XMLExport_Overview\ExamplePlots'

path = "C:/Users/I0337516/Desktop"
nameFile = 'Export3-Trials.xml'
xmlFile = path + "\\" + nameFile
plotON = 1

# Initialisations
rawVT = []
rawFV = []
time_VT = []
vol_VT = []
strTuplesVT = []
flow_FV = []
vol_FV = []
strTuplesFV = []

# Read XML
tree = ET.parse(xmlFile)
root = tree.getroot()
trials = root.findall("VisitTrees/VisitTree/Levels/LevelTree/Measurements/Measurement/Trials/Trial")
for trial in trials:
    number = int(trial.get('Number'))
    curves = trial.findall("./RawCurveData/Curves/Curve")

    # if there is no raw data available for the trial
    if len(curves) == 0:
        print("Trial number ", number, " doesn't contain raw curve data")

    for curve in curves:
        curveType = curve.get('DataType')
        if curveType == 'RawVolumeTime':
            rawVT.append(curve.find("Data").text)
        elif curveType == 'RawFlowVolume':
            rawFV.append(curve.find("Data").text)


# Transform strings from XML into vectors of floats
for t in range(len(rawVT)):
    xVT = []
    yVT = []
    xFV = []
    yFV = []

    strTuplesVT.append(rawVT[t].split(' '))
    for n in range(len(strTuplesVT[t])-1):
        fTuple = np.fromstring(strTuplesVT[t][n], dtype=float, sep=',')
        xVT.append(fTuple[0])
        yVT.append(fTuple[1])

    strTuplesFV.append(rawFV[t].split(' '))
    for n in range(len(strTuplesFV[t])-1):
        fTuple = np.fromstring(strTuplesFV[t][n], dtype=float, sep=',')
        xFV.append(fTuple[0])
        yFV.append(fTuple[1])

    time_VT.append(xVT)
    vol_VT.append(yVT)

    vol_FV.append(xFV)
    flow_FV.append(yFV)

# mini check data
if vol_FV == vol_VT:
    print("Volume vectors from the V-T curve and from the F-V are identical")
else:
    print("WARNING: Volume vectors from the V-T curve and from the F-V are different")

# Plot
nbResp = len(time_VT)

if plotON:
    fig, axs = plt.subplots(2, nbResp)

    for resp in range(nbResp):
        axs[0, resp].plot(time_VT[resp], vol_VT[resp], "k")
        axs[0, resp].set_title(f'Vol-Time (Resp #{resp})')
        axs[1, resp].plot(vol_FV[resp], flow_FV[resp], "r")
        axs[1, resp].set_title(f'Flow-Volume (Resp #{resp})')

    fig.suptitle(('Example File SentrySuite: ' + nameFile))
    plt.show()







'''
# Animation plot Flow-Volume
# Plotting the Animation
animON = 1

if animON:
    fig, ax = plt.subplots(1, nbResp)

    for resp in range(0, 3):
        inter = 1 # time between each point is drawn
        step_draw = 100 # tep length between two drawn point in the vector

        xx = vol_FV[resp][0::step_draw]
        yy = flow_FV[resp][0::step_draw]

        ax[resp].set(xlim=(min(xx)-1000, max(xx)+1000), ylim=(min(yy)-1000, max(yy)+1000))
        line, = ax[resp].plot([], [], lw=2)


        def init():
            line.set_data([], [])
            return line,

        def animation_frame(i):
            line.set_data(xx[:i], yy[:i])
            return line,

        anim = FuncAnimation(fig, animation_frame, init_func= init, frames=(len(xx)+1), interval=inter, blit=False, repeat=False)
        anim.save('testAnim.gif')
        plt.show()
'''



