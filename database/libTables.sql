drop table IF EXISTS fine;
drop table IF EXISTS loan;
drop table IF EXISTS librarian;
drop table IF EXISTS bookItem;
drop table IF EXISTS member;
drop table IF EXISTS book;

PRAGMA foreign_keys=off;

CREATE TABLE fine (l_id INTEGER,
					  amount INT NOT NULL,
                      status varchar(13) NOT NULL,
                      PRIMARY KEY(l_id),
                      FOREIGN KEY (l_id) REFERENCES loan(ID));
CREATE TABLE loan (ID INTEGER PRIMARY KEY,
					  b_id INT NOT NULL,
					  m_id INT NOT NULL,
                      checkout_date DATE,
                      due_date DATE NOT NULL,
                      l_id INT NOT NULL,
					  status varchar(13) NOT NULL,
                      FOREIGN KEY(b_id) REFERENCES bookItem(ID)
					  ON DELETE NO ACTION,
                      FOREIGN KEY(m_id) REFERENCES member(ID)
					  ON DELETE NO ACTION,
					  FOREIGN KEY(l_id) REFERENCES librarian(ID)
					  ON DELETE NO ACTION);
CREATE TABLE librarian (ID INTEGER PRIMARY KEY,
					  username TEXT NOT NULL,
                      phone varchar(22) NOT NULL,
                      email TEXT NOT NULL,
                      password TEXT NOT NULL);
CREATE TABLE bookItem (ID integer PRIMARY KEY,
					  isbn varchar(13) NOT NULL,
					  FOREIGN KEY (isbn) REFERENCES book(ISBN));
CREATE TABLE member (ID INTEGER PRIMARY KEY,
					  name char(50),
					  phone varchar(22) NOT NULL,
					  email char(50),
					  balance INT);
CREATE TABLE book (ISBN varchar(13) NOT NULL,
					  author char(50) NOT NULL,
					  title char(50) NOT NULL,
					  year INT NOT NULL,
					  pages INT NOT NULL,
					  numOfCopies INT NOT NULL,
					  PRIMARY KEY(ISBN));
PRAGMA foreign_keys=on;
