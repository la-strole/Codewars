SELECT best_sellers_book.name,
	best_sellers_book.author,
	best_sellers_book.copies_sold
FROM best_sellers_book
ORDER BY best_sellers_book.copies_sold DESC
LIMIT 5;
