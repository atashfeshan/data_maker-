import math
import random
import pandas as pd
import numpy as np
from MyFunc import *
from client import *
from my import*


def init_players():
    players = [Player(name="tomato", first_pos=Pos(-6.45, 1.6)),
               Player(name="banana", first_pos=Pos(-6, 0.55)),
               Player(name="Melon", first_pos=Pos(-6, -0.55)),
               Player(name="Eggplant", first_pos=Pos(-6.45, -1.6)),
               Player(name="Cucumber", first_pos=Pos(-1, 0))]
    return players


def do_turn(game):
    act = Triple()
    #########################################
    data = pd.read_csv('ee.csv')
    data = list(np.array(data))
    #########################################
    mine = []
    yours = []
    for i in range(5):
        x = game.getOppTeam().getPlayer(i).getPosition().getX()
        y = game.getOppTeam().getPlayer(i).getPosition().getY()
        x1 = game.getMyTeam().getPlayer(i).getPosition().getX()
        y1 = game.getMyTeam().getPlayer(i).getPosition().getY()
        mine.append([x1, y1])
        yours.append([x, y])

    ##########################################
    ##########################################
    obj = mine.copy()
    obj.extend(yours)
    a = int(input('ok'))
    player_id = int(input('enter : '))-1
    x1 = game.getMyTeam().getPlayer(player_id).getPosition().getX()
    y1 = game.getMyTeam().getPlayer(player_id).getPosition().getY()
    x2 = game.getBall().getPosition().getX()
    y2 = game.getBall().getPosition().getY()
    angle = math.fabs(math.degrees(math.atan((y2 - y1) / (x2 - x1))))
    # Calculate the angle from the chosen player to the ball
    if x2 > x1:
        if y2 < y1:
            angle = 360 - angle
    else:
        if y2 < y1:
            angle += 180
        else:
            angle = 180 - angle
    board = list(make_board(obj))
    board.extend([x2, y2])
    data.append(board)
    x = game.getMyTeam().getPlayer(int(player_id)).getPosition().getX()
    y = game.getMyTeam().getPlayer(int(player_id)).getPosition().getY()
    data[len(data)-1].append(x)
    data[len(data) - 1].append(y)
    data = pd.DataFrame(data)
    if a == 1:
        data.to_csv('ee.csv', index=False)
    # Out put
    ##########################################
    act.setPlayerID(player_id)   #
    act.setAngle(angle)          #
    act.setPower(100)            #
    return act                   #
    ##########################################
