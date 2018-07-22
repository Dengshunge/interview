'''
数组里的“山谷”是指一个数组A中的连续子数组B满足一下条件： a) B.length>=3 b) 存在i满足0<i<B.length-1并且B[0]>B[1]>...>B[i-1]>B[i]<B[i+1]<...<B[B.length-1] 
现在给定一个整型数组A，找出数组A里的最长“山谷”B的长度，如果没有，则输出0

我感觉自己这种方法复杂了，网上有种方法是穷举所有符合的值，暴力解法，感觉这种会简单点
'''
def Find_shangu(lis):
    start,end = 0,0
    i = 1
    max_va = 0
    length = len(lis)
    Flag1,Flag2 = True,True#用于判断是否都进入两个循环
    while i < length:
        start = i-1
        while i < length and lis[i] <= lis[i-1]:
            Flag1 = False
            i += 1
        while i < length and lis[i] >= lis[i-1]:
            Flag2 = False
            i += 1
        end = i-1
        result = end-start+1
        if not Flag1 and not Flag2 and result > max_va:
            max_va = result
        Flag1, Flag2 = True, True
    if max_va >= 3:
        return max_va
    else:
        return 0

if __name__ == '__main__':
    # 下面几行的输入处理复杂了，其实就一条语句就OK
    # lis = input()[1:-1]
    lis = input()
    if lis[0] == '[':
        lis = lis[1:]
        lis = lis[:-1]
        lis = list(map(int,lis.split(',')))
    print(Find_shangu(lis))
    
    
'''
当给定长度为n的字符串s1时，可以构成无限长的p,p[i]=s1[i%n]。
现在要通过这个字符串p，来求出最小长度字符串s1

例如p='abcabc'，则s1为'abc'
例如p='111111',则s1为'1'

这道理利用逐一比较，本来想用KMP的，但后来发现不太对，因为abca是输出abc
'''
def Short(p):
    Flag = True
    i = 1
    while i < len(p):
        if p[i] == p[0]:
            if Check(p,i):
                print(p[:i])
                Flag = False
                break
        i += 1
    if Flag:
        print(p)

def Check(p,i):
    j = 0
    while i<len(p):
        if p[j] != p[i]:
            return False
        j += 1
        i += 1
    return True

s1 = 'bababc'
Short(s1)
