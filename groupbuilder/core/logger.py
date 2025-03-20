import logging
from termcolor import colored


class ColoredLogger(logging.StreamHandler):
   """
   A custom logging handler that adds color to output messages.

   This handler extends the built-in StreamHandler and overrides the emit method
   to add color to log messages based on their logging level.

   .. inheritance-diagram:: groupbuilder.core.logger.ColoredLogger
      :parts: 1

   .. autosummary::
      :toctree: generated/

      emit
   """

   #: Dictionary mapping logging levels to their corresponding colors
   COLORS = {
       logging.DEBUG: 'blue',
       logging.INFO: 'green',
       logging.WARNING: 'yellow',
       logging.ERROR: 'red',
       logging.CRITICAL: 'magenta',
   }

   def emit(self, record):
       """
       Override the emit method to add color to log messages.

       This method formats the record, retrieves the color corresponding to the
       record's level, and writes the colored message to the stream.

       :param record: The log record to emit
       :type record: logging.LogRecord
       """
       try:
           message = self.format(record)
           color = self.COLORS.get(record.levelno)
           self.stream.write(colored(message, color) + self.terminator)
           self.flush()
       except Exception:
           self.handleError(record)


class CustomLogger:
   """
   A wrapper around the built-in Logger class.

   This class sets up a colored logger with a given application name and provides
   an easy way to create customized loggers for different parts of an application.

   .. inheritance-diagram:: groupbuilder.core.logger.CustomLogger
      :parts: 1

   .. autosummary::
      :toctree: generated/

      __init__
   """

   def __init__(self, application_name: str):
       """
       Initialize a new instance of the CustomLogger class.

       :param application_name: The name of the application. Used as the logger name
       :type application_name: str
       """
       #: The underlying logger instance
       self.logger = logging.getLogger(application_name)

       # Set up a colored logger handler and add it to the logger
       handler = ColoredLogger()
       formatter = logging.Formatter('%(levelname)s - %(filename)s:%(lineno)d - %(message)s')
       handler.setFormatter(formatter)
       self.logger.addHandler(handler)


if __name__ == '__main__':
   log = CustomLogger('Test').logger
   log.setLevel(logging.DEBUG)
   log.debug('Debug message')
   log.info('Info message')
   log.warning('Warning message')
   log.error('Error message')
   log.critical('Critical message')