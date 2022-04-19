def merge_sort(l):
    if len(l)>1: #checks if this array har more than one elements
        mid=len(l)//2
        L=l[:mid]
        R=l[mid:]
        merge_sort(L)
        merge_sort(R)
        i=j=k=0   #intializes indexes of left and right array to compare leftmost elements
        while i<len(L) and j<len(R):  #checks the leftmost parts of divided arrays
            if L[i]<R[j]:  # checks if leftmost element of left array is less than leftmost element of right array then....
                l[k]=L[i]   #then that element gets added to arr[k] list
                i+=1
            else:
                l[k]=R[j]
                j+=1
            k+=1
        while i<len(L):
            l[k]=L[i]
            i+=1
            k+=1
        while j<len(R): # checks the leftover elements of left divided arrays
            l[k]=R[j]
            j+=1
            k+=1
l=[];
n=int(input("Enter the number of elements in the list: "))
for i in range(n):
    l.append(int(input("Enter the elements: ")))
print("The list of numbers: ",l)
merge_sort(l)
print("The Sorted list: ",l)
