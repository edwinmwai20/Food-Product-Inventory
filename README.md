# Food-Product-Inventory
-This is a program that adds to its inventory items needed  from FoodOpenFacts API
-These products are added by first accessing the barcode for a particular product and giving it credential in order to sell
-The products are added to the programs inventory and are able to be seen in View Inventory Option


# MVC Logic

- As a beginner i tried to implement MVC to the program to give it a an organized and manageable look
- We have the Model-The brain of the program:
                        Contains: 
                                 1.Class_file- contains a class with the neccessary attributes
                                 2.Repo = This is my repository file that contains the abstraction for data storage using CRUD(persistence)
- Next we have Controller which for this particular program i have only the route:
                        Contains: 
                                1.route - the routing py(As my Primary Controller)contains the requests needed as a request is sent for from the interface.
                                          That is:
                                                - get_inventory()
                                                - add_item()
                                                - delete_item()
                                2.The Service layer - this is under the folder services with the ser py ad My Helper controller thats helps   grab products from the FoodOpenFacts so as to add them inside my Inventory
                                                                                               
- Lastly we have the View aka what my view my users see:
                        Contains:
                                1.The CLI- this contains the program to how the use will manage the data.It contain A View Inventory option,A add to inventory option, A delete option and an exit option alone


- All this program link together well