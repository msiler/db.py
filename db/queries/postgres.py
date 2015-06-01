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
        "schema_no_system": """
                select
                    table_name
                    , column_name
                    , udt_name
                from
                    information_schema.columns
                where
                    table_schema not in ('information_schema', 'pg_catalog')
                """,
        "schema_with_system": """
                select
                    table_name
                    , column_name
                    , udt_name
                from
                    information_schema.columns;
                """,
        "schema_specified": """
                select
                    table_name
                    , column_name
                    , udt_name
                from
                    information_schema.columns
                where table_schema in (%s);
                """,
        "foreign_keys_for_table": """
            SELECT
                kcu.column_name
                , ccu.table_name AS foreign_table_name
                , ccu.column_name AS foreign_column_name
            FROM
                information_schema.table_constraints AS tc
                JOIN information_schema.key_column_usage AS kcu
                  ON tc.constraint_name = kcu.constraint_name
                JOIN information_schema.constraint_column_usage AS ccu
                  ON ccu.constraint_name = tc.constraint_name
            WHERE constraint_type = 'FOREIGN KEY' AND tc.table_name='%s';
        """,
        "foreign_keys_for_column": """
            SELECT
                kcu.column_name
                , ccu.table_name AS foreign_table_name
                , ccu.column_name AS foreign_column_name
            FROM
                information_schema.table_constraints AS tc
                JOIN information_schema.key_column_usage AS kcu
                  ON tc.constraint_name = kcu.constraint_name
                JOIN information_schema.constraint_column_usage AS ccu
                  ON ccu.constraint_name = tc.constraint_name
            WHERE constraint_type = 'FOREIGN KEY' AND tc.table_name='%s' and kcu.column_name = '%s';
        """,
        "ref_keys_for_table": """
            SELECT
                ccu.column_name
                , kcu.table_name AS foreign_table_name
                , kcu.column_name AS foreign_column_name
            FROM
                information_schema.table_constraints AS tc
                JOIN information_schema.key_column_usage AS kcu
                  ON tc.constraint_name = kcu.constraint_name
                JOIN information_schema.constraint_column_usage AS ccu
                  ON ccu.constraint_name = tc.constraint_name
            WHERE constraint_type = 'FOREIGN KEY' AND ccu.table_name='%s';
        """
    }
}
