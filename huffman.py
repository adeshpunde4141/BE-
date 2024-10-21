import time
import heapq

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''

    def __lt__(self, nxt):
        return self.freq < nxt.freq

def printNodes(node, val=''):
    newVal = val + str(node.huff)
    if node.left:
        printNodes(node.left, newVal)
    if node.right:
        printNodes(node.right, newVal)
    if not node.left and not node.right:
        print(f"{node.symbol} -> {newVal}")

n = int(input("Enter number of symbols: "))
chars = []
freq = []
for i in range(n):
    char = input(f"Enter symbol : ")
    chars.append(char)
    f = int(input(f"Enter frequency for {char}: "))
    freq.append(f)

nodes = []
for i in range(n):
    heapq.heappush(nodes, Node(freq[i], chars[i]))

start_time = time.time()

while len(nodes) > 1:
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)
    
    left.huff = 0  
    right.huff = 1  
    
    newNode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
    
    heapq.heappush(nodes, newNode)

huffman_tree_root = nodes[0]

print("Huffman Codes:")
printNodes(huffman_tree_root)

end_time = time.time()
execution_time = end_time - start_time
print(f"\nExecution time: {execution_time:.6f} seconds")
