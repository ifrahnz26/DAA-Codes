'''A drama venue needs to be allocated for different drama school 
requests such that maximum profit is obtained for the company 
owning the drama venue. The requests are shown in the table 
with start–time, finish-time and the amount affordable by the drama school. 
Design and implement Weighted Interval Scheduling algorithm 
such that maximum profit is obtained for the company owning 
the drama venue using Dynamic programming principles. 
State the design strategy used and comment on 
the time complexity of the same

INTERVALS:
start finish weight
1       2     100
2       5     200
3       6     300
4       8     400
5       9     500
6       10    100
'''

def get_intervals():
    n = int(input("Enter the number of intervals: "))
    intervals = []
    for _ in range(n):
        start, finish, weight = map(int, input("Enter start time, finish time, and weight (separated by spaces): ").split())
        intervals.append((start, finish, weight))
    return intervals

# Get user input for the intervals
intervals = get_intervals()

# Sort intervals by finish time
intervals.sort(key=lambda x: x[1])

# Precompute p(j) for each interval
def compute_previous_intervals(intervals):
    p = [0] * len(intervals)
    for j in range(len(intervals)):
        for i in range(j - 1, -1, -1):
            if intervals[i][1] <= intervals[j][0]:
                p[j] = i + 1
                break
    return p

p = compute_previous_intervals(intervals)

# Memoization array
M = [0] + [None] * len(intervals)  

# M-Compute-Opt function
def M_Compute_Opt(j):
    if j == 0:
        return 0
    if M[j] is not None:
        return M[j]
    else:
        M[j] = max(intervals[j - 1][2] + M_Compute_Opt(p[j - 1]), M_Compute_Opt(j - 1))
        return M[j]

# Find the optimal weight
optimal_weight = M_Compute_Opt(len(intervals))
print(f"Optimal weight: {optimal_weight}")

def Find_Solution(j):
    if j > 0:
        if intervals[j - 1][2] + M[p[j - 1]] >= M[j - 1]:
            print(f"Interval {j}: {intervals[j - 1]}")
            Find_Solution(p[j - 1])
        else:
            Find_Solution(j - 1)

# Output the intervals belonging to the optimal solution
print("Intervals in the optimal solution:")
Find_Solution(len(intervals))
