# [剑指OfferII042.最近请求次数](https://leetcode-cn.com/problems/H8086Q/solution/shua-chuan-jian-zhi-offer-day18-zhan-ii-de51o/)
> https://leetcode-cn.com/problems/H8086Q/solution/shua-chuan-jian-zhi-offer-day18-zhan-ii-de51o/
> 
> 难度：简单

## 题目
写一个 RecentCounter 类来计算特定时间范围内最近的请求。
请你实现 RecentCounter 类：
- RecentCounter() 初始化计数器，请求数为 0 。
- int ping(int t) 在时间 t 添加一个新请求，其中 t 表示以毫秒为单位的某个时间，并返回过去 3000 毫秒内发生的所有请求数（包括新请求）。
确切地说，返回在 [t-3000, t] 内发生的请求数。

**保证 每次对 ping 的调用都使用比之前更大的 t 值。**

提示：
- 1 <= t <= 10 ^ 9
- 保证每次对 ping 调用所使用的 t 值都 严格递增
- 至多调用 ping 方法 10 ^ 4 次

## 示例

```
输入：
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
输出：
[null, 1, 2, 3, 3]

解释：
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [1]，范围是 [-2999,1]，返回 1
recentCounter.ping(100);   // requests = [1, 100]，范围是 [-2900,100]，返回 2
recentCounter.ping(3001);  // requests = [1, 100, 3001]，范围是 [1,3001]，返回 3
recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002]，范围是 [2,3002]，返回 3
```

## 分析
坦白说第一次见到这个题，真的没有往队列上面去想。既然是ping递增的，然后左边界又确定是t - 3000，那不是标准的二分查找么？
创建一个数组，然后每次执行二分即可。
当然这里有个小技巧，既然每次t都是递增的，我们可以初始化一个left，每次更新left，无需每次左边界从0开始二分.

但根据题意分析，我们还可以使用队列来完成这道题目，由于每次获取的都是t - 3000的数值。
所以在加入t后，我们持续判断队首数值，如果小于t- 3000就出队，然后返回队列的长度。

## 二分解题

**Python:**

```python
class RecentCounter:
    def __init__(self):
        self.req = []
        self.left = 0

    def ping(self, t):
        self.req.append(t)
        self.left = bisect.bisect_left(self.req, t - 3000, self.left)
        return len(self.req) - self.left
```

**Java:**

```java
class RecentCounter {
    private ArrayList<Integer> arr;
    private int left = 0;
    
    public RecentCounter() {
        arr = new ArrayList<>();
    }

    public int ping(int t) {
        return bisect(t);
    }

    private int bisect(int t){
        arr.add(t);
        int right = arr.size();
        while (left < right) {
            int mid = (right - left) / 2 + left;
            if (arr.get(mid) < t - 3000){
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return arr.size() - left;
    }
}
```

## 队列解题

**Python:**

```python
class RecentCounter:
    def __init__(self):
        self.req = deque()

    def ping(self, t):
        self.req.append(t)
        while self.req[0] < t - 3000:
            self.req.popleft()
        return len(self.req)
```

**Java:**

```java
class RecentCounter {
    private Queue<Integer> queue;

    public RecentCounter() {
        queue = new LinkedList<>();
    }

    public int ping(int t) {
        queue.add(t);
        while (queue.peek() < t - 3000) {
            queue.poll();
        }
        return queue.size();
    }
}
```

这道题使用二分和队列到底哪一种效率高呢？
首先定义 ping调用10 ^ 4 次，即O(n) = 10000,然后计算总执行的时间复杂度。
先来说说空间复杂度，对于空间复杂度，那肯定是二分会高一些，因为队列存在出队的情况。
- 二分 O(n)
- 队列 最坏O(3000) 最好O(1) 最好即每次t都比上一次大3000

再来说说时间复杂度：
- 二分 总的时间复杂度为 O(nlogn),执行N次，每次log(n)。
- 队列 粗算O(n)，最好呢？t每次比上一次大1，O(7000),如果ping调用3000次，最好为O(1).


欢迎关注我的公众号: **清风Python**，带你每日学习Python算法刷题的同时，了解更多python小知识。

有喜欢力扣刷题的小伙伴可以加我微信（King_Uranus）互相鼓励，共同进步，一起玩转超级码力！

我的个人博客：[https://qingfengpython.cn](https://qingfengpython.cn)

力扣解题合集：[https://github.com/BreezePython/AlgorithmMarkdown](https://github.com/BreezePython/AlgorithmMarkdown)