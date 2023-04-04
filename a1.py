"""
Name: Malvika Gohil 
Student Number: 501178814

Program Description:As university student living at home commuting is something
                    that I do not look forward to each day so I made this program
                    to calculate the about of money a student would have to earn/save
                    in order to be able to move out after first year.
                    


"""



def Toronto_calc():
    """
    This function dteremines the cost of living in toronto with and without a 
    roommate 

    """
    #creating a roommate variable to store the choice of the user 
    roommate = input("\nWould you like to share the space with a roommate?\n")
    
   
    #calculating the cost of they choose to stay with a roommate
    if roommate == 'yes' or roommate == 'Yes':
        #general print statement 
            print("\nThe current rent prices in Toronto averages "
                  "out to about $2200 a month. Considering you are" 
                  " chosing to split with a roomate your rent would"
                  " be about $1100 a month.")
     #calculating how many more hours the student has to work 
            more_hours = ((((1100+ monthly_exp)*12)/hourly_wage)/12)
            
            print("\nAccording to your expenses and the rent you would " 
                  "have to work "+ str(round(more_hours)) + " hours a month for a whole year" 
                  " in order to afford the living expenses for a year in Toronto.")
    #if the user choses to live without a roommate        
    else:
        print("\nThe current rent prices in Toronto area averages out to about $2200 a month.")
        #calculating the amount of hours they would have to work 
        more_hours = ((((2200 + monthly_exp)*12)/hourly_wage)/12)
        
        #printitng the result 
        print("\nAccording to your expenses and the rent you would" 
              " have to work "+ str(round(more_hours)) + " hours a month for a whole year" 
              " in order to afford the living expenses for a year in Toronto.")
      
    

def Vancouver_calc():
    """
    
    This function dteremines the cost of living in Vancouver with and without a 
    roommate 

    """
    #creating a roommate variable to store the choice of the user
    roommate = input("\nWould you like to share the space with a roommate?\n")
    
   #calculating the cost of they choose to stay with a roommate
    if roommate.lower() == "yes":
            print("\nThe current rent prices in Vancouver averages "
                  "out to about $2600 a month. Considering you are " 
                  "chosing to split with a roomate your rent would "
                  "be about $1300 a month.")
            #calculating how many more hours the student has to work 
            more_hours = ((((1300+ monthly_exp)*12)/hourly_wage)/12)
            
            print("\nAccording to your expenses and the rent you would " 
                  "have to work"+ str(round(more_hours)) + " hours a month for a whole year " 
                  "in order to afford the living expenses for a year in Vancouver.")
    else: 
        print("\nThe current rent prices in Vancouver averages out to about $2600 a month.")
        #calculating how many more hours the student has to work 
        more_hours = ((((2600 + monthly_exp)*12)/hourly_wage)/12)
        
        #printitng the result 
        print(" According to your expenses and the rent you would" 
              " have to work"+ str(round(more_hours)) + " hours a month for a whole year" 
              " in order to afford the living expenses for a year in Vancouver.")
        
def  Newyork_calc():
    """
    
    
    This function dteremines the cost of living in New York with and without a 
    roommate 

    """
    #creating a roommate variable to store the choice of the user
    roommate = input("\nWould you like to share the space with a roommate?\n")
    
   #if the user choses to have a roommate
    if roommate == 'yes' or roommate == 'Yes':
            print("\nThe current rent prices in New York averages"
                  " out to about $3800 a month. Considering you are" 
                  " chosing to split with a roomate your rent would"
                  " be about $1900 a month.")
            #calculating how many more hours the student has to work 
            more_hours = ((((1900+ monthly_exp)*12)/hourly_wage)/12)
            
            #printitng the result
            print("\nAccording to your expenses and the rent you would" 
                  " have to work"+ str(round(more_hours)) + " hours a month for a whole year" 
                  " in order to afford the living expenses for a year in New York.")
    else: 
        
        print("\nThe current rent prices in New York averages"
              " out to about $3800 a month.")
        #calculating how many more hours the student has to work 
        more_hours = ((((3800 + monthly_exp)*12)/hourly_wage)/12)
        
        #printitng the result
        print("\nAccording to your expenses and the rent you would" 
              " have to work"+ str(round(more_hours)) + " hours a month for a whole year" 
              " in order to afford the living expenses for a year in New York.")


