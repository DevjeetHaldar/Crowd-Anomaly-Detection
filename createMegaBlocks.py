import cv2
import numpy as np
import math
import itertools


def createMegaBlocks(motionInfoOfFrames,noOfRows,noOfCols):
   
    n = 2
    megaBlockMotInfVal = np.zeros(((int(noOfRows/n)),(int(noOfCols/n)),len(motionInfoOfFrames),8))
    
    frameCounter = 0
    
    for frame in motionInfoOfFrames:
        
        for index,val in np.ndenumerate(frame[...,0]):
            
            temp = [list(megaBlockMotInfVal[int(index[0]/n)][int(index[1]/n)][frameCounter]),list(frame[index[0]][index[1]])]
           
            megaBlockMotInfVal[int(index[0]/n)][int(index[1]/n)][frameCounter] = np.array(list(map(sum, zip(*temp))))

        frameCounter += 1
    print(((int(noOfRows/n)),(int(noOfCols/n)),len(motionInfoOfFrames)))
    return megaBlockMotInfVal

def kmeans(megaBlockMotInfVal):
   
    cluster_n = 5
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    flags = cv2.KMEANS_RANDOM_CENTERS
    codewords = np.zeros((len(megaBlockMotInfVal),len(megaBlockMotInfVal[0]),cluster_n,8))
    
    for row in range(len(megaBlockMotInfVal)):
        for col in range(len(megaBlockMotInfVal[row])):
            #print("megaBlockMotInfVal ",(row,col),"/n/n",megaBlockMotInfVal[row][col])
            
            ret, labels, cw = cv2.kmeans(np.float32(megaBlockMotInfVal[row][col]), cluster_n, None, criteria,10,flags)
            #print(ret)
            #if(ret == False):
            #    print("K-means failed. Please try again")
            codewords[row][col] = cw
            
    return(codewords)
