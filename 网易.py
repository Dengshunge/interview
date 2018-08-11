# 算法第二题

class Solution:
    def Adjust(self,first,high):
        if len(high) != first[0]:
            return
        num = 0
        insteability = max(high)-min(high)
        action = []
        while num < first[1] and insteability > 0 and insteability != 1:
            tower_max, tower_min = high.index(max(high)), high.index(min(high))
            high[tower_max] -= 1
            high[tower_min] += 1
            insteability =max(high)-min(high)
            num += 1
            action.append([tower_max+1,tower_min+1])
        print(insteability,num)
        for i in action:
            print(' '.join(map(str,i)))

first = [5,5]
high = [8,1,8,8,8]
# first = list(map(int,input().strip().split()))
# high = list(map(int,input().strip().split()))
a = Solution()
a.Adjust(first,high)

