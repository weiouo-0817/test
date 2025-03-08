
def Towers(n, fr, to, spare , count1):
   
    if n == 1:
        printMove(fr, to)
        count1 += 1
        
    else:
        count1=Towers(n-1, fr, spare, to, count1)
        Towers(1, fr, to, spare, count1)
        Towers(n-1, spare, to, fr, count1)
    return count1
        
    
def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))
    
print( Towers(3, 'A', 'B', 'C',0) )
