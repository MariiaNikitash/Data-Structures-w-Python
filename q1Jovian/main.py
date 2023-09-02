#QUESTION 1: Alice has some cards with numbers written on them. She arranges the cards in decreasing order, 
#and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a
#given number by turning over as few cards as possible. Write a function to help Bob locate the card.


#1 Create a variable position with the value 0.
#2 Check whether the number at index position in card equals query.
#3 If it does, position is the answer and can be returned from the function
#4 If not, increment the value of position by 1, and repeat steps 2 to 5 till we reach the last position.
#5 If the number was not found, return -1.

def locate_cards(cards, querry):
    position = 0

    while True:
# Check if element at the current position matche the query
        if cards[position] == querry:
# Answer found! Return and exit..           
            return position
# Increment the position if cards[position] == querry. Repeat the loop
        position += 1

        # Check if we have reached the end of the array
        if position == len(cards):
            # Number not found, return -1
            return -1
        
[]