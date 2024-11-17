import sqlite3
class ql__database:
    def __init__(self,path):
        self.path = path
    
    def connect_database(self):
        try:
            conn = sqlite3.connect(self.path)
        except Exception as e :
            print("lỗi kết nối: ",e)
        else:
            return conn
        
    def create_table(self,name,**dict):
        conn = self.connect_database()
        cur = conn.cursor()
        columns = []
        for i,v in dict.items():
            columns.append(f"{i} {v}")
        sql = f"""
                create table {name} 
                (
                    {", ".join(columns)}
                )
            """
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()

    def insert_table(self,name,**dict):
        conn = self.connect_database()
        cur = conn.cursor()
        columns_name = []
        columns = []
        for i in dict.keys():
            columns_name.append(i)
        for v in dict.values():
            columns.append(v)
        sql = f"""
            insert into {name}
            values ( {", ".join(columns)})
        """ 
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()

    def delete_table(self,name,condition = None):
        conn = self.connect_database()
        cur = conn.cursor()
        if condition:
            sql = f"""
                delete from {name} where {condition}
            """
        else:
            sql = f"""
                delete from {name}
            """
        cur.execute(sql)
        conn.commit()
        conn.close()
        cur.close()
    
    def update_table(self,name,condition = None,**dict):
        conn = self.connect_database()
        cur = conn.cursor()
        columns = []
        for i,v in dict.items():
            columns.append(f"{i} = {v}")
        if condition:
            sql = f"""
                update {name} 
                set {", ".join(columns)}
                where {columns}
            """
        else:
            sql = f"""
                update {name}
                set {", ".join(columns)}
            """
        cur.execute(sql)
        cur.close()
        conn.close()

