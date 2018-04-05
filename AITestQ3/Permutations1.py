import sys

# Function to perform the permutation
def permutation(lst):

  # If the list if empty there are no purmutations and
  # and an empty list is returned
  if len(lst) == 0:
    return []
  
  # If there is only one charater in the list than
  # only one purmutations can be perfomred and is returned
  if len(lst) == 1:
    return [lst]
  
  l = [] #This is an empty list to add the current purmutations to

  # iterates through the length of the list 
  for i in range(len(lst)):
    # this extracts the index of the list for the current purmutation
    m = lst[i] 

    # This is the remaining list 
    remLst = lst[:i] + lst[i+1:]

    # This adds the current element to the current purmutation
    for p in permutation(remLst):
      l.append([m] + p)
  # this returns the new purmutation
  return l

# This opens the text input file
with open(sys.argv[1]) as f:
   # This interates through the lines of the input file
   for line in f:
    # This sorts the word on the line and turns it into a list
    data = list(sorted(line.replace('\n', '')))
    k=[] # This is an emplty list to store the new purmutations

    for p in permutation(data):
      # this adds the new purmutations to the list of other purmutations
      k.append(p)
    # this formats the list of purmutations back into a string
    string = ''.join(str(k).strip('[]'))
    # this prints out the purmutations for the current line
    print(string)