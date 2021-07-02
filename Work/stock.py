class Stock:
 def __init__(self,name,shares,price):
  self.name=name
  self.shares=shares
  self.price=price
  
 def __repr__(self):
   return f'Stock({self.name},{self.shares},{self.price})'
 
 def cost(self):
  return self.shares*self.price
 
 def sell(self,nshares):
  self.shares-=nshares
  
class MyStock(Stock):
 def __init__(self,name,shares,price,factor):
  super().__init__(name,shares,price)
  self.factor=factor
 def panic(self):
  self.sell(self.shares)
 def cost(self):
  return super().cost()* self.factor
  
  
s=MyStock(name='GOOG',shares=100,price=490.1,factor=1.25)
s.sell(35)
print(s.shares)
print(s.shares)
print(s.cost())