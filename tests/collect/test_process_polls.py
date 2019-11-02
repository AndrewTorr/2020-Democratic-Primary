"""Testing functionality for the process_polls module."""

import unittest
import datetime
import database
import constants as c
import collect.process_polls as pp

class TestDatePolls(unittest.TestCase):
    """
    Tests the date_polls function, which changes the weight attributed to polls
    based on how old they are.
    
    """
    def test_standard_case(self):
        """Checks method runs correctly under typical inputs."""
        today = datetime.date.today()
        polls = [database.Poll(c.Q_PRIMARY, c.S_USA, 1,
                 {c.C_BIDEN:40, c.C_WARREN:60}, datetime.date(2019, 11, 1)), 
                 database.Poll(c.Q_PRIMARY, c.S_USA, 1,
                 {c.C_BIDEN:50, c.C_WARREN:50}, datetime.date(2019, 10, 1))]
        dated_polls = pp.date_polls(polls, today)
        self.assertLess(dated_polls[0].weight, 1)
        self.assertLess(dated_polls[1].weight, 1)

    def test_none_polls(self):
        """Tests case where the list of polls is empty."""
        today = datetime.date.today()
        polls = None
        with self.assertRaises(TypeError):
            dated_polls = pp.date_polls(polls, today)

if __name__ == '__main__':
    unittest.main()