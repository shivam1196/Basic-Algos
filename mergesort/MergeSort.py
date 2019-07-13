def merge_sort(list):

    if len(list) <= 1:
        return list


    mid = len(list) // 2

    left = list[:mid]

    right = list[mid:]


    left = merge_sort(left)

    right = merge_sort(right)


    return merged(left,right)



def merged(left,right):

    merged_list = []

    left_index = 0

    right_index = 0


    while left_index < len(left) and right_index < len(right):

        if( left[left_index] > right[right_index]):

            merged_list.append(right[right_index])

            right_index +=1

        else:

            merged_list.append(left[left_index])

            left_index +=1


    merged_list += left[left_index:]

    merged_list += right[right_index:]


    return merged_list




if __name__ == "__main__":

    print merge_sort([1,5,2,4,7,9,0,6])