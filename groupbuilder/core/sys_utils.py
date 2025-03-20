import psutil

class SysUtils:
    """
    Utility class for system information.

    This class provides static methods to retrieve various system metrics
    such as CPU count and memory usage.

    .. inheritance-diagram:: groupbuilder.core.sys_utils.SysUtils
       :parts: 1

    .. autosummary::
       :toctree: generated/

       get_cpu_count
       get_available_memory
       get_used_memory
       get_total_memory
    """
    @staticmethod
    def get_cpu_count() -> int:
        """
        Returns the number of physical CPU cores.

        :return: Number of physical CPU cores
        :rtype: int
        """
        return psutil.cpu_count(logical=False)

    @staticmethod
    def get_available_memory() -> int:
        """
        Returns the available memory in MB.

        :return: Available memory in megabytes
        :rtype: int
        """
        return psutil.virtual_memory().available // 1024 // 1024

    @staticmethod
    def get_used_memory() -> int:
        """
        Returns the used memory in MB.

        :return: Used memory in megabytes
        :rtype: int
        """
        return psutil.virtual_memory().used // 1024 // 1024

    @staticmethod
    def get_total_memory() -> int:
        """
        Returns the total memory in MB.

        :return: Total memory in megabytes
        :rtype: int
        """
        return psutil.virtual_memory().total // 1024 // 1024

if __name__ == "__main__":
    print(SysUtils.get_cpu_count())
    print(SysUtils.get_available_memory())
    print(SysUtils.get_used_memory())
    print(SysUtils.get_total_memory())