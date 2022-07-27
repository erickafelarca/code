# # class Node:
# #
# #     def __init__(self, data=None, next=None):
# #         self.data = data
# #         self.next = next
# #
# #
# # def node(self, data):
# #     node(data)
# #     if self.head:
# #         current = self.head
# #         while current.next:
# #             current = current.next
# #         current.next = node
# #     else:
# #         self.head = node
# #
# #     def display(self):
# #         current = self.head
# #         while (current):
# #             print(current.data)
# #             current = current.next
# #
# #
# # Node()
# # Node.node(1)
# # Node.node(2)
# # Node.node(3)
# # Node.node(4)
# # Node.node(5)
# # Node.node(6)
# # Node.node(7)
# # Node.node(8)
# # Node.node(9)
# # Node.node(10)
# #
# # Node.print()
#
# # class Node:
# #     def __init__(self, data=None):
# #         self.data = data
# #         self.next = None
# #
# #
# # class SortList:
# #     def __init__(self):
# #         self.start = None
# #         self.end = None
# #
# #     def node(self, data):
# #         newNode = Node(data)
# #
# #         if self.start is None:
# #             self.start = newNode
# #             self.end = newNode
# #         else:
# #             self.end.next = newNode
# #             self.end = newNode
# #
# #     def sortList(self):
# #         current = self.start
# #         index = None
# #
# #         if self.start is None:
# #             return
# #         else:
# #             while current is not None:
# #                 index = current.next
# #
# #                 while index is not None:
# #                     if current.data > index.data:
# #                         temp = current.data
# #                         current.data = index.data
# #                         index.data = temp
# #                     index = index.next
# #                 current = current.next
# #
# #     def count_nodes(self):
# #         if self is None:
# #             return 0;
# #             return
# #         count = 1
# #         current = self
# #         while current.next is not None:
# #             current = current.next
# #             count += 1
# #         return count
# #
# #     def get_item(self, index):
# #         if index > self.count_nodes() - 1:
# #             return "Index out of range"
# #         current = self
# #
# #         for n in range(index):
# #             current = current.next
# #         return current.data
# #
# #     def display(self):
# #         current = self.start
# #         if self.start is None:
# #             print("Your list is empty")
# #             return
# #         while current is not None:
# #             print(current.data),
# #             current = current.next
# #         print
# #         ""
# #
# #
# # MyList = SortList()
# #
# #
# #
# # MyList.node(4)
# # MyList.node(1)
# # MyList.node(2)
# # MyList.node(10)
# # MyList.node(7)
# # MyList.node(8)
# # MyList.node(11)
# # MyList.node(3)
# # MyList.node(9)
# # MyList.node(5)
# # MyList.node(6)
# #
# # MyList.sortList()
# #
# # print("Sorted: ")
# # MyList.display()
# #
# # print('\nFirst Box Bottom:')
# # print(MyList.get_item(1))
# # print(MyList.get_item(2))
# # print(MyList.get_item(3))
#
#
# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None
#
#     def sortList(self):
#         current = self.next
#         index = None
#
#         if self.next is None:
#             return
#         else:
#             while current is not None:
#                 index = current.next
#
#                 while index is not None:
#                     if current.data > index.data:
#                         temp = current.data
#                         current.data = index.data
#                         index.data = temp
#                     index = index.next
#                 current = current.next
#
#     def count_nodes(self):
#         if self is None:
#             return 0;
#             return
#         count = 1
#         current = self
#         while current.next is not None:
#             current = current.next
#             count += 1
#         return count
#
#     def print_nodes(self):
#         current = self
#         while current:
#             print(current.data)
#             current = current.next
#
#     def get_item(self, index):
#         if index > self.count_nodes() - 1:
#             return "Index out of range"
#         current = self
#
#         for n in range(index):
#             current = current.next
#         return current.data
#
#     def display(self):
#         current = self.next
#         if self.next is None:
#             print("Your list is empty")
#             return
#         while current is not None:
#             print(current.data),
#             current = current.next
#         print
#         ""
#
#
# head = Node(' ')
# nodeB = Node('4')
# nodeC = Node('1')
# nodeD = Node('2')
# nodeE = Node('10')
#
# head.next = nodeB
# nodeB.next = nodeC
# nodeC.next = nodeD
# nodeD.next = nodeE
#
# head.print_nodes()
#
# print('\nGet Item:')
# print(head.get_item(1))
# print(head.get_item(2))
# print(head.get_item(3))
#
# head.sortList()
#
# print('\nSorted: ')
# head.display()
#
#


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def count_nodes(self):
        if self is None:
            return 0;
            return
        count = 1
        current = self
        while current.next is not None:
            current = current.next
            count += 1
        return count

    def print_nodes(self):
        current = self
        while current:
            print(current.data)
            current = current.next

    def get_item(self, index):
        if index > self.count_nodes() - 1:
            return "Index out of range"
        current = self

        for n in range(index):
            current = current.next
        return current.data


head = Node('4')
nodeB = Node('1')
nodeC = Node('2')
nodeD = Node('10')
nodeE = Node('7')
nodeF = Node('8')
nodeG = Node('11')
nodeH = Node('3')
nodeI = Node('9')
nodeJ = Node('5')
nodeK = Node('6')

head.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE
nodeE.next = nodeF
nodeF.next = nodeG
nodeG.next = nodeH
nodeH.next = nodeI
nodeI.next = nodeJ
nodeJ.next = nodeK

print('Count of Nodes: ')
print(head.count_nodes())

print('\nBottom Nodes of 4:')
print(head.get_item(0))
print(head.get_item(1))
print(head.get_item(2))

print('\nBottom Nodes of 10:')
print(head.get_item(3))
print(head.get_item(4))
print(head.get_item(5))

print('\nBottom Nodes of 3:')
print(head.get_item(7))
print(head.get_item(8))

print('\nBottom Nodes of 5:')
print(head.get_item(9))
print(head.get_item(10))

print('\nRight Nodes of 4:')
print(head.get_item(0))
print(head.get_item(3))
print(head.get_item(7))
print(head.get_item(9))

print('\nRight Nodes of 8:')
print(head.get_item(5))
print(head.get_item(6))




