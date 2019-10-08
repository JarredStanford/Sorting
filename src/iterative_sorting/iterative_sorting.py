# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j  

        # TO-DO: swap
        arr[smallest_index], arr[i] = arr[i], arr[smallest_index] 

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    sorts = -1
    while sorts != 0:
        sorts = 0
        for i in range(len(arr)-1):
                if arr[i] > arr[i+1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    sorts += 1   
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

#hacker rank
def area(cases):
    answer = []
    for i in cases:
        dimensions = min(i)
        dimension_total = 0
        for j in range(0, dimensions):
            dimension_total += (i[0] - j) * (i[1] - j)
        answer.append(dimension_total)
    return answer