import sys, time
def issub(a):
    flag = 1
    for i in range(len(a)-1):
        if(a[i] != a[len(a)-1-i]):
            flag = 0
    return flag

def subbrute(a):
    max = 0
    werd = ""
    for i in range(len(a)-1):
        for j in range(len(a), i, -1):
            #print(a[i:j])
            #print(j-i)
            if(issub(a[i:j])):
               if j-i > max:
                   werd = a[i:j]
                   max = j-i
    return max,werd

def subdyn(a):
    #creating table to be used dynamically
    tab = [[ False for x in range(len(a))] for y in range(len(a))]
    #initialize diagonals to 1 (all substrings with length 1 are palindromes)
    for i in range(len(a)):
        tab[i][i] = True   
    """do it for length 2
    for i in range(len(a)-1):
        if(a[i]==a[i+1]):
            tab[i][i+1] = True"""
    max = 1
    #using previously calculated values, determine max palindrome substring
    for inc in range(1,len(a)):
        for i in range(len(a)-inc):
            j = i+inc
            if(a[i] == a[j] and tab[i+1][j-1]==True):
                tab[i][j] = True
                max = inc+1
    return max

def main():
    i =0
    werd = ""
    z,max = 0,0
    for a in sys.argv:
        if i==1:
            #print(subbrute(a))
            print(subdyn(a))
        i+=1
    #print(max);print(werd)
start_time = time.time()
main()

print(time.time() - start_time, "seconds")
