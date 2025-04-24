def MergeIntervals(intervals):
    intervals.sort(key = lambda i : i[0])
    output = [intervals[0]]

    for start, end in intervals[1:]:
        if start <= output[-1][1]:
            output[-1][1] = max(output[-1][1], end)
        else:
            output.append([start, end])
    return output


# Time complexity: O(n) Space complexity: O(n)
# ✅ Runtime 7ms Beats 73.86% Analyze Complexity Memory 21.77MB Beats 14.99%


intervals = [[1,4],[0,4]]
Output = [[0,4]]

print(MergeIntervals(intervals))
print(MergeIntervals(intervals)== Output)