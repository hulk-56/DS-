class DoublyLinkedList:
    def _init_(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def is_empty(self) -> bool:
        return self.__size == 0

    def get_size(self) -> int:
        return self.__size

    def __display_backward(self):
        if self.is_empty():
            print("Doubly Linked List is empty")
            return
        last = self.__tail
        print("The List: ", end='')
        print("[" + last.element, end='')
        last = last.prev
