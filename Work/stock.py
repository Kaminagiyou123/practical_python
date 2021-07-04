from typedproperty import String,Integer,Float

class Stock:
 name=String('name')
 shares=Integer('shares')
 price=Float('price')
 
 def __init__(self,name,shares,price):
  self.name=name
  self.shares=shares
  self.price=price
  
 @property
 def shares(self):
   return self._shares
 
 @shares.setter
 def shares(self,shares):
   if  not isinstance (shares,int):
     raise TypeError('Expected int')
   self._shares=shares
  
 def __repr__(self):
   return f'Stock({self.name},{self.shares},{self.price})'
 @property
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
  
 @property
 def cost(self):
  return super().cost()* self.factor
  
s=Stock(name='GOOG',shares=100,price=490.1)
