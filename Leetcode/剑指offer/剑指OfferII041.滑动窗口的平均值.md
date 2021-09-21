# [剑指OfferII041.滑动窗口的平均值](https://leetcode-cn.com/problems/qIsx9U/solution/shua-chuan-jian-zhi-offer-day20-dui-lie-09ber/)
> https://leetcode-cn.com/problems/qIsx9U/solution/shua-chuan-jian-zhi-offer-day20-dui-lie-09ber/
> 
> 难度：简单

## 题目
给定一个整数数据流和一个窗口大小，根据该滑动窗口的大小，计算滑动窗口里所有数字的平均值。

实现 MovingAverage 类：
- MovingAverage(int size) 用窗口大小 size 初始化对象。
- double next(int val) 成员函数 next 每次调用的时候都会往滑动窗口增加一个整数，
请计算并返回数据流中最后 size 个值的移动平均值，即滑动窗口里所有数字的平均值。

提示：
- 1 <= size <= 1000
- -10 ^ 5 <= val <= 10 ^ 5
- 最多调用 next 方法 10 ^ 4 次

## 示例

```
输入：
inputs = ["MovingAverage", "next", "next", "next", "next"]
inputs = [[3], [1], [10], [3], [5]]
输出：
[null, 1.0, 5.5, 4.66667, 6.0]

解释：
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // 返回 1.0 = 1 / 1
movingAverage.next(10); // 返回 5.5 = (1 + 10) / 2
movingAverage.next(3); // 返回 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // 返回 6.0 = (10 + 3 + 5) / 3
```

## 分析
这是一道比较明朗的队列题目。
这里只需要关注下，由于每次都需要求滑动窗口里所有数字的平均值。
所以我们应该初始化一个sum，用于队列中所有数的总和。
当队列满时，sum -= 出队的数字
当队列未满时，sum += 本次入队的数字
这样就可以通过O(1)的时间去计算平均值了。

## 解题

**Python:**

```python
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.sum = 0

    def next(self, val: int) -> float:
        self.sum += val
        self.queue.append(val)
        if len(self.queue) > self.size:
            self.sum -= self.queue.popleft()
        return self.sum / len(self.queue)
```

**Java:**

```java
class MovingAverage {
    private int length;
    private Queue<Integer> queue;
    private double sum = 0;


    public MovingAverage(int size) {
        length = size;
        queue = new LinkedList<>();
        sum = 0;
    }

    public double next(int val) {
        if (queue.size() == length) {
            sum -= queue.remove();
        }
        queue.add(val);
        sum += val;
        return sum / queue.size();
    }
}
```

欢迎关注我的公众号: **清风Python**，带你每日学习Python算法刷题的同时，了解更多python小知识。

有喜欢力扣刷题的小伙伴可以加我微信（King_Uranus）互相鼓励，共同进步，一起玩转超级码力！

我的个人博客：[https://qingfengpython.cn](https://qingfengpython.cn)

力扣解题合集：[https://github.com/BreezePython/AlgorithmMarkdown](https://github.com/BreezePython/AlgorithmMarkdown)