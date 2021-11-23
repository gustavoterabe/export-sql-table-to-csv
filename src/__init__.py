#!/usr/bin/env python3
# coding: utf-8

import argparse
from src.ExporterToCsv import Exporter

def StartApp():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-pg", "--postgres", action="store_true")
    group.add_argument("-m", "--mysql", action="store_true")
    parser.add_argument("-host","--host", type=str, required=True)
    parser.add_argument("-u", "--user", type=str, required=True)
    parser.add_argument("-p", "--password", type=str, required=True)
    parser.add_argument("-d", "--database", type=str, required=True)
    parser.add_argument("-t", "--tablename", type=str)
    args = parser.parse_args()

    exp = Exporter(
        databaseType = "postgres" if args.postgres else "mysql",
        user = args.user,
        password= args.password,
        host = args.host,
        database=args.database,
        table = args.tablename
    )

    exp.Export()







