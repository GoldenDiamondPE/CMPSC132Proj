from AdviseeNode import AdviseeNode


class AdviseeLinkedList:
    def __init__(self):
        self.head = None

    def addAdvisee(self, studentID):
        newNode = AdviseeNode(studentID)
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
        current = self.head
        while current:
            result += str(current.getAdviseeNode()) + "\n"
            current = current.next
        return result.strip()

