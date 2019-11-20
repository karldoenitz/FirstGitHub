# -*- coding: utf-8 -*-


def merge_sort(values):
    """ 归并排序

    :param values: 待排序的值
    :type values: list
    :return: 排好序的值
    :rtype: list

    """
    length = len(values)
    if length <= 1:
        return values
    mid = length / 2
    left = merge_sort(values[:mid])
    right = merge_sort(values[mid:])
    return merge(left, right)


def merge(left, right):
    """ 归并

    :param left: 需要归并的数组
    :param right: 需要归并的数组
    :type left: list
    :type right: list
    :return: 归并的结果
    :rtype: list

    """
    ll = len(left)
    lr = len(right)
    i, j = 0, 0
    result = []
    while i < ll and j < lr:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(values, low, high):
    """ 快速排序

    :param values: 待排序的值
    :param low: 首元素下标
    :param high: 尾元素下标
    :type values: list
    :type low: int
    :type high: int
    :return: None

    """
    i, j = low, high
    if i >= j:
        return values
    mid = values[i]
    while i < j:
        while i < j and values[j] >= mid:
            j -= 1
        values[i] = values[j]
        while i < j and values[i] <= mid:
            i += 1
        values[j] = values[i]
    values[i] = mid
    quick_sort(values, low, i - 1)
    quick_sort(values, j + 1, high)


def quick_sort2(values):
    """ 快速排序

    :param values: 待排序的值
    :type values: list
    :return: 排序结果
    :rtype: list

    """
    if len(values) <= 1:
        return values
    else:
        mid = values[0]
        less, greater = [], []
        for i in values[1:]:
            if i <= mid:
                less.append(i)
            else:
                greater.append(i)
        return quick_sort2(less) + [mid] + quick_sort2(greater)


if __name__ == '__main__':
    li = [2, 3, 9, 1, 5, 7, 6, 0, 8]
    print(merge_sort(li))
    li = [2, 3, 9, 1, 5, 7, 6, 0, 8]
    print(quick_sort2(li))
    quick_sort(li, 0, 8)
    print(li)
