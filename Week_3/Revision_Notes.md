# Database Theory Notes

## Contents

1. What is a database?
2. What is a DBMS?
3. Data modelling
4. ERDs (Entity Relationship Diagrams)
5. Normalisation
6. Indexing
7. Query efficiency
8. ACID
9. SQL sub-languages (the 4 types)

---

## 1. What is a database?

A **database** is an organised collection of data, stored electronically so it can be easily accessed, managed, updated and searched. The data is structured, so that information can be retrieved quickly and reliably rather than hunted for in loose files.

**Key characteristics**
- **Organised:** data follows a defined structure.
- **Persistent:** data survives after the program closes or the power goes off.
- **Shared:** many users and applications can use it at the same time.
- **Controlled:** rules and permissions protect the data.

**Types of database**

| Type | How data is stored | Examples |
|---|---|---|
| **Relational (SQL)** | Tables of rows and columns, linked by keys | SQL Server, MySQL, PostgreSQL, Oracle |
| **Document** | JSON-like documents | MongoDB |
| **Key-value** | Key and value pairs | Redis |
| **Column-family** | Columns grouped for large-scale analytics | Cassandra |
| **Graph** | Nodes and relationships | Neo4j |

**Relational database vocabulary**

| Term | Meaning | Formal name |
|---|---|---|
| Table | One kind of entity | Relation |
| Row | One record | Tuple |
| Column | One property | Attribute |
| Primary key | Uniquely identifies each row | |
| Foreign key | References another table's primary key | |

**Why use a database instead of spreadsheets or files?**
- Less duplication and fewer inconsistencies.
- Enforced rules (keys, data types, constraints).
- Handles many simultaneous users and large volumes.
- Powerful querying with SQL.
- Backup, recovery and security features.

---

## 2. What is a DBMS?

A **Database Management System (DBMS)** is the software that creates, stores, manages and controls access to a database. The database is the data; the DBMS is the software that looks after it. An **RDBMS** is a DBMS for relational databases.

```
Users / Applications  -->  SQL  -->  DBMS  -->  Database files on disk
```

**Main functions of a DBMS**

| Function | What it does |
|---|---|
| **Data storage and retrieval** | Stores data efficiently and returns it when queried |
| **Query processing** | Parses SQL and builds an efficient execution plan (query optimiser) |
| **Data definition** | Lets you create and change structures (tables, indexes, views) |
| **Concurrency control** | Lets many users work at once without interfering (locking, isolation) |
| **Transaction management** | Guarantees ACID behaviour |
| **Security** | Authentication and permissions (who can see or change what) |
| **Integrity enforcement** | Applies constraints (primary keys, foreign keys, CHECK) |
| **Backup and recovery** | Restores data after failure |

**Examples:** SQL Server, MySQL, PostgreSQL, Oracle, SQLite (relational); MongoDB, Redis (NoSQL).

**Advantages**
- Centralised, consistent data
- Reduced redundancy
- Data independence: applications do not depend on how data is physically stored
- Better security and recovery

**Disadvantages**
- Cost and complexity (licences, administration)
- Needs skilled staff
- Can be a single point of failure without replication

---

## 3. Data modelling

**Data modelling** is the process of designing how data will be structured and related before building the database. It produces a blueprint that records what data is needed and how the pieces connect.

**Three levels of model**

| Level | Audience | Detail |
|---|---|---|
| **Conceptual** | Business stakeholders | Main entities and relationships only, no technical detail |
| **Logical** | Analysts and designers | Attributes, primary keys, foreign keys, normalisation, independent of any DBMS |
| **Physical** | Developers and DBAs | Actual tables, data types, indexes, constraints for a specific DBMS |

**Typical process**
1. Gather requirements (what does the business need to store and ask?).
2. Identify entities and attributes.
3. Define relationships and cardinality.
4. Choose primary and foreign keys.
5. Normalise to remove redundancy.
6. Convert to a physical design (data types, constraints, indexes).
7. Review, test and refine.

**Why it matters**
- Prevents costly redesign later.
- Improves data quality and consistency.
- Provides shared understanding between business and technical teams.
- Supports performance and scalability.

---

## 4. ERDs (Entity Relationship Diagrams)

An **ERD** is a diagram of the entities in a system and how they relate. It is the main tool used for conceptual and logical data modelling.

### Components

| Component | Meaning | Becomes |
|---|---|---|
| **Entity** | A thing you store data about (Customer, Course) | Table |
| **Attribute** | A property of an entity (CompanyName) | Column |
| **Relationship** | How entities are linked ("places", "teaches") | Foreign key or junction table |
| **Primary key (PK)** | Unique identifier of an entity instance | Primary key |
| **Foreign key (FK)** | Attribute referencing another entity's PK | Foreign key |

