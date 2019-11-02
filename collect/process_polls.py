"""Processes raw polling data to produce useful information."""

import math
import datetime
import database
import sys

# User-defined variables.
POLL_USEFULNESS_DURATION = 50
HIGH_TOTAL_WEIGHT = 10

def attach_primary_polls_to_states(db):
    """
    For each state, and the USA as a whole, process their primary polls into
    useful information and add that to the state object.

    :param db:
        The database containing the state and poll objects.
    :param db:
        The database with the polling averages attached to state objects.
    
    """
    # Setup lists for each state to contain the polls.
    states = db.get_states_dict()
    sorted_polls = {"USA": []}
    for state_name in states:
        sorted_polls[state_name] = []

    # Sort through the polls, adding them to the lists in the sorted_polls dict
    # as appropriate.
    polls = db.get_polls()
    for poll in polls:
        sorted_polls[poll.get_location()].append(poll)

    # For each location, add the confidence level and weighted average to the
    # database, after adjusting the weights to take into account how old the
    # polls are.
    today = datetime.date.today()
    for location in sorted_polls:
        dated_polls = date_polls(sorted_polls[location], today)
        average = weighted_average(dated_polls, db)

        # If no polls were available, use a dict of candidates with 0 support
        # and confidence 0.
        if average == {"confidence":0}:
            average = zero_support_dict(db)
 
        if location == "USA":
            db.nat_primary_environment = average
        else:
            db.states[location].primary_polling = average

    return db

def zero_support_dict(db):
    """
    Creates a dict keying the name of each primary candidate to zero, and
    a confidence level to zero.

    :param db:
        The database containing the candidate names.
    :return zeroes:
        The dict keying names to zeroes.
    
    """
    candidates = db.get_primary_candidates()
    zeroes = {"confidence":0}
    for candidate in candidates:
        zeroes[candidate] = 0
    
    return zeroes

def date_polls(polls, today):
    """
    Adjusts the weight attributed to polls on the basis of how old they are.

    :param polls:
        A list of poll objects.
    :param today:
        A datetime.date object representing today's date.
    :return dated_polls:
        The list of polls with adjusted weights.
    
    """
    if not isinstance(polls, list):
        raise TypeError("Polls must be provided in a list")

    dated_polls = []
    for poll in polls:
        # Calculate how old the poll is.
        poll_date = poll.get_date()
        days_old = (today - poll_date)/datetime.timedelta(days=1)
        if days_old < 0:
            days_old = 0

        # Adjust the poll's weight. Ignore it if it is too old to be useful.
        if days_old < POLL_USEFULNESS_DURATION:
            adjustment_factor = 1 - (days_old/POLL_USEFULNESS_DURATION)
            new_weight = adjustment_factor*poll.get_weight()
            poll.set_weight(new_weight)
            dated_polls.append(poll)

    return dated_polls

def weighted_average(polls, db):
    """
    Finds the weighted average of polls and the confidence in that average.

    :param polls:
        A list of poll objects.
    :param db:
        The database containing data on the simulation, importantly including
        a list of candidates still in the race, which may be different to the
        candidates listed in a poll.
    :return total_support:
        A dict containing the average result of the polls and a "confidence"
        key with a numerical value.
    
    """
    total_weight = 0
    total_support = {}

    # If there are no polls, simply return a dict stating that confidence = 0.
    if polls == []:
        total_support = {"confidence":0}
        return total_support

    # Get the list of candidates/options and set up the counters.
    candidates = db.get_primary_candidates()
    for candidate in candidates:
        total_support[candidate] = 0

    # For each poll, add the weight and weighted results to the cumulative
    # totals.
    for poll in polls:
        weight = poll.get_weight()
        total_weight = total_weight + weight
        result = poll.get_result()
        for candidate in candidates:
            total_support[candidate] = (total_support[candidate] + 
                                        weight*result[candidate])

    # Divide through by the total weight to find weighted averages.
    assert total_weight > 0, "Polls have negative or no weight."
    for candidate in total_support:
        total_support[candidate] = total_support[candidate]/total_weight
    
    # Calculate confidence and add it to the dict.
    assert HIGH_TOTAL_WEIGHT > 0, "HIGH_TOTAL_WEIGHT must be > zero."
    confidence = 1 - math.exp(-total_weight/HIGH_TOTAL_WEIGHT)
    total_support["confidence"] = confidence

    return total_support