"""Provides the API with which to access data on candidates and states."""

import numpy
import datetime
import simulate.voting_patterns as vp
import simulate.state_similarities as ss

class Database:
    """Stores states and territories."""
    def __init__(self, states={}, primary_calendar=[], primary_candidates=[],
                 nat_primary_environment={}, polls=[]):
        """
        Initialises a database object.
        
        :param states:
            Dict used to key state names to objects representing those states.
        :param primary_calendar:
            List of primary objects storing data on each day of primary
            elections in chronological order.
        :param primary_candidates:
            List of candidates in the 2020 Democratic Primary.
        :param nat_primary_environment:
            Dict keying primary candidates to their national polling averages.
        :param polls:
            List of Poll objects storing results of opinion polls.

        """
        self.states = states
        self.primary_calendar = primary_calendar
        self.primary_candidates = primary_candidates
        self.nat_primary_environment = nat_primary_environment
        self.polls = polls

    def get_state(self, name):
        """
        Retrieves a state object in the database.
        
        :param name:
            The name of the state to be returned.
        
        :return self.states[name]:
            The state object.

        """
        return self.states[name]

    def get_states_dict(self):
        """
        Retrieves the full dict of states in the database.
        
        :return self.states:
            The dict keying state names to state objects.

        """
        return self.states

    def add_state(self, state):
        """
        Adds a state to the database by adding it to the states dict.

        :param state:
            The state object to add to the database.

        """
        self.states[state.name] = state

    def get_primary_calendar(self):
        """
        Retrieves the full list of primary dates.
        
        :return self.primary_calendar:
            The list containing PrimaryDate objects.

        """
        return self.primary_calendar

    def add_primary_date(self, primary_date):
        """
        Adds a primary date to the calendar.

        :param primary_date:
            The PrimaryDate object to append to the list of dates.

        """
        self.primary_calendar.append(primary_date)

    def get_primary_candidates(self):
        """
        Retrieves the full list of primary candidates.
        
        :return self.primary_candidates:
            The list containing the surnames of the candidates.

        """
        return self.primary_candidates

    def set_primary_candidates(self, primary_candidates):
        """
        Set the list of primary candidates.
        
        :param primary_candidates:
            A list containing the surnames of the candidates.

        """
        assert len(primary_candidates) > 0, "No primary candidates provided."
        self.primary_candidates = primary_candidates
    
    def get_nat_primary_environment(self):
        """
        Retrieves data on national primary polls.
        
        :return self.nat_primary_environment:
            Dict keying candidate names to their national polling averages.

        """
        return self.nat_primary_environment

    def add_polls(self, polls):
        """
        Adds a list of polls to the database.

        :param polls:
            The list of poll objects to add to the database.

        """
        self.polls = self.polls + polls

    def get_polls(self):
        """
        Retrieves a list of polls from the database.

        :return self.polls:
            The list of poll objects in the database.

        """
        return self.polls

