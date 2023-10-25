class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        _min: int = len(min(strs, key=len))
        output_str: str = ""

        for index in range(_min):
            piece = [word[index] for word in strs]

            if len(set(piece)) == 1:
                output_str += piece[0]
            else:
                break

        return output_str
      
        