#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from flask import Flask, render_template, request, session, redirect, jsonify, Response
from biz import *
import json

def home():
    original_file = request.args.get('original')
    modified_file = request.args.get('modified')
    assert original_file and modified_file

    code_contents = get_diff_code_contents(original_file, modified_file)
    
    return render_template('home.html', original_code=code_contents[0], modified_code=code_contents[1])
