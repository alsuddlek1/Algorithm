SELECT LEFT(product_code, 2) AS CATEGORY, COUNT(LEFT(product_code, 2))
FROM PRODUCT
GROUP BY CATEGORY
ORDER BY CATEGORY