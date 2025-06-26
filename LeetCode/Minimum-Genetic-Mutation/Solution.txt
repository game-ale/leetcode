class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        que = deque()
        ans = 0
        bank_set = set(bank)
        visited = set()
        if endGene not in bank_set:
            return -1
        que.append(startGene)
        visited.add(startGene)
        while que:
            len_que = len(que)
            for j in range(len_que):
                cur = que.popleft()
                if cur == endGene:
                    return ans
                cur_dna = list(cur)
                for i,char in enumerate(cur_dna):
                    new_dna = cur_dna.copy()
                    for c in ['A', 'C', 'G','T']:
                        if char!=c:
                            new_dna[i]=c
                            new_val = "".join(new_dna)
                            if new_val in bank_set and (new_val not in visited):
                                que.append(new_val)
                                visited.add(new_val)
            ans+=1
        return -1


        