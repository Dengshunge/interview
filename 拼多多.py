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


'''
字符串形式的正整数（可能包含前缀0,1<=length<=10),先将这个字符串拆分成两部分，可以在
这两部分中分别加入一个小数点也可以不加入，分别形成一个整数或小数。找出所有“拆分”和“变化”
两次操作后所有可能组合的数目。
要求：
1.对于新形成的整数和小数，不可包含多余的前缀0，比如010和010.1不合法；
2.对于小数，不可包含多余的后缀0，比如0.10不合法；
3..1和1.这样的小数不合法。
实例：
输入123，输出4  [[1,23],[12,3],[1.2,3],[1,2.3]
输入00011，输出2  [[0.001,1],[0,0.011]]

思虑：
当固定从第i个开始切分时，此时第i项的总数为i左边的子串合法的数目乘以i后边的子串合法的数目。
要判断一个子串是否合法，就要举例，抽象，不合法的例子有[0xxx0][xxx00]这两种情况都要特殊考虑。
当[0xxx0]时，不管中间是什么数字，都只能返回1.
当[xxxx0]时，怎么样都加不了小数点，所以返回1.
'''
def Split(s):
    if not s:
        return 0
    count = 0
    for i in range(1,len(s)):
        count += Get(s[:i])*Get(s[i:])
    print(count)

def Get(s):
    if len(s)==1:
        return 1
    elif s[0] == '0':
        if s[-1] == '0':
            return 0
        else:
            return 1
    else:
        if s[-1] == '0':
            return 1
        else:
            return len(s)

s = '10001'
Split(s)

