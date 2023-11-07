from PyQt6 import QtWidgets, QtSql

db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("stewardSalesReport.sqlite")

def createConnection():
    
    if not db.open():
        QtWidgets.QMessageBox.critical(None, "Cannot open database",
                             "Unable to establish a database connection.\n"
                             "This example needs SQLite support. Please read "
                             "the Qt SQL driver documentation for information how "
                             "to build it.")
        return False

    query = QtSql.QSqlQuery()
    query.exec("""CREATE TABLE IF NOT EXISTS  users (username VARCHAR(20) primary key,
                                        password VARCHAR(256))""");
    query.exec("insert into users values('admin', 'admin@4321')");
    query.exec("""CREATE TABLE IF NOT EXISTS  waiterDetails (id INT primary key, 
                                        firstname VARCHAR(20),
                                        lastname VARCHAR(20),
                                        phoneno VARCHAR(20))""");
    query.exec("insert into waiterDetails values(101, 'Danny', 'Young', '+91231231231')");
    query.exec("insert into waiterDetails values(102, 'Christine', 'Holand', '+91213123123')");

    query.exec("""CREATE TABLE IF NOT EXISTS  dailySales (id INT primary key, 
                                        waiter_id INT,
                                        description varchar(100),
                                        sales REAL,
                                        sale_date TEXT,
                                        FOREIGN KEY(waiter_id) REFERENCES waiterDetails(id))""");
    query.exec("insert into dailySales values(1, 101, 'Musical Night 13th hr', 100.5, datetime('now'))");

    print(db.tables())
    return True
