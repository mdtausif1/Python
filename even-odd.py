def count(lst):
    even=0
    odd=0

    for i in lst:
        if i%2==0:
             even+=1
        else:
             odd+=1
    return even, odd
lst=[2,3,4,5,6,7,8,9,1212,343,4546,6789,0]
even,odd=count(lst)
print(even)
print(odd)