## Challenge Set 9: Part 1
#### *Introductory level SQL* ####
Subject:      W3Schools SQL Lab  
Date:         10/16/2010  
Name:         Steven Bierer  

----

This challenge uses the [W3Schools SQL playground](http://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all). Please add solutions to this markdown file and submit.  
&nbsp;
1. Which customers are from the UK?
```
SELECT CustomerID, CustomerName, Country
FROM Customers
WHERE COUNTRY = 'UK';
```
>Answer:  There are 7 customers from the UK, as shown in the listing below   
 &nbsp;  
__CustomerID	CustomerName	Country__  
4  	Around the Horn  	UK   
11  	B's Beverages  	UK   
16  	Consolidated Holdings  	UK   
19  	Eastern Connection  	UK   
38  	Island Trading  	UK   
53  	North/South  	UK   
72  	Seven Seas Imports  	UK   
&nbsp;
2. What is the name of the customer who has the most orders?
```
SELECT Customers.CustomerID, CustomerName, COUNT() AS Cnt FROM Orders
JOIN Customers ON Orders.CustomerID = Customers.CustomerID
GROUP BY CustomerName
ORDER BY Cnt DESC
LIMIT 1
```
> Answer:  Ernst Handel, with 10 orders  
&nbsp;  
__CustomerID	CustomerName	Cnt__  
20	Ernst Handel	10  
63	QUICK-Stop	7  
65	Rattlesnake Canyon Grocery	7
&nbsp;

3. Which supplier has the highest average product price?
```
SELECT Suppliers.SupplierID, Suppliers.SupplierName, AVG(Products.Price)  
AS Avg FROM Products  
JOIN Suppliers ON Products.SupplierID =   Suppliers.SupplierID  
GROUP BY Products.SupplierID  
ORDER BY Avg DESC  
LIMIT 3  
```
>Answer: Aux joeux ecclesiastiques, at 140.75 on average  
&nbsp;   
__SupplierID	SupplierName	Avg__  
18	Aux joyeux ecclésiastiques	140.75  
4	Tokyo Traders	46  
12	Plutzer Lebensmittelgroßmärkte AG	44.678  
&nbsp;

4. How many different countries are all the customers from? (*Hint:* consider [DISTINCT](http://www.w3schools.com/sql/sql_distinct.asp).)
```
SELECT COUNT(DISTINCT Country) AS MoreAwesome from Customers
```
>Answer: 21 countries  
&nbsp;  
__MoreAwesome__  
21  
&nbsp;

5. What category appears in the most orders?
```
SELECT Categories.CategoryID, CategoryName, COUNT(OrderID) AS Cnt FROM OrderDetails
JOIN Products ON OrderDetails.ProductID == Products.ProductID
JOIN Categories ON Products.CategoryID == Categories.CategoryID
GROUP BY Categories.CategoryID
ORDER BY Cnt DESC
LIMIT 3
```
>Answer: Dairy Products, appearing in 100 orders  
&nbsp;  
__CategoryID	CategoryName	Cnt__  
4	Dairy Products	100  
1	Beverages	93  
3	Confections	84  
&nbsp;  

6. What was the total cost for each order?
```
SELECT OrderID, SUM(Products.Price) FROM OrderDetails
JOIN Products ON OrderDetails.ProductID == Products.ProductID
GROUP BY OrderID
```
>Answer:  First 5 items of the list (of 196) are shown below  
&nbsp;  
__OrderID	SUM(Products.Price)__
10248	69.8  
10249	76.25  
10250	83.7  
10251	61.55  
10252	117.5  
&nbsp;  


7. Which employee made the most sales (by total price)?
```
SELECT Employees.EmployeeID,
        Employees.LastName,
        AVG(Price) AS MeanSale,
        SUM(Price*Quantity) As TotalSales
FROM Orders
JOIN Employees ON Orders.EmployeeID == Employees.EmployeeID
JOIN OrderDetails ON Orders.OrderID == OrderDetails.OrderID
JOIN Products ON OrderDetails.ProductID = Products.ProductID
GROUP BY Employees.EmployeeID
ORDER BY TotalSales DESC
LIMIT 3
```
>Answer:  Margaret Peacock made the most sales, with a total of 105,696.5 money units (average per order = 31.6)  
&nbsp;  
__EmployeeID	LastName	FirstName	MeanSale	TotalSales__  
4	Peacock	Margaret	31.603	105696.499  
1	Davolio	Nancy	30.688	57690.389  
3	Leverling	Janet	23.862	42838.350  
&nbsp;  

8. Which employees have BS degrees? (*Hint:* look at the [LIKE](http://www.w3schools.com/sql/sql_like.asp) operator.)
```
SELECT LastName, FirstName FROM Employees
WHERE Notes LIKE '%BS%'
```
>Answer:  Janet Leverling has a BS and Steven Buchanan has a BSC (presumably an equivalent, though it would be easy to filter that out)  
&nbsp;  
__LastName	FirstName__  
Leverling	Janet  
Buchanan	Steven  
&nbsp;  

9. Which supplier of three or more products has the highest average product price? (*Hint:* look at the [HAVING](http://www.w3schools.com/sql/sql_having.asp) operator.)
```
SELECT Suppliers.SupplierID, Suppliers.SupplierName,
    COUNT(Products.ProductID) AS ProductCount,
    AVG(Products.Price) AS ProductAvgPrice
FROM Products
JOIN Suppliers ON Products.SupplierID == Suppliers.SupplierID
GROUP BY Suppliers.SupplierID
HAVING ProductCount >= 3
ORDER BY ProductAvgPrice DESC
```
>Answer:  That would be Tokyo Traders; with just three products, their average price is 46.0 monetary units  
&nbsp;  
__SupplierID	SupplierName	ProductCount	ProductAvgPrice__  
4	Tokyo Traders	3	46  
12	Plutzer Lebensmittelgroßmärkte AG	5	 44.678  
7	Pavlova, Ltd.	5	35.57  
&nbsp;  

