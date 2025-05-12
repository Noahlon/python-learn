# 给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。

# 请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。

# 注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。

# 测试数据
nums1 = [1, 2, 3, 0, 0, 0]  # nums1 的初始长度为 m + n，其中后 n 个元素为 0
m = 3  # nums1 中的有效元素个数
nums2 = [2, 5, 6]  # nums2 的长度为 n
n = 3  # nums2 中的元素个数

def merge(nums1, m, nums2, n):
    # 指针初始化
    p1 = m - 1  # nums1 的有效元素指针
    p2 = n - 1  # nums2 的有效元素指针
    p = m + n - 1  # 合并后数组的指针

    # 从后向前合并
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    # 如果 nums2 中还有剩余元素，直接复制到 nums1 中
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p -= 1
        p2 -= 1
    # 如果 nums1 中还有剩余元素，不需要处理，因为它们已经在正确的位置上了
# 调用函数
merge(nums1, m, nums2, n)
# 打印合并后的 nums1
print(nums1)  # 输出: [1, 2, 2, 3, 5, 6]        
