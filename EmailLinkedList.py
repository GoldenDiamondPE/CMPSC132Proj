from EmailInfoNode import EmailNode

class EmailLinkedList:
    def __init__(self):
        self.head = None

    def addEmail(self, info):
        newNode = EmailNode(info)
        newNode.next = self.head
        self.head = newNode

    def removeEmail(self, info):
        prev = None
        current = self.head
        while current:
            if current.email.getStudentEmail() == info:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True  # successfully removed
            prev = current
            current = current.next
        return False  # course not found

    def __str__(self):
        result = ""
        current = self.head
        while current:
            result += str(current.getStudentEmail()) + "\n"
            current = current.next
        return result.strip()