**Entity types**
- **Strong entity:** exists independently with its own PK (Customer).
- **Weak entity:** depends on another entity to be identified (an order line depends on an order).
- **Associative (junction) entity:** resolves a many-to-many relationship (`[Order Details]`, `Enrolment`).

### Cardinality

Cardinality is how many instances of one entity relate to instances of another.

| Type | Example |
|---|---|
| **One-to-one (1:1)** | One person has one passport |
| **One-to-many (1:N)** | One customer places many orders |
| **Many-to-many (M:N)** | Students enrol on many courses; courses have many students |

A many-to-many relationship cannot be stored directly in a relational database. It is split into two one-to-many relationships using a **junction table**.

```
Student  1 ----< Enrolment >---- 1  Course
```

### Crow's foot notation

| Symbol | Meaning |
|---|---|
| `\|` | exactly one |
| `O` | zero (optional) |
| three-pronged fork | many |

| Notation | Reads as |
|---|---|
| `\|\|` | exactly one |
| `O\|` | zero or one |
| `\|<` | one or many |
| `O<` | zero or many |

```
Customers ||──────O<  Orders ||──────|<  OrderDetails >O──────|| Products
```

The crow's foot end is the table that holds the foreign key.

**Modality (participation):** whether a relationship is mandatory (a bar) or optional (a circle). A customer may have zero orders (optional), but an order must have exactly one customer (mandatory).

### Other notations
- **Chen notation:** rectangles for entities, ovals for attributes, diamonds for relationships.
- **UML class diagrams:** used in object-oriented design.

### Drawing good ERDs
- Use singular nouns for entities.
- Label every PK and FK.
- Show cardinality on every line.
- Resolve every many-to-many relationship with a junction table.
- Keep it readable: avoid crossing lines where possible.

---

## 5. Normalisation

**Normalisation** is organising tables to reduce redundancy and prevent anomalies by splitting data into related tables.

### Anomalies it prevents

