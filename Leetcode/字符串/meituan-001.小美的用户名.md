# [meituan-001.小美的用户名](https://leetcode-cn.com/problems/BaR9fy/solution/meituan-001-xiao-mei-de-yong-hu-ming-pyt-m1n7/)
> https://leetcode-cn.com/problems/BaR9fy/solution/meituan-001-xiao-mei-de-yong-hu-ming-pyt-m1n7/
> 
> 难度：简单

## 题目

小美是美团的前端工程师，为了防止系统被恶意攻击，小美必须要在用户输入用户名之前做一个合法性检查，一个合法的用户名必须满足以下几个要求：

- 用户名的首字符必须是大写或者小写字母。
- 用户名只能包含大小写字母，数字。
- 用户名需要包含至少一个字母和一个数字。 如果用户名合法，请输出 "Accept"，反之输出 "Wrong"。

提示：
- 1 <= T <= 100
- s 的长度不超过 20

## 格式
输入：
- 输入第一行包含一个正整数 T，表示需要检验的用户名数量。
- 接下来有 T 行，每行一个字符串 s，表示输入的用户名。
输出：
- 对于每一个输入的用户名 s，请输出一行，即按题目要求输出一个字符串。

## 示例

```
输入：
     5
     Ooook
     Hhhh666
     ABCD
     Meituan
     6666
输出：
     Wrong
     Accept
     Wrong
     Wrong
     Wrong
```

## 分析
因为是美团2021校招的第一道题，所以较为简单。
仅需考虑字符串的类型识别：
- str.islower() 是否为小写字母
- str.isupper() 是否为大写字母
- str.isdigit() 是否为数字
对于习惯了力扣解题的朋友，针对自己写输入输出，可能需要费一番劲。习惯了就好...

## 解题

```python
nums = int(input())
for _ in range(nums):
    ret, li = True, [False, False]
    strs = input()
    if not (strs[0].islower() or strs[0].isupper()):
        ret = False

    for i in strs:
        if i.islower() or i.isupper():
            li[0] = True
        elif i.isdigit():
            li[1] = True
        else:
            ret = False
            break
    if not all(li):
        ret = False
    print("Accept" if ret else "Wrong")
```

欢迎关注我的公众号: **清风Python**，带你每日学习Python算法刷题的同时，了解更多python小知识。

有喜欢力扣刷题的小伙伴可以加我微信（King_Uranus）互相鼓励，共同进步，一起玩转超级码力！

我的个人博客：[https://qingfengpython.cn](https://qingfengpython.cn)

力扣解题合集：[https://github.com/BreezePython/AlgorithmMarkdown](https://github.com/BreezePython/AlgorithmMarkdown)