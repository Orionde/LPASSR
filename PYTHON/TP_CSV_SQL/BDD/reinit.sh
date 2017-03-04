#!/bin/bash

cat clean_db.sql | sqlite3 office.db
cat tables.sql | sqlite3 office.db
