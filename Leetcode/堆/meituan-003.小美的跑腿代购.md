# [meituan-003.小美的跑腿代购](https://leetcode-cn.com/problems/GXV5dX/solution/pythonji-chu-de-dui-pai-xu-cao-zuo-by-qi-xh1u/)
> https://leetcode-cn.com/problems/GXV5dX/solution/pythonji-chu-de-dui-pai-xu-cao-zuo-by-qi-xh1u/
> 
> 难度：简单

## 题目

小美的一个兼职是美团的一名跑腿代购员，她有 n 个订单可以接，订单编号是 1~n ，但是因为订单的时效性，
他只能选择其中 m 个订单接取，精明的小美当然希望自己总的获利是最大的，已知，一份订单会提供以下信息，跑腿价格 v ，
商品重量 w kg，商品每重 1kg ，代购费用要加 2 元，而一份订单可以赚到的钱是跑腿价格和重量加价之和。
小美可是开兰博基尼送货的人，所以自然不会在意自己会累这种事情。请问小美应该选择哪些订单，使得自己获得的钱最多。
请你按照选择的订单编号的从小到大顺序，如果存在多种方案，输出订单编号字典序较小的方案。

## 格式：
输入：

- 输入第一行包含两个正整数 n，m，表示订单的数量和小美可以接的订单数量。
- 接下来有 n 行，第 i 行表示 i-1 号订单的信息。每行有两个正整数 v 和 w ，表示一个订单的跑腿价格和商品重量。
输出：
- 输出包含 m 个 1~n 之间的正整数，中间用空格隔开，表示选择的订单编号。

## 示例

```
输入：
     5 2
     5 10
     8 9
     1 4
     7 9
     6 10
输出：2 5
```

## 分析
这是一道基础的堆排序问题，不熟悉输入输出的人，估计感觉获取入参和调试比本身题目还难...

- 创建列表
- 获取总订单，及小美可配送的订单数
- 循环获取每单index，并计算每单的最大收益 price + weight * 2
- 由于python不支持大根堆，所以需要将收益转化为负值
- 全部商品入堆后执行循环出堆即可
- 没注意最终要按照订单由小到大排序，提交总失败，这该死的近视...

## 解题

```python
import heapq

total, cur = map(int, input().split())
li, ret = [], []
for i in range(total):
    index = i
    price, wieght = map(int, input().split())
    heapq.heappush(li, [-(price + wieght * 2), index])

for i in range(cur):
    ret.append(heapq.heappop(li)[1])
print(' '.join(str(i + 1) for i in sorted(ret)))
```

欢迎关注我的公众号: **清风Python**，带你每日学习Python算法刷题的同时，了解更多python小知识。

有喜欢力扣刷题的小伙伴可以加我微信（King_Uranus）互相鼓励，共同进步，一起玩转超级码力！

我的个人博客：[https://qingfengpython.cn](https://qingfengpython.cn)

力扣解题合集：[https://github.com/BreezePython/AlgorithmMarkdown](https://github.com/BreezePython/AlgorithmMarkdown)