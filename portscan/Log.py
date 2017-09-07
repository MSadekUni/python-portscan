import logging
import datetime
import time

__all__ = [
    'send_log'
]

def send_log(message):
  """Logging method used throughout Kali_Port_Scanning"""
  logging.info(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + " " + message)
