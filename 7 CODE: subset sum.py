'''Given a set of non-negative integers and a value of variable sum. 
design and implement an algorithm to determine if 
there is a subset of the given set with a sum equal to the given sum. 
A suitable message is to be displayed if the given problem instance 
doesn't have a solution.

'''
def get_input():
   n = int(input("Enter the number of items: "))
   items = []
   for i in range(n):
       #Enter the weights of each item
       w = int(input(f"Enter weight of item {i + 1}: "))
       items.append(w)
   W = int(input("Enter the sum of the subset problem: "))
   return items, W
 
def subset_sum(items, W):
   n = len(items)
   #Create the nxW table
   M = [[0] * (W + 1) for _ in range(n + 1)]
 
   #Populate the M table
   for i in range(1, n + 1):
       for w in range(1, W + 1):
           if items[i - 1] > w:
               M[i][w] = M[i - 1][w]
           else:
               M[i][w] = max(M[i - 1][w], items[i - 1] + M[i - 1][w - items[i - 1]])
 
   return M
 
def find_items(M, items, W):
   n = len(items)
   result = []
   i, k = n, W
   while i > 0 and k > 0:
       if M[i][k] != M[i - 1][k]:
           result.append((i,items[i - 1]))
           k -= items[i - 1]
       i -= 1
   return result
 
#Get the user input
items, W = get_input()
M = subset_sum(items, W)
max_weight = M[len(items)][W]
print(f"Maximum weight: {max_weight}")
#check if it satisfies the bound
if max_weight == W:
   print("The subset satisfies the bound.")
else:
   print("The subset does not satisfy the bound.")
optimal_items = find_items(M, items, W)
optimal_items.reverse()
print("Items in the optimal solution (weights):")
for i in optimal_items:
   print(f"Item {i[0]}: {i[1]}")
                                           
