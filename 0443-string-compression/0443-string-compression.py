class Solution:
    def compress(self, chars: List[str]) -> int:
        char = chars[0]
        chars.append("0")
        count = 1
        i = 1
        while i < len(chars):
            if chars[i]!=char:
                if count>1:
                    count = list(str(count))
                    chars[i:i] = count
                    i+=len(count)
                char = chars[i]
                count=1
                i+=1
            else:
                count+=1
                del chars[i]

        del chars[-1]
        return len(chars)
            
        