class Solution:
  """
  1071. Greatest Common Divisor of Strings
  For two strings s and t, we say "t divides s" if and 
  only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

  Given two strings str1 and str2, 
  return the largest string x such that x divides both str1 and str2.
  
  """
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)
        def isgcd(x):
            if len1%x  or len2%x :
                return False
            return str1[:x] * (len1 // x) == str1 and str1[:x] * (len2 // x) == str2
        for x in range(min(len1, len2), 0, -1):
            if isgcd(x):
                return str1[:x]
        return ""
