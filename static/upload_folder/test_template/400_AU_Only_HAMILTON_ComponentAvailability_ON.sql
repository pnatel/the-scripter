/*
 Limit the component availability to Hamilton QLD store only. 
This is done for pre-release so that Marketing can enable the 
component on production for testing/ research purposes without
it being available nation wide. 
*/

USE [OnlineOrdering_Management]
GO
​
DECLARE @countryCode                NCHAR(2)     =  'AU'
DECLARE @componentCode              NVARCHAR(15) =  'key_componentCode'
DECLARE @status                     NCHAR(3)     =  'OFF'
DECLARE @storeNo                    INT          =  98415 --Hamilton Store Number
​
​
BEGIN TRANSACTION
​
 DECLARE @Store  TABLE
    ([Storeno]      INT
    ,[Processed]    BIT DEFAULT 0)
  
        INSERT INTO @Store  ([StoreNo])
        SELECT StoreNo FROM OnlineOrdering_Store.dbo.[store]
            WHERE Countrycode = @countryCode
            AND IsClosed <> 1
            AND OnlineOrderingEnabled  = 1
            AND IsPulseStore = 1
            AND StoreNo <> @storeNo -- HAMILTON
        ORDER BY StoreNo DESC
   
  
        BEGIN
            WHILE (SELECT COUNT(*) FROM @store WHERE [Processed] = 0) > 0
                BEGIN
                    SET @storeNo = (SELECT TOP 1 StoreNo FROM @Store WHERE [Processed] = 0)
      
                        EXECUTE [content].[SetComponentAvailability]
                            @storeNo = @storeNo,
                            @componentCode = @componentCode,
                            @status = @status
                   
                    UPDATE @Store SET [Processed] = 1   WHERE [Storeno] = @storeNo
                END
        END
           
--ROLLBACK TRANSACTION                        
COMMIT TRANSACTION