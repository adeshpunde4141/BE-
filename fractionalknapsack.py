class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def value_per_weight(self):
        return self.value / self.weight

def fractional_knapsack(items, capacity):
    items = sorted(items, key=lambda x: x.value_per_weight(), reverse=True)

    total_value = 0  
    for item in items:
        if capacity == 0:  
            break

        if item.weight <= capacity:
            total_value += item.value
            capacity -= item.weight
        else:
            fraction = capacity / item.weight
            total_value += item.value * fraction
            capacity = 0 

    return total_value

if __name__ == "__main__":
    n = int(input("Enter the number of items: "))
    
    items = []
    
    for i in range(n):
        value = float(input(f"Enter value for item {i+1}: "))
        weight = float(input(f"Enter weight for item {i+1}: "))
        items.append(Item(value, weight))
    
    capacity = float(input("Enter the capacity of the knapsack: "))

    max_value = fractional_knapsack(items, capacity)
    
    print(f"Maximum value in the knapsack = {max_value:.2f}")
