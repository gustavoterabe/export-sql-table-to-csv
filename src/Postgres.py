#!/usr/bin/env python3
# coding: utf-8

import psycopg2

class Postgres:
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
            connection = psycopg2.connect(
                user = self._user,
                password = self._password,
                host = self._host,
                database = self._database
            )
            return connection

        except Exception as e:
            raise e
    
    def GetConnectionString(self):
        conn_str = "postgresql://{}:{}@{}:{}/{}".format(
            self._user,
            self._password,
            self._host,
            self._port,
            self._database
        ) 

        return conn_str

    def RunQuery(self, query: str):
        res = None
        with self._connect as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, conn)
                try:
                    res = cursor.fetchall()
                except psycopg2.ProgrammingError as error:
                    print(error)
            conn.commit()
        return res

    def GetTableList(self):
        query = (
            """
            SELECT tablename 
            FROM pg_catalog.pg_tables
            WHERE (schemaname != 'information_schema');
            """
        )

        return tuple(self.RunQuery(query))

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

        columns = tuple(self.RunQuery(queryGetColumns))
        columns = [col for col, in columns]
        # print(columns)
        data = self.RunQuery(queryGetData)

        return columns, data