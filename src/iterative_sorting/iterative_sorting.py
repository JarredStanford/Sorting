# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
             



        # TO-DO: swap




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    sorts = -1
    while sorts != 0:
        sorts = 0
        for i in range(len(arr)):
            try:
                if arr[i] > arr[i+1]:
                    x = arr[i]
                    arr.remove(x)
                    arr.insert(i+1, x)
                    sorts += 1
            except:
                continue
            
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr