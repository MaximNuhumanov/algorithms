def mergeSort(a, key = lambda x: x):
    length = len(a)

    if length > 1:
        middle_index = length // 2

        first_half = a[:middle_index]
        second_half = a[middle_index:]

        first_half = mergeSort(first_half, key)
        second_half = mergeSort(second_half, key)

        i = 0
        j = 0 
        output_list = []
        for k in range(length):
            if i >= len(first_half):
                output_list.append(second_half[j])
                j+=1
            elif j >=  len(second_half):
                output_list.append(first_half[i])
                i+=1
            elif key(first_half[i]) > key(second_half[j]):
                output_list.append(second_half[j])
                j+=1
            else:
                output_list.append(first_half[i])
                i+=1
        return output_list
    else:
        return a      
    
