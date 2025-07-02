def leading_0(string):
    return string[0] == "0" and string != "0"

def valid(part):
    return not leading_0(part) and int(part) <= 255

def valid_ip(nums):
    return all(valid(part) for part in nums)

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ret = []
        for i, j, k in itertools.combinations(range(1, len(s)), 3):
            ip = [s[:i], s[i:j], s[j:k], s[k:]]
            if valid_ip(ip):
                ret.append(".".join(ip))
        return ret