import random
import time
from PIL import Image

class IceCreamOrder:
#Constructor
    def __init__(self):
        #The order number
        self.orderNum = 1
        #The number of scoops in the order, which can be 1, 2, or 3 scoops
        #Defaulting as 1, but will randomly generated for each order
        self.scoops = 1
        
        #Options at the Ice Cream Parlor
        self.listOfFlavors = ["Vanilla", "Chocolate", "Strawberry"]
        self.listOfToppings = ["Sprinkles", "Chocolate Chips", "Cherry", "No Topping"]
        self.listOfConesAndCup = ["Waffle Cone", "Cake Cone", "Cup"]
        
        #Default Order
        self.orderFlavors = [None]*3
        self.orderToppings = [None]*3
        self.orderContainer = ""
        
        #Images of Ice Cream Scoops
        self.scoopImages = [None]*3
        
        #Image of Ice Cream Final
        self.iceCream = None
        
#Method: Get the randomly generated ice cream order
    def takeOrder(self):
        #Get the number of scoops
        self.scoops = random.randrange(1,4)
        #Get what the ice cream is put in
        self.orderContainer = random.choice(self.listOfConesAndCup)
        #Get each scoop of ice cream and its topping
        for x in range(3):
            #Will always get at least one scoop of ice cream
            self.orderFlavors[x] = random.choice(self.listOfFlavors)
            self.orderToppings[x] = random.choice(self.listOfToppings)
            #A cherry can only go on the top scoop (when x = 0)
            while x != 0:
                if self.orderToppings[x] == "Cherry":
                    self.orderToppings[x] = random.choice(self.listOfToppings)
                else:
                    break
            #Stop when the predetermined number of scoops are generated
            if x == self.scoops - 1:
                break

#Method: Print the order
    def printOrder(self):
        #Instructions on how the ice cream scoops are stacked
        if self.orderNum == 1:
            print('Scoops are listed from top to bottom. Ex. Scoop 1 is the TOP scoop.\n')
        else:
            #Wait for 5 seconds between orders
            print('\nTaking the next order...\n')
            time.sleep(5)
        #Print top of the order
        #Includes: orderNum, number of scoops, and what the ice cream will be put in
        if self.scoops == 1:
            print(
                f'Order #{self.orderNum}: {self.scoops} scoop in a {self.orderContainer.upper()} ↓'
            )
        else:
            print(f'Order #{self.orderNum}: {self.scoops} scoops in a {self.orderContainer.upper()} ↓')
        #For each scoop, print the ice cream flavor and the topping ('No Topping' if no topping)
        print('#. Flavor \t    \t Topping')
        #Get the order and print it
        for x in range(self.scoops):
            #An iteration loop to print the order
            if self.orderToppings[x] == "Cherry":
                print(f'{x + 1}. {self.orderFlavors[x]} \twith\t a {self.orderToppings[x]}')
            else: 
                print(f'{x + 1}. {self.orderFlavors[x]} \twith\t {self.orderToppings[x]}')
            #Exit the for loop when the requested number of scoops are created
            #x is (0,3) and scoops can be (1,4), 
            #so scoops - 1 can be used to check if it is equal to x
            #if x == self.scoops - 1:
                #Increase orderNum 
                #self.orderNum += 1
                #break
                
#Method: Create the images for the ice cream scoops
    def scoopImage(self):
        for x in range(self.scoops):
            flavorImg = f'{self.orderFlavors[x]}.png'
            print(flavorImg)
            toppingImg = f'{self.orderToppings[x]}.png'
            if self.orderToppings[x] != 'No Topping':
                print(toppingImg)
            layer1 = Image.open(flavorImg)
            if toppingImg in ['No Topping.png', 'Cherry.png']:
                final2 = layer1
            else:
                layer2 = Image.open(toppingImg)

                #Compositing image using Image.paste
                final1 = Image.new("RGBA", layer1.size)
                final1.paste(layer1, (0,0), layer1)
                final1.paste(layer2, (0,0), layer2)

                #Compositing image using Image.alpha_composite
                final2 = Image.new("RGBA", layer1.size)
                final2 = Image.alpha_composite(final2, layer1)
                final2 = Image.alpha_composite(final2, layer2)
            self.scoopImages[x] = final2
            self.scoopImages[x].show()

#Method
    #def finalOrder(self):
        
        
        #return 