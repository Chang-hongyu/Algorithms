# -*- coding:utf-8 -*-
# /usr/bin/env python
# Author:   Chang
# Function: 
# Version : 1.0
# Contact : 582246340@sjtu.edu.cn

# 类似归并排序，快速排序也是基于分治思想，对数组A[p,r]排序分治思想分为三部分。

# 分解：将数组分为A[p,q-1]和A[q+1,r]，前者元素均小于A[q]，后者元素均大于A[q]，下标q也在这一过程中求出。

# 解决：递归调用快速排序，对两个子数组排序。

# 合并：因为两个子数组是就地排序的，所以他们的合并不需要操作，整个数组A[p,r]已经合并


def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q - 1)
        quickSort(A, q + 1, r)


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


if __name__ == "__main__":
    A = [2, 32, 121, 21, 1, 4, 54, 23, 12, 54, 876, 234, 22, 34, 56, 75, 42, 17]
    quickSort(A, 0, len(A) - 1)
    print(A)
