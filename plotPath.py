# -*- coding: utf-8 -*-
"""
Klasse zum plotten der Pfade, welche vom Python-Slicer als *.csv-Datei ausgegeben wurden

@author: Timo Schmid
"""



import sys
import csv
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


class PlotPath:



    def __init__(self):

        self.csvFileName = 'D:\Eigene Dateien\Arbeit\Python-Slicer\outputs\path.csv'

    def readCSV(self):
    
        #Create empty lists
        csvData = []
        X_off = []
        Y_off = []
        Z_off = []
        X_on = []
        Y_on = []
        Z_on = []


        with open(self.csvFileName, 'r') as csvFile:
            csvReader = csv.reader(csvFile, delimiter=' ')
            for csvRow in csvReader:
                csvData.append(csvRow)
    
        # Get X, Y, Z
        csvData = np.array(csvData)
        csvData = csvData.astype(np.float)


        #for idx in range(len(csvData)):

        #    #Check if Extruder is off (0) or on (1)
        #    if csvData[idx,4] == 0.0:  
        #        X_off.append(csvData[idx,1])
        #        Y_off.append(csvData[idx,2])
        #        Z_off.append(csvData[idx,3])
        #    elif csvData[idx,4] == 1.0:
        #        X_on.append(csvData[idx,1])
        #        Y_on.append(csvData[idx,2])
        #        Z_on.append(csvData[idx,3])
        #    else:
        #        print("Fehler in CSV-Datei: Extruder weder an noch aus.")


        X, Y, Z = csvData[:,1], csvData[:,2], csvData[:,3]
    
        # Plot X,Y,Z
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        ax.plot(X,Y,Z, c='red', alpha=1)

        ##Plot points where extruder on (red) and off (blue)
        #ax.scatter(X_on, Y_on, Z_on, c='red', alpha=1)
        #ax.scatter(X_off, Y_off, Z_off, c='blue', alpha = 1)
    
        plt.show()

        print("plotting finished.")

        return 1;



