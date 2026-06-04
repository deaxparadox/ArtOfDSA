# Given a string s, return true if the s can be palindrome after deleting at most one character from it.


class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) -1 

        while l < r:
            if s[l] != s[r]:
                return self.check_palindrome(s, l+1, r) or self.check_palindrome(s, l, r-1)
            l+=1
            r-=1
                
        return True
    
    def check_palindrome(self, s: str, l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True
    
    
def main():
    solution = Solution()
    ss = [
        'aba',
        'absa',
        'absc',
        'deee',
        'racecar'
    ]
    print("\n{:^20}|{:^20}".format("String", "Palindrome"))
    print("_"*41)
    for s in ss:
        result = solution.validPalindrome(s)
        print("{:^20}|{:^20}".format(s, result))

if __name__ == "__main__":
    main()