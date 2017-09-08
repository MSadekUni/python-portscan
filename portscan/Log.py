import logging
import datetime
import os
import time

__all__ = [
    'send_log'
]

def send_log(message):
  """Logging method used throughout python-portscan"""
  logging.info(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + " " + message)

# stuff to run always here such as class/def
def main():
  FULL_PATH = os.path.dirname(os.path.realpath(__file__)) + "/"
  LOG_FILE = FULL_PATH + ".log"
  logging.basicConfig(filename=LOG_FILE, level=logging.INFO)


if __name__ == "__main__":
  # stuff only to run when not called via 'import' here
  main()
