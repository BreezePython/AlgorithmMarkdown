# [剑指Offer31.栈的压入、弹出序列](https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/solution/jian-zhi-offer31zhan-de-ya-ru-dan-chu-xu-342y/)
> https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/solution/jian-zhi-offer31zhan-de-ya-ru-dan-chu-xu-342y/
> 
> 难度：中等

## 题目：

输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。

例如，序列 {1,2,3,4,5} 是某栈的压栈序列，序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，
但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。

提示：

- 0 <= pushed.length == popped.length <= 1000
- 0 <= pushed[i], popped[i] < 1000
- pushed 是 popped 的排列。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


## 示例：

```
示例 1：
输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
输出：true
解释：我们可以按以下顺序执行：
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

示例 2：
输入：pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
输出：false
解释：1 不能在 2 之前弹出。
```

## 分析

这道题考察队栈的基础知识掌握情况，只要对stack的append与pop操作熟悉，其实是一道很简单的题目。
我们应该明确什么情况返回True，必然是执行最终，poped内为空这个判断条件。
1. 创建一个指针poped[i]初始为0
2. 我们循环pushed列表内每个num，准备一个stack，用于模拟压栈操作，
3. 当num入栈后，判断栈顶元素是否等于poped[i]，若等于则栈顶弹出，i+= 1，重复该步骤知直到栈顶元素不等于poped[i]为止
4. 当i == len(poped)，标识已完全弹出此时返回True
5. 这里使用return not popped而非return False，避免空列表无循环场景。

## 解题：

```python
class Solution:
    def validateStackSequences(self, pushed, popped):
        index, ln, stack = 0, len(popped), []
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[index]:
                stack.pop()
                index += 1
            if index == ln:
                return True
        return not popped
```

欢迎关注我的公众号: **清风Python**，带你每日学习Python算法刷题的同时，了解更多python小知识。

有喜欢力扣刷题的小伙伴可以加我微信（King_Uranus）互相鼓励，共同进步，一起玩转超级码力！

我的个人博客：[https://qingfengpython.cn](https://qingfengpython.cn)

力扣解题合集：[https://github.com/BreezePython/AlgorithmMarkdown](https://github.com/BreezePython/AlgorithmMarkdown)
