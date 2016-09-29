import time

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
with open('IntegerArray.txt') as f:
    arr = [int(line.rstrip()) for line in f]

t1=time.time()
arr2 = sorted(arr)
t2=time.time()
print t2-t1

t1=time.time()
main(arr,100000)
t2=time.time()
print t2-t1
