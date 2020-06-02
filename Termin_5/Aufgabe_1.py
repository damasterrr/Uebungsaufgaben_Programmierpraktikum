#Test commit
#Angabe siehe Moodle

liste = [6, -1, 9, -18, 19, 15, 3, 17, 26, 15]
print(liste)

def swap(li,i,j):
    li[i], li[j] = li[j], li[i]
    return li

def minPos(li, lo, hi):
    min = lo
    for i in range(lo+1,hi+1):
        if li[i]<li[min]:
            min = i
    return min

def selectionSort(li):
    hi = len(li)-1
    for k in range(hi):
        min = minPos(li,k,hi)
        if min != k:
            swap(li,min,k)
    return li

print(selectionSort(liste))