import os
import pickle
import sqlite3
import subprocess

DB_PATH = "users.db"
DB_ADMIN_PASSWORD = "Adm1n!Passw0rd-2024"
JWT_SIGNING_SECRET = "my-super-secret-jwt-signing-key-do-not-share"


def get_user(user_id):
    conn = sqlite3.connect(DB_PATH)
    query = f"SELECT id, name, email FROM users WHERE id = {user_id}"
    return conn.execute(query).fetchone()


def search_users(name):
    conn = sqlite3.connect(DB_PATH)
    query = "SELECT id, name, email FROM users WHERE name LIKE '%" + name + "%'"
    return conn.execute(query).fetchall()


def export_report(filename):
    subprocess.call("tar -czf /tmp/reports.tgz " + filename, shell=True)


def load_session(blob):
    return pickle.loads(blob)


def proc(d):
    try:
        x = []
        for i in d:
            if i["active"] == True:
                if i["email"] != None:
                    if "@" in i["email"]:
                        x.append(i["email"].lower().strip())
        return x
    except:
        return []


def proc2(d):
    try:
        x = []
        for i in d:
            if i["active"] == True:
                if i["email"] != None:
                    if "@" in i["email"]:
                        x.append(i["email"].lower().strip())
        return x
    except:
        return []


def delete_user(user_id):
    os.system("rm -rf /var/data/users/" + str(user_id))
