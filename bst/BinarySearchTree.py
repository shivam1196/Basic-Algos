from bst.BSTNode import BSTNode


class BinarySearchTree:
    def __init__(self):
        self.node_value = None


    def insert_node(self,value):
        if self.node_value == None:
            self.node_value = BSTNode(value)

        else:
            is_inserted = False
            current_node = self.node_value

            while(not is_inserted):
                if(value < current_node.data and current_node.has_left_child()):
                    current_node =current_node.get_left_value()

                elif value > current_node.data and current_node.has_right_child():
                    current_node = current_node.get_right_value()

                elif value < current_node.data and not current_node.has_left_child():
                    current_node.set_left_child(BSTNode(value))
                    is_inserted = True

                elif value > current_node.data and not current_node.has_right_child():
                    current_node.set_right_child(BSTNode(value))
                    is_inserted = True

    def delete_node(self,value):
        current_node = self.node_value
        is_deleted = False
        minimum_value = None

        while ( not is_deleted):
            if(value == current_node.data):
                temp_node = current_node.get_right_value()
                minimum_value = temp_node.data

                while(temp_node is not None):
                    if(minimum_value > temp_node.data):
                        minimum_value = temp_node.data
                        temp_node = temp_node.get_right_value()
                    else:
                        temp_node = temp_node.get_right_value()

                if(minimum_value != None):
                    current_node.data = minimum_value








if __name__ == "__main__":
    binary_search_tree = BinarySearchTree()

    binary_search_tree.insert_node(80)
    binary_search_tree.insert_node(10)
    binary_search_tree.insert_node(40)
    binary_search_tree.insert_node(120)
    binary_search_tree.insert_node(100)

    print "Inserted"



