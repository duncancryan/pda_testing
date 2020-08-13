### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.
# There are 6 errors in total. 

```python

class CardGame:
# no __init__ function?

  def checkforAce(self, card): # poor naming of function should be check_for_ace
    if card.value = 1: # use of = instead of ==
      return true # should be capitalised if intended to be a BOOL, otherwise should be a string?
    else # missing colon
      return false # should be capitalised if intended to be a BOOL, otherwise should be a string?

  dif highest_card(self, card1 card2) # missing comma and colon AND should be def not dif
    if card1.value > card2.value # missing colon
      return card # incorrect variable, should be card1
    else # missing colon
      return card2
 

 def cards_total(cards): # should have self as first paramater if method being defined in class, indentation wrong
   total # undefined variable
   for card in cards:
     total += card.value # will not work due to above issue
     return "You have a total of" + total # can not add a string and an int


```
