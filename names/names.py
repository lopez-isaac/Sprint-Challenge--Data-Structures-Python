import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
for name_1 in names_1:
   for name_2 in names_2:
       if name_1 == name_2:
            duplicates.append(name_1)
end_time = time.time()

#My code here:
my_start_time = time.time()
duplicates = []
fitted_tree = BinarySearchTree("isaac lopez")

for name in names_1:
    fitted_tree.insert(name)

for name in names_2:
    if fitted_tree.contains(name):
        duplicates.append(name)


#starter code runtime: 5.622673988342285 seconds O(n^2)
#my runtime: 0.14391708374023438 seconds

my_end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"starter runtime: {end_time - start_time} seconds")
print (f"my runtime: {my_end_time - my_start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
