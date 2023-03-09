#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .code_diff import CodeDiff

def get_diff_code_contents(original_file, modified_file):
    code_diff = CodeDiff(original_file, modified_file, name=modified_file)
    return code_diff.format()
