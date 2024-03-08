#!/usr/bin/python3
"""print file path to screen"""
import os

# The built in variable __file__ already contains the absolute path to a running script

print(os.path.abspath(__file__))
