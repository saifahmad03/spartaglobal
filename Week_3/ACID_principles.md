# ACID Principles (Simply Explained)

ACID is four promises a database makes about **transactions**. A transaction is a group of steps treated as one job.

**Example:** transferring £100 from your account to a friend's is two steps: take £100 off you, then add £100 to them.

---

## A: Atomicity ("all or nothing")

Either **both** steps happen, or **neither** does. If the power cuts out halfway, the database undoes the first step, so your £100 does not just vanish.

## C: Consistency ("follow the rules")

The database must always end up in a **valid state**. If a rule says "balance cannot go below zero" and the transfer would break it, the whole transaction is rejected.

## I: Isolation ("no interference")

When many people use the database at once, each transaction behaves as if it were running **alone**. Nobody sees your transfer half-finished (money gone from you but not yet arrived).

## D: Durability ("it stays saved")

Once the database confirms the transaction (`COMMIT`), the change is **permanent**, even if the server crashes a second later.

---

## Summary

| Letter | Property | Meaning | Think |
|---|---|---|---|
| **A** | Atomicity | The whole transaction succeeds or none of it does | All or nothing |
| **C** | Consistency | Data always moves from one valid state to another | Rules always obeyed |
| **I** | Isolation | Concurrent transactions do not affect each other | Users do not clash |
| **D** | Durability | Committed data survives crashes | Saved for good |

---

## In SQL

```sql
BEGIN TRANSACTION;

UPDATE Accounts SET Balance = Balance - 100 WHERE AccountID = 'A';
UPDATE Accounts SET Balance = Balance + 100 WHERE AccountID = 'B';

COMMIT;       -- make the changes permanent
-- ROLLBACK;  -- or undo everything since BEGIN
```

| Command | Effect |
|---|---|
| `BEGIN TRANSACTION` | Start the transaction |
| `COMMIT` | Save the changes permanently |
| `ROLLBACK` | Undo all changes since the transaction began |

---

## Why it matters

ACID is essential wherever partial or lost updates would be serious: banking, orders, inventory and bookings. Relational databases such as SQL Server, PostgreSQL and MySQL (InnoDB) are ACID-compliant by default.