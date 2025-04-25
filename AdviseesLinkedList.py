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
        current = self.head
        result = ""
        while current:
            result += str(current.student) + "\n\n"
            current = current.next
        return result.strip()
