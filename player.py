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

import random

WAIT = 0
RETURN_HOME = 1
GO_OPP = 2
FALLOW_BALL = 3
KICK_BALL = 4


class player:

    def __init__(self, ind, t, gx, gy):
        self.index = ind
        self.state = WAIT
        self.team = t
        self.pos_goal_x = gx
        self.pos_goal_y = gy
        self.flage = True
        self.reset()

    def change_state(self, b, near_id):
        bx = b.pos_current_x
        by = b.pos_current_y
        d = (self.pos_current_x - bx) ** 2.0
        d = d + (self.pos_current_y - by) ** 2.0
        d = d ** 0.5

        if self.index == near_id:
            if self.state != FALLOW_BALL or self.state != KICK_BALL:
                if d < 20:
                    self.state = KICK_BALL
                else:
                    self.state = FALLOW_BALL

        elif self.state == WAIT:
            if self.index == near_id:
                self.state = FALLOW_BALL
            elif self.team == 0 and bx < 300:
                dd = (self.pos_current_x - self.pos_start_x) ** 2.0
                dd = dd + (self.pos_current_y - self.pos_start_y) ** 2.0
                dd = dd ** 0.5
                if dd > 20:
                    self.state = RETURN_HOME
            elif self.team == 1 and bx > 300:
                dd = (self.pos_current_x - self.pos_start_x) ** 2.0
                dd = dd + (self.pos_current_y - self.pos_start_y) ** 2.0
                dd = dd ** 0.5
                if dd > 20:
                    self.state = RETURN_HOME
            elif self.team == 0 and bx > 300:
                dd = (self.pos_current_x - self.pos_opp_x) ** 2.0
                dd = dd + (self.pos_current_y - self.pos_opp_y) ** 2.0
                dd = dd ** 0.5
                if dd > 20:
                    self.state = GO_OPP
            elif self.team == 1 and bx < 300:
                dd = (self.pos_current_x - self.pos_opp_x) ** 2.0
                dd = dd + (self.pos_current_y - self.pos_opp_y) ** 2.0
                dd = dd ** 0.5
                if dd > 20:
                    self.state = GO_OPP

        elif self.state == FALLOW_BALL:
            if d < 20 and self.index == near_id:
                self.state = KICK_BALL
            elif d > 100 and self.index != near_id:
                self.state = WAIT
        elif self.state == RETURN_HOME:
            if self.pos_current_x - self.pos_start_x > -10:
                if self.pos_current_y - self.pos_start_y > -10:
                    if self.pos_current_x - self.pos_start_x < 10:
                        if self.pos_current_y - self.pos_start_y < 10:
                            self.state = WAIT
            if self.index == near_id:
                self.state = FALLOW_BALL
            elif self.team == 0 and bx > 300:
                dd = (self.pos_current_x - self.pos_opp_x) ** 2.0
                dd = dd + (self.pos_current_y - self.pos_opp_y) ** 2.0
                dd = dd ** 0.5
                if dd > 20:
                    self.state = GO_OPP
            elif self.team == 1 and bx < 300:
                dd = (self.pos_current_x - self.pos_opp_x) ** 2.0
                dd = dd + (self.pos_current_y - self.pos_opp_y) ** 2.0
                dd = dd ** 0.5
                if dd > 20:
                    self.state = GO_OPP
        elif self.state == GO_OPP:
            if self.pos_current_x - self.pos_opp_x > -10:
                if self.pos_current_y - self.pos_opp_y > -10:
                    if self.pos_current_x - self.pos_opp_x < 10:
                        if self.pos_current_y - self.pos_opp_y < 10:
                            self.state = WAIT
            if self.index == near_id:
                self.state = FALLOW_BALL
            elif self.team == 0 and bx < 300:
                dd = (self.pos_current_x - self.pos_start_x) ** 2.0
                dd = dd + (self.pos_current_y - self.pos_start_y) ** 2.0
                dd = dd ** 0.5
                if dd > 20:
                    self.state = RETURN_HOME
            elif self.team == 1 and bx > 300:
                dd = (self.pos_current_x - self.pos_start_x) ** 2.0
                dd = dd + (self.pos_current_y - self.pos_start_y) ** 2.0
                dd = dd ** 0.5
                if dd > 20:
                    self.state = RETURN_HOME
        elif self.state == KICK_BALL:
            if self.index == near_id:
                self.state = FALLOW_BALL
            else:
                self.state = WAIT

    def move(self, b, near, x, y, xd, gole, p1, p2):
        bx = b.pos_current_x
        by = b.pos_current_y

        yy = 0
        if self.team == 0:
            yy = p2[xd[2]].pos_current_y
        else:
            yy = p1[xd[2]].pos_current_y

        if self.state == FALLOW_BALL:
            self.flage = True
            d = (self.pos_current_x - bx) ** 2.0
            d = d + (self.pos_current_y - by) ** 2.0
            d = d ** 0.5
            cos = float(bx - self.pos_current_x) / d
            sin = float(by - self.pos_current_y) / d

            self.pos_current_x = self.pos_current_x + 10.0 * cos
            self.pos_current_y = self.pos_current_y + 10.0 * sin

        elif self.state == RETURN_HOME:
            self.flage = True
            d = (self.pos_current_x - self.pos_start_x) ** 2.0
            d = d + (self.pos_current_y - self.pos_start_y) ** 2.0
            d = d ** 0.5

            cos = float(self.pos_start_x - self.pos_current_x) / d
            sin = float(self.pos_start_y - self.pos_current_y) / d

            self.pos_current_x = self.pos_current_x + 10.0 * cos
            self.pos_current_y = self.pos_current_y + 10.0 * sin
        elif self.state == GO_OPP:
            if self.flage:
                if self.team == 0:
                    if int(bx) >= 550:
                        self.pos_opp_x = random.randrange(549, 550)
                    else:
                        self.pos_opp_x = random.randrange(int(bx), 550)
                    self.pos_opp_y = random.randrange(0, 300)
                else:
                    if int(bx) <= 50:
                        self.pos_opp_x = random.randrange(50, 51)
                    else:
                        self.pos_opp_x = random.randrange(50, int(bx))
                    self.pos_opp_y = random.randrange(0, 300)
                self.flage = False

            d = (self.pos_current_x - self.pos_opp_x) ** 2.0
            d = d + (self.pos_current_y - self.pos_opp_y) ** 2.0
            d = d ** 0.5
            cos = float(self.pos_opp_x - self.pos_current_x) / d
            sin = float(self.pos_opp_y - self.pos_current_y) / d

            self.pos_current_x = self.pos_current_x + 10.0 * cos
            self.pos_current_y = self.pos_current_y + 10.0 * sin

        elif self.state == KICK_BALL:
            self.flage = True
            d = (self.pos_current_x - self.pos_goal_x) ** 2.0
            d = d ** 0.5
            if gole > 20 and d < 60:
                b.pos_stop_x = self.pos_goal_x
                b.pos_stop_y = self.pos_current_y
                b.boust()
            elif xd[0] > 10 or (yy - self.pos_current_y) ** 2.0 > 100:
                if self.team == 0:
                    b.pos_stop_x = bx + 20
                else:
                    b.pos_stop_x = bx - 20
            elif xd[0] < 5 and d < 50:
                b.pos_stop_x = self.pos_goal_x
                b.pos_stop_y = self.pos_current_y
                b.boust()
            elif x == -1:
                if self.team == 0:
                    b.pos_stop_x = bx + 20
                else:
                    b.pos_stop_x = bx - 20
            else:
                if self.team == 0:
                    b.pos_stop_x = x + 10
                    b.pos_stop_y = y
                else:
                    b.pos_stop_x = x - 10
                    b.pos_stop_y = y

        return b

    def reset(self):
        if self.team == 0:
            self.pos_current_x = random.randrange(0, 300)
            self.pos_current_y = random.randrange(0, 300)
            self.pos_start_x = random.randrange(50, 300)
            self.pos_start_y = random.randrange(0, 300)
            self.pos_opp_x = random.randrange(300, 550)
            self.pos_opp_y = random.randrange(0, 300)
        else:
            self.pos_current_x = random.randrange(300, 600)
            self.pos_current_y = random.randrange(0, 300)
            self.pos_start_x = random.randrange(300, 550)
            self.pos_start_y = random.randrange(0, 300)
            self.pos_opp_x = random.randrange(50, 300)
            self.pos_opp_y = random.randrange(0, 300)
        self.state = WAIT
