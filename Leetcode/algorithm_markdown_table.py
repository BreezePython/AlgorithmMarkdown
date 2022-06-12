# -*- coding: utf-8 -*-
# @Author   : 王翔
# @微信号   : King_Uranus
# @公众号    : 清风Python
# @GitHub   : https://github.com/BreezePython
# @Date     : 2021/03/28 18:40:04
# @Software : PyCharm
# @version  ：Python 3.7.3
# @File     : algorithm_markdown_table.py
import os
import re

# 基础模板头，个人自定义
MARKDOWN_TABLE_TEMPLATE = """
# Algorithm coding practice with Python3.

> 力扣解题合集：https://github.com/BreezePython/AlgorithmMarkdown

欢迎关注我的公众号: **清风Python**，带你每日学习Python算法刷题的同时，了解更多python小知识。

有喜欢力扣刷题的小伙伴可以加我微信（King_Uranus）互相鼓励，共同进步，一起玩转超级码力！

我的个人博客：[https://qingfengpython.cn](https://qingfengpython.cn)

PS:题目按照 难度、题号进行排序。

| 编 号  | 分 类 | 题 目 | 难 度 | 我的解题 | 力扣题目链接 |
| ----- | ----- | ---- | ---- |  ------ |  --------  |
"""


class MakeAlgorithmMarkdownTable:
    def __init__(self, search_path, excludes):
        self.search_path = search_path
        self.start_dirname = os.path.basename(self.search_path)
        self.excludes = excludes
        self.programs = []
        self.sidebar_info = []

    def dfs_markdown_path(self, path):
        for child in os.listdir(path):
            if child in self.excludes:
                continue
            start_index = path.find(self.start_dirname)
            markdown_link_dir = path[start_index:].replace('\\', '/')
            if os.path.isfile(os.path.join(path, child)):
                markdown_link_path = '/'.join([markdown_link_dir, child])
                self.sidebar_info.append(
                    f"      * [{os.path.splitext(child)[0]}]({markdown_link_dir}/{child})")
                self.get_code_table(path, child, markdown_link_path)
            else:
                self.sidebar_info.append(f"  - **{child}**")
                self.dfs_markdown_path(os.path.join(path, child))

    def get_code_table(self, file_path, file_name, abs_path):
        algorithm_type = os.path.split(file_path)[-1].strip('_')
        code_file_name = os.path.splitext(file_name)[0]
        # git_file_link = f"[{code_file_name}]({abs_path})"
        git_file_link = f"[我的解题]({abs_path})"
        level = None
        link = None
        with open(os.path.join(file_path, file_name), 'r', encoding='utf-8') as f:
            for i in range(10):
                info = f.readline().strip()
                get_level = re.match('>.*难度[：|:]', info)
                if get_level:
                    # 正则获取解析的span尾节点
                    level = info[get_level.span()[1]:]
                # 获取力扣题目链接
                get_link = re.match('.*https://leetcode-cn.com', info)
                if get_link:
                    link = info[get_link.span()[0]:].strip('> ')
        self.programs.append([algorithm_type,
                              code_file_name,
                              level, git_file_link,
                              f'[点击跳转]({link})'])

    @staticmethod
    def sort_title(title):
        title = title.split('.')[0].strip()
        if title.isdigit():
            return int(title)
        return 1000

    @staticmethod
    def sort_level(level_name):
        level_dict = {"简单": 1, "中等": 2, "困难": 3}
        return level_dict.get(level_name, 4)

    def run(self):
        self.dfs_markdown_path(self.search_path)
        print(self.programs)
        try:
            self.programs.sort(key=lambda x: [self.sort_level(x[2].strip()), self.sort_title(x[1])])
        except Exception as e:
            print(e)
        with open(os.path.join(os.path.dirname(self.search_path), "README.md"),
                  'w', encoding='utf-8') as readme_file:
            readme_file.write(MARKDOWN_TABLE_TEMPLATE)
            for index, info in enumerate(self.programs, start=1):
                readme_file.write("|{}|{}|{}|{}|{}|{}|\n".format(index, *info))


if __name__ == '__main__':
    # 历史算法解题目录
    MARKDOWN_PATH = os.getcwd()
    # 例外文件列表
    EXCLUDE_FILES = ['QuickNote.md', 'algorithm_markdown_table.py', 'leetcode.py']
    m = MakeAlgorithmMarkdownTable(MARKDOWN_PATH, EXCLUDE_FILES)
    m.run()
