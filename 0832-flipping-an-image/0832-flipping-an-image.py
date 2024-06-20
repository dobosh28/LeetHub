class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        
        for row in image:
            # Flip the row horizontally by reversing it
            row.reverse()
            
            # Invert the row
            for j in range(n):
                row[j] = 1 - row[j]
        
        return image
