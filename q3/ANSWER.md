## Part A: SQL

### Question A.(i)
```
SELECT r.request_id
FROM requests r
JOIN senators s ON r.senator_id = s.senator_id
WHERE s.party = 'Democrat';
```

### Question A.(ii)
```
SELECT s.state
FROM senators s
LEFT JOIN requests r ON s.senator_id = r.senator_id
GROUP BY s.state
HAVING COUNT(DISTINCT r.request_id) = 1;
```

## Part B: Architecture Design

### Question B.(i)

##### 1. Database Type
A relational database like PostgreSQL would work well here for structured data and referential integrity. If high scalability or distributed storage is a requirement, a graph database (e.g., Neo4j) might be considered to track connections between duplicates more naturally.

##### 2. Data Schema
- **Requests Table:** Stores each request with basic details (e.g., `request_id`, `title`, `recipient`).
- **Duplicates Table:** Maintains duplicate groupings. It would include `duplicate_group_id` and `request_id`, where each unique `duplicate_group_id` represents a set of duplicate requests.
- **Duplicate Groups Table:** Optionally, if we need metadata on each duplicate set (e.g., who marked them as duplicates), we could have this table, storing information such as `duplicate_group_id`, `marked_by`, and `date_marked`.

##### 3. Duplicate Grouping
When marking requests as duplicates, each request is assigned a `duplicate_group_id`. For example, if A, B, and C are marked as duplicates, all three would have the same `duplicate_group_id` in the Duplicates Table.
This setup allows easy querying for all duplicates within the same group, facilitating efficient retrieval for export.

##### 4. Export Process:
The database supports querying by `duplicate_group_id`, allowing all duplicate requests to be retrieved and exported efficiently into CSV or Excel formats as requested.

### Question B.(ii)

##### 1. Data Schema Changes:
- Add a new table, `Request_Relationships`, with fields `request_id_1`, `request_id_2`, and `relationship_type` (where `relationship_type` can be `CONFIDENT_DISTINCT`, `POTENTIAL_DUPLICATE`, or `DUPLICATE`).
- This setup allows each request pair to have one relationship type and enables tracking whether requests are duplicates, potential duplicates, or confidently distinct.
##### 2. Process:
- When two requests are marked as confidently distinct, an entry is added in `Request_Relationships` with `relationship_type = 'CONFIDENT_DISTINCT'`.
- For potential duplicates, the relationship type would be set to `POTENTIAL_DUPLICATE`. Staff can later review and promote potential duplicates to confirmed duplicates as necessary.