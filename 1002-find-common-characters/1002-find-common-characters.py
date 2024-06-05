class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        words_size = len(words)
        result = []
        
        # Initialize the Counter with the first word
        common_char_counts = Counter(words[0])
        
        # Update the Counter with the minimum occurrences for each subsequent word
        for i in range(1, words_size):
            current_char_counts = Counter(words[i])
                
            for letter in list(common_char_counts.keys()):
                if letter in current_char_counts:
                    common_char_counts[letter] = min(common_char_counts[letter], current_char_counts[letter])
                else:
                    del common_char_counts[letter]
                    
        # Convert the Counter to the result list
        for letter, count in common_char_counts.items():
            result.extend([letter] * count)
                    
        return result

