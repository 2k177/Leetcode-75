class Solution:
  """
  345. Reverse Vowels of a String
  Given a string s, reverse only all the vowels in the string and return it.
  The vowels are 'a', 'e', 'i', 'o', and 'u', and 
  they can appear in both lower and upper cases, more than once.
  Example 1:

  Input: s = "hello"
  Output: "holle"
  Example 2:
  
  Input: s = "leetcode"
  Output: "leotcede"
  """
    def reverseVowels(self, s: str) -> str:
        l = 0
        r = len(s) -1
        s = list(s)
        print(s)
        vowels=set('AEIOUaeiou')
        print(l, r)
        while (l < r):
            while(l<r) and  s[l] not in vowels:
                l += 1
            while (l<r) and  s[r] not in vowels:
                r -= 1
            s[l] , s[r] = s[r], s[l]
            l +=1 
            r -= 1
        s = "".join(s)
        return s
