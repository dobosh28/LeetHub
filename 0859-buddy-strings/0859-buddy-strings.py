class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        mismatched_indices = []

        for i in range(len(s)):
            if s[i] != goal[i]:
                mismatched_indices.append(i)

        if len(mismatched_indices) == 2:
            i, j = mismatched_indices
            return s[i] == goal[j] and s[j] == goal[i]

        if len(mismatched_indices) == 0:
            return len(set(s)) < len(s)

        return False
