# Average: O(log(n)) time | O(1) space
# Worst: O(n) time | O(1) space
def closestValue(tree, target):
    return findClosestValueInBSTHelper(tree, target, float("inf"))

def findClosestValueInBSTHelper(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target.closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest