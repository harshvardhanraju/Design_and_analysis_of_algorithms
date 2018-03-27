"""
@Harsha
Date : 23/3/18
Single source reservation for airlines using bst

TODO:
    1. Need to improve the insert algo. It is too complex now bcoz the logic
    was not properly designed with all edge cases in mind at the begining!
"""


from bst import BST


class RESERVATION_SYS(BST):
    """
    Inherits basic funcs from BST and defines its own insert fns based on req
    """

    def __init__(self, K):
        self.bst = BST()
        self.k = K

    def insert_reservation(self, val):
        if val <= cur_time:
            print("You have entered time in past, You douchebag !")
            return
        elif self.bst.root is None:
                self.bst.insert(val)
        else:
            current_node = self.bst.root
            while True:
                if val < current_node.val:
                    if current_node.left is None:
                        if val < current_node.val + self.k:
                            self.bst.insert(val)
                            return
                        else:
                            print("Error cant Insert")
                            return
                    else:
                        if current_node.left.val + self.k < val:
                            self.bst.insert(val)
                            return
                        elif current_node.val - self.k < val or current_node.left.val + self.k > val and current_node.left.val < val:
                            print("Error cant insert")
                            return
                        else:
                            current_node = current_node.left
                else:
                    if current_node.right is None:
                        if val > current_node.val + self.k:
                            self.bst.insert(val)
                            return
                        else:
                            print("Error cant Insert")
                            return
                    else:
                        if current_node.right.val - self.k > val:
                            self.bst.insert(val)
                            return
                        elif current_node.val + self.k > val or current_node.right.val - self.k < val and current_node.right.val > val:
                            print("Error cant insert")
                            return
                        else:
                            current_node = current_node.right


if __name__ == "__main__":
    cur_time = 5  # useful to reject queries for time which has passed!
    reserve = RESERVATION_SYS(3)
    reserve.insert_reservation(4)
    reserve.insert_reservation(6)
    reserve.insert_reservation(10)
    reserve.insert_reservation(25)
    reserve.insert_reservation(25)
    reserve.insert_reservation(25)
    reserve.insert_reservation(7)
    m = reserve.bst.find_min()
    print(m)
    reserve.bst.delete_min()
    m = reserve.bst.find_min()
    print(m)
