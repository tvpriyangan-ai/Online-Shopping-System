# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 00:58:53 2026

@author: Priyangan
"""

class ShoppingAccount:
    def __init__(self, user_id, wallet_balance, cart_total):
        self.__user_id = user_id
        self.__wallet_balance = wallet_balance
        self.__cart_total = cart_total
        
    def get_user(self):
        return self.__user_id
    def get_wallet(self):
        return self.__wallet_balance
    def get_cart(self):
        return self.__cart_total
    
    def add_to_cart(self,amount):
        if amount>0:
            self.__cart_total+=amount
        else:
            print("Invalid Amount")
    def remove_from_cart(self, amount):
        if amount>0 and self.__cart_total>=amount:
            self.__cart_total-=amount
        else:
            print("Invalid Amount")
            
    def add_money(self,amount):
        if amount>0:
            self.__wallet_balance+=amount
        else:
            print("Invalid Activity")
            
    def checkout(self):
        if self.__wallet_balance>=self.__cart_total:
            self.__wallet_balance -=self.__cart_total
            self.__cart_total=0
        else:
            print("Invalid Activity")  
            
    def transfer_money(self,amount,acc):
        if self.__wallet_balance>=amount:
            self.__wallet_balance-=amount
            acc.add_money(amount)
        else:
            print("Invalid Activity")
            
            
            
            
            
        
        