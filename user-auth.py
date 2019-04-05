#!/usr/bin/env python

import hashlib
import sqlite3
import sys

from config import DB_PATH, HASH_ALGORITHM

# Read username and password from via-file
filename = sys.argv[1]
print("[auth-sqlite] filename: " + filename, file=sys.stdout)
fp = open(filename)
data = fp.readlines()
fp.close()
username = data[0].rstrip()
password = data[1].rstrip()

hash_func = getattr(hashlib, HASH_ALGORITHM)
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute('SELECT * FROM users WHERE username = ?;', (username,))
result = cursor.fetchone()

if result is None:
    print("[auth-sqlite] unknown user: " + username, file=sys.stderr)
    sys.exit(1)

if hash_func(password.encode("utf-8")).hexdigest() != result[1]:
    print("[auth-sqlite] wrong password, username=" + username, file=sys.stderr)
    sys.exit(1)

sys.exit(0)
