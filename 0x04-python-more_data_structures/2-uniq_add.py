#!/usr/bin/python3

def uniq_add(my_list=[]):
    cert = 0
    for x in set(my_list):
        cert += x
    return cert
