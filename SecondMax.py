
def second_largest(arr):

    def find_max_and_comp(low, high, arr):
            
            if low >= high:
                return arr[low], []
            
            mid = (high + low) // 2
            x, lst_x = find_max_and_comp(low, mid, arr)
            y, lst_y = find_max_and_comp(mid + 1, high, arr)
            
            if x > y:    
                lst_x.append(y)
                return x, lst_x
            else:
                lst_y.append(x)
                return y, lst_y

    comparisons = find_max_and_comp(0, len(arr) - 1, arr)[1]
    return find_max_and_comp(0, len(comparisons) - 1, comparisons)[0]

