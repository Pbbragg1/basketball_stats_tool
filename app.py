#importing the file that holds the teams and players
import constants
#importing copy so i can deep copy my constants
import copy
#create a copy of constants so it doesnt alter the original data
copy_of_data = copy.deepcopy(constants.PLAYERS)
#creating a variable that if changed to false it will end the loop and exit the tool
do_continue = True
#defining a function that cleans each persons data so that it seperates the gaurdians name, their first and last name, and sets their experience to true of false instead of yes or no
def clean(data):
    new_data = copy.deepcopy(data)
    cleaned_players = []
    for player in new_data:
        cleaned = {}
        cleaned["first_name"] = player["name"].split(" ")[0]
        cleaned["last_name"] = player["name"].split(" ")[1]
        if "and" in player["guardians"]:
            cleaned["guardians"] = player["guardians"].split(" and ")
        else:
            cleaned["guardians"] = player["guardians"].split(" ")
        if player["experience"] == "Yes" or player["experience"] == "yes" or player["experience"] == "YES":
            cleaned["experience"] = bool("true")
        elif player["experience"] == "No" or player["experience"] == "no" or player["experience"] == "NO":
            cleaned["experience"] = bool("")
        cleaned["height"] = player["height"].split(" ")[0]
        cleaned["height"] = int(cleaned["height"])
        cleaned_players.append(cleaned)
    return cleaned_players
#defines a function that asks for the data inputed, the lower bound, and the upper bound and outputs the players on each team
def players_on_teams(data,lower,upper):
    new_data = copy.deepcopy(data)
    players_on_team = []
    spot = lower
    for player in range(int(lower),int(upper)):
        get_name = new_data[spot]["name"]
        players_on_team.append(get_name)
        spot += 1
    return players_on_team
if __name__ == "__main__":
    clean_players = clean(copy_of_data)
    #creates a variables that devides the number of players by teams so the code knows how many people to put on each team
    players_per_team = int(len(clean_players)) / int(len(constants.TEAMS))
    #makes sure that the numer it outputs is an integer
    players_per_team = int(players_per_team)
    #calls the funtion that puts players on teams and utilizes the variable that calculated how many players were on each team.
    players_on_panthers = players_on_teams(copy_of_data,0,players_per_team)
    players_on_panthers = ", ".join(players_on_panthers)
    players_on_bandits = players_on_teams(copy_of_data, players_per_team , (2 * players_per_team))
    players_on_bandits = ", ".join(players_on_bandits)
    players_on_warriors = players_on_teams(copy_of_data,(2 * players_per_team), (3 * players_per_team))
    players_on_warriors = ", ".join(players_on_warriors)
    #i added a dunder main here so if it gets imported my code doesnt run, my variables and funtions would just be defined
    #starts the while loop that will continue until they want to exit the tool
    while do_continue == True:
        #prints some basic starting stuff like the label of the tool and a menu bar then offers for them to view the team stats or quit the program
        print("BASKETBALL STATS TOOL")
        print()
        print("--menu--")
        print()
        print("Would you like to")
        print("A.) view team stats")
        print("B.) quit the program")
        print()
        #where they input their option
        option = str(input(">> "))
        #starts a try block so if they dont pick one of the options it will ask them to reinput
        try:
            #creating a block of code that runs if they pick to view team stats
            if option == "A" or option == "a":
                #shows them the team names for them to choose which team's stats to view
                print("A.) Panthers")
                print("B.) Bandits")
                print("C.) Warriors")
                print()
                #the input variable for what they choose
                team_select = input(">> ")
                #creates a try block so that if they do not put a valid team it will ask agian
                try:
                    #creates a block to run if they choose A
                    if team_select == "A" or team_select == "a":
                        #sets a continueing variable to a space so it will enter the while loop later
                        continuing = " "
                        #prints the team name and everyone on the team
                        print("Team: Panthers")
                        print()
                        print(f"total players: {players_per_team}")
                        print("Players on the Panthers:")
                        print(str(players_on_panthers))
                        print()
                        #starts the afformentioned loop
                        while continuing != "":
                            #prompts the user to press space if they would like to continue
                            continuing = input("Press enter to continue... ")
                            #creates a try block so if they put in anything expect an empty string then it will ask again
                            try:
                                if continuing == "":
                                    break
                                else:
                                    raise ValueError
                            except ValueError:
                                pass
                    #does everything that was previously mentioned with choice A but with a different team
                    elif team_select == "B" or team_select == "b":
                        continuing = " "
                        print("Team: Bandits")
                        print()
                        print(f"total players: {players_per_team}")
                        print("Players on the Bandits:")
                        print(str(players_on_bandits))
                        print()
                        while continuing != "":
                            continuing = input("Press enter to continue... ")
                            try:
                                if continuing == "":
                                    break
                                else:
                                    raise ValueError
                            except ValueError:
                                pass
                    #does everything that was previously mentioned with choice A but with a different team
                    elif team_select == "C" or team_select == "c":
                        continuing = " "
                        print("Team: Warriors")
                        print()
                        print(f"total players: {players_per_team}")
                        print("Players on the Warriors:")
                        print(str(players_on_warriors))
                        print()
                        while continuing != "":
                            continuing = input("Press enter to continue... ")
                            try:
                                if continuing == "":
                                    break
                                else:
                                    raise ValueError
                            except ValueError:
                                pass
                    #raises a valueerror if they select anything other than the three previously mentioned choices
                    else:
                        raise ValueError
                #excepts the valueerror and asks the user agian
                except ValueError:
                    print("Please input a valid selection")
            #if they chose B in the beggining for quitting the program it breaks the loop and ends the program
            elif option == "B" or option == "b":
                do_continue = False
                break
            #raises a vlue error if they choose anything other than A or B from the first given choice
            else:
                raise ValueError
        #excepts the value error and prompts them to ask again
        except ValueError:
            print("Please input a valid selection")
            pass
    #once the loop is broken it will print a goodbye message and end the program
    print("I hope you enjoyed the app come again!")
