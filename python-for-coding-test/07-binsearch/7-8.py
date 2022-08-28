N,M = map(int,input().split())
length = list(map(int,input().split()))
'''
4 6
19 15 10 17
'''

# def binsearch(arr, target, start, end) : 
#     if start>end : 
#         return 
#     mid = (start + end)//2
#     if arr[mid] == target : return mid
#     elif arr[mid] > target : binsearch(arr, target, start, arr[mid]-1)
#     else : binsearch(arr, target, arr[mid]+1, end)

total = 0
height = max(length)
while (total < M) : 
    for l in length : 
        tmp = (l-height) if (l-height >0) else 0
        total += tmp
    height -= 1 

print(height)