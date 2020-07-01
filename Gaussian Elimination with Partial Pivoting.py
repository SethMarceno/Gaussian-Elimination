def GaussianEliminationPP(A):
    numSwap = 0                           
    n = A.shape[0] 
    xList = list(range(0,n))

    for i in range(0, n):
                                   
        for p in range(i, n):
                                   
            if A[p,i] > A[i,i]:
                
                A[[i,p]] = A[[p,i]]
                numSwap = numSwap + 1  
                        
            if A[p,i] == 0:
                return 'No unique solution exists 1'
            
        for j in range(0, n):
            m = A[j,i]/A[i,i]
            A[j] = A[j] - (m*A[i]) 
            
    if A[n-1,n-1] == 0:
        return 'No unique solution exists 2'

    print('A before back sub:', A)
    xList[n-1] = A[n-1,n]/A[n-1,n-1]
    
    for i in range(n-2, 0, -1):
        xList[i] = (A[i, n] - sum(A[i,j]*xList[j] for j in range(i+1, n)))/(A[i,i])

        
    
    print('# of row exchanges:', numSwap)            
    return xList
