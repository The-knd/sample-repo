class Stack:
  
  def __init__(self):
    self.__items=[]
    
  def isEmpty(self):
    return self.__items == []
    
  def push(self,item):
    self.__items.append(item)
    
  def peek(self):
    return self.__items[-1]
    
  def pop(self):
    return self.__items.pop()








