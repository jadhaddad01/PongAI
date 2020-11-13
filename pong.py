"""
Author: Jad Haddad

https://github.com/jadhaddad01/PongAI
Pong Artificial Intelligence
Using the NEAT Genetic Neural Network Architecture to train a set of blocks to play the popular game Pong. Also playable by user.

License:
-------------------------------------------------------------------------------
MIT License

Copyright (c) 2020 Jad Haddad

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
-------------------------------------------------------------------------------
"""

# -----------------------------------------------------------------------------
# Import libraries
# -----------------------------------------------------------------------------
# Public Libraries
import os
import math
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import neat
import time
import random
import pygame_menu
import pickle
from PIL import Image
# Utils Folder files
from utils import UI, confmodif
# from utils import visualize

# -----------------------------------------------------------------------------
# Pygame and font initialization
# -----------------------------------------------------------------------------
pygame.init()
pygame.font.init()

# Caption and Icon
pygame.display.set_caption("Pong AI")
# icon later update

# -----------------------------------------------------------------------------
# Classes
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Methods
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Main Program
# -----------------------------------------------------------------------------
if __name__== "__main__":
    pass
