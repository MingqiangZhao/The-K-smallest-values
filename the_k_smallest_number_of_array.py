# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 23:31:39 2019

@author: Zhao Mingqiang
"""

#利用堆栈实现，也可以考虑利用小顶堆实现
import numpy as np
class Stack:
  def __init__(self, k):
    self.items = []#Python中强大的链表结构
    self.k = k
  def isEmpty(self):
    return len(self.items) == 0
  
  def push(self, item):
    if len(self.items) < self.k:
      self.items.append(item)
    
  def pop(self):
    return self.items.pop()
  
  def peek(self):
    if not self.isEmpty():
      return self.items[len(self.items) - 1]
    
  def size(self):
    return len(self.items)

data = np.array([1.1,-0.9,3.7,2.8,4.1,6.7,-1,8.4,2.3,0.1])

k = 5
stack1 = Stack(k)
stack2 = Stack(k)


for i in range(len(data)):
  if stack1.isEmpty():
    stack1.push(data[i])
  else:   
    #堆栈stack1中peek比data[i]大就pop，然后push到stack2中，直到遇到peek比data[i]小的数
    #这时候把data[i]push到stack1中。
    #注意push的特殊情况，当stack1为空的时候，说明原来堆栈里所有数都比data[i]小
    #这个时候也要把data[i]push到stack1中
    
    #这个循环主要是把比stack1 peek小的数push到stack1中
    for j in range(k):
      if stack1.peek() > data[i]:
        stack2.push(stack1.pop())
        if stack1.isEmpty():
          stack1.push(data[i])
          break
      else:
        stack1.push(data[i])
        break
       
    #然后把stack2清空，并将保留的数据push到stack1中
    for j in range(k):
      if(not stack2.isEmpty()):
        stack1.push(stack2.pop())
      else:
        break
      
while(not stack1.isEmpty()):    
  print(stack1.pop())   