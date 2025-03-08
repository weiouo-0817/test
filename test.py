

def Towers(n, fr, to, spare, count):
    def printMove(fr, to):
        print('move from ' + str(fr) + ' to ' + str(to))

    if n == 1:
        printMove(fr, to)
        count+=1
    else:
        count = Towers(n-1, fr, spare, to, count)
        count = Towers(1, fr, to, spare, count)
        count = Towers(n-1, spare, to, fr, count)
    
    return count

print(Towers(10,'A','B','C', 0))

