from rawdata import get_raw_vectors, plot_raw_curves, get_parameters
import matplotlib.pyplot as plt

if __name__ == '__main__':

    print('hello')
    # Data path and name
    path = "C:/Users/I0337516/Desktop/"
    nameFile = 'Export3-Trials.xml'

    # build vectors Volume-Time and Flow-Volume
    [vol_VT, time_VT, flow_FV, vol_FV, nameFile] = get_raw_vectors(path, nameFile)

    # plot curves
    plot_raw_curves(vol_VT, time_VT, flow_FV, vol_FV, nameFile)

    # get parameters from SentrySuite output
    get_parameters(path, nameFile)

'''
    # path = 'L:\KKM_LuFu\OfficeData\Biomedical Engineers\Lea\project QC\spirometry_qualityControl\SentrySuite\...
    # XMLExport_Overview\ExamplePlots'
    # nameFile = 'Export3-Trials.xml'
    

    
    # path = "C:/Users/I0337516/Desktop/"
    # nameFile = 'Export3-Trials.xml'
    

    path = "L:\KKM_LuFu\OfficeData\Biomedical Engineers\Lea"
    nameFile = "Eckert151122.xml"
'''

