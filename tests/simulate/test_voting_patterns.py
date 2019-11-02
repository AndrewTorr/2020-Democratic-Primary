"""Testing functionality for the voting_patterns module."""

import unittest
import constants as c
import simulate.voting_patterns as vp

class TestRandomVariation(unittest.TestCase):
    """
    Tests the random_variation function, which applies random variation to
    polling numbers with appropriate standard deviation.
    
    """
    def test_standard_case(self):
        """Checks method runs correctly under typical inputs."""
        average = {c.C_BIDEN:30, c.C_WARREN:30, c.C_SANDERS:20,
                   c.C_BUTTIGIEG:20, "confidence":0.5}
        result = vp.random_variation(average, 25)
        self.assertEqual(result["confidence"], 0.5)
        self.assertIn(c.C_BIDEN, result)
        self.assertIn(c.C_WARREN, result)
        self.assertIn(c.C_SANDERS, result)
        self.assertIn(c.C_BUTTIGIEG, result)

    def test_negative_days_left(self):
        """Tests case where days_left is negative."""
        average = {c.C_BIDEN:30, c.C_WARREN:30, c.C_SANDERS:20,
                   c.C_BUTTIGIEG:20, "confidence":0.5}
        with self.assertRaises(ValueError):
            result = vp.random_variation(average, -100)

    def test_negative_confidence(self):
        """Tests case where the confidence is negative."""
        average = {c.C_BIDEN:30, c.C_WARREN:30, c.C_SANDERS:20,
                   c.C_BUTTIGIEG:20, "confidence":-1}
        with self.assertRaises(ValueError):
            result = vp.random_variation(average, 25)

class TestPrimaryTacticalVoting(unittest.TestCase):
    """
    Tests the primary_tactical_voting function, which adjusts national
    popular vote statistics.
    
    """
    def test_standard_case(self):
        """Checks method runs correctly under typical inputs."""
        average = {c.C_BIDEN:30, c.C_WARREN:30, c.C_SANDERS:20,
                   c.C_BUTTIGIEG:20}
        delegates = {c.C_BIDEN:357, c.C_WARREN:239, c.C_SANDERS:101,
                   c.C_BUTTIGIEG:25}
        result = vp.primary_tactical_voting(average, delegates)
        self.assertIn(c.C_BIDEN, result)
        self.assertIn(c.C_WARREN, result)
        self.assertIn(c.C_SANDERS, result)
        self.assertIn(c.C_BUTTIGIEG, result)

    def test_negative_delegates(self):
        """Tests case where one candidate has negative delegates."""
        average = {c.C_BIDEN:30, c.C_WARREN:30, c.C_SANDERS:20,
                   c.C_BUTTIGIEG:20}
        delegates = {c.C_BIDEN:357, c.C_WARREN:239, c.C_SANDERS:101,
                   c.C_BUTTIGIEG:-25}
        with self.assertRaises(ValueError):
            result = vp.primary_tactical_voting(average, delegates)

    def test_negative_support(self):
        """Tests case where one candidate has negative support."""
        average = {c.C_BIDEN:40, c.C_WARREN:31, c.C_SANDERS:31,
                   c.C_BUTTIGIEG:-2}
        delegates = {c.C_BIDEN:357, c.C_WARREN:239, c.C_SANDERS:101,
                   c.C_BUTTIGIEG:25}
        with self.assertRaises(ValueError):
            result = vp.primary_tactical_voting(average, delegates)

class TestRebalance(unittest.TestCase):
    """
    Tests the rebalance function, which adjusts a polling average or election
    result such that the popular vote adds to 100%.
    
    """
    def test_standard_case(self):
        """Checks method runs correctly under typical inputs."""
        average = {c.C_BIDEN:30, c.C_WARREN:30, c.C_SANDERS:20,
                   c.C_BUTTIGIEG:20}
        result = vp.rebalance(average)
        self.assertIn(c.C_BIDEN, result)
        self.assertIn(c.C_WARREN, result)
        self.assertIn(c.C_SANDERS, result)
        self.assertIn(c.C_BUTTIGIEG, result)
        total = 0
        for candidate in result:
            total = total + result[candidate]
        self.assertEqual(total, 100)

    def test_negative_support(self):
        """Tests case where one candidate has negative support."""
        average = {c.C_BIDEN:40, c.C_WARREN:31, c.C_SANDERS:31,
                   c.C_BUTTIGIEG:-2}
        with self.assertRaises(ValueError):
            result = vp.rebalance(average)

