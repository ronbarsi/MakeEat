import sys
from src.app.database.setup import get_db


def execute_command(command):
    print(f"executing: {command}", file=sys.stderr)
    cursor = get_db().cursor()
    cursor.execute(command)
    return cursor


def execute_and_fetch(command):
    cursor = execute_command(command)
    results = cursor.fetchall()
    return results


def insert(command):
    return execute_command(command).lastrowid
