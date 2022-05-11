from parse_config import Parse, tests
from schedule import Schedule
import argparse
# import daemon
# import sys
# import time
# import datetime
# import rest_api
# import psjson
# import os
# import signal
# import ssid_scan
# import connect_bssid
# import json
# import warnings
# import pika
# import syslog
# import traceback
# import multiprocessing
# import subprocess as sp
# from batch.pscheduler.pscheduler.batchprocessor import BatchProcessor


parser = argparse.ArgumentParser(description='pSSID')
parser.add_argument('file', action='store',
  help='json file')
parser.add_argument('--debug', action='store_true',
  help='sanity check')
args = parser.parse_args()

DEBUG = args.debug

# read config file
# call function in parse_config.py
# parse_config.py sub-main will validate that the config file is correct
config_file = open(args.file, "r")
parsed_file = Parse(config_file)
config_file.close()

schedule = Schedule(parsed_file)
schedule.initial_schedule()
schedule.print_queue()

