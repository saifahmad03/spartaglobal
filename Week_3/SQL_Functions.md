# SQL Reference Guide (SQL Server / T-SQL)

A cheat sheet of the main SQL commands and functions, with Northwind-style examples.

---

## 1. SQL Sub-languages

| Type | Purpose | Commands |
|---|---|---|
| **DDL** | Define structure | `CREATE`, `ALTER`, `DROP`, `TRUNCATE` |
| **DML** | Work with data | `SELECT`, `INSERT`, `UPDATE`, `DELETE` |
| **DCL** | Permissions | `GRANT`, `REVOKE` |
| **TCL** | Transactions | `BEGIN TRANSACTION`, `COMMIT`, `ROLLBACK`, `SAVEPOINT` |

---

## 2. Query Basics (SELECT)

```sql
SELECT * FROM Customers;                          -- all columns
SELECT CompanyName, City FROM Customers;          -- chosen columns
SELECT DISTINCT Country FROM Customers;           -- unique values
SELECT TOP 5 * FROM Customers;                    -- first 5 rows (SQL Server)
SELECT CompanyName AS [Customer Name] FROM Customers;   -- column alias
SELECT * FROM Customers c;                        -- table alias
SELECT UnitPrice * Quantity AS LineTotal FROM [Order Details];   -- calculation
```

### Logical order of a query

1. `FROM` / `JOIN`
2. `WHERE`
3. `GROUP BY`
4. `HAVING`
5. `SELECT`
6. `DISTINCT`
7. `ORDER BY`
8. `TOP`

---

## 3. Filtering (WHERE)

```sql
SELECT * FROM Customers WHERE Country = 'UK';
SELECT * FROM Products WHERE UnitPrice > 20 AND Discontinued = 0;
SELECT * FROM Products WHERE UnitPrice < 10 OR UnitsInStock = 0;
SELECT * FROM Products WHERE NOT CategoryID = 1;
```

| Operator | Meaning | Example |
|---|---|---|
| `=`, `<>`, `!=` | Equal, not equal | `Country <> 'UK'` |
| `>`, `<`, `>=`, `<=` | Comparison | `UnitPrice >= 10` |
| `BETWEEN` | Inclusive range | `UnitPrice BETWEEN 10 AND 20` |
| `IN` | Match a list | `Country IN ('UK', 'France')` |
| `LIKE` | Pattern match | `CompanyName LIKE 'A%'` |
| `IS NULL` / `IS NOT NULL` | NULL test | `Region IS NULL` |
| `AND`, `OR`, `NOT` | Logic | `A AND B` |
| `EXISTS` | Subquery returns rows | `WHERE EXISTS (SELECT ...)` |

### LIKE wildcards

| Wildcard | Meaning | Example |
|---|---|---|
| `%` | Any number of characters | `'A%'` starts with A |
| `_` | Exactly one character | `'_a%'` second letter is a |
| `[abc]` | Any one listed character | `'[AB]%'` starts with A or B |
| `[^abc]` | Not listed characters | `'[^AB]%'` |

> `= NULL` never works. Use `IS NULL`.

---

## 4. Sorting and Limiting

```sql
SELECT * FROM Products ORDER BY UnitPrice DESC;              -- high to low
SELECT * FROM Products ORDER BY CategoryID ASC, UnitPrice DESC;
SELECT TOP 10 * FROM Products ORDER BY UnitPrice DESC;
SELECT * FROM Products ORDER BY UnitPrice
OFFSET 10 ROWS FETCH NEXT 5 ROWS ONLY;                       -- paging
```

MySQL / PostgreSQL / SQLite use `LIMIT 5` instead of `TOP 5`.

---

## 5. Aggregate Functions

| Function | Purpose |
|---|---|
| `COUNT(*)` | Number of rows |
| `COUNT(column)` | Number of non-NULL values |
| `COUNT(DISTINCT column)` | Number of unique non-NULL values |
| `SUM(column)` | Total |
| `AVG(column)` | Average |
| `MIN(column)` | Smallest value |
| `MAX(column)` | Largest value |

```sql
SELECT COUNT(*) AS NumCustomers FROM Customers;
SELECT AVG(UnitPrice) AS AvgPrice, MAX(UnitPrice) AS MaxPrice FROM Products;
```

### GROUP BY and HAVING

