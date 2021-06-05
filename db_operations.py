import sqlite3


class Interaction:
    def __init__(self, db_path):
        self.connection = None
        self.cursor = None
        self.path = db_path

    def do_connect(self):
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        print('success connection')

    def do_disconnect(self):
        self.connection.close()

    def create_tabel(self, table_name):
        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS {} (
            id int "AUTOINCREMENT",
            content text NOT NULL);
            '''.format(table_name)
        )

    def delete_table(self, table_name):
        self.cursor.execute(
            '''
            DELETE FROM {};
            '''.format(table_name)
        )

    def insert(self, content):
        self.cursor.execute(
            '''
            INSERT INTO test(content) VALUES ("{}");
            '''.format(content)
        )
        print('success insert')

    def show_all(self):
        self.cursor.execute(
            '''
            SELECT * FROM test;
            '''
        )
        print('succsess show')
        return self.cursor.fetchall()

    def commit(self):
        self.connection.commit()
        print('success commit')


if __name__ == '__main__':
    pass