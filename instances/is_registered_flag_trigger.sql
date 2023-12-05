--related table and functioon is deleted
--customer and registered user table combined into one table

CREATE OR REPLACE FUNCTION IS_REGISTERED_FLAG_TRIGGER_FUNC()
RETURNS TRIGGER
LANGUAGE PLPGSQL
AS $$
BEGIN

    IF EXISTS(
        SELECT 1 FROM CUSTOMER as C
            WHERE NEW.customer_id = C.customer_id 
    )
    THEN 
        UPDATE CUSTOMER SET is_registered = TRUE 
                WHERE customer_id = NEW.customer_id; -- Adjusted to use NEW.customer_id
    END IF;
    RETURN NEW;
END;
$$;

CREATE OR REPLACE TRIGGER IS_REGISTERED_FLAG_TRIGGER
AFTER INSERT ON REGISTERED_USER
FOR EACH ROW
EXECUTE FUNCTION IS_REGISTERED_FLAG_TRIGGER_FUNC();