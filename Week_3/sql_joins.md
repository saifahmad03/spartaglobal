# SQL JOINs with the Northwind Database

## 1. What is a JOIN?

A **JOIN** combines rows from two or more tables based on a related column between them, usually a primary key in one table matched to a foreign key in another. Relational databases split data across tables to avoid duplication (customers in one table, orders in another). JOINs lets us bring that data back together in a single result set.

```sql
SELECT columns
FROM TableA
JOIN TableB
    ON TableA.key = TableB.key;
```

The ON clause defines how rows match. The type of JOIN defines what happens to rows that dont have a match.

---

## 2. How do JOINs work?

Think of each table as a circle in a Venn diagram. Each JOIN type returns a different region.

![SQL JOINs Venn diagram](https://upload.wikimedia.org/wikipedia/commons/9/9d/SQL_Joins.svg)


### INNER JOIN
Returns only rows where there is a **match in both tables**. Unmatched rows from either side are dropped.

### LEFT JOIN (LEFT OUTER JOIN)
Returns **all rows from the left table**, plus matching rows from the right. Where there is no match, right-side columns are `NULL`.

### RIGHT JOIN (RIGHT OUTER JOIN)
Returns **all rows from the right table**, plus matching rows from the left. Where there is no match, left-side columns are `NULL`.

### FULL JOIN (FULL OUTER JOIN)
Returns **all rows from both tables**. Matches are combined; non-matches get `NULL` on the missing side.

---

## 3. Examples in a very basic database

**Customers**

| CustomerID | CustomerName |
|-----------|--------------|
| 1 | Alfreds |
| 2 | Berglunds |
| 3 | Cactus |

**Orders**

| OrderID | CustomerID |
|---------|-----------|
| 101 | 1 |
| 102 | 1 |
| 103 | 2 |
| 104 | 9 *(no matching customer)* |

### INNER JOIN
```sql
SELECT c.CustomerName, o.OrderID
FROM Customers c
INNER JOIN Orders o ON c.CustomerID = o.CustomerID;
```

| CustomerName | OrderID |
|--------------|---------|
| Alfreds | 101 |
| Alfreds | 102 |
| Berglunds | 103 |

Cactus (no orders) and order 104 (no customer) are both excluded.

### LEFT JOIN
```sql
SELECT c.CustomerName, o.OrderID
FROM Customers c
LEFT JOIN Orders o ON c.CustomerID = o.CustomerID;
```

| CustomerName | OrderID |
|--------------|---------|
| Alfreds | 101 |
| Alfreds | 102 |
| Berglunds | 103 |
| Cactus | NULL |

### RIGHT JOIN
```sql
SELECT c.CustomerName, o.OrderID
FROM Customers c
RIGHT JOIN Orders o ON c.CustomerID = o.CustomerID;
```

| CustomerName | OrderID |
|--------------|---------|
| Alfreds | 101 |
| Alfreds | 102 |
| Berglunds | 103 |
| NULL | 104 |

### FULL JOIN
```sql
SELECT c.CustomerName, o.OrderID
FROM Customers c
FULL JOIN Orders o ON c.CustomerID = o.CustomerID;
```

| CustomerName | OrderID |
|--------------|---------|
| Alfreds | 101 |
| Alfreds | 102 |
| Berglunds | 103 |
| Cactus | NULL |
| NULL | 104 |

---




### 1. Customers Orders List

```sql
SELECT c.CompanyName, o.OrderID
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
ORDER BY c.CompanyName;
```
### 2. Orders with Customer Names

```sql
SELECT o.OrderID, o.OrderDate, c.CompanyName
FROM Customers AS c
JOIN Orders o ON c.CustomerID = o.CustomerID;
```
### 3. Orders with Product Names

```sql
SELECT o.OrderID, p.ProductName, o.Quantity
FROM [Order Details] AS o
JOIN Products p ON o.ProductID = p.ProductID;
```

### 4. Order Totals

```sql
SELECT SUM(UnitPrice * Quantity) AS TOTAL_VALUE, OrderID
FROM [Order Details]
GROUP BY OrderID
ORDER BY OrderID;
``` 

### 5. Total Spend per Customer
```sql
SELECT c.CompanyName,
       SUM(od.UnitPrice * od.Quantity)  AS Total_SPEND
FROM Customers c
INNER JOIN Orders o ON c.CustomerID = o.CustomerID
INNER JOIN [Order Details] od ON o.OrderID = od.OrderID
GROUP BY c.CompanyName
ORDER BY Total_SPEND DESC;
```

### 6. Customers with No Orders
```sql
SELECT c.CustomerID, c.CompanyName
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
WHERE o.OrderID IS NULL;
```

### 7. Products Never Ordered
```sql
SELECT p.ProductID, p.ProductName
FROM Products p
JOIN [Order Details] od ON p.ProductID = od.ProductID
WHERE od.OrderID IS NULL;
```

### 12. Advanced — Average Order Value per Customer
```sql
SELECT c.CompanyName, 
	COUNT(DISTINCT o.OrderID) AS NumberOfOrders,
	SUM(od.UnitPrice * od.Quantity) AS TOTALSPEND, 
	SUM(od.UnitPrice * od.Quantity)/COUNT(DISTINCT o.OrderID) AS AVG_TOTALSPEND
FROM Customers AS c
JOIN Orders o ON o.CustomerID = c.CustomerID
JOIN [Order Details] od ON o.OrderID = od.OrderID
GROUP BY c.CompanyName;
```

### 13. Employees with No Orders
```sql
SELECT e.EmployeeID, e.FirstName, e.LastName
FROM Employees e
LEFT JOIN Orders o ON e.EmployeeID = o.EmployeeID
WHERE o.OrderID IS NULL;
```

### 14. Most Popular Product (by quantity)
```sql
SELECT p.ProductName,
       SUM(od.Quantity) AS TotalQuantity
FROM Products p
JOIN [Order Details] od ON p.ProductID = od.ProductID
GROUP BY p.ProductName
ORDER BY TotalQuantity DESC
LIMIT 1;
```

