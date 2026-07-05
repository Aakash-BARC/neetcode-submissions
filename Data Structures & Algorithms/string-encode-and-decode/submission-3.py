class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for i in strs:
            encoded_str += str(len(i)) + "#"
            encoded_str += i
        return encoded_str

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            code = s.find("#",i)
            l = int(s[i:code])
            ans.append(s[code + 1 : code + 1 + l])
            i = code + 1 + l
        return ans