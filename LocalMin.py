
def localMin(A):
    n = len(A)
    mid = n // 2
    i=0
    j=0
    j = A[mid].index(min(*A[mid]))
    if n <= 2:
        i = A.index(min(A[mid],A[mid-1],key = lambda el: el[j]))
    else:
        i = A.index(min(A[mid],A[mid+1],A[mid-1],key = lambda el: el[j]))
    if n <= 2:
        return A[i][j]    
    if i == mid:
        return A[i][j]
    elif i < mid and j < mid:
        result = localMin([row[:mid] for row in A[:mid]])
    elif i < mid and j >= mid:
        result = localMin([row[mid:] for row in A[:mid]])
    elif i > mid and j < mid:
        result = localMin([row[:mid] for row in A[mid + 1:]])   
    elif i > mid and j >= mid:
        result = localMin([row[mid:] for row in A[mid + 1:]])   
    return result



