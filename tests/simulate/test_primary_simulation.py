"""Testing functionality for the primary_simulation module."""

import unittest
import constants as c
import database
import populate
import simulate.primary_simulation as ps

class TestSimulate(unittest.TestCase):
    """
    Tests the random_variation function, which applies random variation to
    polling numbers with appropriate standard deviation.
    
    """
    def test_standard_case(self):
        """Checks method runs correctly under typical inputs."""
        db = populate.populate()
        nat_environment = {c.C_BIDEN:30, c.C_WARREN:30, c.C_SANDERS:20,
                           c.C_BUTTIGIEG:20, "confidence":0.5}
        candidates = [c.C_BIDEN, c.C_WARREN, c.C_SANDERS, c.C_BUTTIGIEG]
        primary_calendar = db.get_primary_calendar()
        result = ps.simulate(db, nat_environment, candidates, primary_calendar)
        self.assertNotEqual(result.winner, None)

    def test_no_candidates(self):
        """Tests the case where there are no candidates provided."""
        db = populate.populate()
        nat_environment = {c.C_BIDEN:30, c.C_WARREN:30, c.C_SANDERS:20,
                           c.C_BUTTIGIEG:20, "confidence":0.5}
        candidates = []
        primary_calendar = db.get_primary_calendar()
        with self.assertRaises(ValueError):
            result = ps.simulate(db, nat_environment, candidates, primary_calendar)

    def test_negative_support(self):
        """Tests the case where one candidate has negative national support."""
        db = populate.populate()
        nat_environment = {c.C_BIDEN:40, c.C_WARREN:31, c.C_SANDERS:31,
                           c.C_BUTTIGIEG:-2, "confidence":0.5}
        candidates = [c.C_BIDEN, c.C_WARREN, c.C_SANDERS, c.C_BUTTIGIEG]
        primary_calendar = db.get_primary_calendar()
        with self.assertRaises(ValueError):
            result = ps.simulate(db, nat_environment, candidates, primary_calendar)

if __name__ == '__main__':
    unittest.main()