class State:
    """Stores statistics for each state or territory."""
    def __init__(self, name, PVI, electors, pchispanic, pcwhite, pcblack,
                 pcasian, pcnative, status, elasticity, pop1000s, date,
                 delegates, region, primary_polling={}, state_sims={}):
        """
        Initialises a state object.
        
        :param name:
            The name of the state.
        :param PVI:
            The partisan voting index of the state, measuring its leans
            Democratic/Republican lean, None if no data is available.
        :param electors:
            The number of electors the state send to the electoral college,
            None if it is not a state or DC.
        :param pchispanic:
            The percentage of the state's population who identify as Hispanic
            as of 2019.
        :param pcwhite:
            The percentage of the state's population who identify as White as
            of 2019.
        :param pcblack:
            The percentage of the state's population who identify as Black as
            of 2019.
        :param pcasian:
            The percentage of the state's population who identify as Asian as
            of 2019.
        :param pcnative:
            The percentage of the state's population who identify as Native
            American as of 2019.
        :param status:
            Classification of whether the object is a state, a territory
            (incorporated or unincorporated), a congressional district, or the
            District of Columbia as of 2019.
        :param elasticity:
            Measurement that when multiplied by the national level swing
            provides the expected swing in the state.
        :param pop1000s:
            The population of the state in thousands.
        :param date:
            The date on which the state will host its 2020 Democratic primary
            or caucus as a datetime object.
        :param delegates:
            The number of pledged delegates the state has in the 2020
            Democratic primary.
        :param primary_polling:
            Dict keying candidate names to percentage polling in the state, and
            a "confidence" key with a value representing the quality and
            quantity of data used to find this average.
        :param region:
            String giving the region of the USA the state is in.
        :param state_sims:
            Dict keying the names of other states to a coefficient between 0
            and 1 describing the similarities in their political behaivours.

        """
        self.name = name
        self.PVI = PVI
        self.electors = electors
        self.pchispanic = pchispanic
        self.pcwhite = pcwhite
        self.pcblack = pcblack
        self.pcasian = pcasian
        self.pcnative = pcnative
        self.status = status
        self.elasticity = elasticity
        self.pop1000s = pop1000s
        self.date = date
        self.delegates = delegates
        self.primary_polling = primary_polling
        self.region = region
        self.state_sims = state_sims

    def get_raw_primary_result(self, nat_environment, base_nat_environment, 
                               candidates, db):
        """
        Calculates the unadjusted result of the vote in the state's primary.

        :param nat_environment:
            A dict where the keys are candidate surnames and the values are
            their probabilistically predicted % standings in national polls at
            the time of this primary. Additionally the key "confidence" has a
            value representing the confidence in national polling based on the
            quantity and quality of data available, scored from 0 to 1.
        :param base_nat_environment:
            The means of the distributions used to predict the nat_environment.
        :param candidates:
            A list of candidates in the 2020 Democratic Primary race.
        :param db:
            The database object storing the data.
        :return result:
            A dict keying candidate names to the percentage share of the vote
            they are probabilistically predicted to win in this primary. Also
            has a "confidence" key with associated value from 0 to 1.
        
        """
        state_environment = self.get_primary_polling()

        # Account for the difference in national environment between polling
        # and this simulation by finding the difference between them and
        # applying it to the state level polls.
        for candidate in candidates:
            difference = (nat_environment[candidate] - 
                      base_nat_environment[candidate])
            state_environment[candidate] = (state_environment[candidate] + 
                                            difference)

        # Adjust the result to account for state similarities.
        state_environment = ss.apply_comparison(state_environment, db,
                                                self.state_sims)
        
        # Get days left until the election. This is used to gauge uncertainty.
        today = datetime.date.today()
        primary_date = self.date
        time_left = today - primary_date
        days_left = time_left/datetime.timedelta(days=1)
        if days_left < 0:
            days_left = 0

        # Apply random variation to the state results.
        result = vp.random_variation(state_environment, days_left)

        # Prevent any results from being less than zero.
        for candidate in result:
            if candidate != "confidence":
                if result[candidate] < 0:
                    result[candidate] = 0

        # Rebalance support such that the percentages add to 100.
        result = vp.rebalance(state_environment)

        # This is now a result, so set confidence to 1.
        result["confidence"] = 1

        return result

    def distribute_delegates(self, result):
        """
        Approximates the distribution of delegates in the state's primary.

        :param result:
            Dict keying candidate names to their share of the vote, keying
            the string "confidence" to the confidence in the result.
        :return delegates:
            Dict keying candidates to the number of pledged delegates they
            receive from this state's primary.
        
        """
        num_delegates = self.delegates 

        # A dict keying % popular vote to expected proportion of delegates, up
        # to 25% of the popular vote, where delegate share becomes proportional
        # to vote share.
        conversion = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:1, 8:1, 9:1, 10:2,
                      11:2, 12:2, 13:3, 14:5, 15:12, 16:14, 17:15, 18:17,
                      19:18, 20:19, 21:20, 22:21, 23:23, 24:24, 25:25}

        # Find the expected percentage of delegates each candidate should win.
        pc_dels = {}
        for candidate in result:
            if candidate != "confidence":
                votes = result[candidate]
                if votes > 25:
                    pc_dels[candidate] = votes
                else:
                    pc_dels[candidate] = conversion[round(votes)]
        pc_dels = vp.rebalance(pc_dels)

        # Convert the percentages into numbers of delegates
        delegates = {}
        total_dels_distributed = 0
        for candidate in pc_dels:
            dels = round(pc_dels[candidate]*num_delegates/100)
            delegates[candidate] = dels
            total_dels_distributed = total_dels_distributed + dels

        # Account for the fact that due to rounding error, an incorrect number
        # of delegates may have been distributed, and redistribute as
        # necessary.
        unassigned_dels = num_delegates - total_dels_distributed
        if unassigned_dels > 0:
                delegates = vp.assign_leftover_delegates(delegates, pc_dels,
                                                         unassigned_dels)
        elif unassigned_dels < 0:
                delegates = vp.unassign_extra_delegates(delegates, pc_dels, 
                                                        -unassigned_dels)

        return delegates

    def get_PVI(self):
        """
        Retrieves the partisan voting index of the state.

        :return self.PVI:
            The state's PVI.

        """
        return self.PVI

    def get_pcwhite(self):
        """
        Retrieves the percentage of the state's population who identify as
        white.

        :return self.pcwhite:
            The percentage of the state's population who identify as white.

        """
        return self.pcwhite

    def get_pcblack(self):
        """
        Retrieves the percentage of the state's population who identify as
        black.

        :return self.pcblack:
            The percentage of the state's population who identify as black.

        """
        return self.pcblack

    def get_pchispanic(self):
        """
        Retrieves the percentage of the state's population who identify as
        hispanic.

        :return self.pchispanic:
            The percentage of the state's population who identify as hispanic.

        """
        return self.pchispanic

    def get_pcasian(self):
        """
        Retrieves the percentage of the state's population who identify as
        asian.

        :return self.pcasian:
            The percentage of the state's population who identify as asian.

        """
        return self.pcasian
    
    def get_pcnative(self):
        """
        Retrieves the percentage of the state's population who identify as
        native american.

        :return self.pcwhite:
            The percentage of the state's population who identify as native
            american.

        """
        return self.pcnative

    def get_delegates(self):
        """
        Retrieves the number of pledged delegates the state has.

        :return self.delegates:
            The number of delegates.

        """
        return self.delegates

    def get_primary_polling(self):
        """
        Retrieves the average of the primary polling data for the state.

        :return self.primary_polling:
            Dict keying candidate names to their average % polling in the state
            and a "confidence" key with a value representing the quality and
            quantity of data gone into forming this average.

        """
        return self.primary_polling

    def get_region(self):
        """
        Retrieves the region the state is in.

        :return self.region:
            String giving the region.

        """
        return self.region

    def get_state_sims(self):
        """
        Retrieves the dict giving similarities to other states.

        :return self.state_sims:
            Dict keying state names to coefficients betwwen 0 and 1 describing
            the political similarity of the two states.

        """
        return self.state_sims

    def set_state_sims(self, sims):
        """
        Sets the dict giving poltical similarity coefficients to other states.

        :param sims:
            Dict keying state names to coefficients betwwen 0 and 1 describing
            the political similarity of the two states.

        """
        for state in sims:
            assert sims[state] >= 0, "State similarity is negative."
            assert sims[state] <= 1, "State similarity is > 1."
        self.state_sims = sims

    def get_date(self):
        """
        Retrieves the date of the state's primary.

        :return self.date:
            A datetime.date object containing the date for the primary.

        """
        return self.date

