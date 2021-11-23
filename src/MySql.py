#!/usr/bin/env python3
# coding: utf-8

import pymysql
import pymysql.cursors

class MySql:
    def __init__(
        self, 
        user: str, 
        password: str, 
        host: str, 
        database: str) -> None:

        self._user = user
        self._password = password
        self._host = host
        self._database = database

    @property
    def _connect(self):
        try:
            connection = pymysql.connect(
                user = self._user,
                password = self._password,
                host = self._host,
                database = self._database
            )
            return connection

        except Exception as e:
            raise e
    
    def RunQuery(self, query: str):
        res = None
        with self._connect as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)
                try:
                    res = cursor.fetchall()
                except pymysql.ProgrammingError as error:
                    print(error)
            conn.commit()
        return res

    def GetTableList(self):
        query = (
            "SHOW TABLES"
        )

        return self.RunQuery(query)

    def GetTable(self, tableName, cond = ""):
        
        queryGetColumns = (
            f"""
            SELECT COLUMN_NAME 
            FROM information_schema.columns
            WHERE table_name = N'{tableName}'
            """
        )
        queryGetData = (
            f"""
            SELECT *
            FROM {tableName}
            """
        )
        if cond:
            queryGetData += f"WHERE {cond}"

        columns = list(self.RunQuery(queryGetColumns))
        data = self.RunQuery(queryGetData)

        return columns, data