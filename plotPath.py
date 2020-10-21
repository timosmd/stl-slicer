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


def readCSV(filename):
    
    csvData = []
    with open(filename, 'r') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=' ')
        for csvRow in csvReader:
            csvData.append(csvRow)
    
    # Get X, Y, Z
    csvData = np.array(csvData)
    csvData = csvData.astype(np.float)
    X, Y, Z = csvData[:,1], csvData[:,2], csvData[:,3]
    
    # Plot X,Y,Z
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(X, Y, Z, color='white', edgecolors='grey', alpha=0.5)
    ax.scatter(X, Y, Z, c='red')
    plt.show()

    print("plotting finished.")

def main():
	
    csvFileName = 'D:/Eigene Dateien/Arbeit/Python-Slicer/stl-slicer/outputs/path.csv'
    readCSV(csvFileName)


if __name__ == '__main__':
	main()


