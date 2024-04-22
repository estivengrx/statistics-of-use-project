SELECT ROUND(AVG([SumTotalUsage]), 1) AS AverageUsageMinutesThroughDevices
FROM (
    SELECT [date], SUM([total_usage]) AS [SumTotalUsage]
    FROM (
        SELECT [date], [total_usage]
        FROM [statistics_of_use_db].[dbo].[app_usage_time_motorola]

        UNION ALL

        SELECT [date], [total_usage]
        FROM [statistics_of_use_db].[dbo].[web_usage_time_edge]
    ) AS CombinedData
    GROUP BY [date]
) AS AggregatedData;


SELECT ROUND(AVG([total_usage]), 1) AS [AverageTotalUsagePhone]
FROM [statistics_of_use_db].[dbo].[app_usage_time_motorola];

SELECT TOP(5)
    [date] AS [Date],
    [total_usage] AS [UsageTimeInHours],
	DATENAME(WEEKDAY, [date]) AS [DayOfTheWeek]
FROM [statistics_of_use_db].[dbo].[app_usage_time_motorola] AS AggregatedData
ORDER BY [total_usage] DESC;