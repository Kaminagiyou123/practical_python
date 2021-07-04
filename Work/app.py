import logging
import report
logging.getLogger('fileparse').level=logging.DEBUG
a=report.read_portfolio('Work/Data/missing.csv')