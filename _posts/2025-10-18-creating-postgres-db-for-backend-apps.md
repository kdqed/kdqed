---
cover_image: postgres-db-user.webp
title: "Creating PostgreSQL DB for Python Or Other Backend Apps"
permalink: creating-postgresql-db-for-backend-app
---

I've been trying to catch onto the "use PostgreSQL for everything" trend. So here's a personal reference note on how to create a new database along with a user, assign the necessary persmissions, and link it up to your app.

__Step 1:__ Run `psql` as the `postgres`user

```
$ sudo -u postgres psql
```

__Step 2:__ Create Database

```
postgres=# CREATE DATABASE yourDB;
```

__Step 3:__ Create A User With Password

```
postgres=# CREATE USER yourUserName WITH ENCRYPTED PASSWORD 'yourPassword';
```

__Step 4:__  Give User Privileges On Database

```
postgres=# GRANT ALL PRIVILEGES ON DATABASE yourDB TO yourUserName;
```

__Step 5:__ Give User Schema Privileges

One extra step to let your app create tables, columns, etc.

```
postgres=# \c yourDB;
yourDB=# GRANT ALL ON SCHEMA public TO yourUserName;
```

__Step 6:__ Use the URL:

```
postgresql://yourUserName:yourPassword@localhost/yourDB
```


