def merge_inversions(left, right):
        length = len(left) + len(right)
        i = 0
        j = 0 
        inv = 0
        output_list = []
        for k in range(length):
            if i >= len(left):
                output_list.append(right[j])
                j+=1
            elif j >=  len(right):
                output_list.append(left[i])
                i+=1
            elif left[i] > right[j]:
                output_list.append(right[j])
                j+=1
                inv += len(left) - i 
            else:
                output_list.append(left[i])
                i+=1
        return inv, output_list
        
def find_inversions(a):
    length = len(a)

    if length > 1:
        middle_index = length // 2

        left = a[:middle_index]
        right = a[middle_index:]

        left_inv, left_sorted = find_inversions(left)
        right_inv, right_sorted = find_inversions(right)
        split_inv, all_sorted = merge_inversions(left_sorted, right_sorted)
        return split_inv + right_inv + left_inv, all_sorted
    else:
        return 0 , a            
    
