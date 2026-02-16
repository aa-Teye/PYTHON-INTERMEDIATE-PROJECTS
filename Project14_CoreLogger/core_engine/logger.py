import datetime
import os

class LogError(Exception):
    """Custom exception for logging failures."""
    pass

class BaseLogger:
    """Base class defining the logging interface."""
    def __init__(self, source_name):
        self.source_name = source_name

    def format_message(self, level, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"[{timestamp}] [{self.source_name}] [{level}] - {message}"

class ProductionLogger(BaseLogger):
    """A production-grade logger that handles file I/O safely."""
    def __init__(self, source_name, log_file="system.log"):
        # Initialize the parent class
        super().__init__(source_name)
        self.log_file = log_file

    def write_log(self, level, message):
        formatted = self.format_message(level, message)
        print(formatted) # Real-time console feedback
        
        try:
            with open(self.log_file, "a") as f:
                f.write(formatted + "\n")
        except IOError as e:
            # We don't just crash; we raise a meaningful error
            raise LogError(f"FileSystem Error: {e}")

    def info(self, message): self.write_log("INFO", message)
    def warning(self, message): self.write_log("WARN", message)
    def error(self, message): self.write_log("ERROR", message)