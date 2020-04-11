drop table IF EXISTS fine;
drop table IF EXISTS loan;
drop table IF EXISTS librarian;
drop table IF EXISTS bookItem;
drop table IF EXISTS member;
drop table IF EXISTS book;

PRAGMA foreign_keys=off;

CREATE TABLE fine (l_id INTEGER,
					  amount INT NOT NULL,
                      status INT NOT NULL,
                      PRIMARY KEY(l_id),
                      FOREIGN KEY (l_id) REFERENCES loan(ID));
CREATE TABLE loan (ID INTEGER,
					  b_id INT NOT NULL,
					  m_id INT NOT NULL,
                      checkout_date DATE,
                      due_date DATE NOT NULL,
                      l_id INT NOT NULL,
                      PRIMARY KEY (ID),
                      FOREIGN KEY(b_id) REFERENCES bookItem(ID),
                      FOREIGN KEY(m_id) REFERENCES member(ID),
					  FOREIGN KEY(l_id) REFERENCES librarian(ID));
CREATE TABLE librarian (ID INTEGER PRIMARY KEY,
					  username TEXT NOT NULL,
                      phone varchar(22) NOT NULL,
                      email TEXT NOT NULL,
                      password TEXT NOT NULL);
CREATE TABLE bookItem (ID INTEGER NOT NULL,
					  isbn varchar(13) NOT NULL,
					  PRIMARY KEY (ID),
					  FOREIGN KEY (isbn) REFERENCES book(ISBN));
CREATE TABLE member (ID INTEGER NOT NULL,
					  name char(50),
					  phone varchar(22) NOT NULL,
					  email char(50),
					  balance INT,
					  PRIMARY KEY(ID));
CREATE TABLE book (ISBN varchar(13) NOT NULL,
					  author char(50) NOT NULL,
					  title char(50) NOT NULL,
					  year INT NOT NULL,
					  pages INT NOT NULL,
					  PRIMARY KEY(ISBN));

PRAGMA foreign_keys=on;
