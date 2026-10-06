# SQL Sub-languages (The 4 Types)

SQL commands are grouped into four sub-languages, depending on what they do.

## Summary

| Sub-language | Full name | Purpose | Commands |
|---|---|---|---|
| **DDL** | Data Definition Language | Defines and changes the **structure** of the database | `CREATE`, `ALTER`, `DROP`, `TRUNCATE` |
| **DML** | Data Manipulation Language | Works with the **data** inside tables | `SELECT`, `INSERT`, `UPDATE`, `DELETE` |
| **DCL** | Data Control Language | Controls **permissions** and access | `GRANT`, `REVOKE` |
| **TCL** | Transaction Control Language | Manages **transactions** | `COMMIT`, `ROLLBACK`, `SAVEPOINT` |

---

## 1. DDL: Data Definition Language

Defines the **structure** (schema): tables, columns, indexes and constraints.

| Command | Purpose |
|---|---|
| `CREATE` | Create a new table or database object |
| `ALTER` | Modify an existing table's structure |
| `DROP` | Delete a table or object entirely |
| `TRUNCATE` | Remove all rows, keep the table structure |

```sql
CREATE TABLE Shippers (
    ShipperID   INT PRIMARY KEY,
    CompanyName VARCHAR(40)
);

ALTER TABLE Shippers ADD Phone VARCHAR(24);

TRUNCATE TABLE Shippers;

DROP TABLE Shippers;
```

---

## 2. DML: Data Manipulation Language

Reads and changes the **data** (rows) stored in tables.

| Command | Purpose |
|---|---|
| `SELECT` | Retrieve data |
| `INSERT` | Add new rows |
| `UPDATE` | Change existing rows |
| `DELETE` | Remove rows |

```sql
SELECT CompanyName FROM Shippers;

INSERT INTO Shippers (ShipperID, CompanyName)
VALUES (4, 'Fast Freight');

UPDATE Shippers
SET CompanyName = 'Quick Freight'
WHERE ShipperID = 4;

DELETE FROM Shippers
WHERE ShipperID = 4;
```

> Some courses list `SELECT` separately as **DQL** (Data Query Language), giving five types. In a four-type course, `SELECT` belongs under DML.

---

## 3. DCL: Data Control Language

Controls **who can do what** in the database.

| Command | Purpose |
|---|---|
| `GRANT` | Give a user a permission |
| `REVOKE` | Take a permission away |

```sql
GRANT SELECT, INSERT ON Customers TO analyst_user;

REVOKE INSERT ON Customers FROM analyst_user;
```

---

## 4. TCL: Transaction Control Language

Manages **transactions**, groups of statements that succeed or fail together.

| Command | Purpose |
|---|---|
| `BEGIN TRANSACTION` | Start a transaction |
| `COMMIT` | Make the changes permanent |
| `ROLLBACK` | Undo the changes |
| `SAVEPOINT` | Set a point to roll back to |

```sql
BEGIN TRANSACTION;

UPDATE Accounts SET Balance = Balance - 100 WHERE AccountID = 'A';
UPDATE Accounts SET Balance = Balance + 100 WHERE AccountID = 'B';

COMMIT;      -- save the changes
-- ROLLBACK; -- or undo them instead
```

---

## Quick comparison

| | DDL | DML | DCL | TCL |
|---|---|---|---|---|
| Works on | Structure | Data | Permissions | Transactions |
| Analogy | Building the filing cabinet | Putting papers in and taking them out | Giving out keys | Saving or undoing your work |
| Example | `CREATE TABLE` | `INSERT` | `GRANT` | `COMMIT` |

## Memory aid

- **D**efinition: what the table **is**
- **M**anipulation: what is **in** the table
- **C**ontrol (DCL): who is **allowed**
- **T**ransaction: **save or undo**

> Note: `TRUNCATE` removes data but is classed as DDL because it works on the whole table rather than row by row.