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

from Tkinter import *
import player
import random
import ball


players1 = list()
for i in range(0, 5):
    p = player.player(i, 0, 600, 150)
    players1.append(p)

players2 = list()
for i in range(0, 5):
    p = player.player(i, 1, 0, 150)
    players2.append(p)

b = ball.ball(300, 150, 300, 150, 300, 150)


def find_nearest_playerest_to_ball_1(bx, by):
    ls = list()
    for i in range(0, 5):
        d = (players1[i].pos_current_x - bx) ** 2.0
        d = d + (players1[i].pos_current_y - by) ** 2.0
        d = d ** 0.5
        ls.append((d, i))
    ls = sorted(ls)
    return ls[0]


def find_nearest_playerest_to_ball_2(bx, by):
    ls = list()
    for i in range(0, 5):
        d = (players2[i].pos_current_x - bx) ** 2.0
        d = d + (players2[i].pos_current_y - by) ** 2.0
        d = d ** 0.5
        ls.append((d, i))
    ls = sorted(ls)
    return ls[0]


def find_nearest_player_1(px, py):
    ls = list()
    for i in range(0, 5):
        d = (players1[i].pos_current_x - px) ** 2.0
        d = d + (players1[i].pos_current_y - py) ** 2.0
        d = d ** 0.5
        ls.append((d, 0, i))
    ls = sorted(ls)
    return ls[0]


def find_nearest_player_2(px, py):
    ls = list()
    for i in range(0, 5):
        d = (players2[i].pos_current_x - px) ** 2.0
        d = d + (players2[i].pos_current_y - py) ** 2.0
        d = d ** 0.5
        ls.append((d, 1, i))
    ls = sorted(ls)
    return ls[0]


def find_safest_player_1(n):
    mn = 100000
    ind = n
    dd = find_nearest_player_2(players1[n].pos_current_x,
                            players1[n].pos_current_y)[0]
    for i in range(0, 5):
        if i == n:
            continue
        d = find_nearest_player_2(players1[i].pos_current_x,
                                players1[i].pos_current_y)
        yy = (players1[i].pos_current_y - players1[n].pos_current_y) ** 2.0
        if d[0] > dd and yy > 400:
            dst = (players1[i].pos_current_x - players1[i].pos_goal_x) ** 2.0
            if mn > dst:
                mn = dst
                ind = i
    return ind


def find_safest_player_2(n):
    mn = 100000
    ind = n
    dd = find_nearest_player_1(players2[n].pos_current_x,
                            players2[n].pos_current_y)[0]
    for i in range(0, 5):
        if i == n:
            continue
        d = find_nearest_player_1(players2[i].pos_current_x,
                            players2[i].pos_current_y)
        if d[0] > dd:
            dst = (players2[i].pos_current_x - players2[i].pos_goal_x) ** 2.0
            if mn > dst:
                mn = dst
                ind = i
    return ind


def find_friend(t, n):

    ls = list()
    if t == 0:
        for i in range(0, 5):
            if i == n:
                continue
            d1 = (players1[i].pos_current_x - players1[n].pos_current_x) ** 2.0
            d2 = (players1[i].pos_current_y - players1[i].pos_current_y) ** 2.0
            d = (d1 + d2) ** 0.5
            ls.append((d, 0, i))
    else:
        for i in range(0, 5):
            if i == n:
                continue
            d1 = (players2[i].pos_current_x - players2[n].pos_current_x) ** 2.0
            d2 = (players2[i].pos_current_y - players2[n].pos_current_y) ** 2.0
            d = (d1 + d2) ** 0.5
            ls.append((d, 1, i))

    ls = sorted(ls)
    return ls


root = Tk()
root.title("soccer - inf0_warri0r")
chart_1 = Canvas(root,
                width=600,
                height=400,
                background="black")

chart_1.grid(row=0, column=0)


red = 0
blue = 0
flage = True

