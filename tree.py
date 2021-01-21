class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    # A function to do inorder tree traversal


def printInorder(root):
    if root:
        # First recur on left child
        printInorder(root.left)

        # then print the data of node
        print(root.val, end=" ")

        # now recur on right child
        printInorder(root.right)

    # A function to do postorder tree traversal


def printPostorder(root):
    if root:
        # First recur on left child
        printPostorder(root.left)

        # the recur on right child
        printPostorder(root.right)

        # now print the data of node
        print(root.val, end=" ")

    # A function to do preorder tree traversal


def printPreorder(root):
    if root:
        # First print the data of node
        print(root.val, end=" ")

        # Then recur on left child
        printPreorder(root.left)

        # Finally recur on right child
        printPreorder(root.right)

    # Driver code

def heightoftree(root):
    if root:
        print("root: ",root.val)
    if root is None:
        return 0
    else:
        lheight = heightoftree(root.left)
        rheight = heightoftree(root.right)

    if lheight > rheight:
        print("left ==> lheight: " + str(lheight) + "   rheight: " + str(rheight))
        return lheight+1
    else:
        print("right ===> lheight: " + str(lheight) + "   rheight: " + str(rheight))
        return rheight+1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Preorder traversal of binary tree is")
printPreorder(root)

print("\nInorder traversal of binary tree is")
printInorder(root)

print("\nPostorder traversal of binary tree is")
printPostorder(root)

print("\nheight of tree is")
print(heightoftree(root))


arr= [2,3,4,5,6]
arr2 = [2,2,3,5,4,3,5,6,6]
res = { j:i for i,j in enumerate(arr) }
res1 = [ res.get(x) for x in arr2]
print(res1)


lst = ['Cat', 'Bat', 'Sat', 'Cat', 'Mat', 'Cat', 'Sat']
print([{item, lst.count(item)} for item in set(lst)])

def sortSecond(val):
    return val[1]
list1 = [(1,2),(3,3),(1,1)]
list1.sort(key=sortSecond)
print(list1)

# sorts the array in descending according to
# second element
list1.sort(key=sortSecond, reverse=True)
print(list1)


from collections import namedtuple

colour = namedtuple('Colour', ['hue', 'saturation', 'luminosity'])
colour_heuristic = colour(170, 0.1, 0.6)

if colour_heuristic.saturation > 0.5:
	print('that is too bright')
if colour_heuristic.luminosity > 0.5:
	print('wow this is light')

dictt = {1:'a', 1:'b'}
print(dictt[1])

book = "ajay"
hash_book = []
for char in book:
    hash_book[str(char)-"a"] +=1
print(hash_book)