def subArraySum(arr, n, s):
    g_arr=arr
    for i in range(n):
        total=s
        for j in range(i,n):
            total-=g_arr[j] 
            if(total==0):
                
                return [i+1,j+1]
                
            elif(total>s or total<0):
                
                break
    return [-1]
            


            
        
        
