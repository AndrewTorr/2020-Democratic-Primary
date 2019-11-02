"""Analyses and presents presidential primary results."""

import matplotlib.pyplot as plt
import database
import sys

def winners_pie_chart(results):
    """
    Plots a pie chart showing how likely each candidate is to win the first
    ballot at the Democratic National Convention.

    :param results:
        A list of PrimarySimulationResults objects storing data for each
        simulation.
    
    """
    # Sum the results of the simulations and add them to a dict keying name
    # to number of wins.
    total_results = {}
    for result in results:
        winner = result.winner
        if winner in total_results:
            total_results[winner] = total_results[winner] + 1
        else:
            total_results[winner] = 1
    
    # Convert the dict into two lists where the index of a candidate's name
    # in the names list matches the index of their wins in the wins list.
    names = []
    wins = []
    for candidate in total_results:
        names.append(candidate)
        wins.append(total_results[candidate])
    
    plt.pie(wins, labels=names, autopct = '%1.1f%%')
    plt.title("Probability of Winning a Majority of Pledged Delegates.")
    plt.show()

def most_delegates_pie_chart(results):
    """
    Plots a pie chart showing how likely each candidate is to win the most
    pledged delegates in scenarios where no candidate wins a majority at the
    first ballot.

    :param results:
        A list of PrimarySimulationResults objects storing data for each
        simulation.
    
    """
    # Sum the results of the simulations and add them to a dict keying name
    # to number of wins.
    total_results = {}
    for result in results:
        if result.winner == "No majority":
            winner = result.most_delegates
            if winner in total_results:
                total_results[winner] = total_results[winner] + 1
            else:
                total_results[winner] = 1
    
    # Convert the dict into two lists where the index of a candidate's name
    # in the names list matches the index of their most delegates in the wins 
    # list.
    names = []
    wins = []
    for candidate in total_results:
        names.append(candidate)
        wins.append(total_results[candidate])
    
    plt.pie(wins, labels=names, autopct = '%1.1f%%')
    plt.title("Probability of Winning The Most Pledged Delegates.")
    plt.show()

def mean_final_delegates(results, num_sims, candidates):
    """
    Plots a pie chart showing the mean number of pledged delegates each
    candidate has at the end of the primary process.

    :param results:
        A list of PrimarySimulationResults objects storing data for each
        simulation.
    :param num_sims:
        The number of simulations run.
    :param candidates:
        List of strings containing the names of the major candidates in the
        primary.

    """
    LARGE_DEL_COUNT_THRESHOLD = 100
    if num_sims <= 0:
        print("Number of simulations less than or equal to zero.")
        sys.exit()

    # Set up dict keying candidate names to total delegates over all
    # simulations.
    total_dels = {}
    for candidate in candidates:
        total_dels[candidate] = 0

    # Add up the results.
    for result in results:
        dels = result.final_delegates
        for candidate in candidates:
            total_dels[candidate] = total_dels[candidate] + dels[candidate]

    # Divide through by the number of simulations to find the average. 
    for candidate in total_dels:
        total_dels[candidate] = total_dels[candidate]/num_sims

    # Convert the dict into two lists where the index of a candidate's name
    # in the names list matches the index of their mean delegates iun the
    # delegates list. If the total is below 250, add them to the "other" slice of the pie.
    names = ["Other"]
    delegates = [0]
    for candidate in total_dels:
        if total_dels[candidate] >= LARGE_DEL_COUNT_THRESHOLD:
            names.append(candidate)
            delegates.append(total_dels[candidate])
        else:
            delegates[0] = delegates[0] + total_dels[candidate]

    plt.pie(delegates, labels=names, autopct = '%1.1f%%')
    plt.title("Mean Percentage of Delegates Won.")
    plt.show()