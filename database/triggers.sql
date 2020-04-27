CREATE TRIGGER addFineBalance AFTER INSERT ON fine
    BEGIN
        UPDATE member SET balance = balance + NEW.amount WHERE m_id = (SELECT m_id FROM member NATURAL JOIN loan INNER JOIN fine ON loan.l_id = NEW.l_id);
    END;

CREATE TRIGGER removeFineBalance AFTER UPDATE ON fine
    BEGIN
        UPDATE member SET balance = balance - OLD.amount WHERE m_id = (SELECT m_id FROM member NATURAL JOIN loan INNER JOIN fine ON loan.l_id = OLD.l_id);
    END;