import report
portfolio=report.read_portfolio('Work/Data/portfolio.csv')
from tableformat import create_formatter,print_table
formatter=create_formatter('txt')
print_table(portfolio,['name','shares'],formatter)
 
 