class Solution:
    """ 
    There are n kids with candies. You are given an integer array candies, 
    where each candies[i] represents the number of candies the ith kid has, 
    and an integer extraCandies, denoting the number of extra candies that you have.

    Return a boolean array result of length n, where result[i] is true if, 
    after giving the ith kid all the extraCandies, they will have the greatest number of 
    candies among all the kids, or false otherwise.

    Note that multiple kids can have the greatest number of candies.
    """
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxNumCandies = max(candies)
        for idx, candy in enumerate(candies):
            canHaveMaxCandies = (candy + extraCandies) >= maxNumCandies
            candies[idx] = canHaveMaxCandies
        return candies

    def kidsWithCandies1(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = [False] * len(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max(candies):
                res[i] = True
            else:
                res[i] = False
        return res
