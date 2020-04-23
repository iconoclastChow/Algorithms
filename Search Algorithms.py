"""
Title: 搜索算法
Author: Chow
Date: April 22, 2020

"""


"""
二分查找：
	找中间值将序列（等分地）分成两段，判断要找的元素比中间值大还是小，小的话在左侧段继续二分查找，大的在右侧。
	最坏时间复杂度：O(logn)；最优时间复杂度：O(1)；
"""
	def binary_search(alist, item):
	    """非递归实现二分查找"""
	    # 定义出始末下标
	    start = 0
	    end = len(alist)-1
	    # 循环结束条件：二分查找的序列长度为大于0
	    while start <= end:
	        # 找到中间值下标
	        mid_point = (start+end) // 2
	        if item == alist[mid_point]:
	            return True
	        elif item > alist[mid_point]:
	            start = mid_point+1
	        else:
	            end = mid_point-1
	    return False


	def binary_search(alist, item):
    """递归实现二分查找"""
    # 递归结束条件：二分到长度为0时说明未找到
    if len(alist) == 0:
        return False
    mid_point = len(alist) // 2
    if alist[mid_point] == item:
        return True
    if alist[mid_point] > item:
        return binary_search(alist[:mid_point], item)
    else:
        return binary_search(alist[mid_point+1:], item)


# 广度优先搜索——使用二叉树
	class Node(object):
	    """二叉树节点"""
	    # 二叉树节点三个属性：值，左子节点，右子节点
	    def __init__(self, item):
	        self.item = item
	        self.lchild = None
	        self.rchild = None

	class Tree(object):
	    """(满)二叉树"""
	    # 二叉树初始化时需要根节点
	    def __init__(self):
	        self.root = None

	    def add(self, item):
	        """添加元素"""
	        node = Node(item)
	        if self.root is None:
	            self.root = node
	        else:
	            # 核心思想：将头节点加入至队列，先判断左节点，为空则将节点放置左侧；若不为空，判断右节点，为空则放置右节点。若左右都不为空，分别将左右
	            # 节点加入至队列尾，再取队列首节点继续上面逻辑
	            queue = list()
	            queue.append(self.root)
	            while queue:
	                cur = queue.pop(0)  # 注意是取第0个元素，与下面的append相斥
	                if cur.lchild is None:
	                    cur.lchild = node
	                    return
	                if cur.rchild is None:
	                    cur.rchild = node
	                    return
	                # 左右都不为空，将左右节点放置队列尾
	                queue.append(cur.lchild)
	                queue.append(cur.rchild)


	    def preorder(self, root):
	        """递归实现先序遍历"""
	        if root is None:
	            return
	        print(root.item)
	        self.preorder(root.lchild)
	        self.preorder(root.rchild)

	    def inorder(self, root):
	        """递归实现中序遍历"""
	        if root is None:
	            return
	        self.inorder(root.lchild)
	        print(root.item)
	        self.inorder(root.rchild)

	    def postorder(self, root):
	        """递归实现后续遍历"""
	        if root is None:
	            return
	        self.postorder(root.lchild)
	        self.postorder(root.rchild)
	        print(root.item)


	    def breadth_travel(self, root):
	        """广度优先遍历"""
	        if root is None:
	            return
	        queue = list()  # stack = list()，广度用队列、深度用栈
	        queue.append(root)  # stack.qppend(root)
	        while queue:
	            node = queue.pop(0)  # 队列拿出队首元素；深度优先node = stack.pop()，拿出栈顶元素
	            print(node.item)
	            if node.lchild is not None:
	                queue.append(node.lchild)  # stack.append(node.rchild)，出栈反向哦
	            if node.rchild is not None:
	                queue.append(node.rchild)  # stack.append(node.lchild)，出栈反向哦


	if __name__ == '__main__':
	    elements = range(10)
	    tree = Tree()
	    for elem in elements:
	        tree.add(elem)
	    tree.preorder(tree.root)

