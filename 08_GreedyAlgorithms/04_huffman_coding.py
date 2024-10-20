# Huffman Coding for Data Compression using Priority Queue

import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def huffman_encoding(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = Node(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)

    return heap[0]

def huffman_codes(node, prefix="", code={}):
    if node is None:
        return

    if node.char:
        code[node.char] = prefix

    huffman_codes(node.left, prefix + "0", code)
    huffman_codes(node.right, prefix + "1", code)

    return code

# Testing Huffman Coding
frequencies = {
    'A': 5,
    'B': 9,
    'C': 12,
    'D': 13,
    'E': 16,
    'F': 45
}

root = huffman_encoding(frequencies)
codes = huffman_codes(root)
print("Huffman Codes:", codes)