```sql
SELECT Country, COUNT(*) AS NumCustomers
FROM Customers
GROUP BY Country
HAVING COUNT(*) > 5
ORDER BY NumCustomers DESC;
```

| | `WHERE` | `HAVING` |
|---|---|---|
| Filters | Rows | Groups |
| Runs | Before grouping | After grouping |
| Can use aggregates | No | Yes |

> Every non-aggregated column in `SELECT` must appear in `GROUP BY`.

---

## 6. JOINs

A JOIN combines rows from two or more tables using a related column (usually primary key to foreign key).

| Type | Returns |
|---|---|
| `INNER JOIN` | Only rows that match in both tables |
| `LEFT JOIN` | All left rows, plus matches from the right (NULL if none) |
| `RIGHT JOIN` | All right rows, plus matches from the left (NULL if none) |
| `FULL JOIN` | All rows from both tables |
| `CROSS JOIN` | Every row paired with every row (Cartesian product) |
| Self join | A table joined to itself |

```sql
-- INNER JOIN
SELECT c.CompanyName, o.OrderID
FROM Customers c
INNER JOIN Orders o ON c.CustomerID = o.CustomerID;

-- LEFT JOIN
SELECT c.CompanyName, o.OrderID
FROM Customers c
LEFT JOIN Orders o ON c.CustomerID = o.CustomerID;

-- RIGHT JOIN
SELECT c.CompanyName, o.OrderID
FROM Customers c
RIGHT JOIN Orders o ON c.CustomerID = o.CustomerID;

-- FULL JOIN
SELECT c.CompanyName, o.OrderID
FROM Customers c
FULL JOIN Orders o ON c.CustomerID = o.CustomerID;

-- CROSS JOIN
SELECT s.CompanyName, c.CategoryName
FROM Shippers s
CROSS JOIN Categories c;

-- Self join (employee and manager)
SELECT e.FirstName AS Employee, m.FirstName AS Manager
FROM Employees e
INNER JOIN Employees m ON e.ReportsTo = m.EmployeeID;
```

### Joining multiple tables

```sql
SELECT c.CompanyName, o.OrderID, p.ProductName, od.Quantity
FROM Customers c
INNER JOIN Orders o ON c.CustomerID = o.CustomerID
INNER JOIN [Order Details] od ON o.OrderID = od.OrderID
INNER JOIN Products p ON od.ProductID = p.ProductID;
```

### Finding rows with no match

```sql
SELECT c.CustomerID, c.CompanyName
FROM Customers c
LEFT JOIN Orders o ON c.CustomerID = o.CustomerID
WHERE o.OrderID IS NULL;
```

`OrderID` can never be NULL in the table, but a LEFT JOIN creates NULLs for unmatched rows, so the test is reliable.

### ON vs WHERE in a LEFT JOIN

A condition on the right table in `WHERE` removes the NULL rows and cancels the LEFT JOIN. Put it in `ON` to keep all left rows.

---

## 7. Set Operators

```sql
SELECT Country FROM Customers
UNION                      -- combine, remove duplicates
SELECT Country FROM Suppliers;

SELECT Country FROM Customers
UNION ALL                  -- combine, keep duplicates
SELECT Country FROM Suppliers;

SELECT Country FROM Customers
INTERSECT                  -- rows in both
SELECT Country FROM Suppliers;

SELECT Country FROM Customers
EXCEPT                     -- rows in first but not second
SELECT Country FROM Suppliers;
```

Each query must return the same number of columns with compatible types.

---

## 8. Subqueries and CTEs

```sql
-- Subquery in WHERE
SELECT ProductName, UnitPrice
FROM Products
WHERE UnitPrice > (SELECT AVG(UnitPrice) FROM Products);

-- IN subquery
SELECT CompanyName FROM Customers
WHERE CustomerID IN (SELECT CustomerID FROM Orders WHERE ShipCountry = 'UK');

-- NOT EXISTS
SELECT CompanyName FROM Customers c
WHERE NOT EXISTS (SELECT 1 FROM Orders o WHERE o.CustomerID = c.CustomerID);

-- Derived table (subquery in FROM, alias required)
SELECT t.CustomerID, t.Total
FROM (SELECT CustomerID, COUNT(*) AS Total FROM Orders GROUP BY CustomerID) AS t;

-- CTE (Common Table Expression)
WITH OrderTotals AS (
    SELECT OrderID, SUM(UnitPrice * Quantity * (1 - Discount)) AS Total
    FROM [Order Details]
    GROUP BY OrderID
)
SELECT * FROM OrderTotals WHERE Total > 1000;
```

