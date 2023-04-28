def plassMatrix(X,Y):
    Z = []
    for rowX,rowY in zip(X,Y):
        rowZ = []
        for elementX, elementY in zip(rowX, rowY):
            rowZ.append(elementX + elementY)
        Z.append(rowZ) 
    return Z

def minusMatrix(X,Y):
    Z = []
    for rowX,rowY in zip(X,Y):
        rowZ = []
        for elementX, elementY in zip(rowX, rowY):
            rowZ.append(elementX - elementY)
        Z.append(rowZ) 
    return Z

def divideBy4(X):
    n = len(X)
    A, B, C, D = [], [], [], []
    for (index, raw) in enumerate(X):
        if index < n//2:
            A.append(raw[:n//2])
            B.append(raw[n//2:])
        else:
            C.append(raw[:n//2])
            D.append(raw[n//2:])
    return A, B, C, D

def strassen(X,Y):
    if len(X) == 1:
        return [[X[0][0] * Y[0][0]]]

    A, B, C, D = divideBy4(X)
    E, F, G, H = divideBy4(Y)
    P = [
        strassen(A, minusMatrix(F, H)),
        strassen(plassMatrix(A ,B), H),
        strassen(plassMatrix(C, D), E),
        strassen(D, minusMatrix(G, E)),
        strassen(plassMatrix(A, D), plassMatrix(E, H)),
        strassen(minusMatrix(B, D), plassMatrix(G, H)),
        strassen(minusMatrix(A, C), plassMatrix(E, F)) 
    ]
    A = plassMatrix(minusMatrix(plassMatrix(P[4], P[3]), P[1]), P[5])
    B = plassMatrix(P[0], P[1])
    C = plassMatrix(P[2], P[3])
    D = minusMatrix(minusMatrix(plassMatrix(P[0], P[4]), P[2]), P[6])

    Z = []
    for rowA, rowB in zip(A, B):
        Z.append([*rowA, *rowB])
    

    for rowC, rowD in zip(C, D):
        Z.append([*rowC, *rowD])
    

    return Z