class TestAssignLeftoverDelegates(unittest.TestCase):
    """
    Tests the assign_leftover_delegates function, which assists with correct
    distribution of delegates in a primary.
    
    """
    def test_standard_case(self):
        """Checks method runs correctly under typical inputs."""
        delegates = {c.C_BIDEN:51, c.C_WARREN:34, c.C_SANDERS:11,
                     c.C_BUTTIGIEG:2}
        pc_dels = {c.C_BIDEN:52, c.C_WARREN:35, c.C_SANDERS:11,
                     c.C_BUTTIGIEG:2}
        unassigned_dels = 2
        result = vp.assign_leftover_delegates(delegates, pc_dels,
                                              unassigned_dels)
        self.assertEqual(result, {c.C_BIDEN:52, c.C_WARREN:35, c.C_SANDERS:11,
                                  c.C_BUTTIGIEG:2})

    def test_negative_delegates(self):
        """Tests case where one candidate has negative delegates."""
        delegates = {c.C_BIDEN:51, c.C_WARREN:34, c.C_SANDERS:11,
                     c.C_BUTTIGIEG:-2}
        pc_dels = {c.C_BIDEN:52, c.C_WARREN:35, c.C_SANDERS:11,
                     c.C_BUTTIGIEG:2}
        unassigned_dels = 2
        with self.assertRaises(ValueError):
            result = vp.assign_leftover_delegates(delegates, pc_dels,
                                                  unassigned_dels)

    def test_negative_pc_dels(self):
        """Tests case where one candidate's entry in pc_dels is negative."""
        delegates = {c.C_BIDEN:51, c.C_WARREN:34, c.C_SANDERS:11,
                     c.C_BUTTIGIEG:2}
        pc_dels = {c.C_BIDEN:52, c.C_WARREN:35, c.C_SANDERS:11,
                     c.C_BUTTIGIEG:-2}
        unassigned_dels = 2
        with self.assertRaises(ValueError):
            result = vp.assign_leftover_delegates(delegates, pc_dels,
                                                  unassigned_dels)
    
    def test_negative_unassigned_dels(self):
        """Tests case where unassigned_dels is negative."""
        delegates = {c.C_BIDEN:51, c.C_WARREN:34, c.C_SANDERS:11,
                     c.C_BUTTIGIEG:2}
        pc_dels = {c.C_BIDEN:52, c.C_WARREN:35, c.C_SANDERS:11,
                     c.C_BUTTIGIEG:2}
        unassigned_dels = -2
        with self.assertRaises(ValueError):
            result = vp.assign_leftover_delegates(delegates, pc_dels,
                                                  unassigned_dels)

class TestUnassignExtraDelegates(unittest.TestCase):
    """
    Tests the unassign_extra_delegates function, which assists with correct
    distribution of delegates in a primary.
    
    """
    def test_standard_case(self):
        """Checks method runs correctly under typical inputs."""
        delegates = {c.C_BIDEN:52, c.C_WARREN:35, c.C_SANDERS:11,
                     c.C_BUTTIGIEG:2}
        pc_dels = {c.C_BIDEN:51, c.C_WARREN:34, c.C_SANDERS:11,
                     c.C_BUTTIGIEG:2}
        extra_dels = 2
        result = vp.unassign_extra_delegates(delegates, pc_dels,
                                             extra_dels)
        self.assertEqual(result, {c.C_BIDEN:51, c.C_WARREN:34, c.C_SANDERS:11,
                                  c.C_BUTTIGIEG:2})
    
    def test_negative_delegates(self):
        """Tests case where one candidate has negative delegates."""
        delegates = {c.C_BIDEN:51, c.C_WARREN:34, c.C_SANDERS:11,
                     c.C_BUTTIGIEG:-2}
        pc_dels = {c.C_BIDEN:52, c.C_WARREN:35, c.C_SANDERS:11,
                     c.C_BUTTIGIEG:2}
        extra_dels = 2
        with self.assertRaises(ValueError):
            result = vp.unassign_extra_delegates(delegates, pc_dels, 
                                                 extra_dels)

    def test_negative_pc_dels(self):
        """Tests case where one candidate's entry in pc_dels is negative."""
        delegates = {c.C_BIDEN:51, c.C_WARREN:34, c.C_SANDERS:11,
                     c.C_BUTTIGIEG:2}
        pc_dels = {c.C_BIDEN:52, c.C_WARREN:35, c.C_SANDERS:11,
                     c.C_BUTTIGIEG:-2}
        extra_dels = 2
        with self.assertRaises(ValueError):
            result = vp.unassign_extra_delegates(delegates, pc_dels,
                                                 extra_dels)
    
    def test_negative_unassigned_dels(self):
        """Tests case where unassigned_dels is negative."""
        delegates = {c.C_BIDEN:51, c.C_WARREN:34, c.C_SANDERS:11,
                     c.C_BUTTIGIEG:2}
        pc_dels = {c.C_BIDEN:52, c.C_WARREN:35, c.C_SANDERS:11,
                     c.C_BUTTIGIEG:2}
        extra_dels = -2
        with self.assertRaises(ValueError):
            result = vp.unassign_extra_delegates(delegates, pc_dels,
                                                 extra_dels)

if __name__ == '__main__':
    unittest.main()