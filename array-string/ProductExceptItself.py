class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
            a, b, c, d, so multiplying will be:
            prefix:
            ->
            |       a       |   a*b   | a*b*c | a*b*c*d |
            postfix:
            <-
            | a*b*c*d | b*c*d |   c*d   |      d        |
        
            the result is a multiply without the symbol in own position (the left value from prefix and the right one from postfix):
            |    b*c*d  | a*c*d | a*b*d |   a*b*c   |
        
            Another explaination:
            prefix:
                | 1 | a | a * b | a * b * c |
        
            postfix:
                |b * c * d |  c * d | d | 1 |
            result:
                | 1* b * c * d | a * c * d | a * b * d | a * b * c * 1 |
        """

        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        # print(res)
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            # print( i, ":", res[i], "*", postfix,  "=", res[i])
            postfix *= nums[i]
        # print(res)
        return res
