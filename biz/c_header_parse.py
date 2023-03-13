#!/usr/bin/env python3
# -*- coding: utf-8 -*-

MARK=F"#define "

def get_macro_dict(macro_file_path):
    macros = {}
    macro_file = open(macro_file_path, 'r')
    lines = macro_file.readlines()
    for line in lines:
        if line.startswith(MARK):
            define_string = line[len(MARK):].strip()
            i = define_string.find(' ')
            if i>=0:
                macro = define_string[:i]
                name = define_string[i:].strip()
            else:
                macro = define_string.strip()
                name = ''
                
            desc = ''.join(__get_macro_desc(lines, line))
            macros[macro] ={
                'name': name,
                'desc': desc,
            }

    return macros
    

def __get_macro_desc(lines, target_line):
    started_at = -1
    ended_at = -1
    for i in range(0, len(lines)):
        if lines[i] == target_line:
            started_at = i
            ended_at = i
            continue
        if started_at >=0 and lines[i].startswith(MARK):
            ended_at = i
            break
    #print(f"{started_at}:{ended_at}")
    
    desc = []
    for i in range(started_at+1, ended_at):
        if lines[i].strip() == '' or lines[i].strip().startswith('/*') or lines[i].strip().endswith('*/'):
            continue
        desc.append(lines[i])

    return desc

