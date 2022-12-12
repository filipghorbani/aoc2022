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


def get_dir_to_del(tree, minsize):
    size = tree.get_size()
    size = min([get_dir_to_del(child, minsize) for child in tree.children if get_dir_to_del(
        child, minsize) > minsize], default=size)
    return size


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
space_needed = 30000000 - 70000000 + root.get_size()
dir = get_dir_to_del(root, space_needed)
print(dir)
