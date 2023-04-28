def equalToIndex(A, right, left = 0):
    if right == left:
        return False

    mid = (right+left)//2

    if mid < A[mid]:
        right = mid
    elif mid > A[mid]:
        left = mid + 1
    else:
        return True
    max = equalToIndex(A,right,left)

    return max

