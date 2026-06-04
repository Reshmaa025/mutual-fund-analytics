-- Best performing mutual fund
SELECT scheme_name,
       MAX(nav) AS max_nav
FROM nav_history
GROUP BY scheme_name;
SELECT scheme_name,
       AVG(nav) AS avg_nav
FROM nav_history
GROUP BY scheme_name;
SELECT scheme_name,
       MAX(date) AS latest_date,
       nav
FROM nav_history
GROUP BY scheme_name, nav;
SELECT scheme_name,
       (MAX(nav) - MIN(nav)) AS growth
FROM nav_history
GROUP BY scheme_name
ORDER BY growth DESC;
SELECT scheme_name,
       STDDEV(nav) AS volatility
FROM nav_history
GROUP BY scheme_name;