A column alias created in `SELECT` cannot be used in `WHERE` of the same query. Use a subquery or CTE.

---

## 9. CASE Expressions

```sql
-- Searched CASE
SELECT ProductName, UnitPrice,
    CASE
        WHEN UnitPrice < 10 THEN 'Cheap'
        WHEN UnitPrice < 50 THEN 'Mid-range'
        ELSE 'Expensive'
    END AS PriceBand
FROM Products;

-- Simple CASE
SELECT CompanyName,
    CASE Country
        WHEN 'UK' THEN 'United Kingdom'
        WHEN 'USA' THEN 'United States'
        ELSE Country
    END AS CountryName
FROM Customers;
```

- Conditions are checked in order, and the first true one wins.
- With no `ELSE`, unmatched rows return `NULL`.
- `CASE` can be used in `SELECT`, `WHERE`, `ORDER BY` and inside aggregates:

```sql
SELECT SUM(CASE WHEN Country = 'UK' THEN 1 ELSE 0 END) AS UKCustomers
FROM Customers;
```

---

## 10. Creating and Changing Tables (DDL)

### CREATE TABLE

```sql
CREATE TABLE Course_Table (
    CourseID   VARCHAR(10) NOT NULL PRIMARY KEY,
    CourseName VARCHAR(50) NOT NULL,
    StartDate  DATE NOT NULL,
    EndDate    DATE NULL
);

CREATE TABLE Spartans_Table (
    ID         INT IDENTITY(1,1) PRIMARY KEY,
    FirstName  VARCHAR(50) NOT NULL,
    Email      VARCHAR(100) NULL,
    CourseID   VARCHAR(10) NOT NULL,
    CONSTRAINT FK_Spartans_Course
        FOREIGN KEY (CourseID) REFERENCES Course_Table(CourseID)
);
```

### ALTER TABLE

```sql
ALTER TABLE Spartans_Table ADD Title VARCHAR(10) NULL;                  -- add column
ALTER TABLE Course_Table ALTER COLUMN CourseName VARCHAR(100) NOT NULL; -- change type or size
ALTER TABLE Spartans_Table DROP COLUMN Title;                           -- drop column
EXEC sp_rename 'Course_Table.Trainer', 'TrainerName', 'COLUMN';         -- rename column
EXEC sp_rename 'OldTable', 'NewTable';                                  -- rename table
```

### DROP and TRUNCATE

```sql
DROP TABLE IF EXISTS Spartans_Table;      -- remove table and data
DROP DATABASE IF EXISTS Northwind;        -- remove database
TRUNCATE TABLE Spartans_Table;            -- remove all rows, keep table
```

| Command | Effect |
|---|---|
| `DELETE` | Removes rows, can use `WHERE`, can be rolled back |
| `TRUNCATE` | Removes all rows quickly, keeps structure, resets identity |
| `DROP` | Removes the whole table |

---

## 11. Constraints

| Constraint | Purpose |
|---|---|
| `PRIMARY KEY` | Unique, not NULL; identifies each row |
| `FOREIGN KEY` | Value must exist in the parent table |
| `NOT NULL` | A value is required |
| `UNIQUE` | No duplicate values |
| `CHECK` | Value must satisfy a condition |
| `DEFAULT` | Value used when none is supplied |
| `IDENTITY(seed, increment)` | Auto-generated numbers (SQL Server) |

```sql
ALTER TABLE Spartans_Table
ADD CONSTRAINT CK_Spartans_Title CHECK (Title IN ('Mr', 'Mrs', 'Ms', 'Mx', 'Dr'));

ALTER TABLE Spartans_Table
ADD CONSTRAINT UQ_Spartans_Email UNIQUE (Email);

ALTER TABLE Course_Table
ADD CONSTRAINT CK_Course_EndAfterStart CHECK (EndDate IS NULL OR EndDate >= StartDate);

ALTER TABLE Spartans_Table
ADD Status VARCHAR(15) NOT NULL CONSTRAINT DF_Spartans_Status DEFAULT 'Active';

ALTER TABLE Spartans_Table DROP CONSTRAINT CK_Spartans_Title;
```

