class TableFormatter:
 def headings(self,headers):
  raise NotImplementedError()
 
 def row(self,headers):
  raise NotImplementedError()
 
class TextTableFormatter(TableFormatter):
 '''
    Emit a table in plain-text format
 '''
 def headings(self,headers):
  for h in headers:
   print(f'{h:>10s}',end='')
  print()
  print((('-')*10+" ")*len(headers))
   
 def row(self,rowdata):
  for d in rowdata:
   print(f'{d:>10s}',end='')
  print()
  
 
class CSVTableFormatter(TableFormatter):
 '''
 Output portfolio data in csv format
 
 '''
 def headings(self,headers):
  print(','.join(headers))
  
 def row(self,rowdata):
  print(','.join(rowdata))
  
class HTMLTableFormatter(TableFormatter):
 '''
 Output portfolio data in HTML format
 
 '''
 def headings(self,headers):
  print('<tr><th>'+'</th><th>'.join(headers)+'</th></tr>')
  
 def row(self,rowdata):
  print('<tr><td>'+'</td><td>'.join(rowdata)+'</td></tr>')

def create_formatter(fmt):
  if fmt=='txt':
        formatter=TextTableFormatter()
  elif fmt=='csv':
        formatter=CSVTableFormatter()
  elif fmt=='html':
        formatter=HTMLTableFormatter()
  else:
        raise RuntimeError(f'Unknown format {fmt}')
  return formatter