def  Losangelos_calc():
    """
    
    This function dteremines the cost of living in Los Angelos with and without a 
    roommate 
    

    """
    #creating a roommate variable to store the choice of the user
    roommate = input(" \nWould you like to share the space with a roommate?\n")
    
    #if the user choses to have a roommate
    if roommate.lower() == "no":
            print("\nThe current rent prices in Los Angelos averages"
                  " out to about $2400 a month. Considering you are" 
                  " chosing to split with a roomate your rent would"
                  " be about $1200 a month.")
            #calculating how many more hours the student has to work 
            more_hours = ((((1200+ monthly_exp)*12)/hourly_wage)/12)
            
            print("\nAccording to your expenses and the rent you would" 
                  " have to work "+ str(round(more_hours)) + " hours a month for a whole year" 
                  " in order to afford the living expenses for a year in Los Angelos.")
     #if the user choses not to have a roommate 
    else:
         print("\nThe current rent prices in Los Angelos averages out to about"
              " $2400 a month.")
         #calculating how many more hours the student has to work 
         more_hours = ((((2400 + monthly_exp)*12)/hourly_wage)/12)
         
        #printitng the result
         print("\nAccording to your expenses and the rent you would" 
              " have to work "+ str(round(more_hours)) + " hours a month for a whole year" 
              " in order to afford the living expenses for a year in Los Angelos.")
    
   

def Toronto_saved():
    """
    
    Calculates if a student has saved enough money to move out and if not how 
    much they ahve to save.

    """
    #creating a roommate variable to store the choice of the user
    roommate = input("\nWould you like to share the space with a roommate?\n")
    #calculation for figuring out if they have enough money 
    moneyneeded1 = ((1100+monthlyexp)*12) - how_much_save
    moneyneeded2 = ((2200+monthlyexp)*12) - how_much_save
    #if they chose to have a roommate 
    if roommate == 'yes' or roommate == 'Yes':
            print("\nThe current rent prices in Toronto averages"
                  " out to about $2200 a month. Considering you are" 
                  " choosing to split with a roommate your rent would"
                  " be about $1100 a month.")
            #if they ahve more money than required
            if (how_much_save >= ((1100+monthlyexp)*12)):
                print("\nYou have enough to move out.")
            # if they have less money than required
            elif(how_much_save < ((1100+monthlyexp)*12)):
                 print("\nYou still need $" + str(round(moneyneeded1)) + " in order to" 
                       " move out.")
            #if they put invalid info 
            else: 
                print("\nNo valid infromation.")
                
    #if they chose not to have roommates      
    else:
        print("\nThe current rent prices in Toronto averages"
              " out to about $2200 a month.")
        #if they ahve more money than required
        if (how_much_save >= ((2200+monthlyexp)*12)):
            print("\nYou have enough to move out.")
        # if they have less money than required
        elif(how_much_save < ((2200+monthlyexp)*12)):
             print("\nYou still need $" + str(round(moneyneeded2)) + " in order to" 
                   " move out.")
        #if they put invalid info 
        else:
            print("\nNo valid information")

def Vancouver_saved():
    """
    Calculates if a student has saved enough money to move out and if not how 
    much they have to save.

    """
    roommate = input("\nWould you like to share the space with a roommate?\n")
    moneyneeded1 = ((1300+monthlyexp)*12) - how_much_save
    moneyneeded2 = ((2600+monthlyexp)*12) - how_much_save
    if roommate == 'yes' or roommate == 'Yes':
            print("\nThe current rent prices in Vancouver averages"
                  " out to about $2600 a month. Considering you are" 
                  " choosing to split with a roommate your rent would"
                  " be about $1300 a month.")
            #if they ahve more money than required
            if (how_much_save >= ((1300+monthlyexp)*12)):
                print("\nYou have enough to move out.")
            # if they have less money than required
            elif(how_much_save < ((1300+monthlyexp)*12)):
                 print("\nYou still need $" + str(round(moneyneeded1)) + " in order to" 
                       " move out.")
            #if they put invalid info 
            else:
                 print(" no valid information.")
                
          
    else:
        print("\nThe current rent prices in Vancouver area averages"
              " out to about $2200 a month.")
        #if they have more money than required
        if (how_much_save >= ((2600+monthlyexp)*12)):
            print("\nYou have enough to move out")
        # if they have less money than required
        elif(how_much_save < ((2600+monthlyexp)*12)):
             print("\nYou still need $" + str(round(moneyneeded2)) + " in order to" 
                   " move out.")
         #if they put invalid info 
        else:
            print("\nNo valid information.")

def Newyork_saved():
    """
    Calculates if a student has saved enough money to move out and if not how
    much more they need to save.
    """
    roommate = input("\nWould you like to share the space with a roommate?\n")
    moneyneeded1 = ((1900+monthlyexp)*12) - how_much_save
    moneyneeded2 = ((3800+monthlyexp)*12) - how_much_save
    if roommate == 'yes' or roommate == 'Yes':
            print("\nThe current rent prices in New York averages"
                  " out to about $3800 a month. Considering you are" 
                  " choosing to split with a roommate your rent would"
                  " be about $1900 a month.")
            #if they have more money than required
            if (how_much_save >= ((1900+monthlyexp)*12)):
                print("\nYou have enough to move out")
            # if they have less money than required
            elif(how_much_save < ((3800+monthlyexp)*12)):
                 print("\nYou still need $" + str(round(moneyneeded1)) + " in order to" 
                       " move out.")
            #if they put invalid info 
            else:
                print("\nNo valid information.")
                
    #if they chose not to have a roommate       
    else:
        print("\nThe current rent prices in New York averages"
              " out to about $3800 a month.")
        #if they have more money than required
        if (how_much_save >= ((3800+monthlyexp)*12)):
            print("\nYou have enough to move out.")
        # if they have less money than required
        elif(how_much_save < ((3800+monthlyexp)*12)):
             print("\nYou still need $" + str(round(moneyneeded2)) + " in order to" 
                   " move out.")
        #if they put invalid info 
        else:
            print("\nNo valid information.")
             
