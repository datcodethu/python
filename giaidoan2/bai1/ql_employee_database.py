import sqlite3

class ql__database:
    def __init__(self, path):
        self.path = path

    def connect_database(self):
        try:
            conn = sqlite3.connect(self.path)
            return conn
        except Exception as e:
            print("Lỗi kết nối: ", e)
            return None

    def create_table(self, name, **dict):
        conn = self.connect_database()
        if conn:
            try:
                cur = conn.cursor()
                columns = ", ".join([f"{i} {v}" for i, v in dict.items()])
                sql = f"""
                    create table if not exists {name} 
                    (
                        {columns}
                    )
                """
                cur.execute(sql)
                conn.commit()
            finally:
                cur.close()
                conn.close()

    def insert_table(self, name_table, **dict):
        conn = self.connect_database()
        if conn:
            try:
                cur = conn.cursor()
                columns_name = ", ".join(dict.keys())
                placeholders = ", ".join(["?"] * len(dict))
                values = tuple(dict.values())
                sql = f"""
                    insert into {name_table} ({columns_name})
                    values ({placeholders})
                """ 
                cur.execute(sql, values)
                conn.commit()
            finally:
                cur.close()
                conn.close()

    def delete_table(self, name_table, condition=None):
        conn = self.connect_database()
        if conn:
            try:
                cur = conn.cursor()
                if condition:
                    sql = f"delete from {name_table} where {condition}"
                else:
                    sql = f"delete from {name_table}"
                cur.execute(sql)
                conn.commit()
            finally:
                cur.close()
                conn.close()

    def update_table(self, name, condition=None, **dict):
        conn = self.connect_database()
        if conn:
            try:
                cur = conn.cursor()
                columns = ", ".join([f"{i} = ?" for i in dict.keys()])
                values = list(dict.values())
                if condition:
                    sql = f"""
                        update {name} 
                        set {columns}
                        where {condition}
                    """
                else:
                    sql = f"""
                        update {name}
                        set {columns}
                    """
                cur.execute(sql, values)
                conn.commit()
            finally:
                cur.close()
                conn.close()
