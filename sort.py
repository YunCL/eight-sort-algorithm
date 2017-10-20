# -*- coding:utf-8 -*-
def insert_sort(lists):
    # 插入排序
    for i in range(1,len(lists)):
        key = lists[i]
        j = i-1
        while j >= 0:
            if lists[j] > key:
            	lists[j+1] = lists[j]
            	lists[j] = key
            j -= 1
    return lists

def bubble_sort(lists):
    for i in range(len(lists)-1):
        for j in range(i+1,len(lists)):
            if lists[i] > lists[j]:
                lists[i],lists[j] = lists[j],lists[i]
    return lists

def select_sort(lists):
    for i in range(len(lists)):
        minx = i
        for j in range(i+1,len(lists)):
        	if lists[minx] > lists[j]:
        	    minx = j
        lists[minx] ,lists[i] = lists[i],lists[minx]
    return lists

def quick_sort(lists,left,right):
    if left >= right:
        return lists
    low = left
    high = right
    key = lists[low]
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    #print left,right
    lists[right] = key
    quick_sort(lists,low,left-1)
    quick_sort(lists,left+1,high)
    return lists

def heap_sort(lists):
    def build_heap(lists,size):
        for i in range(size/2)[::-1]:
            adjust_heap(lists,i,size)

    def adjust_heap(lists,i,size):
        lchild = 2*i+1
        rchild = 2*i+2
        min = i
        if i < size/2:
            if lchild < size and lists[lchild] < lists[min]:
                min = lchild
            if rchild < size and lists[rchild] < lists[min]:
                min = rchild
            if min != i:
                lists[min],lists[i] = lists[i],lists[min]
                adjust_heap(lists,min,size)
                
    size = len(lists)
    build_heap(lists,size)
    for i in range(size)[::-1]:
        lists[0],lists[i] = lists[i],lists[0]
        adjust_heap(lists,0,i)
    return lists

def shell_sort(lists):
    d = len(lists)/2
    while d:
        for i in range(d):
            j = i+d            
            while j < len(lists):
                k = j-d
                key = lists[j]
                while k >= 0:
                    if lists[k] > key:
                        lists[k+d] = lists[k]
                        lists[k] = key
                    k -= d
                j += d
        print d
        print lists
        d /= 2
    return lists

def merge_sort(lists):
    def merge(m1,m2):
        i,j = 0,0
        result = []
        while i < len(m1) and j < len(m2):
            if m1[i] > m2[j]:
                result.append(m2[j])
                j += 1
            else:
                result.append(m1[i])
                i += 1
        result += m1[i:]
        result += m2[j:]
        return result
    if len(lists) <= 1:
        return lists
    num = len(lists)/2
    m1 = merge_sort(lists[:num])
    m2 = merge_sort(lists[num:])
    return merge(m1,m2)

import math
def radix_sort(lists,radix):
    k = int(math.ceil(math.log(max(lists),radix)))
    bucket = [[] for i in xrange(radix)]
    for i in xrange(1,k+1):
        for val in lists:
            bucket[val%(radix**i)/(radix**(i-1))].append(val)
        del lists[:]
        for bc in bucket:
            lists.extend(bc)
            del bc[:]
    return lists

