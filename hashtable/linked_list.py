class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next if next is not None else None
    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next
    
    def set_next(self, new_next):
        self.next = new_next
        
    def __repr__(self):
        return str(self.value)
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def __repr__(self):
        currString = ""
        curr = self.head
        while curr is not None:
            currString += f'{str(curr.value)} -> '
            curr = curr.next
        return currString
    def add_to_head(self, node):
        node.next = self.head
        self.head = node
        
    def delete(self, value): 
        curr = self.head
        if curr.value == value:
            self.head = curr.next
            return curr
        
        prev = curr
        curr = curr.next
        
        while curr is not None:
            if curr.value == value:
                prev.next = curr.next
                curr.next = None
            else:
                prev = curr
                curr = curr.next      
        return None
    
    def contains(self, value):
        current = self.head
        while current:
            if current.get_value() == value:
                return current
            
            current = current.get_next()
        return None
        
    def insert_or_overwrite(self, node):
        existingNode = self.contains(node.value)
        if existingNode is not None:
            existingNode.value = node.value
        else:
            self.add_to_head(node)