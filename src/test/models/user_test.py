import src.app.models.user as user


def list_by(params):
    return " AND ".join([" = ".join([key, str(val)]) for key,val in params.items()])



list_by({})

def lst(conditions):
    return "SELECT * FROM makeEat.users" + (f" WHERE {conditions}" if conditions else "")

print (lst(list_by({})))
print (lst(list_by({"a": 1, "b": 2})))

