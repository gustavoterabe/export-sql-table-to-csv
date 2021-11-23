#!/usr/bin/env python3
# coding: utf-8

from src.MySql import MySql
from src.Postgres import Postgres
import pandas as pd
import os 


class Exporter:
    def __init__(
        self,
        databaseType,
        user,
        password,
        host,
        database,
        dirname: str = "./tables",
        table: str = None,) -> None:
        if databaseType == "postgres":
            self.db = Postgres(
                user=user,
                password=password,
                host=host,
                database=database
            )
        elif databaseType == "mysql":
            self.db = MySql(
                user=user,
                password=password,
                host=host,
                database=database
            )
        self.database = database
        self.table = table
        self.dirname = dirname

    def Export(self):
        listTables = self.db.GetTableList()
        listTables = [table for table, in listTables]
        if self.table:
            if any(self.table in tables for tables in listTables):
                listTables = [self.table]
            else:
                raise Exception(f"The table doesnt belong to the database {self.database}")
        
        for table in listTables:
            columns, data = self.db.GetTable(tableName=table)
            df = pd.DataFrame(data ,columns=columns)
            print("Saving data from database {} table {} in {}".format(
                self.database,
                table,
                os.path.join(self.dirname ,f"{self.database}-{table}.csv")
            ))
            df.to_csv(
                os.path.join(self.dirname ,f"{self.database}-{table}.csv"), 
                index=False
            )

