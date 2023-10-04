"""Tick-tack toes game with matplotlib visualization"""

import matplotlib.pyplot as plt

class Choice:
    def __init__(self, variant, question, a_return=None):
        self.variant = variant
        self.question = question
        self.a_return = a_return

    def players_choice (self):
        players_choice = None
        while players_choice not in self.variant:
            players_choice = input (self.question)
        if self.a_return != None:
            if players_choice == self.variant[0]:
                return self.a_return[0]
            return self.a_return[1]
        return players_choice
    
def access_fields (fields):
    accessible_fields = []
    for key in fields.keys():
        if fields[key]["access"]:
            accessible_fields.append(key)
    return accessible_fields

def choose_a_field(fields, player):
    accessible_fields = access_fields(fields)
    field = Choice (variant = accessible_fields, question = f"Accessible fields: {accessible_fields}. \
    Please choose the field to put your figure in. ")
    chosen_field = field.players_choice()
    print (f"Your choice is: {chosen_field}")
    return [chosen_field, player]

def modify_the_field(fields, player):
    move = choose_a_field(fields, player)
    fields[move[0]]["figure"]=move[1]
    fields[move[0]]["access"]= False
    return fields

def make_fields ():
    fields = {
            "1": {"coordinates": (1,1), "access": True, "figure": "1"},
            "2": {"coordinates": (3,1), "access": True, "figure": "2"},
            "3": {"coordinates": (5,1), "access": True, "figure": "3"},
            "4": {"coordinates": (1,3), "access": True, "figure": "4"},
            "5": {"coordinates": (3,3), "access": True, "figure": "5"},
            "6": {"coordinates": (5,3), "access": True, "figure": "6"},
            "7": {"coordinates": (1,5), "access": True, "figure": "7"},
            "8": {"coordinates": (3,5), "access": True, "figure": "8"},
            "9": {"coordinates": (5,5), "access": True, "figure": "9"}
            }
    return fields

def find_the_output(fields):
    output = [fields[key]["figure"] for key in fields]
    for index, value in enumerate(output):
        if value.isalpha():
            output[index] = value.upper()
    return (output)

def print_the_field(fields):
    output = find_the_output(fields)
    lines = ["  ".join(output[6:]), "  ".join(output[3:6]), "  ".join(output [:3])]
    print ("\n".join(lines))

def provide_coordinates (fields, player):
    coordinates = []
    for key in fields.keys():
        if fields[key]["figure"] == player:
            coordinates.append(fields[key]["coordinates"])
    return (coordinates)

def plot_the_field (fields, first_player, second_player):   
    x_player = first_player if first_player == "X" else second_player
    o_player = second_player if x_player == first_player else first_player
    xs = provide_coordinates(fields, x_player)
    os = provide_coordinates(fields, o_player)
    x_xs = [item[0] for item in xs]
    y_xs = [item[1] for item in xs]
    x_os = [item[0] for item in os]
    y_os = [item[1] for item in os]
    plt.scatter (x_xs, y_xs, marker = "X", s = 500)
    plt.scatter (x_os, y_os, marker = "o", s = 500)
    plt.xticks(list(range(0, 7, 2)))
    plt.yticks(list(range(0, 7, 2)))
    plt.grid()
    plt. show()

def is_winner (fields, player):
    conditions = [
        fields["1"]["figure"] == fields["2"]["figure"] == fields["3"]["figure"],
        fields["4"]["figure"] == fields["5"]["figure"] == fields["6"]["figure"],
        fields["7"]["figure"] == fields["8"]["figure"] == fields["9"]["figure"],
        fields["1"]["figure"] == fields["4"]["figure"] == fields["7"]["figure"],
        fields["2"]["figure"] == fields["5"]["figure"] == fields["8"]["figure"],
        fields["3"]["figure"] == fields["6"]["figure"] == fields["9"]["figure"],
        fields["3"]["figure"] == fields["5"]["figure"] == fields["7"]["figure"],
        fields["1"]["figure"] == fields["5"]["figure"] == fields["9"]["figure"],
    ]
    if True in conditions:
        print (f"{player} wins!")
        return True
    return False

def make_move (round, player_whose_turn, fields, second_player):
    print (f"Round {round+1}. {player_whose_turn}'s turn. ")
    print_the_field(fields)
    fields = modify_the_field(fields, player_whose_turn)
    plot_the_field(fields, player_whose_turn, second_player)
    return fields

def game_main():
    figure = Choice(["x", "o"], "Do you want to be X or O? (type x or o) ", ["X", "o"])
    another_round = Choice (["y", "n"], "Do you want another round? (type y for yes, n for no) ", [True, False])   
    game=True
    
    while game:
        first_player = figure.players_choice()
        second_player = "o" if first_player == "X" else "X"
        fields = make_fields()
        
        for round in range (5):
            
            fields = make_move (round, first_player, fields, second_player)
            win = is_winner(fields, first_player)
            if win or round == 4: break
            
            fields = make_move (round, second_player, fields, first_player)
            win = is_winner (fields, second_player)
            if win: break
                    
            round+=1
        if not win: print ("It's a draw!")
        game = another_round.players_choice()

game_main()