class BSTNode:
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None


    def set_left_child(self,left_value):
        self.left = left_value

    def set_right_child(self,right_value):
        self.right = right_value

    def get_value(self):
        return self.data

    def get_left_value(self):
        return self.left

    def get_right_value(self):
        return self.right

    def has_left_child(self):
        return  self.left != None

    def has_right_child(self):
        return self.right