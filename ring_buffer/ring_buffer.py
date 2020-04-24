from doubly_linked_list import DoublyLinkedList

#first in first out
class RingBuffer:
    def __init__(self, capacity):
        #max capacity
        self.capacity = capacity
        #current node
        self.current = None
        #list instance
        self.storage = DoublyLinkedList()


    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)

        else:
            # reached capacity
            # drop old
            # first in first out
            #drop head(old) add new to tail
            if self.current == None:
                self.current = self.storage.head

            else:
                # move pointer to next
                self.current = self.current.next
            self.current.value = item



    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here


        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
