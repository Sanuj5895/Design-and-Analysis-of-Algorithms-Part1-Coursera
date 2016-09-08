import numpy as np

def main(arr,siz):
    global inv
    if siz==1:
        return arr
    else:
        left = main(arr[0:siz/2],siz/2)
        right = main(arr[siz/2:],siz-siz/2)
    d = [0]*siz
    i=j=0
    for k in xrange(siz):
        if i == len(left):
            d[k:] = right[j:]
            break
        if j == len(right):
            d[k:] = left[i:]
            break

        if left[i] < right[j]:
            d[k] = left[i]
            i+=1
        else:
            d[k] = right[j]
            j+=1
            inv+=len(left) - i
    return d

inv = 0
arr = [6,5,4,3,2,1]
print main(arr,6),inv