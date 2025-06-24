def shutdown_machine():
    import os
    import platform
    import subprocess

    try:
        if platform.system() == "Windows":
            subprocess.run(["shutdown", "/s", "/t", "0"], check=True)
        elif platform.system() == "Linux" or platform.system() == "Darwin":
            subprocess.run(["shutdown", "now"], check=True)
        else:
            raise Exception("Unsupported operating system")
    except Exception as e:
        print(f"Error during shutdown: {e}")