"""
GroupCalculator Test Module
===========================

This module contains unit tests for the GroupCalculator class.

.. inheritance-diagram:: test.groupcalculator_test
   :parts: 1

.. autosummary::
   :toctree: generated/

   TestGroupCalculator
"""

import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add parent directory to path to import the module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from groupbuilder.groupcalculator import GroupCalculator
from groupbuilder.core.exceptions import AmountPeopleError


class TestGroupCalculator(unittest.TestCase):
    """
    Test cases for the GroupCalculator class.

    This test suite verifies the functionality of the GroupCalculator class
    including initialization, group creation, and group management.

    .. inheritance-diagram:: test.groupcalculator_test.TestGroupCalculator
       :parts: 1

    .. autosummary::
       :toctree: generated/

       setUp
       test_init_valid_parameters
       test_init_invalid_parameters
       test_reset_groups
       test_create_groups
       test_create_multiple_rounds
       test_can_repeat
       test_get_current_groups
       test_get_all_groups
       test_usable_indexes
       test_visualize_groups
       test_multiple_rounds_unique_assignments
    """

    def setUp(self):
        """
        Set up test fixtures before each test method.

        Creates a valid GroupCalculator instance for use in tests.

        :return: None
        :rtype: None

        .. autosummary::
           :toctree: generated/
        """
        self.valid_people = 12
        self.valid_group_size = 4
        self.calculator = GroupCalculator(self.valid_people, self.valid_group_size)

    def test_init_valid_parameters(self):
        """
        Test initialization with valid parameters.

        Verifies that a GroupCalculator can be successfully created with valid parameters.

        :return: None
        :rtype: None

        .. autosummary::
           :toctree: generated/
        """
        calculator = GroupCalculator(12, 4)
        self.assertIsNotNone(calculator)

    def test_init_invalid_parameters(self):
        """
        Test initialization with invalid parameters.

        Verifies that appropriate exceptions are raised when invalid parameters are provided.

        :return: None
        :rtype: None

        .. autosummary::
           :toctree: generated/
        """
        # Test when people < group_size
        with self.assertRaises(AmountPeopleError):
            GroupCalculator(3, 4)

        # Test with negative values
        with self.assertRaises(AmountPeopleError):
            GroupCalculator(-1, 4)

        with self.assertRaises(AmountPeopleError):
            GroupCalculator(12, -1)

    def test_reset_groups(self):
        """
        Test resetting groups.

        Verifies that the reset_groups method properly clears all generated groups.

        :return: None
        :rtype: None

        .. autosummary::
           :toctree: generated/
        """
        # Generate some groups first
        self.calculator.create_groups()

        # Get current groups
        current_groups = self.calculator.get_current_groups()
        self.assertNotEqual(current_groups, {})

        # Reset groups
        self.calculator.reset_groups()

        # Get groups again, should be empty
        new_groups = self.calculator.get_current_groups()
        self.assertEqual(new_groups, {})

    def test_create_groups(self):
        """
        Test creating groups.

        Verifies that groups are correctly created with the right structure and size.

        :return: None
        :rtype: None

        .. autosummary::
           :toctree: generated/
        """
        # Initially no groups
        initial_groups = self.calculator.get_current_groups()
        self.assertEqual(initial_groups, {})

        # Create groups
        self.calculator.create_groups()

        # Check that groups were created
        groups = self.calculator.get_current_groups()
        self.assertNotEqual(groups, {})

        # Check group structure
        self.assertEqual(len(groups), self.valid_people // self.valid_group_size)

        # Check that each group has the correct size
        for group in groups.values():
            self.assertEqual(len(group), self.valid_group_size)

    def test_create_multiple_rounds(self):
        """
        Test creating multiple rounds of groups.

        Verifies that multiple rounds can be created and that they differ from each other.

        :return: None
        :rtype: None

        .. autosummary::
           :toctree: generated/
        """
        # Create first round
        self.calculator.create_groups()
        first_round = self.calculator.get_current_groups()

        # Create second round
        self.calculator.create_groups()
        second_round = self.calculator.get_current_groups()

        # Groups should be different
        self.assertNotEqual(first_round, second_round)

        # Get all groups and verify structure
        all_groups = self.calculator.get_all_groups()
        self.assertEqual(len(all_groups), 2)  # Two rounds

    def test_can_repeat(self):
        """
        Test the can_repeat method.

        Verifies that the can_repeat method correctly calculates the maximum number of rounds.

        :return: None
        :rtype: None

        .. autosummary::
           :toctree: generated/
        """
        max_rounds = self.calculator.can_repeat()

        # For 12 people in groups of 4, max rounds should be 165
        self.assertEqual(max_rounds, 165)

        # Test with different parameters
        calculator = GroupCalculator(10, 2)
        self.assertEqual(calculator.can_repeat(), 9)

    def test_get_current_groups(self):
        """
        Test getting current groups.

        Verifies that the get_current_groups method returns the correct structure.

        :return: None
        :rtype: None

        .. autosummary::
           :toctree: generated/
        """
        # No groups initially
        self.assertEqual(self.calculator.get_current_groups(), {})

        # Create groups
        self.calculator.create_groups()

        # Check structure of returned groups
        groups = self.calculator.get_current_groups()
        self.assertIsInstance(groups, dict)

        # With 12 people and group size 4, should have 3 groups
        self.assertEqual(len(groups), 3)

        # Check that keys are letters (A, B, C) when usable_indexes is False
        expected_keys = ['A', 'B', 'C']
        self.assertEqual(list(groups.keys()), expected_keys)

    def test_get_all_groups(self):
        """
        Test getting all groups.

        Verifies that the get_all_groups method returns the correct nested structure.

        :return: None
        :rtype: None

        .. autosummary::
           :toctree: generated/
        """
        # No groups initially
        self.assertEqual(self.calculator.get_all_groups(), {})

        # Create two rounds
        self.calculator.create_groups()
        self.calculator.create_groups()

        # Get all groups
        all_groups = self.calculator.get_all_groups()

        # Should have 2 rounds
        self.assertEqual(len(all_groups), 2)

        # Check structure
        for round_num, round_groups in all_groups.items():
            self.assertIsInstance(round_num, int)
            self.assertIsInstance(round_groups, dict)
            self.assertEqual(len(round_groups), 3)  # 3 groups per round

    def test_usable_indexes(self):
        """
        Test with usable_indexes=True.

        Verifies that the usable_indexes parameter correctly changes group identifiers.

        :return: None
        :rtype: None

        .. autosummary::
           :toctree: generated/
        """
        calculator = GroupCalculator(12, 4, usable_indexes=True)
        calculator.create_groups()

        groups = calculator.get_current_groups()

        # Keys should be integers (0, 1, 2) instead of letters
        expected_keys = [0, 1, 2]
        self.assertEqual(list(groups.keys()), expected_keys)

    def test_visualize_groups(self):
        """
        Test visualize_groups method.

        Verifies that the visualize_groups method outputs to console correctly.

        :return: None
        :rtype: None

        .. autosummary::
           :toctree: generated/
        """
        # Create some groups
        self.calculator.create_groups()

        # Mock print function to capture output
        with patch('builtins.print') as mock_print:
            self.calculator.visualize_groups()

            # Should have called print at least once
            self.assertTrue(mock_print.called)

    def test_multiple_rounds_unique_assignments(self):
        """
        Test that people are uniquely assigned across rounds.

        Verifies that each person is never grouped with the same other person twice.

        :return: None
        :rtype: None

        .. autosummary::
           :toctree: generated/
        """
        # Create calculator with 6 people in groups of 2
        calculator = GroupCalculator(6, 2)

        # Generate all possible rounds (should be 3 of 5 rounds)
        max_rounds = calculator.can_repeat()
        for _ in range(max_rounds):
            if _ == 3:  # excpet StopIteration
                with self.assertRaises(StopIteration):
                    calculator.create_groups()
                break
            calculator.create_groups()

        all_groups = calculator.get_all_groups()

        # Check that each person is never in the same group with the same other person twice
        person_pairings = set()
        for round_num, round_groups in all_groups.items():
            for group_id, group in round_groups.items():
                # Check all pairs of people in this group
                for i in range(len(group)):
                    for j in range(i+1, len(group)):
                        pair = (min(group[i], group[j]), max(group[i], group[j]))
                        # This pair should not have been seen before
                        self.assertNotIn(pair, person_pairings)
                        person_pairings.add(pair)


if __name__ == '__main__':
    unittest.main()