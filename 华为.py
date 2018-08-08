# 第2题
'''
给定一个价值数组[6,3,5,4,6]
和一个重量数组[2,2,6,5,4]
给定重量不能超过15的情况下
最多能拿到多少价值的东西。
'''
class Solution:
    def __init__(self):
        self.max_money = 0
        self.max_weight = 0
        self.money = []
        self.weight = []

    def Find(self,money,weight,max_sum):
        # if not money or not weight or max_sum<0:
        #     return
        self.money = money
        self.weight = weight
        self.max_weight = max_sum
        for i in range(len(self.weight)):
            self.FindCore1(self.weight[i],self.money[i],i+1)
        print(self.max_money)

    def FindCore1(self, cur_weight_sum, cur_money_sum, begin):
        for i in range(begin,len(self.weight)):
            if cur_weight_sum + self.weight[i] <= self.max_weight:
                if self.money[i] + cur_money_sum > self.max_money:
                    self.max_money = self.money[i] +cur_money_sum
                self.FindCore1(cur_weight_sum + self.weight[i], cur_money_sum + self.money[i], i + 1)

# money = [6,3,5,4,6]
# weigth = [2,2,6,5,4]
# a= Solution()
# a.Find(money,weigth,10)
money = list(map(int,input().split(',')))
weigth = list(map(int,input().split(',')))
max_weigth = int(input())
a = Solution()
a.Find(money,weigth,max_weigth)