while 1:
    chart_1.create_rectangle(0, 0, 600, 300, fill='#1c0',
                            outline='yellow', width=3)
    chart_1.create_oval(240, 90, 360, 210, fill='#1c0',
                            outline='yellow', width=3)
    chart_1.create_line(300, 0, 300, 300, fill='yellow', width=3)
    for i in range(0, 5):
        chart_1.create_oval(players1[i].pos_current_x - 6,
                            players1[i].pos_current_y - 6,
                            players1[i].pos_current_x + 6,
                            players1[i].pos_current_y + 6,
                            fill='red')
        chart_1.create_text(players1[i].pos_current_x + 7,
                            players1[i].pos_current_y + 7,
                            text=str(players1[i].index + 1),
                            fill='white')
    for i in range(0, 5):
        chart_1.create_oval(players2[i].pos_current_x - 6,
                            players2[i].pos_current_y - 6,
                            players2[i].pos_current_x + 6,
                            players2[i].pos_current_y + 6,
                            fill='blue')
        chart_1.create_text(players2[i].pos_current_x + 7,
                            players2[i].pos_current_y - 7,
                            text=str(players2[i].index + 1),
                            fill='white')
    chart_1.create_oval(b.pos_current_x - 5, b.pos_current_y - 5,
                        b.pos_current_x + 5, b.pos_current_y + 5,
                        fill='yellow')

    txt = 'score : red = ' + str(red) + ' blue = ' + str(blue)
    chart_1.create_text(300, 350, text=txt, fill='white')

    if flage:
        chart_1.update()
        chart_1.after(600)
        chart_1.delete(ALL)

    bls1 = find_nearest_playerest_to_ball_1(b.pos_current_x, b.pos_current_y)
    bls2 = find_nearest_playerest_to_ball_2(b.pos_current_x, b.pos_current_y)

    rd = random.randrange(0, 100)
    if rd < 50:
        for i in range(0, 5):
            players1[i].change_state(b, bls1[1])
            ind = find_safest_player_1(i)
            px = -1
            py = -1
            if ind != i:
                px = players1[ind].pos_current_x
                py = players1[ind].pos_current_y
            xd = find_nearest_player_2(players1[i].pos_current_x,
                                        players1[i].pos_current_y)
            gole = find_nearest_player_2(players1[i].pos_goal_x,
                                        players1[i].pos_goal_y)
            b = players1[i].move(b, 0, px, py, xd, gole[0],
                                players1, players2)

        for i in range(0, 5):
            players2[i].change_state(b, bls2[1])
            ind = find_safest_player_2(i)
            px = -1
            py = -1
            if ind != i:
                px = players2[ind].pos_current_x
                py = players2[ind].pos_current_y
            xd = find_nearest_player_1(players2[i].pos_current_x,
                                        players2[i].pos_current_y)
            gole = find_nearest_player_1(players2[i].pos_goal_x,
                                        players2[i].pos_goal_y)
            b = players2[i].move(b, 1, px, py, xd, gole[0],
                                players1, players2)

    else:
        for i in range(0, 5):
            players2[i].change_state(b, bls2[1])
            ind = find_safest_player_2(i)
            px = -1
            py = -1
            if ind != i:
                px = players2[ind].pos_current_x
                py = players2[ind].pos_current_y
            xd = find_nearest_player_1(players2[i].pos_current_x,
                                        players2[i].pos_current_y)
            gole = find_nearest_player_1(players2[i].pos_goal_x,
                                        players2[i].pos_goal_y)
            b = players2[i].move(b, 1, px, py, xd, gole[0],
                                players1, players2)

        for i in range(0, 5):
            players1[i].change_state(b, bls1[1])
            ind = find_safest_player_1(i)
            px = -1
            py = -1
            if ind != i:
                px = players1[ind].pos_current_x
                py = players1[ind].pos_current_y
            xd = find_nearest_player_2(players1[i].pos_current_x,
                                        players1[i].pos_current_y)
            gole = find_nearest_player_2(players1[i].pos_goal_x,
                                        players1[i].pos_goal_y)
            b = players1[i].move(b, 0, px, py, xd, gole[0],
                                players1, players2)

    b.state_change()
    b.move()
    if not flage:
        chart_1.update()
        chart_1.after(100)
        chart_1.delete(ALL)
    else:
        flage = False

    if b.pos_current_x >= 590 or b.pos_current_x <= 10:
        if b.pos_current_x <= 10:
            blue = blue + 1
        else:
            red = red + 1

        for i in range(0, 5):
            players1[i].reset()
            players2[i].reset()
        b.reset()
        flage = True

root.mainloop()
