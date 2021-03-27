import os
import re
from collections import deque


class MakeAlgorithmMarkdownTable:
    def __init__(self, markdown_path):
        self.markdown_path = markdown_path
        self.sidebar_info = []
        self.markdown_table = []

    def dfs_markdown_path(self, path):
        for child in os.listdir(path):
            temp_path = '/'.join(path.split('\\')[2:])
            if child.lower() in ['readme.md','力扣算法刷题目录.md']:
                continue
            elif os.path.isfile(os.path.join(path, child)):
                abs_path = f"{temp_path}/{child}"
                self.sidebar_info.append(f"      * [{os.path.splitext(child)[0]}]({temp_path}/{child})")
                # self.check_title(path, child)
                self.get_code_table(path, child, abs_path)
            else:
                self.sidebar_info.append(f"  - [{child}]({temp_path}/{child})")
                self.dfs_markdown_path(os.path.join(path, child))

    @staticmethod
    def check_title(file_path, file_name):
        markdown_file = os.path.join(file_path, file_name)
        with open(markdown_file, 'r', encoding='utf-8') as f:
            data = deque(f.readlines())
        if not data[0].startswith('# '):
            print(file_name)
            title = os.path.splitext(file_name)[0]
            data.appendleft(f"# {title}\n")
            with open(markdown_file, 'w', encoding='utf-8') as f:
                f.writelines(data)

    def get_code_table(self, file_path, file_name, abs_path):
        code_type = os.path.split(file_path)[-1].strip('_')
        code_name = os.path.splitext(file_name)[0]
        my_answer = f"[{code_name}]({abs_path})"
        level = None
        link = None
        with open(os.path.join(file_path, file_name), 'r', encoding='utf-8') as f:
            for i in range(10):
                info = f.readline().strip()
                get_level = re.match('>.*难度[：|:]', info)
                if get_level:
                    level = info[get_level.span()[1]:]
                get_link = re.match('.*https://leetcode-cn.com', info)
                if get_link:
                    link = info[get_link.span()[0]:].strip('> ')
        self.markdown_table.append([code_type, code_name, level, my_answer, f'[点击跳转]({link})'])

    def sort_title(self, title):
        title = title.split('.')[0].strip()
        if title.isdigit():
            return int(title)
        return 1000

    def run(self):
        self.dfs_markdown_path(self.markdown_path)
        self.markdown_table.sort(key=lambda x: self.sort_title(x[1]))
        print("| 编 号 | 分 类 | 题 目 | 难 度 | 我的解题 | 力扣题目链接 |")
        print("| ---- | ---- | ---- | ---- | ---- | ---- |")

        for index, info in enumerate(self.markdown_table, start=1):
            print("|{}|{}|{}|{}|{}|{}|".format(index, *info))


if __name__ == '__main__':
    # m = MakeAlgorithmMarkdownTable(r'D:\blog\markdown\算法之美')
    m = MakeAlgorithmMarkdownTable(r'D:\AlgorithmMarkdown\Leetcode')
    m.run()
