from src.app.database.executor import execute_and_fetch, execute_command, insert


allowed_creation_keys = ["name", "email", "password"]


def create(params):
    p = {k: params[k] for k in allowed_creation_keys if k in params.keys()}
    return insert(f"INSERT INTO makeEat.users (name, email, password) "
                  f"VALUES ('{p['name']}', '{p['email']}', '{p['password']}')")


def lst(conditions):
    query = "SELECT * FROM makeEat.users" + (f" WHERE {conditions}" if conditions else "")
    users = execute_and_fetch(query)
    return list(
        map(lambda x: {"id": x[0], "name": x[1], "email": x[2], "password": x[3], "created_at": str(x[4])}, users))


def list_all():
    return lst("")


def list_by(params):
    where_clause = " AND ".join([" = ".join([key, str(val)]) for key,val in params.items()])
    return lst(where_clause)