def Losangelos_saved():
    """
    Calculates if a student has saved enough money to move out and if not 
    how much they have to save.
    """
    roommate = input("\nWould you like to share the space with a roommate?\n")
    moneyneeded1 = ((1200+monthlyexp)*12) - how_much_save
    moneyneeded2 = ((2400+monthlyexp)*12) - how_much_save
    if roommate == 'yes' or roommate == 'Yes':
            print("\nThe current rent prices in Los Angelos averages"
                  " out to about $2400 a month. Considering you are" 
                  " choosing to split with a roommate your rent would"
                  " be about $1200 a month.")
            #if they have more money than required
            if (how_much_save >= ((1200+monthlyexp)*12)):
                print("\nYou have enough to move out.")
                
            # if they have less money than required
            elif(how_much_save < ((1200+monthlyexp)*12)):
                 print("\nYou still need $" + str(round(moneyneeded1)) + " in order to" 
                       " move out.")
             #if they put invalid info 
            else:
                 print("\nNo valid information.")
                
    #if they choose not to have a roommate       
    else:
        print("\nThe current rent prices in Los Angelos averages"
              " out to about $2400 a month.")
        #if they have more money than required
        if (how_much_save >= ((2400+monthlyexp)*12)):
            print("\nYou have enough to move out.")
            
        # if they have less money than required
        elif(how_much_save < ((2400+monthlyexp)*12)):
             print("\nYou still need $" + str(round(moneyneeded2)) + " in order to" 
                   " move out.")
         #if they put invalid info 
        else:
             print("\nNo valid information.")
    
      
# intial print statement for the user to determine if they want to continue
ans = int(input(" Welcome to Move Out  calculator. what would you like to do today?"
          "\n1. Get money calculations \n2. Exit\n "))
#if the user choses to get the calculations 
if ans == 1: 
    """
    using while loop to ask the user if they have a job and determining the hours they 
    have to work dependign on what city they choose
    """
    
    while True:
        print("\nGreat, lets get started! ")
        #a job variable to store user input 
        job = input("\nDo you have a job?\n")
         
        #if the user doe shave a job    
        if(job != 'no' and job != 'No'):
            #asking for their hourly wage
             hourly_wage = float(input("\nHow much do you get paid per hour?\n"))
             
             #asking for their monthly expense 
             monthly_exp = int(input("\nOn average how much are your monthly expenses?\n"))
             
             print("\nPlease choose from the following list of cities that you would like to move to:\n")
             #asking them what city they would like to move to
             city = int(input("\n1. Toronto \n2. Vancouver \n3. New York \n4. Los Angelos\n"))
             
             #if and else if statements for the options of the cities
         
             if city == 1:
                 Toronto_calc()
         
             elif city == 2:
                Vancouver_calc()
                    
             elif city == 3: 
                 Newyork_calc()
                     
             elif city == 4:
                 Losangelos_calc()
                 
        #if they dont have a job                
        else:
            #asking if they have savings 
            savings = input("\nDo you have savings?\n")
            
            #if they have saving 
            if savings.lower() == "yes":
                # asking how much they haved saved 
                how_much_save = float(input("\nHow much do you have saved?\n"))
                
                #asking for their expense
                monthlyexp = float(input("\nHow much are your monthly expenses?\n"))
                print("\nPlease choose from the following list of cities that you would like to move to:\n")
                
                #giving them options for the cities they could live in 
                city = int(input("\n1. Toronto \n2. Vancouver \n3. New York \n4. Los Angelos\n"))
                #if statements absed on what otion they pick
                if city == 1:
                    #calling on method 
                    Toronto_saved()
                            
                elif city == 2:
                    #calling on method 
                    Vancouver_saved()
                            
                elif city == 3: 
                    #calling on method 
                    Newyork_saved()
                            
                elif city == 4:
                    #calling on method 
                    Losangelos_saved()
                    
            #else statement they dont have savings and a job                
            else:
                print("Please revisit the site at a later time.")
        
        #breaking the loop so that it stops 
        break
    
#if the user chooses to exit             
else:                  
    print("No problem!")
       
    
                    
   
   
