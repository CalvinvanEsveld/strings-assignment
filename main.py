# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'
# Add your code after this line

first_goal = 'Ruud Gullit'
second_goal = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = first_goal + ' ' + str(goal_0) + ', ' + second_goal + ' ' + str(goal_1)

report = f"{first_goal} scored in the {goal_0}nd minute\n{second_goal} scored in the {goal_1}th minute"

player = 'Ronald Koeman'

first_name = player[:player.find(' ')]

last_name_len = len(player[player.find(' ') + 1:])

name_short = first_name[:1] + '. ' + player[player.find(' ') + 1:]

chant = (first_name + '! ') * (len(first_name) - 1) + (first_name + '!')

good_chant = chant[-1] != ' '

