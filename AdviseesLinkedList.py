from AdviseeNode import AdviseeNode

class AdviseeLinkedList:
    def __init__(self):
        self.head = None

    def addAdvisee(self, student):
        newNode = AdviseeNode(student)
        newNode.next = self.head
        self.head = newNode

    def removeAdvisee(self, studentID):
        prev = None
        current = self.head
        while current:
            if current.student.getID() == studentID:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True  # removed
            prev = current
            current = current.next
        return False  # not found

    def __str__(self):
        result = ""
        traversalPointer = self.head
        while traversalPointer:
            result += traversalPointer.getData() + " --> "
            traversalPointer = traversalPointer.next
        result += "DONE"
        return result

