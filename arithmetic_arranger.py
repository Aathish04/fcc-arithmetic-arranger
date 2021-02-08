from math import fabs
def arithmetic_arranger(problemslist, solve=False):
  
  # The if statement and for loop below do all the checking of input.
  if len(problemslist) > 5:
    return "Error: Too many problems."
  for i in range(len(problemslist)):
    problemslist[i]=problemslist[i].split(" ")
    problem=problemslist[i]
    if problem[1] not in "-+":
      return "Error: Operator must be '+' or '-'."
    try:
      int(problem[0])
      int(problem[2])
    except ValueError:
      return "Error: Numbers must only contain digits."
    
    if int(problem[0])>9999 or int(problem[2])>9999:
      return "Error: Numbers cannot be more than four digits."
  
  # This will be the final output. It will be built by the loops below.
  problemstring=""

  for i in range(len(problemslist)):
    problem=problemslist[i]
    greater=max(problem[0],problem[2],key=len)
    smaller=min(problem[0],problem[2],key=len)
    
    #Gets the number of spaces that go between the operator and second operand.
    n_opspaces=len(greater)-len(smaller) if (problem[0]==greater and not len(greater)==len(smaller)) else 1
    n_opspaces+=1 if len(problem[0]) > len(problem[2]) else 0
    
    #Makes the second operand merge with the operator with the appropriate spacing.
    problem[1]=problem[1]+(n_opspaces)*" "+problem[2]
    
    #The last item of the list isn't needed anymore.
    problem.pop()

    #Properly space the first operand.(Unrelated to the 4 spaces later.)
    problem[0]=" "*(len(problem[1])-len(problem[0]))+problem[0]

  problemstring="    ".join([problem[0] for problem in problemslist]) # 4 spaces spacing for each first operand.
  problemstring+="\n" # Newline before second operands and operators.
  problemstring+="    ".join([problem[1] for problem in problemslist]) # 4 spaces spacing for each first operand.
  problemstring+="\n" # Newline before dashes.

  for problem in problemslist: # Four spaces before each dashes.
    problemstring+= "-"*len(problem[1])+4*" "
  
  problemstring=problemstring.rstrip(" ") #Get rid of spaces at the very end.
  
  if solve:
    problemstring+="\n"
    for problem in problemslist:
      solution=str(eval("".join(problem))) # Solve the problem.
      problemstring+=(len(problem[1])-len(solution))*" "+solution+"    " # Space it properly.
  problemstring=problemstring.rstrip(" ")

  return problemstring
