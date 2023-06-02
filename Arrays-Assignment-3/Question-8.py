# Given an array of meeting time intervals where intervals[i] = [starti, endi],
# determine if a person could attend all meetings.

# Example 1:
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: false

def canAttendMeetings(intervals):
    intervals.sort(key=lambda x: x[0])  

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False

    return True


intervals = []
num_intervals = int(input())
for i in range(num_intervals):
    interval_input = input()
    start, end = map(int, interval_input.split())
    interval = [start, end]
    intervals.append(interval)

result = canAttendMeetings(intervals)
print(result)
