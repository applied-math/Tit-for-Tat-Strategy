import numpy as np  # Importing NumPy library for matrix operations and arrays
import random  # Importing random library for generating random actions


# Function that implements "Always Cooperate" strategy
# Player always cooperates, which is represented by action '0'
def Always_COO(p, i):
    # p: The player's actions array
    # i: The current round index
    p[i] = 0  # Set current round action to 0 (cooperate)
    return p[i]  # Return the player's current action


# Function that implements "Always Defect" strategy
# Player always defects, which is represented by action '1'
def Always_DEF(p, i):
    # p: The player's actions array
    # i: The current round index
    p[i] = 1  # Set current round action to 1 (defect)
    return p[i]  # Return the player's current action


# Function that implements "Tit for Tat" strategy
# Player cooperates in the first round, and then mimics the opponent's last action in subsequent rounds
def Tit_For_Tat(p1, p2, i):
    # p1: The player's actions array (Player 1)
    # p2: The opponent's actions array (Player 2)
    # i: The current round index
    if i == 0:
        p1[i] = 0  # Cooperate in the first round
    else:
        p1[i] = p2[i - 1]  # Mimic opponent's action from the previous round
    return p1[i]  # Return the player's current action


# Function that implements "Suspicious Tit for Tat" strategy
# Player defects in the first round, and then mimics the opponent's last action in subsequent rounds
def Suspicious_TFT(p1, p2, i):
    # p1: The player's actions array (Player 1)
    # p2: The opponent's actions array (Player 2)
    # i: The current round index
    if i == 0:
        p1[i] = 1  # Defect in the first round
    else:
        p1[i] = p2[i - 1]  # Mimic opponent's action from the previous round
    return p1[i]  # Return the player's current action


# Function that implements "Reverse Tit for Tat" strategy
# Player defects in the first round, and then plays the opposite of the opponent's last action
def Reverse_TFT(p1, p2, i):
    # p1: The player's actions array (Player 1)
    # p2: The opponent's actions array (Player 2)
    # i: The current round index
    if i == 0:
        p1[i] = 1  # Defect in the first round
    else:
        p1[i] = 1 - p2[i - 1]  # Play the opposite of the opponent's last action
    return p1[i]  # Return the player's current action


# Function that implements "Random" strategy
# Player randomly cooperates or defects in each round with equal probability
def Random(p, i):
    # p: The player's actions array
    # i: The current round index
    actions = [0, 1]  # Define possible actions: 0 (cooperate), 1 (defect)
    p[i] = random.choice(actions)  # Randomly choose between cooperation and defection
    return p[i]  # Return the player's current action


# Function that implements "Naive Prober" strategy
# Cooperate in the first round, then mostly mimic opponent's action, but sometimes randomly defect
def Naive_Prober(p1, p2, i):
    # p1: The player's actions array (Player 1)
    # p2: The opponent's actions array (Player 2)
    # i: The current round index
    if i == 0:
        p1[i] = 0  # Cooperate in the first round
    else:
        r = random.random()  # Generate a random number between 0 and 1
        if 0 < r < 0.001:  # Small probability of defecting
            p1[i] = 1  # Defect with a very low probability
        else:
            p1[i] = p2[i - 1]  # Otherwise, mimic the opponent's last action
    return p1[i]  # Return the player's current action


# Function to calculate payoffs based on the player's actions and a given payoff matrix
def calc_payoffs(p1, p2, payoff_matrix):
    # p1: Actions of Player 1
    # p2: Actions of Player 2
    # payoff_matrix: A matrix representing the payoffs for different action combinations
    fit1 = 0  # Initialize payoff for Player 1
    fit2 = 0  # Initialize payoff for Player 2
    # Loop through each round's actions and calculate the payoffs
    for i in range(len(p1)):
        fit1 += payoff_matrix[1 - p1[i], 1 - p2[i]][0]  # Payoff for Player 1
        fit2 += payoff_matrix[1 - p1[i], 1 - p2[i]][1]  # Payoff for Player 2
    return fit1, fit2  # Return total payoffs for both players


# Main function to run the Iterated Prisoner's Dilemma game
def IPDGame(Strategy1, Strategy2, p1, p2):
    # Strategy1: Strategy chosen by Player 1
    # Strategy2: Strategy chosen by Player 2
    # p1: Array to store Player 1's actions
    # p2: Array to store Player 2's actions
    for i in range(50):  # Simulate 50 rounds of the game
        # Execute Player 1's strategy based on the provided strategy name
        if Strategy1 == "Always Cooperate":
            p1[i] = Always_COO(p1, i)
        if Strategy1 == "Always Defect":
            p1[i] = Always_DEF(p1, i)
        if Strategy1 == "Tit For Tat":
            p1[i] = Tit_For_Tat(p1, p2, i)
        if Strategy1 == "Suspicious Tit For Tat":
            p1[i] = Suspicious_TFT(p1, p2, i)
        if Strategy1 == "Reverse Tit for Tat":
            p1[i] = Reverse_TFT(p1, p2, i)
        if Strategy1 == "Random":
            p1[i] = Random(p1, i)
        if Strategy1 == "Naive Prober":
            p1[i] = Naive_Prober(p1, p2, i)

        # Execute Player 2's strategy based on the provided strategy name
        if Strategy2 == "Always Cooperate":
            p2[i] = Always_COO(p2, i)
        if Strategy2 == "Always Defect":
            p2[i] = Always_DEF(p2, i)
        if Strategy2 == "Tit For Tat":
            p2[i] = Tit_For_Tat(p2, p1, i)
        if Strategy2 == "Suspicious Tit For Tat":
            p2[i] = Suspicious_TFT(p2, p1, i)
        if Strategy2 == "Reverse Tit for Tat":
            p2[i] = Reverse_TFT(p2, p1, i)
        if Strategy2 == "Random":
            p2[i] = Random(p2, i)
        if Strategy2 == "Naive Prober":
            p2[i] = Naive_Prober(p2, p1, i)

    # Define the payoff matrix for the game
    # The values represent the payoffs for both players in the form (Player 1's payoff, Player 2's payoff)
    payoff_matrix = np.array([[(3, 3), (5, 0)], [(0, 5), (1, 1)]], dtype=object)

    # Calculate the total payoffs for both players using the actions played
    fit1, fit2 = calc_payoffs(p1, p2, payoff_matrix)

    # Determine the winner based on the payoffs
    if fit1 > fit2:
        print("The Winning Strategy is : " + Strategy1 + " Which belongs to Player 1")
    elif fit2 > fit1:
        print("The Winning Strategy is : " + Strategy2 + " Which belongs to Player 2")
    else:
        print("Draw Game, Meaning that The two strategies are equal")


# Initialize two players' actions arrays for 50 rounds (all zeros initially)
p1 = np.zeros(50, dtype=int)  # Player 1's actions
p2 = np.zeros(50, dtype=int)  # Player 2's actions

# Simulate the game for different strategy matchups
IPDGame("Always Cooperate", "Tit For Tat", p1, p2)
IPDGame("Always Defect", "Tit For Tat", p1, p2)
IPDGame("Always Defect", "Suspicious Tit For Tat", p1, p2)
IPDGame("Reverse Tit for Tat", "Suspicious Tit For Tat", p1, p2)

print(".....................................")

# Run multiple games for statistical purposes
for i in range(10):
    IPDGame

("Always Cooperate", "Random", p1, p2)
for i in range(10):
    IPDGame("Tit For Tat", "Random", p1, p2)
for i in range(10):
    IPDGame("Suspicious Tit For Tat", "Naive Prober", p1, p2)
