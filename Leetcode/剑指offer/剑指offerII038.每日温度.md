# [剑指OfferII038.每日温度](https://leetcode-cn.com/problems/iIQa4I/solution/shua-chuan-jian-zhi-offer-day18-zhan-ii-mdv06/)
> https://leetcode-cn.com/problems/iIQa4I/solution/shua-chuan-jian-zhi-offer-day18-zhan-ii-mdv06/
> 
> 难度：中等

## 题目：
请根据每日 气温 列表 temperatures ，重新生成一个列表，要求其对应位置的输出为：
要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。

提示：
- 1 <= temperatures.length <= 10 ^ 5
- 30 <= temperatures[i] <= 100


## 示例：

```
示例 1:
输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]

示例 2:
输入: temperatures = [30,40,50,60]
输出: [1,1,1,0]

示例 3:
输入: temperatures = [30,60,90]
输出: [1,1,0]
```

## 分析
这是一道比较典型的单调栈问题。
根据题意我们需要找到下一个更高的气温，然后计算两者相差的天数。
这里注意，如果气温在这之后都不会升高，则将该位置用0来代替。
1. 根据以上的信息，我们可以先创建一个temperatures等长的全零数组，然后初始化一个栈
2. 这里注意由于需要返回相差天数，所以栈中需要保存元素下标来实现天数计算。
3. 下来循环temperatures进行栈的操作，循环过程中，持续判断当前下标温度与栈顶下标温度的大小差别
4. 如果当前下标的温度大于栈顶下标的温度，表示找到了下一个更大的温度，弹出栈顶下标，计算天数差别，
   更新ret[栈顶下标] = 当前下标 - 栈顶下标
5. 否则将当前下标加入栈顶
6. ret中没有更新的元素，表示未找到更高的温度，最终返回ret即可。

这里模拟题目中示例1，给出栈和ret的变化，供大家参考：
- 输入: temperatures = [73,74,75,71,69,72,76,73]
- 输出: [1,1,4,2,1,1,0,0]

|下标 -> 元素 | 栈           | 等待天数                   | 说明            |
| --------  | ------------ | ------------------------ | --------------- |
| 0 -> 73   | [73]         | [0, 0, 0, 0, 0, 0, 0, 0] | 0入栈            |
| 1 -> 74   | [74]         | [1, 0, 0, 0, 0, 0, 0, 0] | 0出栈、1入栈      |
| 2 -> 75   | [75]         | [1, 1, 0, 0, 0, 0, 0, 0] | 1出栈、2入栈      |
| 3 -> 71   | [75, 71]     | [1, 1, 0, 0, 0, 0, 0, 0] | 3入栈            |
| 4 -> 69   | [75, 71, 69] | [1, 1, 0, 0, 0, 0, 0, 0] | 4入栈            |
| 5 -> 72   | [75, 72]     | [1, 1, 0, 2, 1, 0, 0, 0] | 3、4出栈，5入栈    |
| 6 -> 76   | [76]         | [1, 1, 4, 2, 1, 1, 0, 0] | 2、5出栈、6入栈    |
| 7 -> 73   | [76, 73]     | [1, 1, 4, 2, 1, 1, 0, 0] | 7入栈            |

## 解题：

```python []
class Solution:
    def dailyTemperatures(self, temperatures):
        stack, ret = [], [0] * len(temperatures)
        for i, num in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < num:
                index = stack.pop()
                ret[index] = i - index
            stack.append(i)
        return ret
```

```java []
class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<Integer> stack = new Stack<>();
        int[] ret = new int[temperatures.length];
        for (int i = 0; i < temperatures.length; i++) {
            while (!stack.empty() && temperatures[stack.peek()] < temperatures[i]) {
                int index = stack.pop();
                ret[index] = i - index;
            }
            stack.push(i);
        }
        return ret;
    }
}
```


欢迎关注我的公众号: **清风Python**，带你每日学习Python算法刷题的同时，了解更多python小知识。

有喜欢力扣刷题的小伙伴可以加我微信（King_Uranus）互相鼓励，共同进步，一起玩转超级码力！

我的个人博客：[https://qingfengpython.cn](https://qingfengpython.cn)

力扣解题合集：[https://github.com/BreezePython/AlgorithmMarkdown](https://github.com/BreezePython/AlgorithmMarkdown)
