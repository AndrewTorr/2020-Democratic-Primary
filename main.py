"""Probabilistic model of the 2020 Democratic Primary."""

import populate
import database
import simulate.primary_simulation as ps
import analyse.plot as plot

# Define constants.
NUM_SIMULATIONS = 1000

# Carry out the simulations.
results = []
for simulation in range(NUM_SIMULATIONS):

    # Create a clean database containing required information.
    db = populate.populate()

    # Initialise other variables.
    base_nat_environment = db.get_nat_primary_environment()
    candidates = db.get_primary_candidates()

    # Set up to iterate through the primary calendar.
    primary_calendar = db.get_primary_calendar()

    result = ps.simulate(db, base_nat_environment, candidates,
                          primary_calendar)
    results.append(result)

# Analyse and present the results.
plot.winners_pie_chart(results)
plot.most_delegates_pie_chart(results)
plot.mean_final_delegates(results, NUM_SIMULATIONS, candidates)