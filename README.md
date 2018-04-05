# AI Coding Test
This is a directory which contains code for the AI Coding Test

## Environment
[Python](https://www.python.org/downloads/release/python-364/) ```v3.6.4```

[pip](https://pip.pypa.io/en/stable/installing/) ```v9.0.1```

[MySQL](https://dev.mysql.com/downloads/mysql/) version ```v5.7.21```

## Question 1 Database design

```
Design a set of SQL tables for a blog. Include users, comments, blog posts, and any other objects you feel are relevant. Please include comments for fields that might be unclear. MySQL is the ideal database to target, but if
you're not familiar with it, others are also acceptable.
```

In the terminal, change directory from your root directory to the ```AITest/AITestQ1``` directory.

Type the below command into your Terminal
```
cd AITest/AITestQ1
```

next you will need to install ```pymysql```
```
pip install pymysql
```

Then start you session of MySQL server.

To configure pymysql to use your MySQL root password, in your IDE open the ```Blog_Data_Base.py``` file.

Find this line
 ```
db_password = "test123"
```
and change ```test123``` to match your MySQL root password and then save.

The last step is to type the below command into your Terminal
```
python3 Blog_Data_Base.py
```

This will add the tables in the ```Blog_Data_Base.py``` file to your MySQL data base

apon success you will see the names of the three tables printed in the Terminal


## Question 2 API Interaction

```
Using http://jsonplaceholder.typicode.com, write a script to get the 200 most recent TODOs, create a TODO,
and delete a TODO given an ID.
```

In the terminal, change directory from your root directory to the ```AITest/AITestQ2``` directory.

Type the below command into your Terminal
```
cd AITest/AITestQ2
```

next you will need to install ```requests```
```
pip install requests
```

The last step is to type the below command into your Terminal
```
python3 GetTODO.py
```

This will first perform a GET API call to ```http://jsonplaceholder.typicode.com/todos``` and will return and print the 200 instances in the todos list.

if the GET API fails it will print ```Request Failed```

Next the program will perform a POST API call to add an instance to the todo list.

The request code will be printed in the Terminal.  A succesful call will display ```201```

Last the progrm will perform a DELETE API call and delete the 200th instance to the todo list.

The request code will be printed in the Terminal.  A succesful call will display ```200```


## Question 3 Algorithms

```
Write a script which prints all the permutations of a string in alphabetical order. We consider that digits < upper
case letters < lower case letters. The sorting should be performed in ascending order.

Your program should accept a file as its first argument. The file contains input strings, one per line. Print to
stdout the permutations of the string separated by comma, in alphabetical order.
```

In the terminal, change directory from your root directory to the ```AITest/AITestQ3``` directory.

Type the below command into your Terminal
```
cd AITest/AITestQ2
```

Then type the below command into your Terminal
```
python3 Permutations1.py input.txt
```

The Permutations1 program will take in the lines of the ```input.txt``` file and print to the terminal all the Permutations of the words on each lines.