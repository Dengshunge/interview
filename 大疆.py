'''
给你一个数组，求一个k值，使得前k个数的方差+后面n-k个数的方差最小，并说明时间复杂度

暂时没想到更好的办法，只能一个一个遍历。时间复杂度是O(N^2)。
'''

import numpy as np

def find_max_Var(lis):
    if not isinstance(lis,list) or len(lis) <=1:
        return None,None
    min_index = -1
    min_val = np.inf
    for k in range(1,len(lis)):
        a = np.var(lis[:k])
        temp = np.var(lis[:k]) + np.var(lis[k:])
        if temp < min_val:
            min_index = k
            min_val = temp
    return min_index,min_val

if __name__ == '__main__':
    lis=[10,5,8,9,2,4,1]
    min_index,min_val = find_max_Var(lis)
    print(min_index,min_val)


