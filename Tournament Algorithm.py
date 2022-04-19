def secondSmallestNum(A):
   comparisonCount = 0
   ind = range(0,len(A))

   knockout = [[] for i in ind]
   while len(ind) > 1:
     ind_1 = []
     odd = len(ind) % 2
     for i in range(0, len(ind) - odd, 2):
            findex = ind[i]
            sindex = ind[i+1]
            comparisonCount += 1
            if A[findex] < A[sindex]:
               ind_1.append(findex)
               knockout[findex].append(A[sindex])
            else:
               ind_1.append(sindex)
               knockout[sindex].append(A[findex])
     if odd == 1:
            ind_1.append(ind[i+2])
     ind = ind_1
   print ("Smallest number is ", A[ind[0]])
   print ("Total comparisons are ", comparisonCount)
   print ("Nodes knocked off by the smallest is ", knockout[ind[0]], "\n")

   a = knockout[ind[0]]
   if len(a) > 0:
    v= a[0]
    for i in range(1,len(a)):
           comparisonCount += 1
           if v > a[i]:
               v = a[i]
    print ("Second smallest element is ", v)
A= [8, 3, 6, 15, 10, 8, 11, 1, 4]
print(secondSmallestNum(A))
                    
            
