number = int(input())
arr_chk = [0]*1000000

def compute(val,i,chk):
    if(val == 1):
        return chk
    if(val %3 == 0):
        val = val/3
        compute(val,i,chk)

    if(val %2 == 0):
        val = val/2
        compute(val,i,chk)
        
    compute(val-1,i,chk)

compute(number,-1,chk)
