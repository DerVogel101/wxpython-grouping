import threading
import wx

from groupbuilder import GroupingAlgorithm
from groupbuilder.core import GroupConfig


class RoundWorkerThread(threading.Thread):
    def __init__(self, parent, config):
        super().__init__()
        self._algorithm: GroupingAlgorithm | None = None
        self._parent = parent
        self._stop_flag = False
        self._config: GroupConfig = config
        self._pause_event = threading.Event()
        self._pause_event.set()

    def run(self):
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
        self._pause_event.clear()
        wx.CallAfter(self._parent.update_status, True)

    def resume(self):
        self._pause_event.set()
        wx.CallAfter(self._parent.update_status, False)

    def stop(self):
        self._stop_flag = True
        self._parent.worker_running = False