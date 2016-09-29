def main(arr,siz):
    global comp
    if siz == 1:
        return arr
    comp+=siz-1
    p = Pivot(arr,siz)
    arr[0], arr[p] = arr[p], arr[0]
    p = arr[0]
    i = 0
    for j in xrange(1,siz):
        if arr[j] < p:
            arr[j], arr[i+1] = arr[i+1], arr[j]
            i+=1
    arr[0], arr[i] = arr[i], arr[0]
    if siz-i-1 != 0:
        arr[i+1:] = main(arr[i+1:],siz-i-1)
    if i != 0:
        arr[0:i] = main(arr[0:i],i)
    return arr

def Pivot(arr,siz):
    if siz%2 == 0:
        mid = (siz/2) - 1
    else:
        mid = siz/2

    nums = [arr[0],arr[mid],arr[siz-1]]
    med = sorted(nums)[1]
    if med == arr[0]:
        return 0
    if med == arr[mid]:
        return mid
    return siz-1

comp = 0
with open('IntegerArray.txt') as f:
    arr = [int(line.rstrip()) for line in f]

main(arr,10000)
print comp