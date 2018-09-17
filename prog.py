import math

def find_min_denom(n,sorted_denom):
    ans = -1
    if(sorted_denom[0]<n):
        return ans
    else:
        l_bound =0
        u_bound =len(sorted_denom)

        while(l_bound < u_bound and l_bound !=u_bound-1):
            mid = int((l_bound+u_bound)/2)
            if(sorted_denom[mid] > n):
                u_bound = mid
            elif(sorted_denom[mid] < n):
                l_bound = mid
            elif(sorted_denom[mid] == n):
                ans = sorted_denom[mid]
                break
        if(sorted_denom[l_bound]<n):
            ans = sorted_denom[l_bound]
        return ans

def find_rec_rem(sorted_denom,num,idx):
    
    rem = num % sorted_denom[idx]
    idx_new = find_min_denom(rem,sorted_denom)
    if(idx_new == -1):
        return num
    else:
        find_rec_rem(sorted_denom,rem,idx_new)

    


def rec_div(sorted_denom,k):
    l = len(sorted_denom)
    zero_rem = False
    rem = -1
    for i in range(0,l):
        rem = find_rec_rem(sorted_denom,k,i)
        if(rem == 0):
            zero_rem = True
            break
    if(zero_remainder):
        return 0
    else:
        return rem
    print ("k",k)
    

def find_min(denom_list):
    ans = -1
    found = False
    denom_list = sorted(denom_list,key=int)
    max_num = denom_list[len(denom_list)-1]
    for i in range(max_num+1,max_num+10):
        remainder = rec_div(denom_list,i)
        if(remainder != 0):
            found = True
            ans = i
            break
    if(found):
        print (ans)
    else:
        print ("none")
            
            
