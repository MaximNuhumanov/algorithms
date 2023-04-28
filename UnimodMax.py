def unimodMax(A, right, left = 0):
    if right == left:
        return A[left]
    mid = (right+left)//2

    if A[mid] > A[mid + 1]:
        right = mid
    else:
        left = mid + 1
    max = unimodMax(A,right,left)
    return max

