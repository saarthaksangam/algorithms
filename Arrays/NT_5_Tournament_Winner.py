"""
Problem: Tornament Winner
Problem Statement: https://www.algoexpert.io/questions/Tournament%20Winner
NTID: NT-5
Category: Arrays
Difficulty: Easy
Sprint: 2205.01
Engineer: Saarthak Sangamnerkar
Date: 05/09/2022
"""


def tournamentWinner(competitions, results):
    """
    The tournamentWinner function takes in two parameters:
        1. competitions - a list of list, where each list is a pair of team names competing against each other
        2. results - the results of the competition between those teams

        The function returns a string representing the name of the winning team in all competitions

    :param competitions: Store the list of competitions
    :param results: Store the results of each competition
    :return: The name of the team that won the tournament
    :doc-author: Trelent
    """
    # Write your code here.
    winner = ""
    scorecard = {winner: 0}
    for i, comp in enumerate(competitions):
        res = results[i]
        homeTeam, awayTeam = comp

        winningTeam = homeTeam if res == 1 else awayTeam

        if winningTeam not in scorecard:
            scorecard[winningTeam] = 0
        scorecard[winningTeam] += 3

        if scorecard[winningTeam] > scorecard[winner]:
            winner = winningTeam

    return winner