### Foreign key actions

```sql
FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
    ON DELETE CASCADE        -- delete child rows too
    -- ON DELETE NO ACTION   -- block the delete (default)
    -- ON DELETE SET NULL    -- set child key to NULL
    -- ON UPDATE CASCADE
```

Before adding a constraint, make sure existing data complies, or the `ALTER` fails: check, fix, then apply.

---

## 12. Changing Data (DML)

```sql
-- INSERT one row
INSERT INTO Course_Table (CourseID, CourseName, StartDate)
VALUES ('TECH 200', 'C# Dev', '2026-10-06');

-- INSERT multiple rows
INSERT INTO Course_Table (CourseID, CourseName, StartDate)
VALUES ('TECH 201', 'Java Dev', '2026-09-06'),
       ('TECH 202', 'Data Engineer', '2026-08-06');

-- INSERT from another table
INSERT INTO Customers_Backup SELECT * FROM Customers;

-- UPDATE (always use WHERE)
UPDATE Customers SET City = 'Munich' WHERE CustomerID = 'ALFKI';

-- DELETE (always use WHERE)
DELETE FROM Customers WHERE CustomerID = 'XXXXX';

-- Copy a table
SELECT * INTO Customers_Backup FROM Customers;
```

- Text and dates use single quotes. Dates use `'YYYY-MM-DD'`.
- A single quote inside text is doubled: `'O''Brien'`.
- Insert into the parent table before the child, and delete from the child before the parent.

---

## 13. String Functions

| Function | Purpose | Example | Result |
|---|---|---|---|
| `LEN(s)` | Length | `LEN('Spartan')` | 7 |
| `UPPER(s)` / `LOWER(s)` | Change case | `UPPER('abc')` | ABC |
| `LTRIM(s)` / `RTRIM(s)` / `TRIM(s)` | Remove spaces | `TRIM('  hi  ')` | hi |
| `LEFT(s, n)` / `RIGHT(s, n)` | First or last n characters | `LEFT('Spartan', 3)` | Spa |
| `SUBSTRING(s, start, len)` | Part of a string | `SUBSTRING('Spartan', 2, 3)` | par |
| `CHARINDEX(find, s)` | Position of text | `CHARINDEX('t', 'Spartan')` | 4 |
| `REPLACE(s, old, new)` | Replace text | `REPLACE('a-b', '-', '/')` | a/b |
| `CONCAT(a, b, ...)` | Join strings | `CONCAT('A', 'B')` | AB |
| `a + b` | Join strings (NULL gives NULL) | `'A' + 'B'` | AB |
| `CONCAT_WS(sep, a, b)` | Join with separator | `CONCAT_WS(' ', 'Jo', 'Bo')` | Jo Bo |
| `REVERSE(s)` | Reverse | `REVERSE('abc')` | cba |
| `STRING_AGG(col, sep)` | Join rows into one string | see below | |

```sql
SELECT FirstName + ' ' + LastName AS FullName FROM Employees;
SELECT STRING_AGG(CompanyName, ', ') FROM Shippers;
```

---

## 14. Numeric Functions

| Function | Purpose | Example | Result |
|---|---|---|---|
| `ROUND(n, d)` | Round | `ROUND(3.456, 2)` | 3.46 |
| `FLOOR(n)` | Round down | `FLOOR(3.9)` | 3 |
| `CEILING(n)` | Round up | `CEILING(3.1)` | 4 |
| `ABS(n)` | Absolute value | `ABS(-5)` | 5 |
| `POWER(n, p)` | Power | `POWER(2, 3)` | 8 |
| `SQRT(n)` | Square root | `SQRT(16)` | 4 |
| `n % m` | Remainder | `10 % 3` | 1 |
| `RAND()` | Random 0 to 1 | | |

---

## 15. Date and Time Functions

| Function | Purpose |
|---|---|
| `GETDATE()` | Current date and time |
| `SYSDATETIME()` | Current date and time (higher precision) |
| `YEAR(d)`, `MONTH(d)`, `DAY(d)` | Extract a part |
| `DATEPART(part, d)` | Extract any part |
| `DATENAME(part, d)` | Part as text (e.g. month name) |
| `DATEADD(part, n, d)` | Add or subtract time |
| `DATEDIFF(part, start, end)` | Difference between dates |
| `EOMONTH(d)` | Last day of the month |
| `FORMAT(d, 'dd/MM/yyyy')` | Format a date |
| `CONVERT(type, value, style)` | Convert and format |

