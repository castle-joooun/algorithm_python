def is_valid(string):
  check = []

  for s in string:
    if len(check) > 0:
      if s == ')' and '(' == check[-1]:
        check.pop()
        continue
      
      if s == '}' and '{' == check[-1]:
        check.pop()
        continue

      if s == ']' and '[' == check[-1]:
        check.pop()
        continue
    
    if s in ['(', '{', '[']:
              check.append(s)
    else:
      return False
    
  return True if len(check) == 0 else False