class PrimaryDate:
    """Represents a single day of primaries."""
    def __init__(self, date, primaries):
        """
        Store data on a day of primaries.

        :param date:
            A datetime object storing the date of the primaries.
        :param primaries:
            A list of the names of states that have their primaries that day.

        """
        self.date = date
        self.primaries = primaries

    def get_primaries(self):
        """
        Retrieves the list of primaries happening on this date.

        :return self.primaries:
            A list of strings, each of which is the name of a state with a
            primary on this date.

        """
        return self.primaries

class Poll:
    """Represents a single opinion poll."""
    def __init__(self, question, location, weight, result, date):
        """
        Store data about a poll.

        :param question:
            A string saying what the poll is asking about, such as "Primary".
        :param location:
            A string saying where the poll was conducted, e.g. "USA" or "Iowa".
        :param weight:
            A number representing the weight afforded to the poll in
            calculating weighted polling averages, based on number of
            respondents, type of respondents (e.g. likely voters, registered
            voters, adults), pollster and official margin of error.
        :param result:
            A dict keying names of the options on the poll (usually candidates)
            to their percentage share of the vote in the poll.
        :param date:
            A datetime.date object stating the final day on which data was
            collected for the poll. Note that the distinction between the date
            on which data was collected and when the poll was published may be
            significant.
        
        """
        self.question = question
        self.location = location
        self.weight = weight
        self.result = result
        self.date = date

    def get_location(self):
        """
        Retrieves the place where the poll was performed.

        :return self.location:
            A string giving the location.

        """
        return self.location

    def get_weight(self):
        """
        Retrieves the weight of the poll, which could also be decribed as its
        quality or reliability.

        :return self.weight:
            A small number giving the weight of the poll.

        """
        return self.weight

    def set_weight(self, weight):
        """
        Set the weight to attribute the poll when calculating polling averages.

        :param weight:
            The new weight to set.

        """
        assert weight > 0, "Poll has zero or negative weight."
        self.weight = weight

    def get_result(self):
        """
        Retrieves the results of the poll.

        :return self.result:
            A dict keying strings representing the options on the poll to the
            percentage of respondents who chose that option.

        """
        return self.result

    def get_date(self):
        """
        Retrieves the date of the last day of data collection of the poll.

        :return self.date:
            A datetime.date object containing the date for the poll.

        """
        return self.date

