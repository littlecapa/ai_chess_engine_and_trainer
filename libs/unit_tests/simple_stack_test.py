import sys
sys.path.append('..')

from src.stack import Stack

s = Stack()

s.push(2)
s.push(3)
print(s.len())
print(s.pop())
s.push(4)
print(s.top())
print(s.pop())
print(s.pop())
print(s.pop())
if s.is_empty:
  print("Empty")