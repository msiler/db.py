queries = {
    "column": {
        "head": "select {column} from {table} limit {n};",
        "all": "select {column} from {table};",
        "unique": "select distinct {column} from {table};",
        "sample": "select {column} from {table} order by random() limit {n};"
    },
    "table": {
        "select": "select {columns} from {table};",
        "select_limit": "select {columns} from {table} limit {limit};",
        "select_unique": "select distinct {columns} from {table};",
        "select_limit_unique": "select distinct {columns} from {table} limit {limit};",
        "count": "select count(*) from {table};"
    },
    "system": {
        "schema_no_system": "select table_name, column_name, data_type from tmp_dbpy_schema;",
        "schema_with_system": "select table_name, column_name, data_type from tmp_dbpy_schema;",
        "foreign_keys_for_table": """
            select
                column_name
                , foreign_table as foreign_table_name
                , foreign_column as foreign_column_name
            from
                tmp_dbpy_foreign_keys
            where
                table_name = '{table}';
        """,
        "foreign_keys_for_column": """
            select
                column_name
                , foreign_table as foreign_table_name
                , foreign_column as foreign_column_name
            from
                tmp_dbpy_foreign_keys
            where
                table_name = '{table}' and column_name = '{column}';
        """,
        "ref_keys_for_table": """
            select
                 foreign_column
                 , table_name
                 , column_name
            from
                tmp_dbpy_foreign_keys
            where
                foreign_table = '{table}';
        """,
    }
}
