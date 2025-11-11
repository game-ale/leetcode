ok = 0  # always possible to give 0 candies to k children
ng = sum(candies) // k + 1  # impossible to give this number of candies to k children
while abs(ok - ng) > 1:  # depending on the problem it can be ok > ng
    mid = (ok + ng) // 2
    if check(mid):  # check whether mid is feasible
        ok = mid
    else:
        ng = mid
return ok