from src.router import app
from src.database.setup import db_startup


if __name__ == '__main__':
    # create an instance of MySQL DB
    db_startup()

    # run app router
    print(f"Server is running in port {5000}")
    app.run(host='0.0.0.0', port=5000, debug=True)

