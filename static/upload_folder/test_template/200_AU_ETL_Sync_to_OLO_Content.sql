USE [OnlineOrdering_Content]
  
DECLARE @NOW DATETIME = GETDATE()
   
EXECUTE [OnlineOrdering_Content].[etl].[SyncToOLOContent_Product] @NOW
   
EXECUTE [OnlineOrdering_Content].[etl].[SyncToOLOContent_ProductRecipe] @NOW