class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain(p, t):
            return (p + 1) / (t + 1) - p / t
    
        # Create a max heap with the initial classes based on their gain
        max_heap = []
        for p, t in classes:
            heapq.heappush(max_heap, (-gain(p, t), p, t))

        # Assign extra students to the classes
        for _ in range(extraStudents):
            g, p, t = heapq.heappop(max_heap)
            p += 1
            t += 1
            heapq.heappush(max_heap, (-gain(p, t), p, t))

        # Calculate the final average pass ratio
        total_pass_ratio = 0
        for _, p, t in max_heap:
            total_pass_ratio += p / t

        return total_pass_ratio / len(classes)
