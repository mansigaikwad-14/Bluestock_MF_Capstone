-- Query 1: Total number of mutual fund schemes
SELECT COUNT(*) AS total_schemes
FROM cleaned_01_fund_master;

-- Query 2: Total number of fund houses
SELECT COUNT(DISTINCT fund_house) AS total_fund_houses
FROM cleaned_01_fund_master;

-- Query 3: Top 5 fund houses by AUM
SELECT *
FROM cleaned_03_aum_by_fund_house
ORDER BY aum DESC
LIMIT 5;

-- Query 4: Average NAV by scheme
SELECT amfi_code,
AVG(nav) AS average_nav
FROM cleaned_02_nav_history
GROUP BY amfi_code;

-- Query 5: Total SIP inflows
SELECT SUM(amount) AS total_sip_inflow
FROM cleaned_04_monthly_sip_inflows;

-- Query 6: Total investor transactions
SELECT COUNT(*) AS total_transactions
FROM cleaned_08_investor_transactions;

-- Query 7: Category-wise scheme count
SELECT category,
COUNT(*) AS scheme_count
FROM cleaned_01_fund_master
GROUP BY category;

-- Query 8: Highest expense ratio funds
SELECT *
FROM cleaned_07_scheme_performance
ORDER BY expense_ratio DESC
LIMIT 5;

-- Query 9: Total portfolio holdings
SELECT COUNT(*) AS total_holdings
FROM cleaned_09_portfolio_holdings;

-- Query 10: Benchmark index records
SELECT COUNT(*) AS benchmark_records
FROM cleaned_10_benchmark_indices;