class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n =len(neededTime)
        ans = 0
        stk = [(neededTime[0], colors[0])]
        for i in range(1,n):
            if stk and colors[i]==stk[-1][1] and stk[-1][0]< neededTime[i]:
                x,y = stk.pop()
                ans += x
                stk.append((neededTime[i], colors[i]))
            elif stk and colors[i]==stk[-1][1]:
                ans += neededTime[i]
            else:
                stk.append((neededTime[i], colors[i]))
         


        return ans                
            

            

        