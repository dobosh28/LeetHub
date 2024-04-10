class Solution:
    def compress(self, chars: List[str]) -> int:
        write = left = 0
        for read in range(len(chars) + 1):
            if read == len(chars) or chars[read] != chars[left]:
                chars[write] = chars[left]
                write += 1
                if read - left > 1:
                    for digit in str(read - left):
                        chars[write] = digit
                        write += 1
                left = read
        return write
