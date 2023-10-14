# Overview


This program uses SQLite to create and interact with an SQL database. The 'sales.py' file is responsible for modularizing the SQL commands and the 'bet_stickers_app.py' is responsible for running those modularized commands that the user calls. I used SQLite to initialize the database and create the tables associated with it. The "main" function displays a menu that the user can choose from. Then, after they choose their option, the "main" function calls the functions necessary to fulfill the option.  



I decided to tackle this project so I can learn to integrate my knowlege of Python in a relational database. My wife runs a small sticker business called Bet Stickers. This program will help her keep inventory of their stickers and evaluate which stickers are making her the most money. There are a lot of components that need to be improved to help the program be more user friendly, but it will work if she uses it carefully.

[Demo Video Link](https://youtu.be/etNDO5-IOuM)

# Relational Database

This database uses 2 tables. The "stickers" table contains general information about the sticker and the "sales" table contains the important information of each sale. The stickers table uses the name as the primary key because each name is going to be different. I would have used a sticker ID, but I thought it would be better to use the name since there is not very much data and the name will be easier for my wife to work with. The sales table uses the name of the sticker as the foreign key and the sale ID as the primary key. 


# Development Environment

For this project I just used VSCode. I was able to include the sqlite3 library which allowed me to use SQLite to create my database and manipulate the information inside. Other than that, I did not need to use any other libraries.  


# Useful Websites

- [SQLite Tutorial](https://www.sqlitetutorial.net/)
- [Codemy SQLite Full Course Video](https://www.youtube.com/watch?v=byHcYRpMgI4)

# Future Work


- Create error handling to allow more forgiveness if the user does not provide the correct input(ex.choosing to query a name that does not exist)
- Make the user interface more visually pleasing by possibly creating a web app that allows for more choices to manipulate the database
- Develop more tables and attributes that will keep track of processing orders.  
