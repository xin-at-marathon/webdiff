#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, current_app

from controller import *

if __name__ == "__main__":
    app = Flask(__name__, template_folder="view", static_folder="view")
    
    app.add_url_rule('/', view_func=home)
    
    print("start server on port: 3000")
    app.run(host='0.0.0.0', port=3000, debug=True, use_reloader=True)
