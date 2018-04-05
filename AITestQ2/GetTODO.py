import json
import requests

# Below sets the variables for the API call URL & Headers
url = 'http://jsonplaceholder.typicode.com/todos'
headers = {'Content-Type': 'application/json',}

# Below is the function to perform a GET method call using requests
def get_TODO_List():

  # Below performs the GET call
  response = requests.get(url, headers=headers)

  # Below returns the todo list package in a JSON format if the response code is 200
  # if the response code is not 200 it returns "None"
  if response.status_code == 200:
    return json.loads(response.content.decode('utf-8'))
  else:
    return None

# Below is the function to perform a POST method call using requests
# a parameter representing the number of todo instances in the list is required
def add_TODO_list(todo_len):

  # Below adds the new instance to the end of the list
  add_id = todo_len + 1
  # Below are the items being added to the new instance
  payload = {"userId": 10,
      "id": add_id,
      "title": 'make dinner',
      "completed": False
    }
  
  # Below performs the POST call
  response = requests.post(url, data=payload)

  return response.status_code

# Below is the function to perform a DELETE method call using requests
# 
def delete_TODO_list(del_num):

  # This concatonates the url with the instance to be deleted
  fin_url = url + "/" + str(del_num)
  # Below performs the DELETE call
  response = requests.delete(fin_url)

  return response.status_code

# Below is the funtion for printing the Todo list
def print_TODO(TODO_List,TODO_List_Len):
  if TODO_List is not None:
    print("Here is your To Do List: ")
    for i in range(TODO_List_Len):
      for k, v in TODO_List[i].items():
        print('{0}:{1}'.format(k,v))
      print("")
  else:
    print('Request Failed')

# Below calls the Get_TODO_List Function
TODO_List = get_TODO_List()
# Below sets the number of instaces of the todo list to a variable
TODO_List_Len = len(TODO_List)

# this calls the print todo list functions
print_TODO(TODO_List,TODO_List_Len)

# These two lines prints the status of the add todo list function
# and prints the statsu of the delete todo list function
print(add_TODO_list(TODO_List_Len))
print(delete_TODO_list(200))

# if the API was real and I could change the instances I would perfomr 
# another GET to the API and print the new todo lists to the screen to
# show the changes took place