CREATE OR REPLACE PROCEDURE public.add_primary_key(t_name varchar, c_name varchar)
LANGUAGE plpgsql
AS $$
DECLARE
    row record;
BEGIN
    FOR row IN SELECT table_name, column_name FROM INFORMATION_SCHEMA.COLUMNS  WHERE table_schema = 'public'
	AND table_name LIKE t_name
	AND column_name LIKE c_name
    LOOP
        EXECUTE 'ALTER TABLE public.' || quote_ident(row.table_name) || ' ADD PRIMARY KEY ' || '(' || row.column_name || ')';
    END LOOP;
END;
$$