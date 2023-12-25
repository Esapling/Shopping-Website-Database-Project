CREATE OR REPLACE FUNCTION IS_CATEGORY_EXIST_IN_STORE_FUN()
RETURNS TRIGGER
LANGUAGE PLPGSQL
AS $$ 
BEGIN 
    PERFORM 1
    FROM CATEGORY c
    WHERE c.category_id = NEW.category_id
      AND c.store_id = NEW.store_id;
    IF NOT FOUND THEN
    -- there is not a category in the given store so raise an error
    RAISE EXCEPTION 'Category does not exist in the specified store';
    END IF;
    RETURN NEW;
END;
$$;

CREATE OR REPLACE TRIGGER CATEGORY_VALIDATOR
BEFORE INSERT ON PRODUCT 
FOR EACH ROW
--WHEN (pg_trigger_depth() < 1) this can also be added not to have inf loop
EXECUTE FUNCTION IS_CATEGORY_EXIST_IN_STORE_FUN();
