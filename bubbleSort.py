#03 Using Brute Force implement Bubble Sort
def BubbleSort(a,n):
    for i in range (n-1):
        for j in range(n-1-i):
            if(a[j+1]<a[j]):
                a[j],a[j+1] = a[j+1],a[j]

a = [12,30,43,56]
BubbleSort(a,len(arr))
print(a)