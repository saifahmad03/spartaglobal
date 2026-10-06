# CRUD

**CRUD** stands for the four basic operations you can perform on stored data.

| Letter | Operation | Meaning | SQL command |
|---|---|---|---|
| **C** | Create | Add new data | `INSERT` |
| **R** | Read | Retrieve data | `SELECT` |
| **U** | Update | Change existing data | `UPDATE` |
| **D** | Delete | Remove data | `DELETE` |

---

## Examples (film_table)

```sql
-- Create
INSERT INTO film_table (film_name, film_type)
VALUES ('Inception', 'Sci-Fi');

-- Read
SELECT film_name, film_type
FROM film_table
WHERE film_type = 'Sci-Fi';

-- Update
UPDATE film_table
SET film_type = 'Thriller'
WHERE film_name = 'Inception';

-- Delete
DELETE FROM film_table
WHERE film_name = 'Inception';
```

> Always use `WHERE` with `UPDATE` and `DELETE`, or every row in the table is affected.

---

## Why it matters

Almost every application is built on CRUD. For example, on a website:

- Signing up is **Create**
- Viewing a profile is **Read**
- Editing details is **Update**
- Deleting an account is **Delete**

---

## CRUD in web APIs (REST)

| CRUD | HTTP method |
|---|---|
| Create | `POST` |
| Read | `GET` |
| Update | `PUT` / `PATCH` |
| Delete | `DELETE` |

---

## Link to SQL sub-languages

`INSERT`, `SELECT`, `UPDATE` and `DELETE` are all **DML** commands. CRUD only covers working with the **data**. Creating or altering tables (`CREATE TABLE`, `ALTER`) is **DDL**, not CRUD.