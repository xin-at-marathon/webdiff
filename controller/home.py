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

    original_macro_file_path = None
    modified_macro_file_path = "sample/modified/macro.h"

    original_code, modified_code = get_diff_code_contents(original_file, modified_file,
                                           original_macro_file_path, modified_macro_file_path)

    title = f"diff: {original_file} => {modified_file}"
    return render_template('home.html', title=title,
                           original_code=original_code, modified_code=modified_code)
