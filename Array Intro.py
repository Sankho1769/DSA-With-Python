# Creating a list
arr = [10, 20, 30, 40]

# Access by index (O(1))
print(arr[2])   # 30

# Append at the end (O(1) amortized)
arr.append(50)  
print(arr)      # [10, 20, 30, 40, 50]

# Insert at position (O(n))
arr.insert(2, 25)
print(arr)      # [10, 20, 25, 30, 40, 50]

# Delete (O(n))
arr.remove(40)
print(arr)      # [10, 20, 25, 30, 50]

# Search (O(n))
print(25 in arr)  # True
