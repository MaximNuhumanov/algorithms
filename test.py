import Inversions
import Karatsuba
import MergeSort
import SecondMax
import Strassen
import ClosestPair
import UnimodMax
import ElementEqualToIndex
import random
import LocalMin

print("Inversions O(nlog(n))")
A = [6,5,4,3,2,1,0]
print("A =", A)
print("Count of inversions -",Inversions.find_inversions(A)[0])

print("\nKaratsuba O(n^1.58)")
A = 287769407308846640970310151509826255482575362419155842891311909556878670000425352112987881085839680
B = 13306827740879180856696800391510469038934180115260
print("a =", A)
print("b =", B)
print("a * b =",Karatsuba.karatsuba(A,B))

print("\nMergeSort O(nlog(n))")
A = [2,5,6,3,4,1,7,8,4.5]
print("A =", A)
print("A sorted -",MergeSort.mergeSort(A))    

print("\nSecondMax n + log(n) + 2")
A = [2,11,5,6,3,4,1,7,8,9,10,5,7,8,10,4,2,11,5,6,3,4,1,7,8,9,10,5,7,8,10,4]
print("A =", A)
print("second largest -",SecondMax.second_largest(A))    

print("\nStrassen O(n^(2.8))")
#Длина стороны матрицы n кратна 2
X =[
    [1 ,5 ,6 ,7 ],
    [3 ,4 ,5 ,1 ],
    [13,40,1 ,2 ],
    [2 ,3 ,11,2 ]
]
Y =[
    [7 ,7 ,6 ,7 ],
    [6 ,5 ,5 ,14],
    [1 ,4 ,3 ,4 ],
    [23,33,1 ,2 ]
]
print("X =", X)
print("Y =", Y)
print("X * Y =", Strassen.strassen(X, Y))

print("\nClosestPair O(nlog(n))")
A = [
    (0,1),
    (10,0),
    (5,12),
    (6,3),
    (66,8),
    (4,7),
    (3,19),
    (7,3.1),
    (10,0.1)
]
print("A =", A)
print("ClosestPair in A -",ClosestPair.closestPair(A))

print("\nUnimodMax O(log(n))")
A = [0,1,2,10,9,8,7,6,5,4,3]
print("A =", A)
print("Max =",UnimodMax.unimodMax(A,len(A)-1))

print("\nElementEqualToIndex O(log(n))")
A = [-1,0,1,2,3,4,5,6,7,8]
B = [-1,0,1,2,3,4,6,8]
print("A =", A)
print("B =", B)
print("A -",ElementEqualToIndex.equalToIndex(A,len(A)))
print("B -",ElementEqualToIndex.equalToIndex(B,len(B)))

print("\nLocalMin O(log(n))")
N = 5
l = list(range(1, N**2 + 1))
random.shuffle(l)
num = 0
print("A =")
A=[[ l[(len(l)//N) * i + j] for j in range(0,5)] for i in range(0,5)]
for row in A:
    print(*row, sep="\t")
print("localMin =",LocalMin.localMin(A))