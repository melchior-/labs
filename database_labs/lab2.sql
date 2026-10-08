CREATE TABLE books (
	book_id INTEGER PRIMARY KEY,
	title TEXT NOT NULL,
	author TEXT,
	year INTEGER
);

DROP TABLE books;

CREATE TABLE books (
	book_id INTEGER PRIMARY KEY,
	title TEXT NOT NULL,
	author TEXT,
	year INTEGER CHECK (year > 1400)
);

ALTER TABLE books ADD COLUMN isbn TEXT;

DROP TABLE books;

CREATE TABLE reviews(
	review_id INTEGER PRIMARY KEY,
	product_id INTEGER NOT NULL,
	rating INTEGER NOT NULL CHECK (rating >= 1 AND rating <= 5),
	comment TEXT NOT NULL,
	FOREIGN KEY (product_id) REFERENCES products(product_id)
);

INSERT INTO reviews VALUES(1, 1, 6, "lol");

INSERT INTO reciews VALUES(2, 50, 5, "Good");