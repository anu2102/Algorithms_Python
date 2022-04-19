value = []
huffman_code = {}
class Node:
    def _init_(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
    def Huffman_code(self):
        global value
        if type(self.left.key) == type(""):
            value.append(0)
            huffman_code[self.left.key]=value
            value = value[:len(value)-1]
        else:
            value.append(0)
            self.left.key.Huffman_code()
            value = value[:len(value)-1]

        if type(self.right.key) == type(""):
            value.append(1)
            huffman_code[self.right.key]=value
            value = value[:len(value)-1]
        else:
            value.append(1)
            self.right.key.Huffman_code()
            value = value[:len(value)-1]

def small(dic):
    small = -1
    small_letter = ""
    for i, j in dic.items():
        if small == -1:
            small = j
            small_letter = i
        else:
            if j<small:
                small = j
                small_letter = i
    return small_letter

string = "she sell seashell at the sea shore"
d = {}
for i in string:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
while len(d)!=1:
    node1 = Node(small(d), d[small(d)])
    key1 = d.pop(small(d))
    node2 = Node(small(d), d[small(d)])
    key2 = d.pop(small(d))
    node3 = Node(None, key1+key2)
    node3.left = node1
    node3.right = node2
    d[node3] = node3.val
 
for i, j in d.items():
    node = i
i.Huffman_code()
print(huffman_code)
