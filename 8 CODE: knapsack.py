'''Alia is planning for a trekking expedition with a backpack
 that can hold 7kg. She needs to select the most valuable items 
 from the following list that can be accommodated within the backpack. 
 Design and implement Knapsack algorithm that displays the most 
 valuable items that can be carried by her using Dynamic programming principle 
 and find the time complexity of the same.
 
 ITEMS:
 Item Weight Value
 1      3      10
 2      5      4
 3      6      9
 4      2      11
 '''
def get_input():
   n = int(input("Enter the number of items: "))
   items = []
   for i in range(n):
       #Enter the weights of each item
       w = int(input(f"Enter weight of item {i + 1}: "))
       v = int(input(f"Enter value of item {i + 1}: "))
       items.append((w,v))
   W = int(input("Enter the capacity of knapsack: "))
   return items, W
 
def knapsack(items, W):
   n = len(items)
   #Create the nxW table
   M = [[0] * (W + 1) for _ in range(n + 1)]
 
   #Populate the M table
   for i in range(1, n + 1):
       for w in range(1, W + 1):
           if items[i - 1][0] > w:
               M[i][w] = M[i - 1][w]
           else:
               M[i][w] = max(M[i - 1][w], items[i - 1][1] + M[i - 1][w - items[i - 1][0]])
   return M
 
def find_items(M, items, W):
   n = len(items)
   result = []
   i, k = n, W
   while i > 0 and k > 0:
       if M[i][k] != M[i - 1][k]:
           result.append((i,items[i - 1][0],items[i - 1][1]))
           k -= items[i - 1][0]
       i -= 1
   return result
 
#Get the user input
items, W = get_input()
M = knapsack(items, W)
max_value = M[len(items)][W]
print(f"Maximum value: {max_value}")
#check if it satisfies the bound
optimal_items = find_items(M, items, W)
print("Items in the optimal solution:")
print("Item:\tWeight Value")
for i in optimal_items:
   print(f"Item {i[0]}:\t {i[1]}\t{i[2]}")
