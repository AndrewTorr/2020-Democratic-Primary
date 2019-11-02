"""Contains helper functions simulating variations in voting patterns."""

import numpy

# Define constants.
BASE_STANDARD_DEVIATION = 1.31
MAX_STANDARD_DEVIATION = 4.3
SD_PER_DAY = 0.13
TAC_COEFFS = [1, 1, 0.97, 0.93, 0.89, 0.83, 0.78, 0.71, 0.66, 0.58, 0.52, 0.44,
              0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4]

def random_variation(polling_averages, days_left):
    """
    Accounts for uncertainty in a polling average by adding random variation
    between candidates, then adjusting the numbers such that they add to 100%
    again.

    :param polling_averages:
        Dict keying candidate names to their support in the polls in percent.
        Also contains a "confidence" key indicating the quality and quantity of
        data gone into forming this polling average, between 0 and 1.
    :param days_left:
        Days until the election.
    :return polling_averages:
        The polling averages with random variation applied.
    
    """
    if days_left < 0:
        raise ValueError("Days until the election cannot be negative.")
    if (polling_averages["confidence"] < 0 or 
        polling_averages["confidence"] > 1):
        raise ValueError("Confidence must be between zero and one.")

    # Calculate the standard deviation to use.
    standard_deviation = BASE_STANDARD_DEVIATION + days_left*SD_PER_DAY
    standard_deviation = standard_deviation/(0.5 + 
                                              polling_averages["confidence"]/2)
    if standard_deviation > MAX_STANDARD_DEVIATION:
        standard_deviation = MAX_STANDARD_DEVIATION

    # Add the random variation and sum the results.
    total_new_votes = 0
    for key in polling_averages:
        if key != "confidence":
            polling_averages[key] = numpy.random.normal(polling_averages[key], 
                                                        standard_deviation)
            total_new_votes = total_new_votes + polling_averages[key]

    # Divide each value through by the total/100 to ensure they add to 100%.
    divisor = total_new_votes/100
    for key in polling_averages:
        if key != "confidence":
            polling_averages[key] = polling_averages[key]/divisor

    return polling_averages

def primary_tactical_voting(nat_environment, total_delegates):
    """
    Models supporters of candidates doing poorly switching their support to
    candidates with a better chance of winning the primary.

    :param nat_environment:
        Dict keying candidates to their national support levels.
    :param total_delegates:
        Dict keying candidates to their current total delegate count.
    :return nat_environment:
        An adjusted dict reflecting changes due to tactical voting.

    """
    for candidate in nat_environment:
        if nat_environment[candidate] < 0:
            raise ValueError("Candidates cannot have negative support.")
    for candidate in total_delegates:
        if total_delegates[candidate] < 0:
            raise ValueError("Cannot have negative numbers of delegates")

    # Order the candidates by their delegate count (descending order).
    leaderboard = sorted(total_delegates, key=total_delegates.__getitem__,
                         reverse=True)

    # Multiply candidates national support levels by tactical voting
    # coefficients to gauge how many voters abandon them. Then rebalance the
    # votes so they add to 100 again.
    for i in range(len(leaderboard)):
        candidate = leaderboard[i]
        nat_environment[candidate] = nat_environment[candidate]*TAC_COEFFS[i]
    nat_environment = rebalance(nat_environment)

    return nat_environment

def rebalance(polling):
    """
    Rebalances a set of polling results or election results such that the
    percentages add to 100.

    :param polling:
        A dict keying various options to their percentage support.
    :return polling:
        The same dict, with the values rebalanced such that they add to 100.
    
    """
    for candidate in polling:
        if polling[candidate] < 0:
            raise ValueError("Candidates cannot have negative support.")

    # Add up the numbers to find the necessary divisor.
    total = 0
    for key in polling:
        if key != "confidence":
            total = total + polling[key]
    divisor = total/100
    assert divisor != 0, "No support detected - divide by zero error."

    # Divide each number by the divisor such that they add to 100.
    for key in polling:
        if key != "confidence":
            polling[key] = polling[key]/divisor

    return polling

def assign_leftover_delegates(delegates, pc_dels, unassigned_dels):
    """
    Assigns leftover delegates to candidates.

    :param delegates:
        Dict keying candidate names to delegate counts from this primary.
    :param pc_dels:
        The expected percentage of delegates each candidate should win.
    :param unassigned_dels:
        The number of delegates so far not assigned to candidates.
    :return delegates:
        Updated dict keying candidate names to delegate counts from this
        primary.
    """
    for candidate in delegates:
        if delegates[candidate] < 0:
            raise ValueError("Cannot have negative numbers of delegates")
    for candidate in pc_dels:
        if pc_dels[candidate] < 0:
            raise ValueError("Cannot have negative percentage of delegates")
    if unassigned_dels < 0:
        raise ValueError("unassigned_dels must be a natural number.")

    # Order the candidates by their delegate count (descending order).
    leaderboard = sorted(pc_dels, key=pc_dels.__getitem__, reverse=True)

    # Add the delegates to the leading candidates' totals.
    for i in range(unassigned_dels):
        candidate = leaderboard[i]
        delegates[candidate] = delegates[candidate] + 1

    return delegates

def unassign_extra_delegates(delegates, pc_dels, extra_dels):
    """
    Removes delegates from candidates in the situation where too many
    delegates have been assigned due to rounding.

    :param delegates:
        Dict keying candidate names to delegate counts from this primary.
    :param pc_dels:
        The expected percentage of delegates each candidate should win.
    :param extra_dels:
        The number of excess delegates assigned so far.
    :return delegates:
        Updated dict keying candidate names to delegate counts from this
        primary.

    """
    for candidate in delegates:
        if delegates[candidate] < 0:
            raise ValueError("Cannot have negative numbers of delegates")
    for candidate in pc_dels:
        if pc_dels[candidate] < 0:
            raise ValueError("Cannot have negative percentage of delegates")
    if extra_dels < 0:
        raise ValueError("extra_dels must be a natural number.")

    # Order the candidates by their delegate count (descending order).
    leaderboard = sorted(pc_dels, key=pc_dels.__getitem__, reverse=True)

    # Remove the delegates from the leading candidates' totals.
    for i in range(extra_dels):
        candidate = leaderboard[i]
        delegates[candidate] = delegates[candidate] - 1

    return delegates