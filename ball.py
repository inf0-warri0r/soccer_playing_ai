"""
Author : tharindra galahena (inf0_warri0r)
Project: soccer playing ai agents using finite state machines
Blog   : http://www.inf0warri0r.blogspot.com
Date   : 21/07/2013
License:

     Copyright 2013 Tharindra Galahena

This is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version. This is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
details.

* You should have received a copy of the GNU General Public License along with
this. If not, see http://www.gnu.org/licenses/.

"""

MOVE = 0
STOP = 1
QUICK_MOVE = 2


class ball:

    def __init__(self, x, y, ox, oy, gx, gy):
        self.pos_current_x = x
        self.pos_current_y = y
        self.pos_stop_x = gx
        self.pos_stop_y = gy
        self.pos_start_x = ox
        self.pos_start_y = oy
        self.state = STOP

    def state_change(self):
        d = (self.pos_current_x - self.pos_stop_x) ** 2.0
        d = d + (self.pos_current_y - self.pos_stop_y) ** 2.0
        d = d ** 0.5

        if self.state == STOP:
            if d > 2:
                self.state = MOVE
        elif self.state == MOVE:
            if d < 2:
                self.state = STOP
        elif self.state == QUICK_MOVE:
            if d < 2:
                self.state = STOP

    def boust(self):
        self.state = QUICK_MOVE

    def move(self):
        if self.state == MOVE:
            if self.pos_stop_y < 0:
                self.pos_stop_y = 0
            elif self.pos_stop_y > 300:
                self.pos_stop_y = 300
            d = (self.pos_current_x - self.pos_stop_x) ** 2.0
            d = d + (self.pos_current_y - self.pos_stop_y) ** 2.0
            d = d ** 0.5
            if d > 10:
                cos = (self.pos_stop_x - self.pos_current_x) / d
                sin = (self.pos_stop_y - self.pos_current_y) / d
                self.pos_current_x = self.pos_current_x + 20.0 * cos
                self.pos_current_y = self.pos_current_y + 20.0 * sin

        if self.state == QUICK_MOVE:
            if self.pos_stop_y < 0:
                self.pos_stop_y = 0
            elif self.pos_stop_y > 300:
                self.pos_stop_y = 300
            d = (self.pos_current_x - self.pos_stop_x) ** 2.0
            d = d + (self.pos_current_y - self.pos_stop_y) ** 2.0
            d = d ** 0.5
            if d > 10:
                cos = (self.pos_stop_x - self.pos_current_x) / d
                sin = (self.pos_stop_y - self.pos_current_y) / d
                self.pos_current_x = self.pos_current_x + 30.0 * cos
                self.pos_current_y = self.pos_current_y + 30.0 * sin

    def reset(self):
        self.pos_current_x = self.pos_stop_x = self.pos_start_x
        self.pos_current_y = self.pos_stop_y = self.pos_start_y
        self.state = STOP
