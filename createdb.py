#!/usr/bin/env python

import os
import sqlite3
import sys

from config import DB_PATH

if os.path.exists(DB_PATH):
    print("ERROR: File already exists: %s" % DB_PATH)
    sys.exit(2)

db = sqlite3.connect(DB_PATH)
cursor = db.cursor()
cursor.execute("CREATE TABLE users (username text PRIMARY KEY, password text);")
print("* Users database created at %s" % DB_PATH)
