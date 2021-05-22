import sqlite3


class SqliteUtil:

    @staticmethod
    def get_connection(database='../db/pet.db'):
        return sqlite3.connect(database)

    @staticmethod
    def execute(sql, connection=None):
        """
        执行增删改操作
        :param sql: sql语句
        :param connection: 数据库连接
        :return:
        """

        if connection is None:
            return

        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        return cursor.rowcount

    @staticmethod
    def query(sql, connection=None):
        """
        执行查询语句
        :param sql: 待查询的sql语句
        :param connection:  数据库连接
        :return:
        """
        if connection is None:
            return

        cursor = connection.cursor()
        cursor.execute(sql)
        return cursor.fetchall()


if __name__ == '__main__':
    # connection = SqliteUtil.get_connection()
    # count = SqliteUtil.execute("insert into users (username, password) values ('123', '123456')", connection)
    # print(count)
    #
    # records = SqliteUtil.query("select username, password from users", connection)
    # print(records)

    import os
    print(os.path.abspath('../db/pet.db'))