class Solution:
    def reverseBits(self, n):
        # 1. 首先我们获取n的二进制
        # '0b10100101000001111010011100'
        bin_n = bin(n)
        # 2. 接下来我们将'0b'替换为完整的全零前缀
        # 3. 然后将tmp_n倒置
        tmp_n = bin_n[2:].zfill(32)[::-1]
        # 4. 最后我们将tmp_n转换为整数返回
        ret = int(tmp_n,2)
        return ret

if __name__ == '__main__':
    s = Solution()
    print(s.reverseBits(43261596))