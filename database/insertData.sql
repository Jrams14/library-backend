delete from fine;
delete from loan;
delete from librarian;
delete from bookItem;
delete from member;
delete from book;

insert into member(name, phone, email, balance) values ('Michael Scott', '738-222-4533', 'Michael@gmail.com', '0');
insert into member(name, phone, email, balance) values ('Jim Halpert', '898-333-4533', 'Jim@gmail.com', '0');
insert into member(name, phone, email, balance) values ('Pam Beesly', '433-444-54', 'Pam@gmail.com', '0');
insert into member(name, phone, email, balance) values ('Creed Bratton', '222-433-5778', 'Creed@gmail.com', '0');
insert into member(name, phone, email, balance) values ('Dwight Schrute', '347-432-2899', 'Dwight@gmail.com', '0');


insert into loan(bi_id, m_id, checkout_date, due_date, librarian_id, status)  values ('1', '1', '02-20-2020', '03-20-2020', '1', 'complete');
insert into loan(bi_id, m_id, checkout_date, due_date, librarian_id, status)  values ('2', '2', '02-20-2020', '03-20-2020', '1', 'complete');
insert into loan(bi_id, m_id, checkout_date, due_date, librarian_id, status)  values ('4', '2', '02-20-2020', '03-20-2020', '1', 'complete');
insert into loan(bi_id, m_id, checkout_date, due_date, librarian_id, status)  values ('1', '2', '02-20-2020', '03-20-2020', '1', 'complete');
insert into loan(bi_id, m_id, checkout_date, due_date, librarian_id, status)  values ('5', '3', '02-20-2020', '03-20-2020', '1', 'complete');
insert into loan(bi_id, m_id, checkout_date, due_date, librarian_id, status)  values ('8', '4', '02-20-2020', '03-20-2020', '1', 'complete');
insert into loan(bi_id, m_id, checkout_date, due_date, librarian_id, status)  values ('8', '5', '02-20-2020', '03-20-2020', '1', 'complete');
insert into loan(bi_id, m_id, checkout_date, due_date, librarian_id, status)  values ('8', '1', '02-20-2020', '03-20-2020', '1', 'complete');
insert into loan(bi_id, m_id, checkout_date, due_date, librarian_id, status)  values ('20', '4', '02-20-2020', '03-20-2020', '1', 'complete');
insert into loan(bi_id, m_id, checkout_date, due_date, librarian_id, status)  values ('20', '2', '02-20-2020', '03-20-2020', '1', 'complete');
insert into loan(bi_id, m_id, checkout_date, due_date, librarian_id, status)  values ('20', '3', '02-20-2020', '03-20-2020', '1', 'complete');
insert into loan(bi_id, m_id, checkout_date, due_date, librarian_id, status)  values ('16', '2', '02-20-2020', '03-20-2020', '1', 'complete');
insert into loan(bi_id, m_id, checkout_date, due_date, librarian_id, status)  values ('16', '5', '02-20-2020', '03-20-2020', '1', 'complete');
insert into loan(bi_id, m_id, checkout_date, due_date, librarian_id, status)  values ('14', '2', '02-20-2020', '03-20-2020', '1', 'complete');









insert into book(ISBN, author, title, year, pages, numOfCopies)  values ('978-3-16-148410-0', 'Miller','Pandemic',  '2020','330','2');
insert into book(ISBN, author, title, year, pages, numOfCopies)  values ('549-3-16-148410-0', 'Johnson','Search','1990','500','2');
insert into book(ISBN, author, title, year, pages, numOfCopies)  values ('222-3-16-148410-0', 'James','Legend','1990','500','2');
insert into book(ISBN, author, title, year, pages, numOfCopies)  values ('456-3-16-148410-0', 'Thomas','The Hill','1990','500','2');
insert into book(ISBN, author, title, year, pages, numOfCopies)  values ('432-1-18-198410-0', 'Ramsey','Wash Ya Hands','2020','500','2');
insert into book(ISBN, author, title, year, pages, numOfCopies)  values ('992-1-12-347410-0', 'Schrute','Assistant Regional Manager Guide','2006','300','2');
insert into book(ISBN, author, title, year, pages, numOfCopies)  values ('352-1-19-340070-0', 'Scott','Somehow I Manage','2006','300','2');
insert into book(ISBN, author, title, year, pages, numOfCopies)  values ('444-8-19-632070-0', 'Halpert','Best Office Pranks','2006','300','2');
insert into book(ISBN, author, title, year, pages, numOfCopies)  values ('843-4-14-637830-0', 'Hart','The Calling','2003','500','2');
insert into book(ISBN, author, title, year, pages, numOfCopies)  values ('123-4-00-983440-0', 'Rowling','Harry Potter and the Goblet of Fire','2000','586','2');

insert into bookItem(isbn) values('978-3-16-148410-0');
insert into bookItem(isbn) values('978-3-16-148410-0');
insert into bookItem(isbn) values('549-3-16-148410-0');
insert into bookItem(isbn) values('549-3-16-148410-0');
insert into bookItem(isbn) values('222-3-16-148410-0');
insert into bookItem(isbn) values('222-3-16-148410-0');
insert into bookItem(isbn) values('456-3-16-148410-0');
insert into bookItem(isbn) values('456-3-16-148410-0');
insert into bookItem(isbn) values('432-1-18-198410-0');
insert into bookItem(isbn) values('432-1-18-198410-0');
insert into bookItem(isbn) values('992-1-12-347410-0');
insert into bookItem(isbn) values('992-1-12-347410-0');
insert into bookItem(isbn) values('352-1-19-340070-0');
insert into bookItem(isbn) values('352-1-19-340070-0');
insert into bookItem(isbn) values('444-8-19-632070-0');
insert into bookItem(isbn) values('444-8-19-632070-0');
insert into bookItem(isbn) values('843-4-14-637830-0');
insert into bookItem(isbn) values('843-4-14-637830-0');
insert into bookItem(isbn) values('123-4-00-983440-0');
insert into bookItem(isbn) values('123-4-00-983440-0');





