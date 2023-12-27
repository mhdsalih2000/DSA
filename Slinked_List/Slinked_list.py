class Node:
    def __init__(self,data):
        self.data =data
        self.Next =None

class Slinked_list:
    def __init__(self):
        self.Head = None
        self.Tail= None


    def addNode(self,data):
        new_Node =Node(data)

        if self.Head is None:
            self.Head = new_Node
            self.Tail =new_Node
        else:
            self.Tail.Next =new_Node
            self.Tail=new_Node
            
    def print_sls(self):
        if self.Head is None:
            print("list is Empty")
            return
        temp =self.Head
        while temp != None:
            print(temp.data)
            temp =temp.Next

    def Delete(self,data):
        temp = self.Head
        if temp!=None and temp.data==data:
            self.Head =temp.Next
            return 
        







s1 = Slinked_list()
s1.addNode(10)
s1.addNode(20)
s1.print_sls()