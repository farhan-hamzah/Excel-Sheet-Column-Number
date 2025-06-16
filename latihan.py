class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            value = ord(char) - ord('A') + 1
            result = result * 26 + value
        return result

# Contoh penggunaan:
sol = Solution()
print(sol.titleToNumber("A"))    # Output: 1
print(sol.titleToNumber("Z"))    # Output: 26
print(sol.titleToNumber("AA"))   # Output: 27
print(sol.titleToNumber("AB"))   # Output: 28
print(sol.titleToNumber("ZY"))   # Output: 701
