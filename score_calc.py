from dice import Die

# score calcs for farkle


# farkle rules -> taken form kdc wiki
# Single 1	                                            100
# Single 5	                                            50
# Partial straight (1, 2, 3, 4, 5)	                    500
# Partial straight (2, 3, 4, 5, 6)	                    750
# Full straight (1, 2, 3, 4, 5, 6)	                    1,500
# Three 1s	                                            1,000
# Three 2s	                                            200
# Three 3s	                                            300
# Three 4s	                                            400
# Three 5s	                                            500
# Three 6s	                                            600
# Four or more of a kind (e.g.: five 2s)	double the points of three of a kind, so four 4s are worth 800 points (400 times 2), five 4s are worth 1,600 points (800 times 2), etc..

class UndescriptDiceGameScorer:
    @staticmethod
    def calc_score(dice_array: list[Die]):
        UndescriptDiceGameScorer.handle_full_straight(dice_array)
        UndescriptDiceGameScorer.handle_three_of_a_kind(dice_array)
 

    def handle_full_straight(self, dice_arr: list[Die]):
        pass
        # for die in dice_arr:
        #     if()

            

    def handle_three_of_a_kind(self):
        pass
