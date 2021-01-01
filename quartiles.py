import sys

mainlist = '\n'.join(sys.stdin.readlines()).split()

#identical list with float
mainlist_i = [int(num) for num in mainlist]
num_elem = mainlist_i[0]
#sort list of numbers
intlist = sorted(mainlist_i[1:])

#determine midpoint of list of numbers
#if even take midpoint between upper and lower lists
midpoint = int(num_elem/2)

#if num_elem % 2 == 0:  
#    median = (intlist[mid] + intlist[mid+1])/2
#if odd take middle position
#else:
#    median = intlist[mid]

def get_median(list_):
    #get median value from a list of integers
    mid = int(len(list_)/2)
    
    #if even length list
    if len(list_) % 2 == 0:
        return (list_[mid-1] + list_[mid])/2
    #if odd take middle position
    else:
        return list_[mid]

#create lower and upper lists to calculate lower and upper quartiles
lower = intlist[:midpoint]
upper = intlist[midpoint:]

lowq= get_median(lower)
median = get_median(intlist)
upq = get_median(upper)

#print(intlist)
#print(upper)
#print(lower)
print(int(lowq))
print(int(median))
print(int(upq))