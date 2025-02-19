import psutil

class SysUtils:
    """Utility class for system information"""
    @staticmethod
    def get_cpu_count() -> int:
        """Returns the number of CPU cores"""
        return psutil.cpu_count(logical=False)

    @staticmethod
    def get_available_memory() -> int:
        """Returns the available memory in MB"""
        return psutil.virtual_memory().available // 1024 // 1024

    @staticmethod
    def get_used_memory() -> int:
        """Returns the used memory in MB"""
        return psutil.virtual_memory().used // 1024 // 1024

    @staticmethod
    def get_total_memory() -> int:
        """Returns the total memory in MB"""
        return psutil.virtual_memory().total // 1024 // 1024

if __name__ == "__main__":
    print(SysUtils.get_cpu_count())
    print(SysUtils.get_available_memory())
    print(SysUtils.get_used_memory())
    print(SysUtils.get_total_memory())