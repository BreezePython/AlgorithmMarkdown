# [LCP30.魔塔游戏](https://leetcode-cn.com/problems/p0NxJO/solution/lcp-30-mo-ta-you-xi-biao-zhun-de-xiao-ge-4gkk/)
> https://leetcode-cn.com/problems/p0NxJO/solution/lcp-30-mo-ta-you-xi-biao-zhun-de-xiao-ge-4gkk/
> 
> 难度：中等

## 题目：

小扣当前位于魔塔游戏第一层，共有 N 个房间，编号为 0 ~ N-1。每个房间的补血道具/怪物对于血量影响记于数组 nums，其中正数表示道具补血数值，即血量增加对应数值；负数表示怪物造成伤害值，即血量减少对应数值；0 表示房间对血量无影响。

小扣初始血量为 1，且无上限。假定小扣原计划按房间编号升序访问所有房间补血/打怪，为保证血量始终为正值，小扣需对房间访问顺序进行调整，每次仅能将一个怪物房间（负数的房间）调整至访问顺序末尾。请返回小扣最少需要调整几次，才能顺利访问所有房间。若调整顺序也无法访问完全部房间，请返回 -1。

提示：

1 <= nums.length <= 10^5

-10^5 <= nums[i] <= 10^5

## 示例：

示例 1：

输入：nums = [100,100,100,-250,-60,-140,-50,-50,100,150]

输出：1

解释：初始血量为 1。至少需要将 nums[3] 调整至访问顺序末尾以满足要求。

示例 2：

输入：nums = [-200,-300,400,0]

输出：-1

解释：调整访问顺序也无法完成全部房间的访问。

## 分析

这道题看似题目很长，其实仔细分析，就是一个贪心算法。

思路上可以使用现成的堆排序，也可以自己创建列表列表每次删除最小值即可。

这里恶心的一点是，初始血量为1，然后雪莲需要始终保持在正值，绕来绕去没什么意义。

直接设置初始值为0，值不小于0就完了。

方便的一点是这道题是小根堆，python默认的堆排序就是小根堆，解题会方便很多。

## 解题1：堆排序

```python
import heapq


class Solution:
    def magicTower(self, nums):
        if sum(nums) < 0: 
            return -1
        hurts = []
        blood = 0
        counts = 0
        for i in nums:
            blood += i
            if i < 0:
                heapq.heappush(hurts, i)   
            if blood < 0:
                counts += 1
                blood -= heapq.heappop(hurts)
        return counts
```

## 解题2：列表删除最小值

```python
class Solution:
    def magicTower(self, nums):
        if sum(nums) < -1:
            return -1
        hurts = []
        counts = 0
        blood = 0
        for i in nums:
            if i < 0:
                hurts.append(i)
            blood += i
            if blood < 0:
                hurt = min(hurts)
                hurts.remove(hurt)
                blood -= hurt
                counts += 1
        return counts
```

欢迎关注我的公众号: **清风Python**，带你每日学习Python算法刷题的同时，了解更多python小知识。

有喜欢力扣刷题的小伙伴可以加我微信（King_Uranus）互相鼓励，共同进步，一起玩转超级码力！

我的个人博客：[https://qingfengpython.cn](https://qingfengpython.cn)

力扣解题合集：[https://github.com/BreezePython/AlgorithmMarkdown](https://github.com/BreezePython/AlgorithmMarkdown)
