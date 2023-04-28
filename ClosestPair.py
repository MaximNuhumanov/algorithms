from xmlrpc.client import MAXINT
import MergeSort   

def bruteForce(P):
    min_val = float('inf') 
    bestPair = None
    for i in range(len(P)):
        for j in range(i + 1, len(P)):
            if dist(P[i], P[j]) < min_val:
                min_val = dist(P[i], P[j])
                bestPair = [P[i], P[j]]
  
    return bestPair
  
def findSplitPair(Px, Py, d):
    medianX = Px[:max(1,len(Px)//2)][-1][0]
    Sy = [point for point in Py if point[0] > medianX - d and point[0] < medianX + d]
    best = d
    bestPair = None
    for i in range(len(Sy)-1):
        for j in range(1,min(8,len(Sy)-i)):
            if dist(Sy[i],Sy[i+j]) < best:
                best = dist(Sy[i],Sy[i+j])
                bestPair = [Sy[i],Sy[i+j]]
    return bestPair

def dist(point1, point2):
    return (point1[0] - point2[0])**2 + (point1[1] - point2[1])**2

def minPair(*args):
    bestPair = args[0]
    for i in range(1,len(args)):
        if dist(*bestPair) > dist(*args[i]):
            bestPair = args[i]
    return bestPair

def findPair(Px,Py):
    if len(Px)<= 3:
        return bruteForce(Px)
    else:
        n = len(Px)//2
        Lx = Px[:n]
        Ly = [point for point in Py if point in Px[:n]]
        Rx = Px[n:]
        Ry = [point for point in Py if point in Px[n:]]
        leftPair = findPair(Lx,Ly)
        rightPair = findPair(Rx,Ry)
        d = min(dist(*leftPair), dist(*rightPair))
        splitPair = findSplitPair(Px, Py, d)
        if splitPair:
            return minPair(leftPair, rightPair, splitPair)
        else:
            return minPair(leftPair, rightPair)

def closestPair(P):
    Px = MergeSort.mergeSort(P, lambda x: x[0])
    Py = MergeSort.mergeSort(P, lambda x: x[1])

    return findPair(Px, Py)

