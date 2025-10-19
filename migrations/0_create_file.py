import os

os.makedirs("/data", exist_ok=True)
with open("/data/db.sqlite", "w"):
    pass
