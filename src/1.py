"""
给定一个字符串 s ，请你找出其中不含有重复字符的最长子串的长度。

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是"wke"，所以其长度为 3。
    请注意，你的答案必须是子串的长度，"pwke"是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


def solution(s):
    res = s[0]
    max_len_s = res
    for i in s:
        if i not in res:
            res = res + i
        else:
            res = res[1:]
            while i in res:
                res = res[1:]
            res = res + i
        if len(res) > len(max_len_s):
            max_len_s = res
    return max_len_s


print(solution("abcabcbb"))
print(solution("bbbbb"))
print(solution("pwwkew"))
print(solution("abc"))

