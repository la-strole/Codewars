You work at a book store. It's the end of the month, and you need to find out the 5 bestselling books at your store. Use a select statement to list names, authors, and number of copies sold of the 5 books which were sold most.

books table schema

    name
    author
    copies_sold

NOTE: Your solution should use pure SQL. Ruby is used within the test cases just to validate your answer.

<<<<<<< HEAD:Best-Selling Books (SQL for Beginners #5)/readme.md
helper_table_insert_function.py - создает books.csv. поля name, author, copies_sold.
				   1000 записей, author - случайное из 0-100, books_name - 					   уникальное, copies sold - случайное из 0-1000.

=======
helper_table_insert_function.py - создает books.csv. поля name, author, copies_sold. 1000 записей, 
				author - случайное из 0-100, 
				books_name - уникальное, 
				copies sold - случайное из 0-1000.
				   
>>>>>>> a2875e895cf226e93f884ce69a98d6ce2c114f91:Best-Selling Books (SQL for Beginners #5)/readme.txt
books.csv - результат работы helper_table_insert_function.py
books.db - база данных с таблицей best_sellers_book из books.csv
best_sellers.sql - набор команд для создания БД 

Запуск и создание окружения:

`$ sqlite3 books.db`<br/>
`sqlite> .read best_sellers.sql`

Решение задачи:
<<<<<<< HEAD:Best-Selling Books (SQL for Beginners #5)/readme.md

`sqlite> .read five_best_books.sql`
=======
> .read five_best_books.sql

Требования к окружению:
1. sqlite3
>>>>>>> a2875e895cf226e93f884ce69a98d6ce2c114f91:Best-Selling Books (SQL for Beginners #5)/readme.txt
