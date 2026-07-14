CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET n=n-1;
  RETURN (
      # Write your MySQL query statement below.
    select distinct salary
    from Employee
    order by salary desc
    limit 1 offset n
  );
END

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna