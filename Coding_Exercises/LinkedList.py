from typing import Optional


class Node:
    def __init__(self, data: Optional[int]=None):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self, data:Optional[int]=None):
        if data is None:
            self.head = None
        else:
            self.head = Node(data)

    def append(self, data):
        current = self.head
        if current is None:
            current = Node(data)
           # print(current.data)
            return
        while current.next is not None:


            current = current.next



        current.next = Node(data)
        #print(current.next.data)

        # while current.next != None:
        #     current = current.next
        # current.next = Node(data)

    # def display1(self, head):
    #     if head.next == None:
    #         return
    #     current = head.next
    #     self.display1(current)
    #     print(str(current.data))

    def display(self):
        cur = self.head
        arr = []
        while cur is not None:
            arr.append(cur.data)
            cur = cur.next
        # while cur.next is not None:
        #     cur = cur.next
        #     arr.append(cur.data)
        #
        print(arr)

    def length(self):
        count = 0
        current = self.head
        while current.next is not None:
            count += 1
            current = current.next
        return count

    def remove(self, index):
        try:
            if index > self.length():
                raise IndexError("Out of range")

            cur = self.head
            count = 0
            while True:

                if count == index:
                    print(cur.next.data)
                    cur.next = cur.next.next
                    break
                count += 1
                cur = cur.next
        except IndexError as e:
            print(e)

    def insertAtPosition(self, index, data):
        cur = self.head
        count = 0
        node = Node(data)
        while cur is not None:
            if count == index-1:

                n = cur.next
                p = cur
                p.next = node
                p.next.next = n
                break

            cur = cur.next
            count += 1
    def insertAfterValue(self, value, data):
         current = self.head
         arr =[]
         while current.data != value:
             arr.append(current.data)
             current = current.next
             if current.next == None:
                print("Value doesn't exists")
                return
         new_node= Node(data)
         new_node.next =current.next
         current.next = new_node

    def insertBeforeValue(self, value, data):
         current = self.head
         arr =[]

         while  current.next.data != value:
             arr.append(current.data)
             current = current.next
             if current.next == None:
                print("Value doesn't exists")
                return
         new_node = Node(data)
         new_node.next =current.next
         current.next = new_node


    def sum_values(self, head, value=0):
        if head is None:
            return
        else:
            current = head.next
            self.sum_values(current)
            value += current.data
            return value
        # if head.next != None:
        #     current = head.next
        #     value += current.data
        #     print(str(value))
        #     self.sum_values(current, value)
        #     return value
        # else:
        #     return


#l = linked_list(1)
#l.display()
l = linked_list(1)
l.append(2)
l.append(3)
l.display()
# l.head = Node(10)
# l.display()
# [l.append(k) for k in range(3)]

# l.display1(l.head)
# l.insertAt(3, 7)
# l.display()

l.insertAfterValue(2, 4)
l.display()
#l.insertAfterValue(4, 6)
#l.insertBeforeValue(4,8)
l.insertBeforeValue(11,18)
l.display()
l.insertAfterValue(11,18)
# print(l.sum_values(l.head))
