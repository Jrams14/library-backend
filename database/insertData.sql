delete from fine;
delete from loan;
delete from librarian;
delete from bookItem;
delete from member;
delete from book;

insert into member(name, phone, email, balance) values ('Jordan', '738-222-4533', 'email@gmail.com', '0');

insert into bookItem(isbn) values('978-3-16-148410-0');

insert into loan(b_id, m_id, checkout_date, due_date, l_id)  values ('1', '1', '02-20-2020', '03-20-2020', '1');

insert into book(ISBN, author, title, year, pages)  values ('978-3-16-148410-0', 'Miller','Pandemic','2020','330');

insert into librarian(username, phone, email, password) values ('admin', '483-433-4334', 'admin@gmail.com', 'password');
