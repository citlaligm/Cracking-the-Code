import unittest



class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def append(self, new_element):
        """Adds an elemen to the end of the linked list"""
        current = self.head
        if self.head :
            while current.next:
                current = current.next

            current.next = new_element

        else:
            self.head = new_element

        self.size+=1


    def insert_first(self, new_element):
        """Inserts an element at the start of the linked list"""
        new_element.next = self.head
        self.head = new_element
        self.size += 1

    def delete_first(self):
        if self.head:
            value = self.head.value
            self.head = self.head.next
            self.size -= 1
            return value

        else:
            return None





class ElementTestCase(unittest.TestCase):
    def test_initializer(self):
        element_1 = Element(1)
        self.assertEqual(element_1.value,1,"Value is not 1")
        self.assertEqual(element_1.next, None, "Default value is not None")

class LinkedListTestCase(unittest.TestCase):
    def test_initializer(self):
        my_ll1 = LinkedList()
        self.assertEqual(my_ll1.head,None)

    def test_append(self):
        my_ll2 = LinkedList()
        val = 1
        element = Element(val)
        my_ll2.append(element)
        self.assertEqual(my_ll2.head.value,val)

    def test_size(self):
        my_ll2 = LinkedList()
        val = 1
        element = Element(val)
        my_ll2.append(element)
        val = 1
        element = Element(val)
        my_ll2.append(element)
        self.assertEqual(my_ll2.size,2)


    def test_insert_first(self):
        my_ll3 = LinkedList()
        val = 1
        element = Element(val)
        my_ll3.append(element)
        val = 2
        element = Element(val)
        my_ll3.insert_first(element)

        self.assertEqual(my_ll3.head.value, val)

    def test_delete_first(self):
        my_ll4 = LinkedList()
        val1 = 1
        element = Element(val1)
        my_ll4.append(element)
        val2 = 2
        element = Element(val2)
        my_ll4.insert_first(element)
        val3 = 3
        element = Element(val3)
        my_ll4.append(element)

        my_ll4.delete_first()
        self.assertEqual(my_ll4.head.value, val1)


#Testing Stack

class Stack(object):
    def __init__(self, top=None):
        self.ll = LinkedList(top)

    def push(self,new_element):
        self.ll.insert_first(new_element)

    def pop(self):
        return self.ll.delete_first()







class StackTestCase(unittest.TestCase):
    def testConstructor(self):
        """Test the constructor for class Stack"""
        my_stack = Stack()
        self.assertEqual(my_stack.ll.head,None)

    def testPush(self):
        my_stack = Stack()
        value = 10
        element = Element(value)
        my_stack.push(element)
        self.assertEqual(my_stack.ll.head.value, value)


    def testPop(self):
        my_stack = Stack()
        value1 = 10
        element = Element(value1)
        my_stack.push(element)
        value2 = 20
        element = Element(value2)
        my_stack.push(element)
        value3 = 30
        element = Element(value3)
        my_stack.push(element)
        my_stack.pop()
        self.assertEqual(my_stack.ll.head.value, value2)




#Queue


class Queue(object):
    def __init__(self):
        self.stackOld = Stack()
        self.stackNew = Stack()

    def reverse(self):
        while self.stackNew.ll.size != 0:
            pop_value = self.stackNew.pop()
            element = Element(pop_value)
            self.stackOld.push(element)


    def enqueue(self, element):
        self.stackNew.push(element)

    def deque(self):
        self.reverse()
        return self.stackOld.pop()

    def peek(self):
        self.reverse()
        return self.stackOld.ll.head.value


class QueueTestCase(unittest.TestCase):
    def testConstructor(self):
        my_queue = Queue()
        self.assertEqual(my_queue.stackOld.ll.head,None)
        self.assertEqual(my_queue.stackNew.ll.head,None)


    def testEnque(self):
        my_queue = Queue()
        value1 = 10
        element = Element(value1)
        my_queue.enqueue(element)

        value2 = 2
        element = Element(value2)
        my_queue.enqueue(element)


        value3 = 3
        element = Element(value3)
        my_queue.enqueue(element)


        self.assertEqual(my_queue.peek(), 10)






    def testDequeue(self):
        my_queue = Queue()
        value1 = 1
        element = Element(value1)
        my_queue.enqueue(element)

        value2 = 20
        element = Element(value2)
        my_queue.enqueue(element)

        value3 = 30
        element = Element(value3)
        my_queue.enqueue(element)


        self.assertEqual(my_queue.deque(), 1)



unittest.main()