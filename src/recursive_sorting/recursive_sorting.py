# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    x = ""
    print(arrA)
    while arrA and arrB:
        if arrA[0] > arrB[0]:
            merged_arr.append(arrB[0])
            arrA.pop(0)
        if arrA[0] < arrB[0]:
            merged_arr.append(arrB[0])
            arrB.pop(0)
        if arrA[0] == arrB[0]:
            merged_arr.append(arrA[0])
            merged_arr.append(arrB[0])
            arrA.pop(0)
            arrB.pop(0)
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[mid:]
        right = arr[:mid]
        merge_sort(left)
        merge_sort(right)
        x = 0
        y = 0
        z = 0
        while x < len(left) and y < len(right):
            if left[x] < right[y]:
                arr[z] = left[x]
                x += 1
            else:
                arr[z] = right[y]
                y += 1
            z += 1
            print(arr)
        while x < len(left):
            arr[z] = left[x]
            x += 1
            z += 1
            print(arr)
        while y < len(right):
            arr[z] = right[y]
            y += 1
            z += 1
            print(arr)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
