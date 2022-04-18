# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# 1.1 Create a variable for every player that scored, for example:
player_0 = "Ruud Gullit"
player_1 = "Marco van Basten"

print(type(player_0))
print(type(player_1))

# 1.2 Create a variable for each minute of the match that a goal was scored in
goal_0= 32
goal_1 = 54

# 1.3 Using the +-operator, create a string that reports on who scored when,

scorers=player_0 +' ' +str(goal_0) +', '+ player_1 +' '+str(goal_1)
 

"""1.4 Use f-strings or the + -operator to create a single string with information about
who scored when in the format """
report = f'{player_0} scored in the {goal_0}nd minute\n{player_1} scored in the {goal_1}th minute' 



# 2.1. Choose a player that played in the soccer match and store his name as a string in the variable player
player = 'Ronald Koeman'

# 2.2 first_name : use slicing and the find -method
find1 = player.find(" ")
first_name = player[0: find1 ]



# 2.3 last_name_len : use find , slicing and len to isolate and store the length of their last name
last_name_len = len(player[find1 +1 : ])
  


# 2.4 name_short : isolate and store the player's name in this format: G. van Examplestein
name_short = first_name[0] + '. ' + (player[find1 +1 : ])


# 2.5 their first name len() times plus an exclamation mark( ! )
x = len(first_name)
chant = ((first_name + '! ') * x).rstrip()




# 2.6 good_chant : Make super-sure last character chant is not a space by using the inequality operator ( != ).

good_chant = chant[-1] != ' '






# print opdrachten

print('scorers is :' ,scorers)
print(report)
print(f' first name is {first_name}')
print(f' len last name is {last_name_len}')
print(f' name short is {name_short}')
print(f' chant is {chant}')
print(f' good_chant is {good_chant}')
print('nw')

#  wincpy check strings is OK
