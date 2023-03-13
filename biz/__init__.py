#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .code_diff import CodeDiff
from .c_header_parse import get_macro_dict

def get_diff_code_contents(original_file, modified_file, original_macro_file_path, modified_macro_file_path):
    code_diff = CodeDiff(original_file, modified_file, name=modified_file)
    code_contents = code_diff.format()

    original_code = code_contents[0]
    modified_code = code_contents[1]
    
    if modified_macro_file_path:
        print(modified_code)
        macros = get_macro_dict(modified_macro_file_path)
        for i, (k, v) in enumerate(macros.items()):
            if v["name"]:
                md = '# ' + v["name"] + '\n' + v["desc"]
            else:
                md = v["desc"]
            modified_code = modified_code.replace(k, f'<a href="#" class="macro" boundary="window" data-toggle="tooltip" data-html="true" data-title="{md}">{k}</a>')
    
    return original_code, modified_code
