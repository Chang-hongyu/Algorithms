# -*- coding:utf-8 -*-
# Author:   Chang
# Function: 输入一个主串t 一个模式串p 若p在t中出现，则返回其具体位置，负责返回-1
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn

# 暴力求解法 若不匹配，则i后移一位，j移到第一位，继续遍历，时间复杂度O(MN)

# 考虑：i可以不动，只需要移动j即可，利用已匹配部分的有效信息，保持指针i不回溯，通过修改j指针，让模式尽可能移动到有效的位置。

# 关键在于当某一个字符与主串不匹配时，我们应该找出j指针应该移动到哪里，即维护一个next数组。

# 当匹配失败时，j要移动的下一个位置k，存在着这样的性质：最前面的k个字符和j之前的最后k个字符是一样的，即p[0~k-1]==p[j-k~j-1]

# 即当t[i]!=p[j]时，有t[i-j~i-1]==p[0~j-1]

# 且p[0~k-1]==p[j-k~j-1]。则有t[i-k~i-1]==p[0~k-1]

# next[j]=k表示，当t[i]!=p[j]时，j指针的下一个位置。当j为0时，不可能再移动了，则应该要i指针后移，所以有next[0]=-1

# 当j为1的时候，j指针一定是移动到0位置的。且当p[k]==p[j]时，有next[j+1]=next[j]+1

# 若p[k]!=p[j]，则k=next[k] 注意如果p[j]==p[next[j]]，则需要跳过,具体实现在getNext()函数中。


class Solution:

    def getNext(self, p):
        char_p = list(p)
        next = [0 for _ in range(len(char_p))]
        # 初始化，第一个位置的next值为-1
        next[0] = -1
        j = 0
        # k实时变化，记录上一个位置next指向的元素
        k = -1
        while j < len(char_p) - 1:
            if k == -1 or p[j] == p[k]:
                j += 1
                k += 1
                if p[j] == p[k]:
                    next[j] = next[k]
                else:
                    next[j] = k
            else:
                k = next[k]
        return next

    def KMP(self, t, p):
        char_t = list(t)
        char_p = list(p)
        # 主串的位置
        i = 0
        # 模式串的位置
        j = 0
        # 模式串的更新指针位置列表
        next = self.getNext(p)
        while i < len(char_t) and j < len(char_p):
            # 当j为-1时，要移动的是i，当然j也要归0
            # 当对应位置相等时，i和k都加1，两种情况可以合并处理
            if j == -1 or t[i] == p[j]:
                i += 1
                j += 1
            else:
                # 更新j的指针位置
                j = next[j]
        if j == len(char_p):
            return i - j
        else:
            return -1


if __name__ == "__main__":
    t1 = "ABACBCDHI"
    p1 = "ABAB"
    t2 = "abbaabbbabaa"
    p2 = "bbabaa"
    ans1 = Solution().KMP(t1, p1)
    ans2 = Solution().KMP(t2, p2)
    print(ans1)
    print(ans2)
