#!/usr/bin/env python
'''
:author: drownedcoast
:date: 3-24-2018
'''
import multiprocessing as mp
import re
import time
import random
import string
import argparse

import pyburstlib.lib.crypto as crypto
import pyburstlib.lib.brs_address as brs

MATCH = 'A' #Default
START = time.time()

# Parse command line arguments
##------------------------------------------------------------------------------------------
def Arguments():
	parser = argparse.ArgumentParser(description='Burst Vanity Address Generator')

	parser.add_argument('-m', "--match",  help="Address Prefix to match", required=True)

	gl_args = parser.parse_args()

	return gl_args

def rand_string(length):
    rand_str = ''.join(random.choice(
                        string.ascii_lowercase
                        + string.ascii_uppercase
                        + string.digits)
                   for i in range(random.randint(1,length)))
    return rand_str

def get_address(passphrase):
    account_id = crypto.get_account_id(passphrase)
    b = brs.BRSAddress()
    b.set_address(account_id)
    return b.to_string()

def is_match(address):
    if address[6:len(MATCH)+6] == MATCH:
        return True

def write_pw(passphrase):
    with open('burst-vanity-password.txt', 'w') as f: 
        f.write(passphrase) 

def worker(i, quit, foundit):
    print("[+] Worker {} Started looking for {}".format(i, MATCH))
    while not quit.is_set():
        rand_pass = rand_string(100)
        try:
            rand_addr = get_address(rand_pass)
        except:
            rand_addr = '                 '
        if is_match(rand_addr):
            print('\n[+] MATCH FOUND for {}'.format(MATCH))
            print('[+] Address - {}'.format(rand_addr))
            write_pw(rand_pass)
            print('[+] Passphrase written to - {}'.format('burst-vanity-password.txt'))
            foundit.set()
            break

def mp_handler():
    quit = mp.Event()
    foundit = mp.Event()
    for i in range(mp.cpu_count()):
        p = mp.Process(target=worker, args=(i, quit, foundit))
        p.start()
    foundit.wait()
    quit.set()
    print("[+] Address generation took {} Seconds".format(time.time() - START))

if __name__ == '__main__':
    args = Arguments()
    MATCH = args.match if not None else MATCH
    print("""
                       ______ _   _______ _____ _____                           
                      | ___ | | | | ___ /  ___|_   _|                          
                      | |_/ | | | | |_/ \ `--.  | |                            
                      | ___ | | | |    / `--. \ | |                            
                      | |_/ | |_| | |\ \/\__/ / | |                            
 _   _             _ _\____/ \________\_\____/  \_/              _             
| | | |           (_| |         |  __ \                         | |            
| | | | __ _ _ __  _| |_ _   _  | |  \/ ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
| | | |/ _` | '_ \| | __| | | | | | __ / _ | '_ \ / _ | '__/ _` | __/ _ \| '__|
\ \_/ | (_| | | | | | |_| |_| | | |_\ |  __| | | |  __| | | (_| | || (_) | |   
 \___/ \__,_|_| |_|_|\__|\__, |  \____/\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                          __/ |                                                
                         |___/                                                
                         """)
    print('BY: drownedcoast')
    print('DONATE: BURST-Q944–2MY3–97ZZ-FBWGB\n\n')
    if not bool(re.match('^[23456789ABCDEFGHJKLMNPQRSTUVWXYZ]+$', MATCH)):
        print('[!] Search must only contain 23456789ABCDEFGHJKLMNPQRSTUVWXYZ')
        exit()
    if len(MATCH) > 4:
        print('[!] Currently only 4 character addresses are supported.')
    print('[+] Searching for address beginning with {}'.format(MATCH))
    mp_handler()
