# [meituan-006.小团的神秘暗号](https://leetcode-cn.com/problems/z3XKBp/)
> https://leetcode-cn.com/problems/z3XKBp/
> 
> 难度：简单

## 题目
小团深谙保密工作的重要性，因此在某些明文的传输中会使用一种加密策略，小团如果需要传输一个字符串 S ，
则他会为这个字符串添加一个头部字符串和一个尾部字符串。头部字符串满足至少包含一个 “MT” 子序列，且以 T 结尾。
尾部字符串需要满足至少包含一个 “MT” 子序列，且以 M 开头。例如 AAAMT 和 MAAAT 都是一个合法的头部字符串，
而 MTAAA 就不是合法的头部字符串。很显然这样的头尾字符串并不一定是唯一的，因此我们还有一个约束，
就是 S 是满足头尾字符串合法的情况下的最长的字符串。
很显然这样的加密策略是支持解码的，给出一个加密后的字符串，请你找出中间被加密的字符串 S 。


## 格式：
输入：
- 输入第一行是一个正整数 n ，表示加密后的字符串总长度。
- 输入第二行是一个长度为 n 的仅由大写字母组成的字符串 T 。
输出：
- 输出仅包含一个字符串 S 。

## 示例

```
输入：
     10
     MMATSATMMT
输出：SATM
```

## 分析
这道题是一个窗口收缩问题，既然要找到最长的字符串，则分别从左、有开始向中间缩进。
当左找到MT，右找到TM，即终止搜索。这里为了好看，使用栈的弹出操作进行解题。

## 解题

```python
n = int(input())
words = input()
left, right, l_comp, r_comp = 0, n - 1, ["T", "M"], ["M", "T"]
while l_comp or r_comp:
    if l_comp:
        if words[left] == l_comp[-1]:
            l_comp.pop()
        left += 1
    if r_comp:
        if words[right] == r_comp[-1]:
            r_comp.pop()
        right -= 1
print(words[left:right + 1])
```

```java
import java.util.Scanner;
import java.util.Stack;

public class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int lg = scanner.nextInt();
        String words = scanner.next();
        Stack<Character> l_comp = new Stack<Character>();
        l_comp.push('T');
        l_comp.push('M');

        Stack<Character> r_comp = new Stack<Character>();
        r_comp.push('M');
        r_comp.push('T');
        int left = 0;
        int right = lg - 1;
        while (!l_comp.isEmpty() || !r_comp.isEmpty()) {
            if (!l_comp.isEmpty()) {
                if (words.charAt(left) == l_comp.peek()) {
                    l_comp.pop();
                }
                left++;
            }
            if (!r_comp.isEmpty()) {
                if (words.charAt(right) == r_comp.peek()) {
                    r_comp.pop();
                }
                right--;
            }
        }
        System.out.println(words.substring(left, right + 1));
    }
}
```

欢迎关注我的公众号: **清风Python**，带你每日学习Python算法刷题的同时，了解更多python小知识。

有喜欢力扣刷题的小伙伴可以加我微信（King_Uranus）互相鼓励，共同进步，一起玩转超级码力！

我的个人博客：[https://qingfengpython.cn](https://qingfengpython.cn)

力扣解题合集：[https://github.com/BreezePython/AlgorithmMarkdown](https://github.com/BreezePython/AlgorithmMarkdown)