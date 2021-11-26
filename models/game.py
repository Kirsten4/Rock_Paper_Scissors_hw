class Game:

    def compare_choices(self,player_1,player_2):
        winning_player = None
        if player_1.choice == "rock":
            if player_2.choice == "paper":
                winning_player = player_2
            elif player_2.choice == "scissors":
                winning_player = player_1

        elif player_1.choice == "scissors":
            if player_2.choice == "paper":
                winning_player = player_1
            elif player_2.choice == "rock":
                winning_player = player_2

        elif player_1.choice == "paper":
            if player_2.choice == "rock":
                winning_player = player_1
            elif player_2.choice == "scissors":
                winning_player = player_2
        
        return winning_player
















