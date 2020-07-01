def GaussianEliminationBS(A):
    numSwap = 0
    n = A.shape[0]
    
    for i in range(0, n):
        stop = True
        
        for p in range(i, n):    
            
            #print('A[p,i] is', A[p, i])
        
            if A[p, i] != 0 and stop == True:
                stop = False
            
                if p != i:
                    A[[i, p]] = A[[p, i]]
                    numSwap = numSwap + 1
                
        for j in range(i+1, n):
            
            mji = A[j, i]/A[i, i]
            #print('mji is', mji)
            A[j] = A[j] - (mji*A[i])
            #print('A[j] is', A[j])
        #print('A', A, 'in the iteration', i)
            
        if stop == True:
            return 'No unique solution exists 1'
          
        
        
    if A[n-1, n-1] == 0:
        return 'No unique solution exists 2'
    
    xList = list(range(0,n))
    print('A is', A[n-1,n])
    xList[n-1] = (A[n-1,n])/(A[n-1,n-1])
    
    for i in range(n-1, -1, -1):
        xList[i] = (A[i, n] - (sum(A[i, j]*xList[j] for j in range(i+1, n))))/A[i,i]
        
        
    print('# of row swaps:', numSwap)
    return xList
