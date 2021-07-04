import time
def timethis(func):
 def wrapper(*arg,**kwargs):
  start=time.time()
  func(*arg,**kwargs)
  end=time.time()
  print('%s.%s:%f' %(func.__module__,func.__name__,end-start))
  return func(*arg,**kwargs)
 return wrapper