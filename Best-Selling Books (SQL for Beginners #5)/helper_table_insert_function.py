import csv
from random import randint

def books_maker():
    with open('books.csv', 'a+') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(['name', 'author', 'copies_sold'])
        
        for _ in range(1000):
            writer.writerow([f'{str(_)} name', f'{str(randint(0, 100))} author', f'{str(randint(0, 1000))}'])
            
            
if __name__ == "__main__":
    books_maker()
    
