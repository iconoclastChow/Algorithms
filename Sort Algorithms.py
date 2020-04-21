'''
Sort Algorithms
Author: Chow
Date: 2020/4/20

原理：
	冒泡排序：相邻元素两两对比，将值大(小)的元素位置后移；
	选择排序：特定位置的元素与其他元素对比，确保该位置元素最大(小)；
	插入排序：列表分为两部分，前者为已有序列表，将后者无序元素挨个和前者中元素比较，放置对应位置；
	快速排序：找一个基准元素，将所有小于基准元素的放置一侧，大于(等于)基准元素的放置另一侧，递归，直至列表大小为0或者1，即肯定有序；
	希尔排序：插入排序的改进版，先按一定间隔分组，每组插入排序，然后缩小间隔继续，直至间隔大小为1；
	归并排序：将数组分解最小之后，然后合并两个有序数组，基本思路是比较两个数组的最前面的数，谁小就先取谁，
			取了后相应的指针就往后移一位，然后再比较，直至一个数组为空，最后把另一个数组的剩余部分复制过来；
注意：排序一般需要多层循环，先定义外层循环，然后定义内层循环。
'''


# 冒泡排序
def bubble_sort(alist):
    # 因为冒泡排序每次将最大的数移动到最后，因此需要n-1次循环即可，因为其他排好后，第一个即是最小元素
    for i in range(len(alist)-1):  # n-1次循环
        # 每次循环旨在将前n-i个元素中的最大元素放置至最后
        # 由于是两两相邻比较，即拿到一个元素与该元素后元素比较，因此循环至n-i-1即可
        for j in range(len(alist)-i-1):
            # 核心思想为：将大的数向后移动
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]


# 选择排序
def select_sort(alist):
    # 第一次将首位置换成最小值，以此类推，共需要n-1次
    for i in range(len(alist)-1):
        # 拿到第i个元素，与其之后的元素挨个比较，把较小值放置i位
        for j in range(i+1, len(alist)):
            if alist[i] > alist[j]:
                alist[i], alist[j] = alist[j], alist[I]


# 插入排序
def insert_sort(alist):
    # 首次分为第一个元素和其余元素两部分，从第二个元素开始，与前面元素挨个比较，直到找到属于自己的位置。因此外层需要n-1次
    for i in range(len(alist)-1):
        # 将i+1位置的元素，向前挨个比较，找到自己的位置。即由第i个元素依次向前直至第0个元素
        for j in range(i+1, 0, -1):
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]



"""
 快速排序，和前面三种思想上有较大不同，不再是外层循环次数下，内层循环实现将某一元素放至某位置。其核心思想是以某个值作为基准值，
 将小于该值的元素放至左侧（交换位置），大于该值的元素放至右侧（交换位置），然后分别将左右两侧列表递归再次排序。
	lists = [30, 24, 5, 58, 18, 36, 12, 42, 39]
	for i in quick_sort(lists, 0, len(lists) - 1):
	    print(i, end=" ")
为了实现递归而 ->不用重新定义左右列表变量<- ，将左右下标作为参数
"""
def quick_sort(alist, left, right):
    # 1. 递归退出条件
    if left >= right:
        return
    # 2. 核心：
    # 以首值为基准值，判断元素大小交换位置
    mid_value = alist[0]
    while left < right:
        # 循环找出小于基准值的元素放至左侧
        while left < right and alist[right] >= mid_value:
            right -= 1
        alist[left] = alist[right]
        # 循环找出大于基准值的元素放至右侧
        while left < right and alist[left] <= mid_value:
            left += 1
        alist[right] = alist[left]
    # 循环结束后，left=right，该位置放基准值
    alist[left] = mid_value
    # 对基准值左右两侧元素递归快排
    quick_sort(alist, 0, left-1)
    quick_sort(alist, left+1, right)
    return alist



"""
希尔排序，是插入排序的改进版，先以一定步长将列表分为多个子列表，然后对每个子列表插入排序。执行完成后，缩小步长继续，直至步长为0。
这里可能会有疑惑，最终步长为1时就是插入排序，为什么还要多几次步长不为1的循环？
实际上，前面知道插入排序后面每个元素向前插入时，需要从前往后遍历比较，但如果比首个元素都小则可直接插入。我们可以理解为，对大部分
无序随机数列，步长取合适时，时间复杂度会有很大改善。
"""
def shell_sort(alist):
    # 取首次步长为列表长度一半
    gap = len(alist) // 2
    while gap > 0:
        # 内层类似插入排序，只不过步长为gap
        # 循环次数：gap->len
        for i in range(gap, len(alist)):
            # 内层：将第i个元素依次与前面元素比较调整位置，不过步长为gap
            for j in range(i, 0, -gap):
                if alist[j] < alist[j-gap]:
                    alist[j], alist[j-gap] = alist[j-gap], alist[j]
        # 排序后gap减小
        gap = gap // 2



"""
归并排序，如名字一样，是将序列一边合并一边排序。其核心思想为：
先将序列递归的折半拆分，直到长度为1，然后执行排序后作为本层递归的返回。
需注意归并排序每层递归都有返回值，因此比前面几个排序耗费空间。
"""
def merge_sort(alist):
    # 1. 递归退出条件
    if len(alist) <= 1:
        return alist  # 注意有返回值
    # 2.核心思想
    # 二分分解
    num = len(alist) // 2
    # 取左右两截（内部递归）
    left_list = merge_sort(alist[0:num])
    right_list = merge_sort(alist[num:])
    # 返回根据左右两截实现的排序序列
    return merge(left_list, right_list)


def merge(left_list, right_list):
    # 排序核心：将左右两个有序数列内依次取满足大小比较的元素，放置新序列
    # 定义左右两序列的其实元素位置
    left, right = 0, 0
    # 定义一个新序列接收排序后序列
    result = list()
    # 循环退出条件：一侧遍历完，将另一侧剩余元素直接添加至后面
    while left < len(left_list) and right < len(right_list):
        if left_list[left] < right_list[right]:
            result.append(left_list[left])
            left += 1
        else:
            result.append(right_list[right])
            right += 1
    result += left_list[left:]
    result += right_list[right:]
    return result

