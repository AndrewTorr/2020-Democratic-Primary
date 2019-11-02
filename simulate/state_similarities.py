"""Creates the dicts describing how similar states are politically."""

import database

# Define constants for the module.
HIGH_DEM_DIFFERENCE_COEFFICIENT = 50
HIGH_PVI_DIFFERENCE = 30

def save_state_similarities(db):
    """
    Calculates state similarities and adds them to the database.

    :param db:
        The database object containing data about the states.
    :return db:
        The updated database with state similarity dicts added.
    
    """
    # Iterate through each pair of states, adding the similarities for each.
    states = db.get_states_dict()
    for state_1_name in states:
        state_1 = states[state_1_name]
        if state_1.get_date() != None:
            state_1_sims = state_1.get_state_sims()
            for state_2_name in states:
                if state_1_name != state_2_name:
                    state_2 = states[state_2_name]
                    if state_2.get_date() != None:
                        sim = find_similarity(state_1, state_2)
                        state_1_sims[state_2_name] = sim
            # Save the updated similarities dict to the database.
            state_1.set_state_sims(state_1_sims)

    return db

def find_similarity(state_1, state_2):
    """
    Calculates a coefficient of similarity between 0 and 1 between 2 states.

    :param state_1:
        The first state object.
    :param state_2:
        The second state object.
    :return sim:
        The political similarity coefficient between the two states.
    
    """
    
    # Calculate a demographic similarity coefficient.
    white_diff = abs(state_1.get_pcwhite() - state_2.get_pcwhite())
    black_diff = abs(state_1.get_pcblack() - state_2.get_pcblack())
    hispanic_diff = abs(state_1.get_pchispanic() - state_2.get_pchispanic())
    asian_diff = abs(state_1.get_pcasian() - state_2.get_pcasian())
    native_diff = abs(state_1.get_pcnative() - state_2.get_pcnative())
    diff = white_diff + black_diff + hispanic_diff + asian_diff + native_diff
    if diff >= HIGH_DEM_DIFFERENCE_COEFFICIENT:
        dem_sim = 0
    else:
        dem_sim = 1 - diff/HIGH_DEM_DIFFERENCE_COEFFICIENT

    # Calculate a partisan similarity coefficient.
    pvi_diff = abs(state_1.get_PVI() - state_2.get_PVI())
    if pvi_diff >= HIGH_PVI_DIFFERENCE:
        par_sim = 0
    else:
        par_sim = 1 - pvi_diff/HIGH_PVI_DIFFERENCE

    # Calculate a regional similarity coefficient.
    if state_1.get_region() == state_2.get_region():
        reg_sim = 1
    else:
        reg_sim = 0

    # Average the coefficients to find the overall similarity.
    sim = (dem_sim + par_sim + reg_sim)/3

    return sim

def apply_comparison(state_environment, db, state_sims):
    """
    Adjusts a non-randomised state primary popular vote result to include
    information inferred from polling and results in other states.

    :param state_environment:
        Dict keying candidate names to their percentage popular vote support,
        and a "confidence" key representing the confidence in the result. This
        confidence value ranges from 0 to 1.
    :param db:
        The database in which the state similarity data is stored.
    :param state_sims:
        Dict keying state names to similarity coefficients between 0 and 1
        decribing the similarity between the current state and the state named
        in the key.
    :return state_environment:
        An updated state environment dict with adjusted support levels.
    
    """
    # Define how heavily to weight inferred support compared to a weight of 0-1
    # for state level polling.
    INFERRED_WEIGHT = 0.22

    # Set up a dict to collect support totals ready to find a weighted average.
    total_weight = 0
    inferred_support = {}
    for candidate in state_environment:
        if candidate != "confidence":
            inferred_support[candidate] = 0
    
    # Iterate through the states, creating weighted support totals based on
    # the confidence level of predictions for each state.
    for state_name in state_sims:
        state = db.get_state(state_name)
        polling = state.get_primary_polling()
        confidence = polling["confidence"]
        total_weight = total_weight + confidence
        for candidate in inferred_support:
            inferred_support[candidate] = (inferred_support[candidate] + 
                                           confidence*polling[candidate])
    
    # Divide through by total weight to find the weighted average.
    for candidate in inferred_support:
        inferred_support[candidate] = inferred_support[candidate]/total_weight
    
    # Find the weighted average of the inferred and polled support.
    state_confidence = state_environment["confidence"]
    weight = INFERRED_WEIGHT + state_confidence
    for candidate in state_environment:
        if candidate != "confidence":
            state_environment[candidate] = (
                state_confidence*state_environment[candidate] + 
                INFERRED_WEIGHT*inferred_support[candidate])
            state_environment[candidate] = state_environment[candidate]/weight
            
    return state_environment