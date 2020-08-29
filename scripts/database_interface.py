"""
This module contains SQL adn Database interface definitions
"""
import sqlite3
import datetime
import pdb
from app_config import db_name

class SQL_Interface:
    """
    doc
    """

    def __init__(self,):
        """
        doc
        """
        self.db_file = db_name
        self.conn = None
        self._connect()

    def _connect(self):
        """
        doc
        :return:
        """
        try:
            self.conn = sqlite3.connect(self.db_file)
            print("Opened database successfully")
        except FileNotFoundError as err:
            print(err)

    def get_settings(self):
        """
        doc
        :return: Settings in tuple ('ID', 'HOST', 'PORT', 'CA_PATH', 'KEY_PATH', 'PEM_PATH', 'CC_TOPIC', 'DEVICE_TOPIC')
        """
        cursor = self.conn.execute('''SELECT * FROM "SETTINGS"''')
        return cursor.fetchone()

    def set_settings(self, *args):
        """
        insert settings into table
        :param kwargs:
        :return: True if success else False
        """
        try:
            query = f'''UPDATE SETTINGS set HOST = "{args[0]}", PORT ={args[1]} , CA_PATH ="{args[2]}", KEY_PATH="{args[3]}", PEM_PATH="{args[4]}",CC_TOPIC="{args[5]}", DEVICE_TOPIC="{args[6]}" where ID = 1;'''
            self.conn.execute(query)
            self.conn.commit()
            print ("Settings saved")
            return True
        except Exception as err:
            return False

    def get_test_cases(self, control_center_id):
        """
        doc
        :return:
        """
        query = f'''SELECT * FROM TEST_CASES where CONTROL_CENTER_ID={control_center_id}'''
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def insert_test_cases(self,*args):
        """
        doc
        :param args:
        :return:
        """
        query = f'''INSERT INTO TEST_CASES (TIME_STAMP,HOST,DEVICE_ID,TEMPERATURE,CONTROL_RESPONSE,STATUS,REMARKS,CONTROL_CENTER_ID) \
                                   VALUES ("{args[0]}","{args[1]}",{args[2]},{args[3]},"{args[4]}","{args[5]}","{args[6]}",{args[7]})'''
        self.conn.execute(query)
        self.conn.commit()
        return True

    def __del__(self):
        """
        doc
        :return:
        """
        if self.conn is not None:
            self.conn.close()
            print("DB connection closed")

if __name__ == "__main__":
    obj = SQL_Interface()
    # print(obj.get_settings())
    # obj.set_settings('127.0.0.1', 8883, '', '', '', '', '')
    time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # print(obj.insert_test_cases(time_stamp,"1270.0.1",1601,30,"Normal","PASS","",1101))
    # print(obj.insert_test_cases(time_stamp, "1270.0.10", 1602, 50, "High to normal", "PASS", "", 1101))
    for i in obj.get_test_cases(1101):
        print(i)
    # # print("\n".join(obj.get_test_cases()))