```sql
SELECT GETDATE();
SELECT YEAR(OrderDate) AS OrderYear FROM Orders;
SELECT DATEADD(WEEK, 12, StartDate) FROM Course_Table;
SELECT DATEDIFF(DAY, OrderDate, ShippedDate) AS DaysToShip FROM Orders;
SELECT DATENAME(MONTH, OrderDate) FROM Orders;
```

### Calculating age

`DATEDIFF(YEAR, ...)` counts calendar year boundaries, so it can be one year too high before the birthday. For a whole-number age use:

```sql
SELECT FirstName, LastName,
    FLOOR(DATEDIFF(DAY, BirthDate, GETDATE()) / 365.25) AS Age
FROM Employees;
```

---

## 16. NULL Handling and Conversion

| Function | Purpose | Example |
|---|---|---|
| `ISNULL(x, y)` | Replace NULL (SQL Server) | `ISNULL(Region, 'N/A')` |
| `COALESCE(a, b, c)` | First non-NULL value (standard) | `COALESCE(Region, City, 'N/A')` |
| `NULLIF(a, b)` | NULL if the values are equal | `NULLIF(Qty, 0)` avoids divide by zero |
| `CAST(x AS type)` | Convert type | `CAST(UnitPrice AS INT)` |
| `CONVERT(type, x)` | Convert type (SQL Server) | `CONVERT(VARCHAR, OrderDate, 103)` |
| `TRY_CAST(x AS type)` | Convert, NULL on failure | `TRY_CAST('abc' AS INT)` |
| `IIF(cond, a, b)` | Inline if (SQL Server) | `IIF(UnitPrice > 20, 'High', 'Low')` |

---

## 17. Window Functions

Calculate across a set of rows without collapsing them into groups.

```sql
SELECT ProductName, CategoryID, UnitPrice,
    ROW_NUMBER() OVER (ORDER BY UnitPrice DESC) AS RowNum,
    RANK()       OVER (ORDER BY UnitPrice DESC) AS PriceRank,
    DENSE_RANK() OVER (ORDER BY UnitPrice DESC) AS DensePriceRank,
    AVG(UnitPrice) OVER (PARTITION BY CategoryID) AS CategoryAvg,
    SUM(UnitPrice) OVER (ORDER BY ProductID) AS RunningTotal
FROM Products;
```

| Function | Purpose |
|---|---|
| `ROW_NUMBER()` | Unique sequence number |
| `RANK()` | Rank with gaps after ties |
| `DENSE_RANK()` | Rank without gaps |
| `NTILE(n)` | Split into n buckets |
| `LAG(col)` / `LEAD(col)` | Previous or next row's value |
| `SUM/AVG/COUNT() OVER (...)` | Aggregates per partition or running |

`PARTITION BY` restarts the calculation for each group; `ORDER BY` sets the order inside it.

---

## 18. Views, Indexes, Stored Procedures, Functions, Triggers

### View

A saved query that behaves like a virtual table.

```sql
CREATE VIEW vw_CustomerOrders AS
SELECT c.CompanyName, o.OrderID, o.OrderDate
FROM Customers c
INNER JOIN Orders o ON c.CustomerID = o.CustomerID;

SELECT * FROM vw_CustomerOrders;
DROP VIEW IF EXISTS vw_CustomerOrders;
```

### Index

Speeds up reads at the cost of slower writes and extra storage.

```sql
CREATE INDEX IX_Customers_Country ON Customers (Country);
CREATE UNIQUE INDEX IX_Spartans_Email ON Spartans_Table (Email);
DROP INDEX IX_Customers_Country ON Customers;
```

### Stored procedure

A saved, named block of SQL that can take parameters.

```sql
CREATE PROCEDURE GetCustomerContactName
    @CustomerID NCHAR(5)
AS
BEGIN
    SELECT ContactName FROM Customers WHERE CustomerID = @CustomerID;
END;
GO

EXEC GetCustomerContactName @CustomerID = 'ALFKI';
```

### User-defined function

```sql
CREATE FUNCTION dbo.LineTotal (@Price MONEY, @Qty INT)
RETURNS MONEY
AS
BEGIN
    RETURN @Price * @Qty;
END;
GO

SELECT dbo.LineTotal(10, 3);
```

