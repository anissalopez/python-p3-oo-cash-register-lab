#!/usr/bin/env python3
#class ShoppingCart:
   # def __init__(self, coupon=0):
       # self.coupon = coupon

    #def checkout(self):
       #total = sum([item.price for item in self.shopping_cart()])
       # total -= total * self.coupon / 100
       # return total
#
class CashRegister:
    def __init__(self, discount = 0, total = 0, items = None, last_item = None ):
        self.discount = discount
        self.total = total
        self.items = [] if items is None else items
        self.last_item = 0 if last_item is None else last_item
  

    def add_item(self, title, price, quantity = 1):
        self.last_item = price * quantity 

        for i in range(quantity):
            self.items.append(title)
        self.total = self.total + (price * quantity)
        return self.total
    

    def apply_discount(self):
        if(self.discount > 0):
          self.total -= self.total * self.discount / 100
          print(f"After the discount, the total comes to ${int(self.total)}.")
          return int(self.total)
        else:
           print("There is no discount to apply.")
           return self.total
        
    def void_last_transaction(self):
       self.total = self.total - self.last_item
       return self.total

        


       
        
    
      




        

        
    

