import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

def brackets_ok(expression):
   expression_queue = queue.LifoQueue()
   opening_brackets = ["{", "(", "["]
   closing_brackets = ["}", ")", "]"]
   for char in expression:
      if char in opening_brackets:
         expression_queue.put(char)
      elif char in closing_brackets:
         bracket_of = expression_queue.get()
         if bracket_of + char == "{}" or bracket_of + char == "()" or bracket_of + char == "[]":
            return True
         else:
            return False
    
   
print(brackets_ok(expression1))
print(brackets_ok(expression2))
print(brackets_ok(expression3))