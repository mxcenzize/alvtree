class Binary_Search_Tree:

  class _BST_Node:
    
    def __init__(self, value):
      self._value = value
      self._left = None
      self._right = None
      self._height = 1
      
    def _update_height(self):
      max_value = 0
      
      if self._left is not None or self._right is not None:
        
        if self._left is None:
          max_value = self._right._height
          
        elif self._right is None:
          max_value = self._left._height
        
        else:
          if self._right._height > self._left._height: 
            max_value = self._right._height
          
          else:
            max_value = self._left._height
          
        height = max_value + 1
        return height
      
      else:
        height = 1
        return height
      
  def __init__(self):
    self._root = None

  def insert_element(self, value):
    self._root = self._private_insert(value, self._root)
      
  def _private_insert(self, value, node):
    if node is None:
      node = Binary_Search_Tree._BST_Node(value)    
      
    else:    
      if value < node._value:
        node._left = self._private_insert(value, node._left)
        
      elif value > node._value: 
        node._right = self._private_insert(value, node._right)   
      
      else:
        raise ValueError 
    
    return self._balance(node)

  def remove_element(self, value):
    self._root = self._private_remove(value, self._root)
  
  def _private_remove(self, value, node):
    if node is None: 
      raise ValueError    
    
    #When value to be removed is at root
    if node._value == value:
      if node._left is None and node._right is None:
        node = None
        
      elif node._left is None and node._right is not None:
        node = node._right
        
      elif node._right is None and node._left is not None:
        node = node._left
  
      else:
        #check for min in right tree
        min_value = node._right
        while min_value._left is not None:
          min_value = min_value._left
          
        #update root node
        node._value = min_value._value 
        node._right = self._private_remove(min_value._value, node._right)
         
    else:
      if value < node._value:
        node._left = self._private_remove(value, node._left)
      elif value > node._value:
        node._right = self._private_remove(value, node._right) 
        
    return self._balance(node)
  
  def _balance(self, t):
    
    if t is None:
      return t

    elif t._right is not None and t._left is not None:
      if abs((t._right._height) - (t._left._height)) <= 1:
        t._height = t._update_height()
        return t

    elif t._right is None and t._left is not None:
      if abs(0 - (t._left._height)) <= 1:
        t._height = t._update_height()
        return t

    elif t._left is None and t._right is not None:
      if abs((t._right._height) - 0) <=1:
        t._height = t._update_height()
        return t

    elif t._left is None and t._right is None:
      return t

#left-heavy
    else:
      if t._right._right._height - t._right._left._height == -1 or 0:
        
        floater = t._left._right
        child = t._left
        child._right = t
        child._right._left = floater
        t = child

        child._right._height = child._right._update_height()
        t._height = t._update_height()
        return t
          #rotate right about t and return new root

      elif t._right._right._height - t._right._left._height == 1:
        
        #2 rotation
        #is it better to just say else?

        #1
        floater = t._left._right._left
        child = t._left
        t._left = t._left._right
        t._left._left = child
        child._right = floater
        #rotate left about t's left child.

        child._height = child._update_height()
        t._left._height = t._left._update_height()

        #2
        the_child = t._left
        second_floater = t._left._right
        t._left._right = t
        t = the_child
        t._right._left = second_floater

        t._right._height = t._right._update_height()
        t._height = t._update_height()
        return t
        #then rotate right about t and return new root

      else:
          
        #right heavy
        #1 rotation
        if t._right._right._height - t._right._left._height == 1 or 0:
          floater = t._right._left
          child = t._right
          child._left = t
          t = child

          t._left._height = t._left._height
          t._height = t._update_height()
          return t
        #rotate left about t and return the new root

        #2 rotations
        elif t._right._right._height - t._right._left._height == -1:

          #1
          floater = t._right._left._right
          child = t._right
          t._right = t._right._left
          t._right._right = child
          child._left = floater
          #rotate right about t's left child

          child._height = child._update_height()
          t._right._height = t._right._update_height()

          #2
          second_floater = t._right._left
          temporary = t
          t = t._right
          t._left = temporary
          t._left._right = second_floater

          t._left._height = t._left._update_height()
          t._height = t._update_height()
          return t
          #then rotate left about t and return the new root

      
  def in_order(self):
    
    if self._root is None:
      return "[ ]"
    else:
      tree_string = self._private_in_order(self._root)
      tree_string = tree_string[:-2] 

      final_string = "[ " + tree_string + " ]"

      return final_string
    	   
  def _private_in_order(self, node):
    #In-Order: Left child first, then parent, then right child(recursively)
    if node is None:
      return str("")
    
    else:
      left_node_string = self._private_in_order(node._left)
      right_node_string = self._private_in_order(node._right)
      
      tree = str(left_node_string) + str(node._value) + ", "\
        + str(right_node_string)
      return tree

  def pre_order(self):
    tree_string = self._private_pre_order(self._root)
    tree_string = tree_string[:-2]
    
    final_string = "[ " + tree_string + " ]"
    return final_string
   
  def _private_pre_order(self, node):
    #Pre-Order: Parent first, then left child, then right child(recursively)
    if node is None:
      return str("")
    
    else:
      left_node_string = self._private_pre_order(node._left)
      right_node_string = self._private_pre_order(node._right)
      tree = str(node._value) + ", " + str(left_node_string) +\
        str(right_node_string)   
      return tree

  def post_order(self):
    tree_string = self._private_post_order(self._root)
    tree_string = tree_string[:-2]
        
    final_string = "[ " + tree_string + " ]"
    return final_string   
  
  def _private_post_order(self, node):
    #Post-Order: Left child first, then right child, then parent(recursively)
    if node is None:
      return str("")
      
    else:
      left_node_string = self._private_post_order(node._left)
      right_node_string = self._private_post_order(node._right)
      tree = str(left_node_string) + str(right_node_string) +\
        str(node._value) + ", "   
      return tree  

  def get_height(self):
    if self._root is None:
      return 0
    else:  
      return self._root._height

  def __str__(self):
    return self.in_order()

if __name__ == '__main__':
  pass #unit tests make the main section unnecessary.
