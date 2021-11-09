# Best-Selling Books (SQL for Beginners #5)
## https://www.codewars.com/kata/591127cbe8b9fb05bd00004b

You work at a book store. It's the end of the month, and you need to find out the 5 bestselling books at your store. Use a select statement to list names, authors, and number of copies sold of the 5 books which were sold most.

books table schema

    name
    author
    copies_sold

NOTE: Your solution should use pure SQL. Ruby is used within the test cases just to validate your answer.

## Create DB:
1. `helper_table_insert_function.py` - create 1000 random items and save it on `books.csv`;
2. `best_sellers.sql` - import `books.csv` to `best_sellers_book` table;
3. `books.db` - database with 1000 random rows of book from `books.csv`.

## How to run:
1. Open `books.db`;
2. Run `five_best_books.sql`;
