#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 02:49:51 2018

@author: avinash
"""

import sqlite3
conn = sqlite3.connect('facebase.db')
c = conn.cursor()
c.execute("INSERT INTO people VALUES (1,'ajay',55)")