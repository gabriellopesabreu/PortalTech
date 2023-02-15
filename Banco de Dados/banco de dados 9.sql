
CREATE PROCEDURE prod_compr_dia (dia int)
BEGIN 
select sum quantiti
from products
where date = dia
END;

CALL prod_compr_dia(20220505);