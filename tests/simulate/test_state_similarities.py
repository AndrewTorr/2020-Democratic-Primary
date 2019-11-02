"""Testing functionality for the state_similarities module."""

import unittest
import database
import datetime
import constants as c
import simulate.state_similarities as ss

class TestFindSimilarity(unittest.TestCase):
    """
    Tests the find_similarity function, which calculates a metric for the
    political similarity of two states.
    
    """
    def test_similar_states(self):
        """Tests the case where the two states are politically similar."""
        ND = database.State(c.S_NORTH_DAKOTA, 17, 3, 3.5, 84.4, 3.0, 1.7, 5.4, c.T_STATE, 0.98, 760, datetime.date(2019, 3, 10), 14, c.R_MIDWEST)
        SD = database.State(c.S_SOUTH_DAKOTA, 14, 3, 3.6, 82.3, 1.9, 1.2, 8.6, c.T_STATE, 1.01, 882, datetime.date(2019, 6, 2),  14, c.R_MIDWEST)
        similarity = ss.find_similarity(ND, SD)
        print(similarity)
        self.assertGreater(similarity, 0.9)
        self.assertLessEqual(similarity, 1)
    
    def test_dissimilar_states(self):
        """Tests the case where the two states are politically dissimilar."""
        ND = database.State(c.S_NORTH_DAKOTA, 17, 3, 3.5, 84.4, 3.0, 1.7, 5.4, c.T_STATE, 0.98, 760, datetime.date(2019, 3, 10), 14, c.R_MIDWEST)
        DC = database.State(c.S_DC, -43, 3, 11.0, 36.5, 45.3, 4.0, 0.2, c.T_DC, 0.80, 702, datetime.date(2019, 6, 16), 17, c.R_SOUTH)
        similarity = ss.find_similarity(ND, DC)
        print(similarity)
        self.assertLess(similarity, 0.1)
        self.assertGreaterEqual(similarity, 0)

if __name__ == '__main__':
    unittest.main()