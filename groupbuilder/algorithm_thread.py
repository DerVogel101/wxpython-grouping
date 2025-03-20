"""
Algorithm Thread Module
======================

This module provides threading functionality to execute the grouping algorithm
in the background while keeping the main UI responsive.

.. inheritance-diagram:: groupbuilder.algorithm_thread
   :parts: 1

.. autosummary::
   :toctree: generated/

   RoundWorkerThread
"""

import threading
import wx

from groupbuilder import GroupingAlgorithm
from groupbuilder.core import GroupConfig


class RoundWorkerThread(threading.Thread):
    """
    A worker thread that generates group assignment rounds in the background.

    This thread handles the execution of the grouping algorithm while allowing
    the main UI thread to remain responsive. It supports pausing, resuming,
    and stopping the generation process.

    .. inheritance-diagram:: groupbuilder.algorithm_thread.RoundWorkerThread
       :parts: 1

    .. autosummary::
       :toctree: generated/

       __init__
       run
       pause
       resume
       stop
    """
    def __init__(self, parent, config):
        """
        Initialize the round worker thread.

        :param parent: The parent object that will receive callback notifications.
        :type parent: object
        :param config: Configuration settings for the grouping algorithm.
        :type config: GroupConfig
        """
        super().__init__()
        self._algorithm: GroupingAlgorithm | None = None
        self._parent = parent
        self._stop_flag = False
        self._config: GroupConfig = config
        self._pause_event = threading.Event()
        self._pause_event.set()

    def run(self):
        """
        Main execution method of the thread.

        Sets up the GroupingAlgorithm and continuously generates new rounds
        until either stopped or the algorithm reaches its end. Updates the
        parent object with progress information via wx.CallAfter.

        :raises: No explicit exceptions, but may propagate exceptions from GroupingAlgorithm
        """
        wx.CallAfter(self._parent.setup_status)
        self._algorithm = GroupingAlgorithm(self._config)
        wx.CallAfter(self._parent.update_status, False)
        while not self._stop_flag:
            self._pause_event.wait()
            try:
                self._algorithm.generate_next_round()
                current_round = self._algorithm.get_round()
                wx.CallAfter(self._parent.on_round_generated, current_round, len(self._algorithm._rounds),
                             self._algorithm.get_max_rounds(), not self._pause_event.is_set())
            except StopIteration:
                self._parent.worker_running = False
                break

    def pause(self):
        """
        Pause the generation process.

        Clears the pause event, causing the thread to wait at the next
        pause_event.wait() call, and updates the UI status.

        :return: None
        :rtype: None
        """
        self._pause_event.clear()
        wx.CallAfter(self._parent.update_status, True)

    def resume(self):
        """
        Resume the generation process.

        Sets the pause event, allowing the thread to continue execution,
        and updates the UI status.

        :return: None
        :rtype: None
        """
        self._pause_event.set()
        wx.CallAfter(self._parent.update_status, False)

    def stop(self):
        """
        Stop the generation process.

        Sets the stop flag to True, which will cause the run method to
        exit its loop, and updates the worker status in the parent.

        :return: None
        :rtype: None
        """
        self._stop_flag = True
        self._parent.worker_running = False