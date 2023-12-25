CREATE OR REPLACE FUNCTION VERIFY_INVENTORY_FUNC()
    RETURNS TRIGGER
    LANGUAGE plpgsql AS $$
DECLARE
    stock INT;
BEGIN
    SELECT inventory INTO stock
    FROM PRODUCT as p
    WHERE p.product_id = NEW.product_id;

    IF NEW.inventory > stock THEN
        RAISE EXCEPTION 'NOT ENOUGH STOCK TO PROVIDE INTENDED AMOUNT OF PRODUCTS';
    END IF;
    RETURN NEW;
END;
$$;

CREATE TRIGGER VERIFY_INVENTORY_TRIGGER
    BEFORE INSERT ON ORDER_JUNCTION
    FOR EACH ROW
EXECUTE FUNCTION VERIFY_INVENTORY_FUNC();