class Solution:
    def defangIPaddr(self, address: str) -> str:
        ret = []
        for ch in address:
            if ch == '.':
                ret.append('[.]')
            else:
                ret.append(ch)
        return "".join(ret)