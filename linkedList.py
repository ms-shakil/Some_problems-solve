############ singal lInked list

class Node:
    def __init__(self ,value = None , next =None):
        self.data  = value
        self.next = next

class Linked_list:

    def __init__(self):
        self.head  = None


    def Add(self,value):
        node = Node(value)
        if self.head is  None:
            self.head = node
            return
        cu_node = self.head
        while cu_node.next is not None:
            cu_node =cu_node.next
        cu_node.next = node

    def prepend(self,value):
        node  = Node(value)
        if self.head is not None:
            node.next = self.head
            self.head = node    
    
    def add_after_item(self, old_value,new_value):
        hd = self.head
        while hd is not None:
            if hd.data == old_value:
                break
            hd = hd.next
        if hd is None :
            print("Old item not here")
        else:
            node = Node(new_value)
            node.next = hd.next
            hd.next = node

    def Search(self,value):
        hd = self.head
        while hd is not None:
            if hd.data == value:
                print(f"Yes we find that >>> { value}")
                return 
            hd = hd.next    
        return "we don't find this value"                       

    def __str__(self):
        _list = []
        hd = self.head
        while hd is not None :
            _list.append(hd.data)
            hd = hd.next
        return f"{_list}"
         

LL = Linked_list()
LL.Add("Shakil") 
LL.Add("main")
LL.Add("payer") 
LL.Add("sajjad")
LL.prepend("Fahad")
LL.prepend("Asif")
LL.add_after_item("main","Noyon")
LL.add_after_item("Fahad","Me")
LL.Search("Fahad")
print(LL)


############ Doubly LInked List 


class Node :
    
    def __init__(self,value):
        self.data = value
        self.next = None
        self.prev = None

class Doubly_Linked_list():
    def __init__(self):
        self.head = None

    def Add (self,value):
        node = Node(value)

        if self.head is  None :
            self.head  = node
            return

        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next

        curr_node.next = node
        node.prev = curr_node
    
    def prepend(self,value):
        node = Node(value)
        if self.head is not None:
            self.head.prev = node
            node.next = self.head
            self.head = node


    def Add_after_Item(self,old_value,new_value):
        node = Node(new_value)
        hd = self.head
        while hd is not None:
            if hd.data == old_value:
                break
            hd = hd.next
        if hd is None:
            print("Don't get This element")
        else:
            node.next = hd.next
            hd.next.prev = node
            hd.next = node
            node.prev = hd              

    def Delete(self,value):
        hd = self.head
        while hd is not None:
            if hd.data == value:
                hd.prev.next= hd.next
                hd.next.prev = hd.prev
                break
            hd = hd.next    

    def __str__(self):
        _list = []
        hd = self.head
        while hd is not None :
            _list.append(hd.data)
            hd = hd.next
        return f"{_list}"                


DL = Doubly_Linked_list()

DL.Add("Shakil")
DL.Add("Main")
DL.Add("Payer")
DL.prepend("Fahad")
DL.Add_after_Item("Main","Me")
DL.Delete("Me")
print(DL)