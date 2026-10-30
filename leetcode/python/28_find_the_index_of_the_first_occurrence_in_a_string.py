class Solution1:
    """
    Over extended solution
    """

    def get_indexes(self, haystack: str, needle_first_char: str) -> list[int]:
        _temp = []
        haystack_len = len(haystack)
        haystack_lst = [x for x in haystack]
        for i in range(haystack_len):
            if needle_first_char == haystack_lst[i]:
                _temp.append(i)
        return _temp
        
    def strStr(self, haystack: str, needle: str) -> int:
        needle_first_char = needle[0]
        needle_len = len(needle)
        indexes = self.get_indexes(haystack, needle_first_char)
        for idx in indexes:
            if haystack.startswith(needle, idx, idx + needle_len):
                return idx
        return -1
    

class Solution2:
    """
    Single loop solution
    """
    def strStr(self, haystack: str, needle: str) -> int:
        hay_len = len(haystack)
        needle_len = len(needle)
        for idx in range(hay_len):
            if haystack.startswith(needle, idx, idx + needle_len):
                return idx
        return -1