### Trigger

Runs automatically when an `INSERT`, `UPDATE` or `DELETE` occurs.

```sql
CREATE TRIGGER trg_LogDelete ON Customers
AFTER DELETE
AS
BEGIN
    INSERT INTO CustomerLog (CustomerID, DeletedAt)
    SELECT CustomerID, GETDATE() FROM deleted;
END;
```

| | View | Stored procedure | Function | Trigger |
|---|---|---|---|---|
| Is | Saved `SELECT` | Saved SQL block | Returns a value or table | Runs on an event |
| Called with | `SELECT ... FROM` | `EXEC` | Inside a query | Automatically |
| Parameters | No | Yes | Yes | No |

---

## 19. Transactions (TCL)

```sql
BEGIN TRANSACTION;

UPDATE Accounts SET Balance = Balance - 100 WHERE AccountID = 'A';
UPDATE Accounts SET Balance = Balance + 100 WHERE AccountID = 'B';

COMMIT;       -- make permanent
-- ROLLBACK;  -- or undo everything since BEGIN
```

### ACID

| Letter | Property | Meaning |
|---|---|---|
| A | Atomicity | All or nothing |
| C | Consistency | Rules always obeyed |
| I | Isolation | Concurrent transactions do not interfere |
| D | Durability | Committed data survives crashes |

---

## 20. Permissions (DCL)

```sql
GRANT SELECT, INSERT ON Customers TO analyst_user;
REVOKE INSERT ON Customers FROM analyst_user;
DENY DELETE ON Customers TO analyst_user;
```

---

## 21. Variables and Control Flow (T-SQL)

```sql
DECLARE @Country NVARCHAR(15) = 'UK';
SELECT * FROM Customers WHERE Country = @Country;

IF EXISTS (SELECT 1 FROM Customers WHERE Country = 'UK')
    PRINT 'Found UK customers';
ELSE
    PRINT 'None found';

DECLARE @i INT = 1;
WHILE @i <= 3
BEGIN
    PRINT @i;
    SET @i += 1;
END;
```

---

## 22. Useful System Queries

```sql
SELECT * FROM INFORMATION_SCHEMA.TABLES;                                   -- list tables
SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'Customers';                                            -- list columns
EXEC sp_help 'Customers';                                                  -- table details
SELECT DB_NAME();                                                          -- current database
```

---

## 23. Common Data Types (SQL Server)

| Category | Types |
|---|---|
| Whole numbers | `TINYINT`, `SMALLINT`, `INT`, `BIGINT` |
| Decimals | `DECIMAL(p,s)`, `NUMERIC(p,s)`, `FLOAT`, `REAL`, `MONEY` |
| Text | `CHAR(n)`, `VARCHAR(n)`, `NVARCHAR(n)`, `VARCHAR(MAX)` |
| Date and time | `DATE`, `TIME`, `DATETIME2`, `DATETIMEOFFSET` |
| Other | `BIT` (true/false), `UNIQUEIDENTIFIER`, `VARBINARY` |

---

## 24. Quick Comparisons

| Pair | Difference |
|---|---|
| `WHERE` vs `HAVING` | Rows before grouping vs groups after grouping |
| `UNION` vs `UNION ALL` | Removes duplicates vs keeps them |
| `DELETE` vs `TRUNCATE` vs `DROP` | Some rows vs all rows vs whole table |
| `UPDATE` vs `ALTER` | Changes values vs changes structure |
| `DISTINCT` vs `GROUP BY` | Both remove duplicates, only `GROUP BY` aggregates |
| `IN` vs `EXISTS` | Match a list vs check a subquery returns rows |
| `CHAR` vs `VARCHAR` | Fixed length vs variable length |
| `ISNULL` vs `COALESCE` | SQL Server only, 2 values vs standard, many values |

---

## 25. Good Practice

- Always use `WHERE` with `UPDATE` and `DELETE`. Test with a `SELECT` first.
- Wrap risky changes in a transaction so you can `ROLLBACK`.
- Back up before big changes: `SELECT * INTO Customers_Backup FROM Customers;`
- Use parameterised queries to prevent SQL injection, never string concatenation of user input.
- Name constraints so errors are easy to read.
- Avoid `SELECT *` in production code; list the columns you need.