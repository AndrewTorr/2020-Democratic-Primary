"""Main file carrying out a simulation of the 2020 Democratic Primary."""

import datetime
import simulate.voting_patterns as vp
import database

def simulate(db, base_nat_environment, candidates, primary_calendar):
    """
    Simulates the 2020 Democratic Primary.

    :param base_nat_environment:
        Dict keying candidate names to their standings in national polls.
    :param candidates:
        List of candidates in the race.
    :primary_calendar:
        List of PrimaryDate objects in chronological order, forming a calendar
        containing every primary and caucus in the primary process.
    :return result_object:
        A PrimarySimulationResults object storing various information about the
        results of the simulation.
    
    """
    if len(candidates) == 0:
        raise ValueError("No candidates provided.")
    for candidate in base_nat_environment:
        if base_nat_environment[candidate] < 0:
            raise ValueError("Candidates cannot have negative support.")

    # Set up variables specific to this simulation.
    result_object = database.PrimarySimulationResults()
    nat_environment = vp.random_variation(base_nat_environment, 0)
    total_delegates = {}

    # Make sure no values in nat_environment are below zero.
    for candidate in nat_environment:
        if nat_environment[candidate] < 0:
            nat_environment[candidate] = 0
    nat_environment = vp.rebalance(nat_environment)

    for candidate in candidates:
        total_delegates[candidate] = 0

    for primary_date in primary_calendar:
        primaries = primary_date.get_primaries()
        for state_name in primaries:
            state = db.get_state(state_name)
            result = state.get_raw_primary_result(nat_environment,
                                                  base_nat_environment,
                                                  candidates, db)

            # Save the result in the database.
            state.primary_polling = result

            # Convert the result to delegates and add to delegate totals.
            delegates = state.distribute_delegates(result)
            for candidate in candidates:
                total_delegates[candidate] = (total_delegates[candidate] + 
                                              delegates[candidate])

        # Poorly placed candidates lose support as voters make tactical choices.
        nat_environment = vp.primary_tactical_voting(nat_environment, total_delegates)

    # Add data regarding the final delegate total to the results object.
    result_object.add_final_delegates(total_delegates)

    return result_object
