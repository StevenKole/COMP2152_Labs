# Question 2: Shopping Cart (Lists - Searching and Removal)
cart = ["apple", "banana", "milk", "bread", "apple", "eggs"]
print("Number of apples", cart.count("apple"))
print("Position of milk", cart.count("milk"))
cart.remove("apple")
print("Removed item using pop: ", cart.pop())
print("Is banana in cart?", "banana" in cart)
print("Final cart: ", cart)