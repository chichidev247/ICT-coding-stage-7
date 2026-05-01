# Let's bake!
import time
print ("Welcome to our bakery named 'In the corner'!")
time.sleep(2)
print ("Today, we will teach you how to make a banana cake!")
print ("There are some ingredients that we need, some is not related: banana, watermelon, flour, credit card, butter, sugar, a pig, egg, milk, Harry Potter series.")
time.sleep(6)
print ("Every ingredients is a number in order, for example: banana is 1, watermelon is 2, flour is 3,...")
time.sleep(5)
ingre = input("Now write the number of ingredients we need in order (e.g:12345)! ")
if ingre == "135689":
    print ("Congratulation! Your answer is correct!")
else:
    print ("Ops! You are wrong! It should be 135689")
time.sleep(3)
print ("You will need 3 - 4 bananas, 200g flour, 100g sugar, 200ml milk, 1 - 2 eggs and some butter.")
time.sleep(5)
print("These are the steps, however, not in the right order:")
print("1. Bake or steam for about 30 minutes.")
print("2. Pour into a greased pan.")
print("3. Mix with eggs, sugar, and milk.")
print("4. Add flour and stir well.")
print("5. Mash ripe bananas.")
time.sleep(4)
steps = input("Now put these step in the right order (e.g:14253)! ")
if steps == "53421":
    print ("WOW! You are a masterpiece!")
else:
    print ("Oh no! Wrong! It should be 53421!")
time.sleep(4)
print("That is how to make banana cake! Enjoy your own hand - made cake!")
print("Thank you for stopping by!")
