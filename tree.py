# -*- coding: utf-8 -*-


pre_order = []
in_order = []
post_order = []
level_order = []


class Queue(object):
    def __init__(self):
        self.__queue = []

    def is_empty(self):
        """ 判断队列是否为空

        :return: True or False
        :rtype: bool

        """
        return len(self.__queue) == 0

    def push(self, value):
        """ 进入队列

        :param value: 入队列的值
        :return: None

        """
        self.__queue.append(value)

    def pop(self):
        """ 出队列

        :return: 出队列的值
        :rtype: Any

        """
        if self.is_empty():
            return None
        value = self.__queue[0]
        self.__queue = self.__queue[1:]
        return value

    def size(self):
        """ 获取当前队列大小

        :return: 队列大小
        :rtype: int

        """
        return len(self.__queue)


class Stack(object):
    def __init__(self):
        self.__stack = []

    def is_empty(self):
        """ 判断栈是否为空

        :return: True or False
        :rtype: bool

        """
        return len(self.__stack) == 0

    def push(self, value):
        """ 入栈

        :param value: 入队列的值
        :return: None

        """
        self.__stack.append(value)

    def pop(self):
        """ 出栈

        :return: 出栈的值
        :rtype: Any

        """
        if self.is_empty():
            return None
        value = self.__stack[-1]
        self.__stack = self.__stack[:-1]
        return value


class Node(object):
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None


# -------------------------------------------------------递归法----------------------------------------------------------
def search_tree_pre(node):
    """ 前序遍历

    :param node: 二叉树节点
    :type node: Node
    :return: None

    """
    pre_order.append(node.value)
    if node.left is not None:
        search_tree_pre(node.left)
    if node.right is not None:
        search_tree_pre(node.right)


def search_tree_in(node):
    """ 中序遍历

    :param node: 二叉树节点
    :type node: Node
    :return: None

    """
    if node.left is not None:
        search_tree_in(node.left)
    in_order.append(node.value)
    if node.right is not None:
        search_tree_in(node.right)


def search_tree_post(node):
    """ 后序遍历

    :param node: 二叉树节点
    :type node: Node
    :return: None

    """
    if node.left is not None:
        search_tree_post(node.left)
    if node.right is not None:
        search_tree_post(node.right)
    post_order.append(node.value)


# ------------------------------------------------------非递归法---------------------------------------------------------

def get_pre_order(node):
    """ 前序遍历非递归

    :param node: 二叉树节点
    :type node: Node
    :return: 遍历结果
    :rtype: list

    """
    result = []
    stack = Stack()
    while not stack.is_empty() or node is not None:
        while node is not None:
            result.append(node.value)
            stack.push(node)
            node = node.left
        if not stack.is_empty():
            node = stack.pop()
            node = node.right
    return result


def get_in_order(node):
    """ 中序遍历非递归

    :param node: 二叉树节点
    :type node: Node
    :return: 遍历结果
    :rtype: list

    """
    result = []
    stack = Stack()
    while not stack.is_empty() or node is not None:
        while node is not None:
            stack.push(node)
            node = node.left
        if not stack.is_empty():
            node = stack.pop()
            result.append(node.value)
            node = node.right
    return result


def get_post_order(node):
    """ 二叉树后序遍历非递归

    :param node: 二叉树节点
    :type node: Node
    :return: 遍历结果
    :rtype: list

    """
    result = []
    stack1 = Stack()
    stack2 = Stack()
    stack1.push(node)
    while not stack1.is_empty():
        temp = stack1.pop()
        stack2.push(temp)
        if temp.left is not None:
            stack1.push(temp.left)
        if temp.right is not None:
            stack1.push(temp.right)
    while not stack2.is_empty():
        result.append(stack2.pop().value)
    return result


def search_tree_level(node):
    """ 层次遍历

    :param node: 二叉树节点
    :type node: Node
    :return: None

    """
    queue = Queue()
    queue.push(node)
    while not queue.is_empty():
        n = queue.pop()
        level_order.append(n.value)
        if n.left is not None:
            queue.push(n.left)
        if n.right is not None:
            queue.push(n.right)


def get_tree_width(node):
    """ 获取二叉树宽度

    :param node: 二叉树根节点
    :type node: Node
    :return: 二叉树宽度
    :rtype: int

    """
    width = 0
    queue1 = Queue()
    queue2 = Queue()
    queue2.push(node)
    while not queue2.is_empty():
        width = queue2.size() if queue2.size() > width else width
        while not queue2.is_empty():
            queue1.push(queue2.pop())
        while not queue1.is_empty():
            n = queue1.pop()
            if n.left is not None:
                queue2.push(n.left)
            if n.right is not None:
                queue2.push(n.right)
    return width


def get_tree_depth(node):
    """ 获取二叉树深度

    :param node: 二叉树根节点
    :type node: Node
    :return: 二叉树深度
    :rtype: int

    """
    depth = 0
    queue1 = Queue()
    queue2 = Queue()
    queue2.push(node)
    while not queue2.is_empty():
        depth += 1
        while not queue2.is_empty():
            queue1.push(queue2.pop())
        while not queue1.is_empty():
            n = queue1.pop()
            if n.left is not None:
                queue2.push(n.left)
            if n.right is not None:
                queue2.push(n.right)
    return depth


def mirror_tree(node):
    """ 翻转二叉树

    :param node: 二叉树节点
    :type node: Node
    :return: None

    """
    node.left, node.right = node.right, node.left
    if node.left is not None:
        mirror_tree(node.left)
    if node.right is not None:
        mirror_tree(node.right)


def init_tree(values):
    """ 构建二叉搜索树

    :param values: 数值列表
    :type values: list
    :return: 二叉树根节点
    :rtype: Node

    """
    if len(values) == 0:
        return None
    root = Node()
    root.value = values[0]
    for i in values[1:]:
        insert_to_tree(root, i)
    return root


def insert_to_tree(node, value):
    """ 向二叉树插入一个节点

    :param node: 二叉树节点
    :type node: Node
    :param value:
    :type value: int
    :return: None

    """
    if node.value is None:
        node.value = value
        return
    if value > node.value:
        if node.right is None:
            node.right = Node()
        insert_to_tree(node.right, value)
    if value < node.value:
        if node.left is None:
            node.left = Node()
        insert_to_tree(node.left, value)


def main():
    values = [6, 7, 4, 5, 3, 9, 1, 0, 2]
    root = init_tree(values)
    search_tree_pre(root)
    print(pre_order)
    print(get_pre_order(root))
    search_tree_in(root)
    print(in_order)
    print(get_in_order(root))
    search_tree_post(root)
    print(post_order)
    print(get_post_order(root))
    search_tree_level(root)
    print(level_order)
    print(get_tree_width(root))
    print(get_tree_depth(root))


if __name__ == '__main__':
    main()
