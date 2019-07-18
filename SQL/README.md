A collection of items pertaining to SQL, Relational Algebra, and common statistical definitions for the field of Data Science. 

# General Database Definitions

### General Definitions

**Database:** A collection of interrelated data that is relevant to an enterprise

**Database Management System:** A set of programs/packages to access/store database information

**Database Schema:** The logical design of the database

**Database Instance:** A snapshot of the data in the database

### Relational Model Definitions

**Relation:** A table that has rows and columns

**Tuple:** A row in a relation

**Attribute:** A column name in a relation

**Relational Database**: A collection of identifiable relations

**Superkey:** A set of one or more attributes taken together to *uniquely identify* a typle in the relation

**Candidate key:** A minimal superkey

**Primary key:** A candidate key chosen by the database designer to distinguish between tuples

**Foreign key:** A set of attributes in a relation that is a primary key in another relation

**Relation Schema:** A display of relations listing all attributes with primary keys underlined

### Schema Constraints

**Referential Integrity Constraint:** Values appearing in specified attributes of any tuple in the referencing relation must appear in specified attributes of at least one tuple in the referenced relation

**Foreign Key Constraint:** A foreign key value in one relation must appear in the referenced relation

# Relational Algebra Operators

**Selection:** $\sigma_p(x)$

Get specific tuples if it fulfills a predicate

* p is the selection predicate
  * p is a boolean formula of terms and connectives
  * Connectives: AND, OR, ~(not)
  * <, >, <=, >=, =, !=
* x is a relation

**Projection:** $pi_{a_1, a_2... a_n}(x)$

* a_i are the only attributes selected from the relation
* x is a relation

**Cartesian Product:** $R1 \times R2$

Repeat all of R1 with each row of R2, with R2's attributes added to R1's relation

**Theta-Join:** $R1 \bowtie_p R2$

* Take the product of $R1 \times R2$
* Then apply $\sigma_p(x)$ to the result

**Natural Join:** $R1 \bowtie R2$

Combine two relations into a single relation; tuples are joined if there is at least one common attribute (that has the same name). Anagolous to a theta join, the selection predicate is if all common attributes are equal to each other

**Renaming:** $\rho_{old \rightarrow new}(x), \rho_{s}(x)$

Changes attribute `old` to attribute `new` in the relation OR returns the relation x with `s.` prefacing it


### Bag operations: Analogous to set operations

Given relations R1 and R2, the following are properties are needed for bag operations to be valid:
* R1 and R2 must have the same arity (# of attributes)
* R1 and R2 must have the same attribute names
* Attribute domains must be compatible (i.e. same type of value)

**Union:** **R1 U R2**

Uniquely adds R2 tuples to R1. Commutative (i.e. add R1 tuples to R2)

**Difference:**  **R1 - R2**

Remove any R1 tuples that R2 has. Not commutative or associative

**Intersection:** **R1 n R2 = R1 - (R1 - R2)**

Only get common tuples between R1 and R2

# SQL

All basic queries in SQL are in the form of

```
SELECT A1, A2 ... AN
FROM R1 [JOIN] R2 ... RN
WHERE P1, P2, ... PN;
```

such that A_i are attributes, R_i are relations and P_i are predicates.

In this basic form:
* `SELECT` statements are the equivalent to Projection statements in Relational Algebra; retrieving specified attributes
* `WHERE` statements are the equivalent to Selection statements in Relational Algebra; retrieving specified tuples given predicates

Joins are slightly more complicated, but can be summarized here (after doing a quick google search):

<img src="http://i.imgur.com/1m55Wqo.jpg" />

Joins can be complicated, so there exists something called *views*. **Views** are virtual tables that are subsets of the tables in a database (within SQL) defined using a query. However, views are not part of the database, but it is similarly treated like a table. A view is created by the basic form below

```
CREATE VIEW [view name] AS
SELECT A1, A2 ... AN
FROM R1 [JOIN] R2 ... RN
WHERE P1, P2, ... PN;
```

From here, the newly created view can be treated like a table.

# Database Creation/Modification in SQL

Prior to creating a table, some basic attribute types are as follows:

* `CHAR(n)`: A fixed-length character string with a maximum length of n
* `VARCHAR(n)`: A variable-length character string with a maximum length of n
* `INT`: An Integer
* `NUMERIC(p, d)`: A fixed-point number with p digits which d of the digits are to the right of the decimal point
* `FLOAT(n)`: A floating point number with at least n digits of precision
* `NULL`: Unknown Value / may not exist

Integrity Constraints are as follows
* `PRIMARY KEY (list of attributes)`: These attributes form the primary keys for the relation. Primary keys must be non-null and unique
* `FOREIGN KEY (list of attributes) references [another relation name]`: The value of the listed attributes must correspond to values of the primary key attributes of some tuple in another relation
* `NOT NULL`: Specifies that this attribute may not have the null value

To create a table, the query goes as follows

```
CREATE TABLE [table name] (
[attribute 1] [attribute type],
[attribute 2] [attribute type],
[attribute 3] [attribute type] NOT NULL,  # signifiying an attribute cannot be NULL
...
PRIMARY KEY ([attribute 3], [attribute 4]...),
FOREIGN KEY ([attribute 4, attribute 5...]) REFERENCES [another relation name],
FOREIGN KEY ([attribute 5]) REFERENCES [another relation name],
...
);
```

### Basic Tuple Insertion

Independently insert tuples into a table:

```
INSERT INTO [table name]
VALUES ([value 1], [value 2] ... [value n]), ([value a], [value b] ... [value n])...;
```

Insert tuples into the table using a query

```
INSERT INTO [table name]
    SELECT ...
    FROM ...
    WHERE ...;
```

### Basic Tuple Removal

Remove a table

```
DROP TABLE [table name];
```

Remove tuples that satisfy a predicate

```
DELETE FROM [table name]
WHERE [predicates];
```

### Editing tables

Adding a column

```
ALTER TABLE [table name]
ADD [column name];
```

Removing a column

```
ALTER TABLE [table name]
DROP [column name]
```
