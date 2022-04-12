import os
import datetime

def _log_entry(from_c, to_c):
    log = f"{datetime.datetime.now() - {from_c} - {to_c}}"
    
    if os.path.exists("./log.txt"):
        log_file = open("log.txt", "a")
        log_file.write(log)
        log_file.close()
    else:
        log_file = open("log.txt", "w")
        log_file.write(log)
        log_file.close()
