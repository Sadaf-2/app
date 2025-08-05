# Creating a list
fruits = ["apple", "banana", "cherry", "mango"]

# Indexing
print(fruits[0])      # apple
print(fruits[-1])     # mango

# Slicing
print(fruits[1:3])    # ['banana', 'cherry']

# List methods
fruits.append("grape")
fruits.remove("banana")
fruits.insert(1, "orange")
fruits.sort()

print(fruits)
