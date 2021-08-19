PRINT 'AU - ADD NEW COMPONENT (Topping)'
PRINT '-- Plant-Based Chicken'
GO
  
USE OnlineOrdering_Admin
GO
  
DECLARE @countryCode        NCHAR(2)            = 'key_countryCode'
DECLARE @componentCode      NVARCHAR(15)        = 'key_componentCode'
DECLARE @componentTypeCode  NVARCHAR(100)       = 'key_componentTypeCode'
DECLARE @componentGroups    NVARCHAR(100)       = 'key_componentGroups'
DECLARE @componentName      NVARCHAR(100)       = 'key_componentName'
DECLARE @posSystemCode      NVARCHAR(15)        = 'key_componentCode'
DECLARE @makeOrder          INT                 = 'key_makeOrder'
DECLARE @crustShape         NVARCHAR(15)        =  key_CrustShape
DECLARE @releaseDate        DATETIME            =  GETDATE()  
DECLARE @crustPosFlavorCode NVARCHAR(8)         =  key_crustPosFlavorCode       
DECLARE @productClassCode   NVARCHAR(100)      
DECLARE @startDate          DATE                =  GETDATE()
  
--Create Component price model
--Price : $2.49
  
DECLARE @componentPriceModelCode    NVARCHAR(50)    = 'key_componentPriceModelCode'
DECLARE @name                       NVARCHAR(255)   = 'key_name'
DECLARE @allowCustomPrice           INT             = key_allowCustomPrice
DECLARE @displayOrder               INT             = key_displayOrder
DECLARE @surchargeCode              NVARCHAR(50)    = 'key_surchargeCode'
DECLARE @price                      MONEY           = key_price
DECLARE @endDate                    DATE            = key_endDate
BEGIN TRANSACTION
  
------Add New Component---------
    EXECUTE [content].[AddComponent]
       @countryCode
      ,@componentCode
      ,@componentTypeCode
      ,@componentGroups
      ,@componentName
      ,@posSystemCode
      ,@makeOrder
      ,@crustShape
      ,@startDate
      ,@crustPosFlavorCode
  
  
---- Create New PriceModel-------
    EXECUTE [content].[AddComponentPriceModel]
        @countryCode
        ,@componentPriceModelCode
        ,@name
        ,@allowCustomPrice
        ,@displayOrder
        ,@startDate
        ,@endDate
        ,@price
        ,@surchargeCode
  
  
SET @productClassCode = 'Class.Pizza'
    EXECUTE [content].[AddComponentPriceModelComponent]
       @countryCode
      ,@componentPriceModelCode
      ,@productClassCode
      ,@componentCode
      ,'Pizza.Large'
      ,@startDate
  
    EXECUTE [content].[AddComponentPriceModelComponent]
       @countryCode
      ,@componentPriceModelCode
      ,@productClassCode
      ,@componentCode
      ,'Pizza.ExtraLarge'
      ,@startDate
  
    EXECUTE [content].[AddProductClassValidComponent]
        @countryCode
        ,@productClassCode
        ,'Pizza.Large'
        ,@componentCode
        ,@startDate
        ,NULL
  
    EXECUTE [content].[AddProductClassValidComponent]
        @countryCode
        ,@productClassCode
        ,'Pizza.ExtraLarge'
        ,@componentCode
        ,@startDate
        ,NULL
  
  
     SET @productClassCode = 'Class.Pizza.Designa'
  
    EXECUTE [content].[AddComponentPriceModelComponent]
       @countryCode
      ,@componentPriceModelCode
      ,@productClassCode
      ,@componentCode
      ,'Pizza.Large'
      ,@startDate
  
    EXECUTE [content].[AddComponentPriceModelComponent]
       @countryCode
      ,@componentPriceModelCode
      ,@productClassCode
      ,@componentCode
      ,'Pizza.ExtraLarge'
      ,@startDate
  
    EXECUTE [content].[AddProductClassValidComponent]
       @countryCode
      ,@productClassCode
      ,'Pizza.Large'
      ,@componentCode
      ,@startDate
      ,NULL
  
       
    EXECUTE [content].[AddProductClassValidComponent]
       @countryCode
      ,@productClassCode
      ,'Pizza.ExtraLarge'
      ,@componentCode
      ,@startDate
      ,NULL
  
  
        
   SET @productClassCode = 'Class.Pizza.Traditional.PhillyCheese'
  
    EXECUTE [content].[AddComponentPriceModelComponent]
       @countryCode
      ,@componentPriceModelCode
      ,@productClassCode
      ,@componentCode
      ,'Pizza.Large'
      ,@startDate
  
    EXECUTE [content].[AddComponentPriceModelComponent]
       @countryCode
      ,@componentPriceModelCode
      ,@productClassCode
      ,@componentCode
      ,'Pizza.ExtraLarge'
      ,@startDate
  
    EXECUTE [content].[AddProductClassValidComponent]
       @countryCode
      ,@productClassCode
      ,'Pizza.Large'
      ,@componentCode
      ,@startDate
  
      
    EXECUTE [content].[AddProductClassValidComponent]
       @countryCode
      ,@productClassCode
      ,'Pizza.ExtraLarge'
      ,@componentCode
      ,@startDate
  
   
      
--ROLLBACK TRANSACTION
COMMIT TRANSACTION