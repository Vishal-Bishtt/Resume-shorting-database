import subprocess
import os
from dotenv import load_dotenv

load_dotenv()

# MongoDB backup directory
backup_dir = "./db_backups"
mongo_uri = os.getenv("MONGODB_URI")

def backup_database():
    """Creates a backup of the MongoDB database."""
    os.makedirs(backup_dir, exist_ok=True)
    cmd = f"mongodump --uri='{mongo_uri}' --out {backup_dir}"
    subprocess.run(cmd, shell=True, check=True)
    print("Backup completed successfully.")

def restore_database():
    """Restores the MongoDB database from backup."""
    cmd = f"mongorestore --uri='{mongo_uri}' {backup_dir}"
    subprocess.run(cmd, shell=True, check=True)
    print("Database restored successfully.")

