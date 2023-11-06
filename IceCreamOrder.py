import random
from sys import displayhook
import time
from PIL import Image

class IceCreamOrder:
#Constructor
    def __init__(self):
        #The order number
        self.orderNum   = 1
        
        #The number of scoops in the order, which can be 1, 2, or 3 scoops
        #Defaulting as 1, but will randomly generated for each order
        self.scoopNum     = 1
        
        #Default Order
        self.orderFlavors   = [None]*3
        self.orderToppings  = [None]*3
        self.orderContainer = ""
        
        #Images of Ice Cream Scoops
        self.scoopImages = [None]*3
        
        #Image of Ice Cream Final
        self.iceCreamOrder    = None
        
#Method: Get the randomly generated ice cream order
    def takeOrder(self):
        
        #Options at the Ice Cream Parlor
        listOfFlavors      = ["Vanilla", "Chocolate", "Strawberry"]
        listOfToppings     = ["Sprinkles", "Chocolate Chips", "Cherry", "No Topping"]
        listOfConesAndCup  = ["Waffle Cone", "Cake Cone", "Cup"]
        #Get the number of scoops
        self.scoopNum = random.randrange(1,4)
        #Get what the ice cream is put in
        self.orderContainer = random.choice(listOfConesAndCup)
        #Get each scoop of ice cream and its topping
        for x in range(self.scoopNum):
            #Will always get at least one scoop of ice cream
            self.orderFlavors[x]    = random.choice(listOfFlavors)
            self.orderToppings[x]   = random.choice(listOfToppings)
            #A cherry can only go on the top scoop (when x = 0)
            while x != 0:
                if self.orderToppings[x] == "Cherry":
                    self.orderToppings[x] = random.choice(listOfToppings)
                else:
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
        if self.scoopNum == 1:
            print(
                f'Order #{self.orderNum}: {self.scoopNum} scoop in a {self.orderContainer.upper()} ↓'
            )
        else:
            print(f'Order #{self.orderNum}: {self.scoopNum} scoops in a {self.orderContainer.upper()} ↓')
        #For each scoop, print the ice cream flavor and the topping ('No Topping' if no topping)
        print('#. Flavor \t    \t Topping')
        #Get the order and print it
        for x in range(self.scoopNum):
            #An iteration loop to print the order
            if self.orderToppings[x] == "Cherry":
                print(f'{x + 1}. {self.orderFlavors[x]} \twith\t a {self.orderToppings[x]}')
            else: 
                print(f'{x + 1}. {self.orderFlavors[x]} \twith\t {self.orderToppings[x]}')
        #Increase orderNum 
        self.orderNum += 1
                
#Method: Create the images for the ice cream scoops
    def scoopImage(self):
        for x in range(self.scoopNum):
            #Get the name of the .png image file for
            #the flavor and topping of scoop x
            flavorImg   = f'{self.orderFlavors[x]}.png'
            toppingImg  = f'{self.orderToppings[x]}.png'
            
            #Get the image for the ice cream
            iceCreamLayer = Image.open(flavorImg)
            #The cherry will be added elsewhere, so leave as is
            if toppingImg in ['No Topping.png', 'Cherry.png']:
                finalScoop = iceCreamLayer
            #Add the topping
            else:
                #Get the image for the topping
                toppingLayer = Image.open(toppingImg)

                #Get the composite image with the topping on the ice cream
                #using Image.alpha_composite
                finalScoop = Image.new("RGBA", iceCreamLayer.size)
                finalScoop = Image.alpha_composite(finalScoop, iceCreamLayer)
                finalScoop = Image.alpha_composite(finalScoop, toppingLayer)
            self.scoopImages[x] = finalScoop
            #displayhook(self.scoopImages[x])

#Method: Get an image with the stacked scoops of ice cream from the provided images
    def getStackScoops(self, iceCreamScoops, addToStack):
        # Open Front Image 
        addToStack = addToStack 
        # Open Background Image 
        iceCreamScoops = iceCreamScoops
        # Convert image to RGBA 
        addToStack = addToStack.convert("RGBA") 
        # Convert image to RGBA 
        iceCreamScoops = iceCreamScoops.convert("RGBA") 
        # Calculate width to be at the center
        #All scoops are the same size 
        width = 0
        # Calculate height to be at the center 
        height = (addToStack.height)// 2
        scoopStack = Image.new('RGB', (iceCreamScoops.width, iceCreamScoops.height + height))
        # Paste the frontImage at (width, height)
        scoopStack.paste(iceCreamScoops, (0, scoopStack.height-iceCreamScoops.height), iceCreamScoops) 
        scoopStack.paste(addToStack,(width,0), addToStack)
        return scoopStack
    
#Method: Add the cherry on top of the image, and return the image
    def addCherry(self, scoopStack):
        #Open Front Image 
        cherry = Image.open("Cherry.png") 
        #Open Background Image 
        iceCreamScoops = scoopStack
        #Convert image to RGBA 
        cherry = cherry.convert("RGBA") 
        #Convert image to RGBA 
        iceCreamScoops = iceCreamScoops.convert("RGBA") 
        #Calculate width to be at the center 
        #Had to adjust since the stem of the cherry moves it over some
        width = (iceCreamScoops.width - cherry.width) // 2 + 20
        #Calculate height of cherry 
        height = cherry.height-iceCreamScoops.height // 8
        stack = Image.new('RGB', (iceCreamScoops.width, iceCreamScoops.height + height))
        #Paste the ice cream scoops
        stack.paste(iceCreamScoops, (0, stack.height-iceCreamScoops.height), iceCreamScoops)
        #Paste the cherry 
        stack.paste(cherry,(width,0), cherry)
        return stack

#Method: Add the container to an image with the stacked scoops of ice cream
    def addStackContainer(self, scoopStack):
        #Container Image 
        containerFileName = f'{self.orderContainer}.png'
        # Open Front Image 
        iceCreamContainer = Image.open(containerFileName)
        # Open Background Image 
        scoopStack = scoopStack 
        # Convert image to RGBA 
        iceCreamContainer = iceCreamContainer.convert("RGBA") 
        # Convert image to RGBA 
        scoopStack = scoopStack.convert("RGBA") 
        # Calculate width to be at the center 
        width   = (iceCreamContainer.width - scoopStack.width) // 2
        # Calculate height so ice cream is in the container 
        height  = scoopStack.height-100
        order   = Image.new('RGB', (iceCreamContainer.width, iceCreamContainer.height + height))
        # Paste the frontImage at (width, height) 
        order.paste(scoopStack,(width,0), scoopStack)
        order.paste(iceCreamContainer, (0, order.height-iceCreamContainer.height), iceCreamContainer)
        return order 

#Method: Get the image for the final order
    def getFinalOrder(self):
        self.scoopImage()
        y = self.scoopNum
        #Set the default as 1 scoop
        stack = self.scoopImages[y-1]
        #Only combine scoops if there are more than one scoop in the order
        while y != 1: 
            #Get the image for bottom 2 scoops
            stack = self.getStackScoops(stack, self.scoopImages[y-2])
            #Decrease by 1 so that the next loop will get the 
            #stacked scoops image with the third scoop added
            y -= 1
        #Check if a cherry is on top
        if self.orderToppings[0]  == "Cherry":
            stack = self.addCherry(stack)
        self.iceCreamOrder = self.addStackContainer(stack)
        # Save this image 
        self.iceCreamOrder.save("order.png", format="png")
