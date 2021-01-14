from heapq import heapify,heappush,heappop
from collections import defaultdict


def encode(d):
    heap=[ [frequency ,[symbol,frequency,'']] for symbol,frequency in d.items() ]
    heapify(heap)
    while(len(heap)>1):
        left=heappop(heap)
        right=heappop(heap)
        for i in left[1:]:
            i[2]+='0'
        for i in right[1:]:
            i[2]+='1'
        heappush(heap,[left[0]+right[0]]+left[1:]+right[1:])
    return heap
            
        
        
message="HHyyyyeee!!! Huuuffmann Encoodinng!!"
d=defaultdict(int)
for i in message:
    d[i]=d[i]+1
print(d,"\n\n")

huff = encode(d)
print("\t Si  ","   Fi","  encoded\n")
for i in huff[0]:
    if type(i)==list:
        print("\t",i[0],"\t",i[1],"\t",i[2][::-1],"\t")

