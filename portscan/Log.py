import logging
import datetime
import os
import time

__all__ = [
    'send_log'
]

LOG_FILE = "/var/log/python-portscan/log"
os.system("mkdir -p /var/log/python-portscan && touch /var/log/python-portscan/log")
logging.basicConfig(filename=LOG_FILE, level=logging.INFO)


def send_log(message):
  """Logging method used throughout python-portscan"""
  logging.info(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + " " + message)

# stuff to run always here such as class/def
#def main():


#if __name__ == "__main__":
  # stuff only to run when not called via 'import' here
#  main()
