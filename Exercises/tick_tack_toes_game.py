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
    field = Choice (variant = accessible_fields, question = f"Accessible fields: {accessible_fields}. Please choose the field to put your figure in. ")
    chosen_field = field.players_choice()
    print (f"Your choice is: {chosen_field}")
    return [chosen_field, player]

def modify_the_field(fields, player):
    move = choose_a_field(fields, player)
    fields[move[0]]["figure"]=move[1]
    fields[move[0]]["access"]: False
    print (fields)
    return fields

def game_main():
    figure = Choice(["x", "o"], "Do you want to be X or O? (type x or o) ", ["X", "o"])
    another_round = Choice (["y", "n"], "Do you want another round? (type y for yes, n for no) ", [True, False])   
    game=True
    fields = {
            "1": {"coordinates": (1,5), "access": True, "figure": "1"},
            "2": {"coordinates": (3,5), "access": True, "figure": "2"},
            "3": {"coordinates": (5,5), "access": True, "figure": "3"},
            "4": {"coordinates": (1,3), "access": True, "figure": "4"},
            "5": {"coordinates": (3,3), "access": True, "figure": "5"},
            "6": {"coordinates": (5,3), "access": True, "figure": "6"},
            "7": {"coordinates": (1,1), "access": True, "figure": "7"},
            "8": {"coordinates": (3,1), "access": True, "figure": "8"},
            "9": {"coordinates": (5,1), "access": True, "figure": "9"}
            }
    while game:
        first_player = figure.players_choice()
        second_player = "o" if first_player == "X" else "X"
        for round in range (5):
            print (f"Round {round}. First player's turn. "),
            # working out the function to display the available fields with print () - see the "pieces"
            fields = modify_the_field(fields, first_player)
            print ("Second player's turn! ")
            fields = modify_the_field(fields, second_player)
            round+=1
        game = another_round.players_choice()