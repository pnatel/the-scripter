/* 
In the below template, we are adding this component to 
4 addition sets('Pizzas','Designa Pizzas','Plant-Based','Pizzas PCS'),
you may need to add or remove lines if your component needs to be added
to more or less sets:
*/

USE OnlineOrdering_Admin
GO
  
----------------------------************************ TEST TO DETERMINE WHICH SwapAdditionSetCodes EXIST FOR OUR TARGET COUNTRY *********************************
   
--USE OnlineOrdering_Content
--GO
  
--SELECT
--    *
--FROM [product].[SwapAdditionSetComponent] (nolock)
--WHERE
--      [CountryCode] = 'au'
--      AND [SwapAdditionSetCode] IN
--            (
--                  SELECT
--                        [SwapAdditionSetCode]
--                  FROM [product].[SwapModelRules]
--                  WHERE
--                        [CountryCode] = 'au'
--                        AND [SwapAdditionSetType] = 'Topping'
--            )
  
   
  
DECLARE @countryCode NCHAR(2) = 'key_countryCode'
DECLARE @componentCode NVARCHAR(15)
DECLARE @swapAdditionSetCode nvarchar(50)
DECLARE @user nvarchar(255) = system_user
DECLARE @rowReport              NVARCHAR(10)
  
    SET @componentCode =  'key_componentCode'
    SET @swapAdditionSetCode = 'Pizzas'
      
    EXECUTE [OnlineOrdering_Content].[admin].[SwapAdditionSetCode]
       @countryCode
      ,@swapAdditionSetCode
      ,@componentCode
      ,@user
  
        SET @rowReport = @@ROWCOUNT
  
        IF(@rowReport) > 0
        BEGIN
            PRINT ''
            PRINT '*** ComponentCode (' + @componentCode + ') added to SwapAdditionSet (' + @swapAdditionSetCode + ') for Country (' + @countryCode + ').'
        END
  
  
    SET @swapAdditionSetCode = 'Designa Pizzas'
    EXECUTE [OnlineOrdering_Content].[admin].[SwapAdditionSetCode]
       @countryCode
      ,@swapAdditionSetCode
      ,@componentCode
      ,@user
  
        SET @rowReport = @@ROWCOUNT
  
        IF(@rowReport) > 0
        BEGIN
            PRINT ''
            PRINT '*** ComponentCode (' + @componentCode + ') added to SwapAdditionSet (' + @swapAdditionSetCode + ') for Country (' + @countryCode + ').'
        END
  
  
  
    SET @swapAdditionSetCode = 'Pizzas PCS'  --PhillyCheeseSteak Pizzas
    EXECUTE [OnlineOrdering_Content].[admin].[SwapAdditionSetCode]
       @countryCode
      ,@swapAdditionSetCode
      ,@componentCode
      ,@user
  
        SET @rowReport = @@ROWCOUNT
  
        IF(@rowReport) > 0
        BEGIN
            PRINT ''
            PRINT '*** ComponentCode (' + @componentCode + ') added to SwapAdditionSet (' + @swapAdditionSetCode + ') for Country (' + @countryCode + ').'
        END
  
    SET @swapAdditionSetCode = 'IndiPizzas'  --India Range Pizzas
    EXECUTE [OnlineOrdering_Content].[admin].[SwapAdditionSetCode]
       @countryCode
      ,@swapAdditionSetCode
      ,@componentCode
      ,@user
  
        SET @rowReport = @@ROWCOUNT
  
        IF(@rowReport) > 0
        BEGIN
            PRINT ''
            PRINT '*** ComponentCode (' + @componentCode + ') added to SwapAdditionSet (' + @swapAdditionSetCode + ') for Country (' + @countryCode + ').'
        END
  
  
    SET @swapAdditionSetCode = 'Plant-Based' 
    EXECUTE [OnlineOrdering_Content].[admin].[SwapAdditionSetCode]
       @countryCode
      ,@swapAdditionSetCode
      ,@componentCode
      ,@user
  
        SET @rowReport = @@ROWCOUNT
  
        IF(@rowReport) > 0
        BEGIN
            PRINT ''
            PRINT '*** ComponentCode (' + @componentCode + ') added to SwapAdditionSet (' + @swapAdditionSetCode + ') for Country (' + @countryCode + ').'
        END