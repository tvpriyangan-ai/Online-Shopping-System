# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 00:59:25 2026

@author: Priyangan
"""
from Lab11_library import ShoppingAccount
user1=ShoppingAccount(301,500,0)
user2=ShoppingAccount(302,500,0)
user_details=[user1,user2]

for user in user_details:
    user.add_to_cart(100)
    
for user in user_details:
    user.remove_from_cart(20)
    
for user in user_details:
    user.checkout()
    
for user in user_details:
    print(user.get_user(), user.get_wallet())
    
user1.transfer_money(50, user2)

for user in user_details:
    print(user.get_user(), user.get_wallet())

