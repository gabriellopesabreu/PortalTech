CREATE FUNCTION contar_clientes_por_dia (@data DATE)
RETURNS INT
BEGIN
   DECLARE @contador INT;
   SET @contador = (SELECT COUNT(*) FROM clientes WHERE data_cadastro = @data);
   RETURN @contador;
END;