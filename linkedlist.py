########################
# LINKEDLIST
########################

class LinkedList:
    def __init__(self):
        self.list = [Node("hello", 1), Node("hi", 3), Node("bye", None), Node("hi again", 2)]
        self.startPointer = 0
        self.currentNode = self.startPointer

    def traverse(self):
        if self.__isEmpty():
            return False

        data = self.list[self.currentNode].data
        nextNode = self.list[self.currentNode].nextNode

        if self.list[self.currentNode].nextNode == None:
            self.__returnToStart()
        else:
            self.currentNode = self.list[self.currentNode].nextNode

        return data, nextNode

    def newNode(self, data, pos):
        if self.__isEmpty:
            self.list[0] = Node(data, None)
            self.startpointer = 0
        elif pos == len(self.list):
            self.list.append(Node(data, None))
        else:
            tempNode = self.currentNode
            self.__returnToStart()
            for i in range(0, pos+1):
                self.list[i].nextNode = i
                pointNode = self.traverse()[1]
            self.list.append(Node(data, pointNode))            
            self.__returnToPosition(tempNode)
    
    def __isEmpty(self):
        if len(self.list) == 0: return True
        return False

    def __returnToStart(self):
        self.currentNode = self.startPointer

    def __returnToPosition(self, oldNode):
        self.currentNode = oldNode

class Node:
    def __init__(self, data, nextNode):
        self.data = data
        self.nextNode = nextNode

list = LinkedList()

print(list.traverse())
print(list.traverse())
print(list.traverse())
print(list.traverse())
print(list.traverse())