delete from fine;
delete from loan;
delete from librarian;
delete from bookItem;
delete from member;
delete from book;

insert into member(name, phone, email, balance) values ('Jordan', '738-222-4533', 'email@gmail.com', '0');
insert into member(name, phone, email, balance) values ('Bob', '738-322-4533', 'email@gmail.com', '0');
insert into member(name, phone, email, balance) values ('James', '222-322-4893', 'email@gmail.com', '0');


insert into bookItem(isbn) values('978-3-16-148410-0');
insert into bookItem(isbn) values('549-3-16-148410-0');
insert into bookItem(isbn) values('222-3-16-148410-0');
insert into bookItem(isbn) values('456-3-16-148410-0');


insert into loan(b_id, m_id, checkout_date, due_date, librarian_id, status)  values ('1', '1', '02-20-2020', '03-20-2020', '1', 'active');
insert into loan(b_id, m_id, checkout_date, due_date, librarian_id, status)  values ('1', '2', '02-20-2020', '03-20-2020', '1', 'complete');
insert into loan(b_id, m_id, checkout_date, due_date, librarian_id, status)  values ('1', '2', '02-20-2020', '03-20-2020', '1', 'complete');

insert into book(ISBN, author, title, year, pages, numOfCopies)  values ('978-3-16-148410-0', 'Miller','Pandemic',  '2020','330','2');
insert into book(ISBN, author, title, year, pages, numOfCopies)  values ('549-3-16-148410-0', 'Johnson','Search','1990','500','2');
insert into book(ISBN, author, title, year, pages, numOfCopies)  values ('222-3-16-148410-0', 'James','Legend','1990','500','2');
insert into book(ISBN, author, title, year, pages, numOfCopies)  values ('456-3-16-148410-0', 'Thomas','The Hill','1990','500','2');
