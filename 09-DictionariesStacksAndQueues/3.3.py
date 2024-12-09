import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

def brackets_ok(expression):
   expression_queue = queue.LifoQueue()
   matching_brackets = {")":"(", "}":"{", "]":"["}
   for char in expression:
      if char in matching_brackets.values():
         expression_queue.put(char)
      elif char in matching_brackets.keys():
         if expression_queue.empty() or expression_queue.get() != matching_brackets[char] :
            return False
   if expression_queue.empty() :
      return True
   elif not expression_queue.empty():
      return False
  
   
print(brackets_ok(expression1))
print(brackets_ok(expression2))
print(brackets_ok(expression3))