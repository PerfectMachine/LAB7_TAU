#!/usr/bin/env python3
import math

from ev3dev.ev3 import *
import time

mA = LargeMotor('outA')
mA.position = current_time = start_time = 0

fh = open("data.txt", "w")
fh.write('0 ' + '0 ' + '0' + '\n')

start_time = time.time()


def sign(number):
    if number > 0.0:
        return 1.0
    if number < 0.0:
        return -1.0
    return 0.0


a1 = 94.75
a2 = 13.5
a3 = 8.5

kP = 1.0
kI = 0.0
kD = 0.0
kS = 0.0

maxI = float(50.0)
maxSpeed = 100.0
errorOld = 0.0
errorOldOld = 0.0
powerOld = 0.0
powerOldOld = 0.0
timeOld = 0.0


def reg(target):
    global errorOld, timeOld, errorOldOld, powerOld, powerOldOld
    timeDelta = (time.time() - start_time) - timeOld
    timeOld = time.time() - start_time
    pos = mA.position
    error = target - pos
    power = 0.0
    P = 0.0
    D = 0.0
    S = 0.0
    if target != pos:
        p1 = a1 * (error - 2 * errorOld + errorOldOld) / (timeDelta ** 2)
        p2 = a2 * (error - errorOld) / timeDelta
        p3 = a3 * error
        p4 = (2 * powerOld - powerOldOld) / (timeDelta ** 2)
        power = (p1 + p2 + p3 + p4) / (2 - 1 / (timeDelta ** 2))
        errorOld = error
        errorOldOld = errorOld
        powerOld = power
        powerOldOld = powerOld
    else:
        power = 0.0
        powerOld = 0.0
        powerOldOld = 0.0
        errorOld = 0.0
        errorOldOld = 0.0
    power = min(abs(power), maxSpeed) * sign(power)
    return power


goto = int(200)

try:
    while True:
        current_time = time.time() - start_time
        mA.run_direct(duty_cycle_sp = round(reg(3 * math.cos(2 * current_time + math.pi / 4))))
        fh.write(str(current_time) + ' ' + str(mA.position) + ' ' + str(mA.speed) + ' ' + str(goto) + '\n')
finally:
    mA.stop(stop_action = 'brake')
    fh.close()