class PrimarySimulationResults:
    """Stores the results of a Democratic 2020 primary simulation"""
    def __init__(self, winner=None, final_delegates={}, most_delegates=None):
        """
        Creates a new object to store the results of one simulation.

        :param winner:
            The winner of the primary.
        :param final_delegates:
            Dict keying candidate names to their delegate totals at the end
            of the primary.
        :param most_delegates:
            String containing the name of the candidate with the most pledged
            delegates.
        
        """
        self.winner = winner
        self.final_delegates = final_delegates
        self.most_delegates = most_delegates

    def add_final_delegates(self, final_delegates):
        """
        Sets the final_delegates field giving the number of delegates each
        candidate has at the end of the primary and uses this to fill in the
        winner field.

        :param final_delegates:
            Dict keying candidate names to their pledged delegate counts at the
            end of the primary.
        
        """
        self.final_delegates = final_delegates
        self.winner = self.determine_winner(final_delegates)
        self.most_delegates = self.determine_most_delegates(final_delegates)

    def determine_winner(self, final_delegates):
        """
        Determines whether one candidate has won a majority on the first ballot
        or not and fills in the winner field accordingly.

        :param final_delegates:
            Dict keying candidate names to their pledged delegate counts at the
            end of the primary.
        :return candidate:
            The name of the winner of the primary, or "undecided" if no
            candidate has a first ballot majority.
        
        """
        total_pledged_delegates = 3769
        for candidate in final_delegates:
            if final_delegates[candidate] > total_pledged_delegates/2:
                return candidate
        return "No majority"

    def determine_most_delegates(self, final_delegates):
        """
        Determines which candidate has the most delegates.

        :param final_delegates:
            Dict keying candidate names to their pledged delegate counts at the
            end of the primary.
        :return highest_candidate:
            The name of the candidate with the most pledged delegates.
        
        """
        highest_candidate = None
        highest_max_dels = 0
        for candidate in final_delegates:
            if final_delegates[candidate] > highest_max_dels:
                highest_max_dels = final_delegates[candidate]
                highest_candidate = candidate
        return highest_candidate