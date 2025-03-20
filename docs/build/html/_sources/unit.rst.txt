Unit Test
=========
This is the unit test for the `groupbuilder.groupcalculator` module interface.

.. automodule:: test.groupcalculator_test
   :members:
   :special-members: __init__
   :undoc-members:
   :show-inheritance:

Why The App Is Manually Tested
=============================

The ``GroupApp`` component of our application is tested through manual testing rather than automated unit tests for several reasons:

GUI Testing Complexity
---------------------

The ``GroupApp`` class primarily implements a wxPython graphical user interface with numerous interactive elements:

- Event handlers for various UI controls
- Complex window layouts and sizing behaviors
- Modal dialogs for user interaction
- Dynamic grid-based data display

These GUI components are inherently difficult to test through traditional unit testing frameworks due to:

1. Event-driven architecture that relies on user interactions
2. Platform-specific behavior of window rendering
3. Visual elements that require human verification

Framework Limitations
--------------------

While tools exist for automated GUI testing, they present challenges:

- **Setup Complexity**: GUI test frameworks require significant configuration
- **Brittleness**: Tests often break with minor UI changes
- **Non-deterministic Behavior**: Race conditions in event handling
- **Test Environment Requirements**: Need for display servers or virtual displays

Focus on Core Logic Testing
--------------------------

Our testing strategy prioritizes comprehensive unit testing of the core logic:

.. code-block:: text

    ✓ GroupCalculator - Fully unit tested
    ✓ Core algorithms - Fully unit tested
    ⨯ GroupApp GUI - Manually tested

This approach ensures that the fundamental algorithms (the most critical components) have robust test coverage, while the presentation layer is verified through human interaction.

Manual Testing Protocol
---------------------

For the ``GroupApp`` component, we follow a structured manual testing protocol:

1. Verify CSV import/export functionality
2. Test group configuration parameter validation
3. Confirm proper display of generated groups
4. Validate worker thread pause/resume functions
5. Check proper sizing and layout across different window dimensions
6. Test error handling for invalid inputs

Future Considerations
-------------------

While current testing relies on manual verification, potential future improvements include:

- Integration testing for key workflows
- Snapshot testing for UI components
- Behavior-driven tests for critical user journeys

By combining thorough unit tests for core logic with systematic manual testing of the UI, we maintain high quality while acknowledging the practical limitations of automated GUI testing.