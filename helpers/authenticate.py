from PyQt6.QtSql import QSqlQuery

def auth_login(username, password):
    query = QSqlQuery()
    query.prepare("SELECT * FROM users WHERE username = ? AND password = ?")
    query.addBindValue(username)
    query.addBindValue(password)
    query.exec()

    if query.next():
        return True
    else:
        return False