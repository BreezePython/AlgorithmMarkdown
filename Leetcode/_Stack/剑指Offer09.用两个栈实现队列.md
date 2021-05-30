# [剑指Offer09.用两个栈实现队列](https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/solution/jian-zhi-offer09yong-liang-ge-zhan-shi-x-hybm/)
> https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/solution/jian-zhi-offer09yong-liang-ge-zhan-shi-x-hybm/
> 
> 难度：简单

## 题目：

用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，

分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead操作返回 -1 )

提示：
- 1 <= values <= 10000
- 最多会对 appendTail、deleteHead 进行 10000 次调用

## 示例：

```
示例 1：

输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]
示例 2：

输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]
```

## 分析

首先扫盲队列与栈的知识：
- 队列：先进先出
- 栈：后进先出

那么，为什么要双栈实现队列呢？其实大家只要思考下：
我们准备两个栈add_stack和pop_stack：
1. 先把1,2,3先挨个加入add_stack栈
2. 下来依次将add_stack栈内的数据出栈，同时将出栈的数据加入pop_stack栈中
3. 1、2执行完成后，add_stack变成了空，pop_stack栈中存储的数据成了[3,2,1]
4. 那么下次出栈时，直接将pop_stack的栈内数据弹出，不就成了列队的先进先出！

关于什么时候执行2步骤需要注意下：
1. 如果pop_stack栈中有数据，就直接return pop的数据 
2. 如果pop_stack栈中没有数据
   a. add_stack也没有数据，return -1 
   b. add_stack有数据，执行上面步骤2，将add_stack数据加入pop_stack中
3. 返回pop_stack栈弹出的数据

## 解题：

```python
class CQueue:
    def __init__(self):
        self.add_stack, self.pop_stack = [], []

    def appendTail(self, value: int) -> None:
        self.add_stack.append(value)

    def deleteHead(self) -> int:
        if self.pop_stack:
            return self.pop_stack.pop()
        if not self.add_stack:
            return -1
        while self.add_stack:
            self.pop_stack.append(self.add_stack.pop())
        return self.pop_stack.pop()
```

欢迎关注我的公众号: **清风Python**，带你每日学习Python算法刷题的同时，了解更多python小知识。

有喜欢力扣刷题的小伙伴可以加我微信（King_Uranus）互相鼓励，共同进步，一起玩转超级码力！

我的个人博客：[https://qingfengpython.cn](https://qingfengpython.cn)

力扣解题合集：[https://github.com/BreezePython/AlgorithmMarkdown](https://github.com/BreezePython/AlgorithmMarkdown)
