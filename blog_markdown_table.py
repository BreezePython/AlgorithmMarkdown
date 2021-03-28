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
# 清风Python的博客
> 欢迎大家访问我的博客，我的微信公众号 **清风Python**，坚持更新有趣的Pyhton内容。
> 
> 快去左侧列表挑选你喜欢的内容观看吧。

## 力扣算法刷题记录
> 劝学 · 荀子
> 
> 不积跬步，无以至千里；不积小流，无以成江海。 
> 
> 骐骥一跃，不能十步；驽马十驾，功在不舍。
> 
> 锲而舍之，朽木不折；锲而不舍，金石可镂。

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
            if child.lower() in self.excludes:
                continue
            start_index = path.find(self.start_dirname)
            markdown_link_dir = path[start_index:].replace('\\', '/')
            if os.path.isfile(os.path.join(path, child)):
                markdown_link_path = '/'.join([markdown_link_dir, child])
                self.sidebar_info.append(
                    f"      * [{os.path.splitext(child)[0]}](markdown/{markdown_link_dir}/{child})")
                self.get_code_table(path, child, markdown_link_path)
            else:
                self.sidebar_info.append(f"  - **{child}**")
                self.dfs_markdown_path(os.path.join(path, child))

    def get_code_table(self, file_path, file_name, abs_path):
        algorithm_type = os.path.split(file_path)[-1].strip('_')
        code_file_name = os.path.splitext(file_name)[0]
        git_file_link = f"[{code_file_name}](markdown/{abs_path})"
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

    def run(self):
        self.dfs_markdown_path(self.search_path)
        self.programs.sort(key=lambda x: self.sort_title(x[1]))
        with open(os.path.join(os.path.dirname(os.path.dirname(self.search_path)), "README.md"),
                  'w', encoding='utf-8') as readme_file:
            readme_file.write(MARKDOWN_TABLE_TEMPLATE)
            for index, info in enumerate(self.programs, start=1):
                readme_file.write("|{}|{}|{}|{}|{}|{}|\n".format(index, *info))
        for i in self.sidebar_info:
            print(i)


if __name__ == '__main__':
    # 历史算法解题目录
    # MARKDOWN_PATH = r'D:\AlgorithmMarkdown\Leetcode'
    MARKDOWN_PATH = r'D:\blog\markdown\算法之美'
    # 例外文件列表
    EXCLUDE_FILES = ['readme.md', '力扣算法刷题目录.md']
    m = MakeAlgorithmMarkdownTable(MARKDOWN_PATH, EXCLUDE_FILES)
    m.run()
