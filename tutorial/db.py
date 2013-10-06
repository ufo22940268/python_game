#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2013 ccheng <ccheng@cchengs-MacBook-Air.local>
#
# Distributed under terms of the MIT license.

"""

"""

import pymongo

def get_db():
    conn = pymongo.Connection('localhost', 27017)
    return conn.game

def get_item():
    return get_db().item

def insert_item(i):
    return get_item().insert(i)

def clear_game():
    return get_item().drop()

def get_items():
    return list(get_item().find())
