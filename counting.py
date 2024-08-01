def sort_and_count(L):
    if len(L) <= 1:
        return 0, L
    mid = len(L) // 2
    left = L[:mid]
    right = L[mid:]
    invL, sorted_left = sort_and_count(left)
    invR, sorted_right = sort_and_count(right)
    invS, sorted_list = merge_and_count(sorted_left, sorted_right)
    total = invL + invR + invS
    return total, sorted_list

def merge_and_count(A, B):
    merged = []
    i = inv = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            merged.append(A[i])
            i += 1
        else:
            merged.append(B[j])
            j += 1
            inv += len(A) - i
    merged.extend(A[i:])
    merged.extend(B[j:])
    return inv, merged

users = []
for i in range(3):
    print(f"Enter song ranking for user {i+1}: ")
    user = list(map(int, input().split()))
    users.append(user)

invC = sort_and_count(users[1])
invB = sort_and_count(users[2])

print(f"User 2 has {invB[0]} inversions.")
print(f"User 3 has {invC[0]} inversions.")

if invC[0] < invB[0]:
    print("User 3 has similar taste to user 1")
elif invB[0] < invC[0]:
    print("User 2 has similar taste to user 1")
else:
    print("All users have similar taste.")