| Anomaly | Problem |
|---|---|
| **Insert** | Cannot add one fact without another (a product without an order) |
| **Update** | Changing a value in one row but missing others, causing inconsistency |
| **Delete** | Deleting a row also removes unrelated facts (the customer's details) |

### Normal forms

| Form | Rule |
|---|---|
| **1NF** | Atomic values in every cell, no repeating groups |
| **2NF** | In 1NF, and every non-key column depends on the **whole** primary key (no partial dependencies) |
| **3NF** | In 2NF, and non-key columns depend **only** on the key (no transitive dependencies) |
| **BCNF** | Stricter 3NF: every determinant is a candidate key |

Memory aid: *the key, the whole key, and nothing but the key.*

### Example

Unnormalised:

| OrderID | CustomerName | CustomerCity | Products |
|---|---|---|---|
| 101 | Alfreds | Berlin | Chai, Chang |

- **1NF:** one product per row.
- **2NF:** move order-level facts away from product-level rows.
- **3NF:** move the customer's city into a `Customers` table, so it is stored once.

### Denormalisation

Deliberately adding redundancy to speed up reads (for example, in data warehouses). It trades storage and update complexity for faster queries.

---

## 6. Indexing

An **index** is a separate data structure that lets the DBMS find rows without scanning the whole table, like the index at the back of a book.

### How it works

Without an index, the DBMS performs a **table scan**: it reads every row to find matches. With an index, it performs an **index seek**: it navigates a sorted structure (usually a **B-tree**) straight to the matching rows.

```
Table scan:  read row 1, row 2, row 3 ... row 1,000,000
Index seek:  root -> branch -> leaf -> row   (a handful of steps)
```

### Types of index

| Type | Description |
|---|---|
| **Clustered** | Defines the physical order of the rows. Only one per table (usually the primary key) |
| **Non-clustered** | A separate structure with key values and pointers to rows. Many per table |
| **Unique** | Enforces no duplicate values |
| **Composite** | Covers more than one column |
| **Covering** | Contains every column a query needs, so the table is not touched |
| **Filtered** | Indexes only a subset of rows |

```sql
CREATE INDEX IX_Customers_Country ON Customers (Country);
CREATE UNIQUE INDEX IX_Spartans_Email ON Spartans_Table (Email);
CREATE INDEX IX_Orders_Cust_Date ON Orders (CustomerID, OrderDate);   -- composite
DROP INDEX IX_Customers_Country ON Customers;
```

Primary key and `UNIQUE` constraints create indexes automatically.

### Trade-offs

| Benefit | Cost |
|---|---|
| Much faster reads, joins, sorting and filtering | Slower `INSERT`, `UPDATE` and `DELETE` (indexes must be maintained) |
| Faster lookups on foreign keys | Extra storage |
| Enforces uniqueness | Too many indexes hurt performance |

### What to index
- Columns used in `WHERE`, `JOIN`, `ORDER BY` and `GROUP BY`.
- Foreign key columns.
- Columns with high **selectivity** (many distinct values).

### What not to index
- Very small tables.
- Columns with few distinct values (for example, a yes/no flag).
- Columns that are updated very frequently.

### Composite index column order

In `(CustomerID, OrderDate)`, the index helps queries filtering on `CustomerID`, or on `CustomerID` and `OrderDate`, but not on `OrderDate` alone (the **leftmost prefix** rule).

---

## 7. Query efficiency

Query efficiency is about getting the same correct result using less time, CPU, memory and disk I/O.

### How a query is processed

1. **Parse:** check syntax.
2. **Bind:** check that tables and columns exist.
3. **Optimise:** the **query optimiser** chooses an **execution plan**, using indexes, statistics and cost estimates.
4. **Execute:** run the plan and return results.

SQL is **declarative**: you say *what* you want, and the optimiser decides *how* to get it.

### Logical order vs execution order

| Logical processing order |
|---|
| 1. `FROM` / `JOIN` |
| 2. `WHERE` |
| 3. `GROUP BY` |
| 4. `HAVING` |
| 5. `SELECT` |
| 6. `DISTINCT` |
| 7. `ORDER BY` |
| 8. `TOP` / `LIMIT` |

The logical order defines the **meaning** of a query (and why `WHERE` cannot use a `SELECT` alias). The actual **execution order** is chosen by the optimiser and may differ, for example by filtering early, as long as the result is the same.

### Viewing the plan

```sql
-- SQL Server: Ctrl+M in SSMS, then run the query
SET STATISTICS IO ON;
SET STATISTICS TIME ON;

-- MySQL / PostgreSQL
EXPLAIN SELECT * FROM Customers WHERE Country = 'UK';
```

| Operation in a plan | Meaning |
|---|---|
| Table / clustered index **scan** | Reads everything (often slow on large tables) |
| Index **seek** | Jumps to matching rows (fast) |
| **Key lookup** | Extra trip to the table for missing columns |
| **Nested loop / hash / merge join** | Different join algorithms chosen by the optimiser |

### Techniques for faster queries

| Technique | Why it helps |
|---|---|
| **Select only needed columns** (avoid `SELECT *`) | Less data read and sent, enables covering indexes |
| **Filter early with `WHERE`** | Reduces rows before grouping and joining |
| **Index the right columns** | Replaces scans with seeks |
| **Join on indexed keys** | Faster matching |
| **Use `EXISTS` instead of `IN`** for large subqueries | Stops at the first match |
| **Avoid functions on indexed columns in `WHERE`** | Functions stop the index being used |
| **Avoid leading wildcards** (`LIKE '%abc'`) | Cannot use an index |
| **Use `UNION ALL` instead of `UNION`** when duplicates are fine | Skips the duplicate-removal step |
| **Limit results** (`TOP`, paging) | Returns less data |
| **Keep statistics up to date** | Helps the optimiser choose good plans |
| **Avoid unnecessary `DISTINCT` and `ORDER BY`** | They require sorting |

### SARGable conditions

A condition is **SARGable** (Search ARGument able) when the DBMS can use an index for it.

```sql
-- Not SARGable: function on the column prevents index use
SELECT * FROM Orders WHERE YEAR(OrderDate) = 1997;

-- SARGable: compares the raw column to a range
SELECT * FROM Orders
WHERE OrderDate >= '1997-01-01' AND OrderDate < '1998-01-01';
```

### Other efficiency considerations
- **Normalisation** reduces redundancy but adds joins; **denormalisation** can speed up reads.
- **Partitioning** splits very large tables into smaller pieces.
- **Caching** and **materialised or indexed views** store pre-computed results.
- **Avoid row-by-row processing** (cursors, loops); use set-based operations.
- **Keep transactions short** to reduce locking and blocking.

---

## 8. ACID

**ACID** is a set of four guarantees a database gives for **transactions**. A transaction is a group of operations treated as a single unit of work.

**Example:** transferring £100 from account A to account B.

```sql
BEGIN TRANSACTION;
UPDATE Accounts SET Balance = Balance - 100 WHERE AccountID = 'A';
UPDATE Accounts SET Balance = Balance + 100 WHERE AccountID = 'B';
COMMIT;       -- make permanent
-- ROLLBACK;  -- or undo everything since BEGIN
```

| Letter | Property | Meaning |
|---|---|---|
| **A** | **Atomicity** | All or nothing: if any step fails, everything is undone |
| **C** | **Consistency** | The database moves from one valid state to another, obeying all rules and constraints |
| **I** | **Isolation** | Concurrent transactions do not interfere with each other |
| **D** | **Durability** | Once committed, changes survive crashes (via the transaction log) |

### Isolation levels

| Level | Prevents |
|---|---|
| Read Uncommitted | Nothing (dirty reads possible) |
| Read Committed | Dirty reads |
| Repeatable Read | Dirty reads and non-repeatable reads |
| Serializable | Dirty, non-repeatable and phantom reads |

| Problem | Meaning |
|---|---|
| **Dirty read** | Reading another transaction's uncommitted data |
| **Non-repeatable read** | Same row read twice gives different values |
| **Phantom read** | Same query returns different rows because another transaction added or removed some |

Higher isolation gives more safety but less concurrency and speed.

### Transaction commands

| Command | Effect |
|---|---|
| `BEGIN TRANSACTION` | Start |
| `COMMIT` | Save permanently |
| `ROLLBACK` | Undo |
| `SAVEPOINT` | Mark a point to roll back to |

### Related ideas
- **Deadlock:** two transactions each hold a lock the other needs, so both wait forever. The DBMS detects it and aborts one (the victim).
- **Locking:** how the DBMS controls concurrent access to data.
- **Transaction log:** a record of changes that provides durability and recovery.
- **BASE:** a looser model used by many NoSQL systems (Basically Available, Soft state, Eventually consistent).

ACID matters wherever partial or lost updates would be serious: banking, orders, inventory and bookings.

---

## 9. SQL sub-languages (the 4 types)

| Sub-language | Full name | Purpose | Commands |
|---|---|---|---|
| **DDL** | Data Definition Language | Defines and changes the **structure** | `CREATE`, `ALTER`, `DROP`, `TRUNCATE` |
| **DML** | Data Manipulation Language | Works with the **data** | `SELECT`, `INSERT`, `UPDATE`, `DELETE` |
| **DCL** | Data Control Language | Controls **permissions** | `GRANT`, `REVOKE` |
| **TCL** | Transaction Control Language | Manages **transactions** | `COMMIT`, `ROLLBACK`, `SAVEPOINT` |

> Some courses list `SELECT` separately as **DQL** (Data Query Language), giving five types. In a four-type course, `SELECT` belongs under DML.

### DDL: Data Definition Language

```sql
CREATE TABLE Shippers (ShipperID INT PRIMARY KEY, CompanyName VARCHAR(40));
ALTER TABLE Shippers ADD Phone VARCHAR(24);
TRUNCATE TABLE Shippers;
DROP TABLE Shippers;
```

`TRUNCATE` removes data, but it is DDL because it works on the whole table rather than row by row.

### DML: Data Manipulation Language

```sql
SELECT CompanyName FROM Shippers;
INSERT INTO Shippers (ShipperID, CompanyName) VALUES (4, 'Fast Freight');
UPDATE Shippers SET CompanyName = 'Quick Freight' WHERE ShipperID = 4;
DELETE FROM Shippers WHERE ShipperID = 4;
```

Always use `WHERE` with `UPDATE` and `DELETE`, or every row is affected. These four commands are also known as **CRUD** (Create, Read, Update, Delete).

### DCL: Data Control Language

```sql
GRANT SELECT, INSERT ON Customers TO analyst_user;
REVOKE INSERT ON Customers FROM analyst_user;
```

### TCL: Transaction Control Language

```sql
BEGIN TRANSACTION;
UPDATE Accounts SET Balance = Balance - 100 WHERE AccountID = 'A';
COMMIT;       -- or ROLLBACK;
```

### Comparison

| | DDL | DML | DCL | TCL |
|---|---|---|---|---|
| Works on | Structure | Data | Permissions | Transactions |
| Analogy | Building the filing cabinet | Putting papers in and taking them out | Giving out keys | Saving or undoing your work |
| Example | `CREATE TABLE` | `INSERT` | `GRANT` | `COMMIT` |

---

## Quick revision summary

| Topic | One-line summary |
|---|---|
| **Database** | An organised, persistent collection of data |
| **DBMS** | Software that stores, manages, secures and queries the database |
| **Data modelling** | Designing the structure of data before building it (conceptual, logical, physical) |
| **ERD** | A diagram of entities, attributes and relationships, with cardinality |
| **Normalisation** | Splitting tables to remove redundancy and anomalies (1NF, 2NF, 3NF) |
| **Index** | A structure (usually a B-tree) that speeds up reads at the cost of slower writes |
| **Query efficiency** | Help the optimiser: filter early, index well, select only what you need |
| **ACID** | Atomicity, Consistency, Isolation, Durability: reliable transactions |
| **SQL sub-languages** | DDL (structure), DML (data), DCL (permissions), TCL (transactions) |