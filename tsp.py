#Here is a 6 nodes tsp problem solved with brute force. 
from itertools import permutations

w=[ [0,0,0,0,0,0,0],[0,9999,1,2,3,4,5],[0,6, 9999, 7,8,9,10],[0,11, 12, 9999,13,14,15],[0,16,17,18,9999,19,20],[0,21,22,23,24,9999,25],[0,26,27,28,29,30,9999]]
a= list(permutations(range(1,6)))
costs=[]

for k in range(len(a)):
    total=0
    for i in range(len(a[k])):
        
        if i==0:  
            continue
    
        else: 
           #this line makes the algorithm take so long so i hide here.
           #if you work with less nodes it would be useful see the steps.
           #print("considering", a[i-1], "to", a[i])
           total=total+w[a[k][i-1]][a[k][i]]
    total=total+w[a[k][len(a[k])-1]][a[k][0]]
    costs.append(total)
    

#This one takes a little less time. And shows the results for all cases.
for k in range(len(a)):
    print(a[k],costs[k])


minn=9999999999

for k in range(len(costs)):
    if(costs[k]<minn):
        minn=costs[k]
        index_of_min=k

print("minimum tour is",a[index_of_min]," with total cost of",minn)
