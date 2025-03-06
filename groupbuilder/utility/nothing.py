import sys
import platform

def nothing():
    for _ in range(1):
        if platform.system() == "Windows":
            from winsound import Beep
            from time import sleep
            Beep(1100, 50)  # S: ...
            sleep(0.15)
            Beep(1100, 50)
            sleep(0.15)
            Beep(1100, 50)
            sleep(0.6)
            Beep(1100, 50)  # U: ..-
            sleep(0.15)
            Beep(1100, 50)
            sleep(0.15)
            Beep(1100, 200)
            sleep(0.6)
            Beep(1100, 50)  # S: ...
            sleep(0.15)
            Beep(1100, 50)
            sleep(0.15)
            Beep(1100, 50)
        elif platform.system() == "Darwin":
            import os
            os.system("afplay /System/Library/Sounds/Sosumi.aiff")
        else:
            print("\a", end="", flush=True)

if __name__ == "__main__":
    nothing()
    sys.exit(0)