class Tree:
    def __init__(self, name='/', size=0, parent=None):
        self.children = []
        self.name = name
        self.size = size
        self.parent = parent

    def get_size(self):
        return self.size + sum([child.get_size() for child in self.children])

    def get_child_by_value(self, value):
        for child in self.children:
            if child.name == value:
                return child
        return None


def get_tree_size(tree):
    sum = 0
    if tree.get_size() < 100000 and tree.size == 0:
        sum += tree.get_size()

    for child in tree.children:
        sum += get_tree_size(child)
    return sum


input = open("7/input.txt", "r")
root = Tree()
currentNode = root

for line in input.readlines():
    line = line[:-1].split(" ")
    if line[0] == '$':
        if line[1] == "cd":
            if line[2] == '/':
                currentNode = root
            elif line[2] == "..":
                currentNode = currentNode.parent
            else:
                if currentNode.get_child_by_value(line[2]) != None:
                    currentNode = currentNode.get_child_by_value(line[2])
                else:
                    newChild = Tree(line[2], 0, currentNode)
                    currentNode.children.append(newChild)
                    currentNode = newChild
        elif line[1] == "ls":
            continue
    else:
        if line[0] == "dir":
            if currentNode.get_child_by_value(line[1]) == None:
                newChild = Tree(line[1], 0, currentNode)
                currentNode.children.append(newChild)
        else:
            if currentNode.get_child_by_value(line[1]) == None:
                newChild = Tree(line[1], int(line[0]), currentNode)
                currentNode.children.append(newChild)
print(get_tree_size(root))
