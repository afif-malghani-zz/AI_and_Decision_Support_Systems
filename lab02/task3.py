# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                        Coded by:                                        #
#                                Muhammad Afif Ul Hasnain                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import time

# create class Binary tree
class Binarytree:

    # class constructor
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # create function for insertion
    def inserting(self, data):
        if self.data:

            # if input data i.e. integer is less than pre-existing data:
            if data < self.data:

                # if there is no child node at left
                if self.left is None:

                    # create new node and insert at left
                    self.left = Binarytree(data)
                # Else insert to left node
                else:
                    self.left.insert(data)

            # if input data is greater than existing data
            elif data > self.data:

                # if no child node at right
                if self.right is None:

                    # create new node and insert at right
                    self.right = Binarytree(data)
                # Else insert at righ
                else:
                    self.right.insert(data)

            # If equal insert at current node
            else:
                self.data = data

    # create a function for search
    # Inorder traversal
    def search(self, data):

        # If there exists a child node to left call the function again from child
        if self.left:
            self.left.search()

        # If the data is at the current node display that is has been found
        if self.data == data:
            return True

        # If there exists a node to right call the function from that node
        if self.right:
            self.right.search()



# create all node as given in the question diagram
root =Binarytree(8)
root.inserting(3)
root.inserting(10)
root.inserting(1)
root.inserting(14)
root.inserting(6)
root.inserting(13)
root.inserting(7)
root.inserting(4)

# starting time
start = time.time()

# search for 13 in the tree
check = root.search(13)

# ending time after the search is complete
end = time.time()

# time taken is time difference between start time and end time
print('time = ', end - start)