# interview
汇总这一路以来的笔试题和面试题

## 大疆
笔试：机器学习算法

两道算法题：
1. 对n个数的序列:a[0],a[1],...,a[n-1]，n大于4，则一定存在i,j,p,q，使得i<j<p<q，并且a[j]-a[i]+a[q]-a[p]的值最大。求出这个最大值，并说明复杂度
2. 对n个数的序列:a[0],a[1],...,a[n-1]，求一个整数k，使得前k个数的方差和后面n-k个数的方差之和最小，并说明算法复杂度。

其它还考察了BP网络的推导，adagrad,leakyRelu等内容，神经网络的内容偏多。  
对于机器学习，主要考察了SVM，LR的内容。还有sigmoid函数。

[这里有专门的帖子记录了试题](https://www.nowcoder.com/discuss/85562)

[为什么一些机器学习模型需要对数据进行归一化？](https://www.cnblogs.com/bonelee/p/7124695.html)  
1. 提高收敛速度，若不采用归一化，模型很难收敛甚至不收敛。
2. 归一化有可能提高模型的精度。
3. 归一化的类型:1.线性归一化（即减去最小值然后除以范围）（适合数据比较集中的情况）；2.z分数归一化（即0均值）（经过处理的数据符合正太分布）；3.非线性归一化（利用数学函数进行映射）（适合数据分化比较大的场景）

## 拼多多
感觉有点难度，自己还是太菜了，应该多刷题，好好总结思路。  
4道编程题。
1. 数组里的“山谷”是指一个数组A中的连续子数组B满足一下条件：
a) B.length>=3
b) 存在i满足0<i<B.length-1并且B[0]>B[1]>...>B[i-1]>B[i]<B[i+1]<...<B[B.length-1]
现在给定一个整型数组A，找出数组A里的最长“山谷”B的长度，如果没有，则输出0

例如输入[4,3,2,5,3,1,4,8],输出5

2. 当给定长度为n的字符串s1时，可以构成无限长的p,p[i]=s1[i%n]。现在要通过这个字符串p，来求出最小长度字符串s1。
例如p='abcabc'，则s1为'abc'，再例如p='111111',则s1为'1'

3. 在二维坐标里面，A位于原点，每次都能向左或向右移动，但移动的第n步的位移是n，例如第5步时移动的长度为5。当给定一个B的左边时，求A移动B最少需要多少步。例如B=6时，最少移动3步，B=2时，最少移动3步

4. 给定一个电话号码（长度小于9），前面可以填充0。可以换数字，换数字的费用是旧数字和新数字差值的绝对值，例如旧数字是1，新数字是5，则费用是4。  
现在给定一个电话号码，给需要相同的数字的个数，就换数字最小的费用。  
例如电话号码是454678，需要相同数字的个数是4，则变换后的电话号码是444478，费用是3


字符串形式的正整数（可能包含前缀0,1<=length<=10),先将这个字符串拆分成两部分，可以在这两部分中分别加入一个小数点也可以不加入，分别形成一个整数或小数。找出所有“拆分”和“变化”两次操作后所有可能组合的数目。
要求：
1. 对于新形成的整数和小数，不可包含多余的前缀0，比如010和010.1不合法；
2. 对于小数，不可包含多余的后缀0，比如0.10不合法；
3. .1和1.这样的小数不合法。
实例：
输入123，输出4  [[1,23],[12,3],[1.2,3],[1,2.3]  
输入00011，输出2  [[0.001,1],[0,0.011]]  

思虑：
当固定从第i个开始切分时，此时第i项的总数为i左边的子串合法的数目乘以i后边的子串合法的数目。  
要判断一个子串是否合法，就要举例，抽象，不合法的例子有[0xxx0][xxx00]这两种情况都要特殊考虑。  
当[0xxx0]时，不管中间是什么数字，都只能返回1.  
当[xxxx0]时，怎么样都加不了小数点，所以返回1.  

## 华为
考了三道题，其中第一道是将大写转换成小写，小写转换成大写，其他字符不变。  
第二道题是普通的背包问题。为此，我准备研究了下背包问题，[可见这篇文章的分析](https://blog.csdn.net/rubik_wong/article/details/54854547)
