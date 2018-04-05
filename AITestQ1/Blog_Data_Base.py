import pymysql

# Setup variables for connection to data base
db_server_name = "localhost"
db_user = "testuser"
db_password = "test123"
db_name = "testdb"
char_set = "utf8mb4"
cursor_type = pymysql.cursors.DictCursor

# Connect to the data base server
connection_object = pymysql.connect(
  host = db_server_name,
  user = db_user,
  password = db_password,
  db = db_name,
  charset = char_set,
  cursorclass = cursor_type)

try:
  cursor_object = connection_object.cursor()
  # Variables to Create the SQL Tables and thier feilds
  sql_users = "CREATE TABLE IF NOT EXISTS `Users`(`id` INT NOT NULL AUTO_INCREMENT, `FirstName` VARCHAR(32), `LastName` VARCHAR(32), `UserName` VARCHAR(32), `StartDate` DATE, PRIMARY KEY (`id`))"

  sql_comments = "CREATE TABLE IF NOT EXISTS `Comments`(`id` INT NOT NULL AUTO_INCREMENT, `Blog_Comment_Belongs_To` VARCHAR(32), `UserName` VARCHAR(32), `Date_Created` DATE, PRIMARY KEY (`id`))"

  sql_blogs = "CREATE TABLE IF NOT EXISTS `Blogs`(`id` INT NOT NULL AUTO_INCREMENT, `Author` VARCHAR(32), `Title` VARCHAR(32), `Description` VARCHAR(100), `Date_Created` DATE, PRIMARY KEY (`id`))"
  
  # Statements that create the tables in the data base
  cursor_object.execute(sql_users)   

  cursor_object.execute("show tables")

  cursor_object.execute(sql_comments)   

  cursor_object.execute("show tables")

  cursor_object.execute(sql_blogs)   

  cursor_object.execute("show tables")

  # Variable to help display creation of tables
  rows = cursor_object.fetchall()

  # For statement to display creation of tables
  for row in rows:
    print(row)

# Exception to display errors
except Exception as e:
  print("Exception occured:{}".format(e))

# Close the connection to the data base
finally:
  connection_object.close()