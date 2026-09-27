class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []

        # Step 1: Sort intervals by their start times
        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]

        # Step 2: Iterate and merge adjacent intervals
        for current in intervals[1:]:
            last_merged = merged[-1]

            # Check if current interval overlaps with the last merged interval
            if current[0] <= last_merged[1]:
                # Overlap: extend the end of the last merged interval
                last_merged[1] = max(last_merged[1], current[1])
            else:
                # No overlap: append current interval
                merged.append(current)

        return merged