from datetime import datetime

selection_time = datetime.now()
from multiprocessing import Process, Pipe
import math
import statistics
import random
import tkinter as tk
import inflect
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import scipy.stats as stats
import sys
import os


def f(child_conn):
    data_1 = table_dataframe
    # data_2 = table_dataframe2
    child_conn.send(data_1)
    child_conn.close()


trials = 10000
root = tk.Tk()
module_time = datetime.now()
initialization_time = module_time - selection_time
root.title('Tekton Sim Version 1.2')
root.geometry('280x205')
check_var1 = tk.BooleanVar()
check_var2 = tk.BooleanVar()
check_var3 = tk.BooleanVar()
check_var4 = tk.BooleanVar()
check_var5 = tk.BooleanVar()
check_var6 = tk.BooleanVar()
check_var7 = tk.BooleanVar()
check_var8 = tk.BooleanVar()
check_var9 = tk.BooleanVar()
check_var10 = tk.BooleanVar()
check_var11 = tk.BooleanVar()
check_var12 = tk.BooleanVar()
check_var13 = tk.BooleanVar()
check_var14 = tk.BooleanVar()
check_var15 = tk.BooleanVar()
check_var16 = tk.BooleanVar()
check_var17 = tk.BooleanVar()


def abort():
    return sys.exit(0)


def trials_selection():
    global trials
    if check_var10.get():
        trials = 1000
        string_variable.set('number of trials ' + str(trials))
    elif check_var12.get():
        trials = 10000
        string_variable.set('number of trials ' + str(trials))
    elif check_var13.get():
        trials = 100000
        string_variable.set('number of trials ' + str(trials))
    elif check_var15.get():
        trials = 1000000
        string_variable.set('number of trials ' + str(trials))
    else:
        trials = 10000
        string_variable.set('number of trials ' + str(trials))
    return trials


def check_correction_temp1():
    return check_correction_new('1')


def check_correction_temp2():
    return check_correction_new('2')


def check_correction_temp3():
    return check_correction_new('3')


def check_correction_temp4():
    return check_correction_new('4')


def check_correction():
    if check_var5.get():
        if check_var6.get():
            return C6.toggle()
        else:
            return


def fang_checker_lb():
    while not check_var4.get():
        return C9.toggle()


def check_correction_new(num):
    while num == '1':
        C12.deselect()
        C13.deselect()
        C15.deselect()
        return trials_selection()
    while num == '2':
        C10.deselect()
        C13.deselect()
        C15.deselect()
        return trials_selection()
    while num == '3':
        C12.deselect()
        C10.deselect()
        C15.deselect()
        return trials_selection()
    while num == '4':
        C13.deselect()
        C12.deselect()
        C10.deselect()
        return trials_selection()


def spec_ring():
    if check_var4.get():
        return
    else:
        C9.deselect()


def check_correction2():
    if check_var6.get():
        if check_var5.get():
            return C5.toggle()
        else:
            return


def check_correction_veng():
    if check_var11.get():
        if check_var17.get():
            return C17.toggle()
        else:
            return


def check_correction_veng2():
    if check_var17.get():
        if check_var11.get():
            return C11.toggle()
        else:
            return

string_variable = tk.StringVar()
C1 = tk.Checkbutton(root, text="five tick only", variable=check_var1, onvalue=1, offvalue=0)
C1.place(x=25, y=80)
C2 = tk.Checkbutton(root, text="CM", variable=check_var2, onvalue=1, offvalue=0)
C2.place(x=25, y=55)
C2.toggle()
C3 = tk.Checkbutton(root, text="inq", variable=check_var3, onvalue=1, offvalue=0)
C3.place(x=75, y=55)
C3.toggle()
C4 = tk.Checkbutton(root, text="fang", variable=check_var4, onvalue=1, offvalue=0)
C4.place(x=140, y=130)
C5 = tk.Checkbutton(root, text="b ring", variable=check_var5, onvalue=1, offvalue=0, command=check_correction)
C5.place(x=75, y=155)
C6 = tk.Checkbutton(root, text="brim", variable=check_var6, onvalue=1, offvalue=0, command=check_correction2)
C6.place(x=25, y=155)
C7 = tk.Checkbutton(root, text="feros", variable=check_var7, onvalue=1, offvalue=0)
C7.place(x=75, y=130)
C8 = tk.Checkbutton(root, text="tort", variable=check_var8, onvalue=1, offvalue=0)
C8.place(x=25, y=130)
C11 = tk.Checkbutton(root, text="pre veng", variable=check_var11, onvalue=1, offvalue=0, command=check_correction_veng)
C11.place(x=120, y=55)
C11.toggle()
C9 = tk.Checkbutton(root, text="lightbearer", variable=check_var9, onvalue=1, offvalue=0, command=spec_ring)
C9.place(x=140, y=155)
C10 = tk.Checkbutton(root, text="1000", variable=check_var10, onvalue=1, offvalue=0, command=check_correction_temp1)
C10.place(x=25, y=30)
C12 = tk.Checkbutton(root, text="10000", variable=check_var12, onvalue=1, offvalue=0, command=check_correction_temp2)
C12.place(x=85, y=30)
trials_selection()
C12.toggle()
C13 = tk.Checkbutton(root, text="100000", variable=check_var13, onvalue=1, offvalue=0, command=check_correction_temp3)
C13.place(x=150, y=30)
C15 = tk.Checkbutton(root, text="1mil", variable=check_var15, onvalue=1, offvalue=0, command=check_correction_temp4)
C15.place(x=225, y=30)
C14 = tk.Checkbutton(root, text="vuln", variable=check_var14, onvalue=1, offvalue=0)
C14.place(x=130, y=80)
C14.toggle()
C16 = tk.Checkbutton(root, text="vuln book", variable=check_var16, onvalue=1, offvalue=0)
C16.place(x=190, y=55)
C17 = tk.Checkbutton(root, text="veng camp", variable=check_var17, onvalue=1, offvalue=0, command=check_correction_veng2)
C17.place(x=190, y=80)

trials_text = tk.Label(root, textvariable=string_variable)
trials_text.place(x=30, y=10)
notif_text = tk.Label(root, text='lb is for fang spec only')
notif_text.place(x=30, y=110)
exit_button = tk.Button(root, text="Exit", command=abort)
exit_button.place(x=230, y=0)
button_submit = tk.Button(root, text="Submit", command=root.destroy)
button_submit.place(x=100, y=180)
root.mainloop()

start_time = datetime.now()
result_array = ["hit", "miss"]
inq = check_var3.get()
cm = check_var2.get()
fang = check_var4.get()
five_only = check_var1.get()
if fang:
    scythe = False
else:
    scythe = True
lightbearer_equipped = check_var9.get()
print('inq:', inq)
print('cm:', cm)
print('fang:', fang)
print('five tick only:', five_only)
print('b ring:', check_var5.get())
print('brim ring:', check_var6.get())
print('tort:', check_var8.get())
print('feros:', check_var7.get())
print('vuln', check_var14.get())
print('vuln book', check_var16.get())
print('preveng', check_var11.get())
print('lightbearer', check_var9.get())
if five_only:
    four_and_five = False
else:
    four_and_five = True
attack_level = 118
strength_level = 118
piety_attack = 1.2
piety_strength = 1.23
effective_strength_lvl = int(strength_level * piety_strength + 3 + 8)
effective_attack_lvl = int(attack_level * piety_attack + 0 + 8)
effective_spec_attack_lvl = int(attack_level * piety_attack + 3 + 8)
effective_spec_strength_lvl = int(strength_level * piety_strength + 0 + 8)
no_h_one_anvil_temp = 0
one_h_one_anvil_temp = 0
two_h_one_anvil_temp = 0
no_h_one_a = 0
one_h_one_a = 0
two_h_one_a = 0
anvils = [0] * 30
times = []
tick_times = []
tick_times_one_anvil = []
no_hammer_total = 0
one_hammer_total = 0
two_hammer_total = 0
crush = 'crush'
slash = 'slash'
stab = 'stab'


class Offensive:
    def __init__(self, four_tick_hit_counter, five_tick_hit_counter, time_parameter, phase, idle_time, fang_spec_status,
                 specced_last_anvil, no_hammer_count, one_hammer_count, two_hammer_count, hp_pool):
        self.four_tick_hit_counter = four_tick_hit_counter
        self.five_tick_hit_counter = five_tick_hit_counter
        self.time_parameter = time_parameter
        self.phase = phase
        self.idle_time = idle_time
        self.fang_spec_status = fang_spec_status
        self.specced_last_anvil = specced_last_anvil
        self.no_hammer_count = no_hammer_count
        self.one_hammer_count = one_hammer_count
        self.two_hammer_count = two_hammer_count
        self.hp_pool = hp_pool


class Gear:
    def __init__(self, dwh_att_bonus, dwh_str_bonus, four_tick_att_bonus, four_tick_str_bonus, fang_att_bonus,
                 fang_str_bonus, scy_att_bonus, scy_str_bonus, gear_multiplier, static_crush_weapon, five_tick_weapon):
        self.dwh_att_bonus = dwh_att_bonus
        self.dwh_str_bonus = dwh_str_bonus
        self.four_tick_att_bonus = four_tick_att_bonus
        self.four_tick_str_bonus = four_tick_str_bonus
        self.fang_att_bonus = fang_att_bonus
        self.fang_str_bonus = fang_str_bonus
        self.scy_att_bonus = scy_att_bonus
        self.scy_str_bonus = scy_str_bonus
        self.gear_multiplier = gear_multiplier
        self.static_crush_weapon = static_crush_weapon
        self.five_tick_weapon = five_tick_weapon


def gear_selection():
    attack_gear = 0
    strength_gear = 0
    if check_var5.get():
        strength_gear += 8
    if check_var6.get():
        attack_gear += 4
        strength_gear += 4
    if check_var8.get():
        attack_gear += 5
        strength_gear += 2
    if check_var7.get():
        attack_gear += 4
        strength_gear += 2
    if fang:
        five_tick_weapon = stab
    else:
        if inq:
            five_tick_weapon = crush
        else:
            five_tick_weapon = slash
    loadout_adjuster(attack_gear, strength_gear, five_tick_weapon)
    return loadout


def loadout_adjuster(att_modifier, str_modifier, five_tick_style):
    loadout.dwh_str_bonus += str_modifier
    loadout.four_tick_str_bonus += str_modifier
    loadout.fang_str_bonus += str_modifier
    loadout.scy_str_bonus += str_modifier
    loadout.dwh_att_bonus += att_modifier
    loadout.four_tick_att_bonus += att_modifier
    loadout.fang_att_bonus += att_modifier
    loadout.scy_att_bonus += att_modifier
    loadout.five_tick_weapon = five_tick_style
    return


if inq:
    loadout = Gear(dwh_att_bonus=183, dwh_str_bonus=136, four_tick_att_bonus=183, four_tick_str_bonus=140,
                   fang_att_bonus=155, fang_str_bonus=154, scy_att_bonus=90, scy_str_bonus=118, gear_multiplier=1.025,
                   static_crush_weapon=crush, five_tick_weapon='')
    gear_selection()
    print('loadout bonuses selected: ', loadout.dwh_att_bonus, loadout.dwh_str_bonus, loadout.four_tick_att_bonus,
          loadout.four_tick_str_bonus, loadout.fang_att_bonus, loadout.fang_str_bonus, loadout.scy_att_bonus,
          loadout.scy_str_bonus, loadout.gear_multiplier)
    print('----------')
else:
    loadout = Gear(dwh_att_bonus=151, dwh_str_bonus=144, four_tick_att_bonus=151, four_tick_str_bonus=148,
                   fang_att_bonus=163, fang_str_bonus=162, scy_att_bonus=138, scy_str_bonus=126, gear_multiplier=1,
                   static_crush_weapon=crush, five_tick_weapon='')
    gear_selection()
    print('loadout bonuses selected: ', loadout.dwh_att_bonus, loadout.dwh_str_bonus, loadout.four_tick_att_bonus,
          loadout.four_tick_str_bonus, loadout.fang_att_bonus, loadout.fang_str_bonus, loadout.scy_att_bonus,
          loadout.scy_str_bonus, loadout.gear_multiplier)
    print('----------')


class NPC:
    def __init__(self, hp, defence, stab_def, slash_def, crush_def, veng_count, alive_status=True, anvil_checked=False):
        self.hp = hp
        self.defence = defence
        self.stab_def = stab_def
        self.slash_def = slash_def
        self.crush_def = crush_def
        self.alive_status = alive_status
        self.anvil_checked = anvil_checked
        self.veng_count = veng_count

    def lower_hp(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        if self.hp == 0:
            self.alive_status = False
        else:
            self.alive_status = True

    def lower_def(self, amount):
        self.defence -= amount
        if self.defence < 0:
            self.defence = 0


def hit_value_roll(spec_bonus, four_tick, five_tick, max_hit_modifier=1.0):
    def strength_selector():
        strength_bonus = 0
        if spec_bonus:
            strength_bonus = loadout.dwh_str_bonus
        elif four_tick:
            strength_bonus = loadout.four_tick_str_bonus
        elif five_tick:
            if fang:
                strength_bonus = loadout.fang_str_bonus
            elif scythe:
                strength_bonus = loadout.scy_str_bonus
        return strength_bonus

    damage_selection = 0
    if spec_bonus:
        max_hit = int(
            int(0.5 + effective_spec_strength_lvl * ((strength_selector() + 64) / 640)) * 1.5 * loadout.gear_multiplier)
        damage_selection = random.randint(0, max_hit)
    else:
        max_hit = int(int(0.5 + effective_strength_lvl * ((strength_selector() + 64) / 640)) * loadout.gear_multiplier)
        if four_tick:
            damage_selection = random.randint(0, max_hit)
        elif five_tick:
            if fang:
                max_hit = int(((0.5 + effective_strength_lvl * ((strength_selector() + 64) / 640)) * max_hit_modifier))
                min_hit = int((0.5 + effective_strength_lvl * ((strength_selector() + 64) / 640)) * .15)
                damage_selection = random.randint(min_hit, max_hit)
            else:
                damage_selection = random.randint(0, int(max_hit * max_hit_modifier))
    return int(damage_selection)


def is_whole(whole):
    return whole % 1 == 0


def adjust_def_integer():
    if not is_whole(tekton.defence):
        tekton.defence = int(tekton.defence) + 1


def attack_roll(spec_attack, four_tick, five_tick, multiplier):
    def attack_selector():
        attack_bonus = 0
        if spec_attack:
            attack_bonus = loadout.dwh_att_bonus
        elif four_tick:
            attack_bonus = loadout.four_tick_att_bonus
        elif five_tick:
            if fang:
                attack_bonus = loadout.fang_att_bonus
            elif scythe:
                attack_bonus = loadout.scy_att_bonus
        return attack_bonus

    if spec_attack:
        max_attack_roll_basic = int(effective_spec_attack_lvl * (attack_selector() + 64))
    else:
        max_attack_roll_basic = int(effective_attack_lvl * (attack_selector() + 64))
    if lightbearer_equipped:
        if fang:
            max_attack_roll = int(max_attack_roll_basic * multiplier)
        else:
            max_attack_roll = int(max_attack_roll_basic * loadout.gear_multiplier)
    else:
        max_attack_roll = int(max_attack_roll_basic * loadout.gear_multiplier)
    first_roll = random.randint(0, max_attack_roll)
    return first_roll


def hit_chancer(spec, four_tick, five_tick, fang_spec_hit, status):
    attack_roll_check = 0
    def_roll_check = defence_roll(spec, four_tick, five_tick, status)
    if spec:
        attack_roll_check = attack_roll(True, False, False, multiplier=1.0)
    elif four_tick:
        attack_roll_check = attack_roll(False, True, False, multiplier=1.0)
    elif five_tick:
        if fang:
            if fang_spec_hit:
                attack_roll_check = attack_roll(False, False, True, multiplier=1.5)
                attack_roll_check2 = attack_roll(False, False, True, multiplier=1.5)
            else:
                attack_roll_check = attack_roll(False, False, True, multiplier=1.0)
                attack_roll_check2 = attack_roll(False, False, True, multiplier=1.0)
            roll_list = [attack_roll_check, attack_roll_check2]
            if any(i > def_roll_check for i in roll_list):
                return True
            else:
                return False
        else:
            attack_roll_check = attack_roll(False, False, True, multiplier=1.0)
    if attack_roll_check > def_roll_check:
        return True
    else:
        return False


def vuln_check():
    if check_var14.get():
        vuln = np.random.choice(result_array, 1, replace=True, p=[.62, (1 - .62)])
        if check_var16.get():
            book_of_water = .15
        else:
            book_of_water = .10
        if vuln:
            tekton.lower_def(int(tekton.defence * book_of_water))
            adjust_def_integer()
        else:
            tekton.lower_def(0)
        return
    else:
        return


def tek_check():
    global no_h_one_a, one_h_one_a, two_h_one_a, no_hammer_total, one_hammer_total, two_hammer_total
    if not tekton.alive_status:
        if not tekton.anvil_checked:
            if hit_metrics.phase == 0:
                anvils[0] += 1
                tekton.anvil_checked = True
            elif hit_metrics.phase == 1:
                anvils[1] += 1
                tekton.anvil_checked = True
                if hit_metrics.one_hammer_count == 2:
                    two_h_one_a += 1
                    two_hammer_total += 1
                elif hit_metrics.no_hammer_count == 2:
                    no_h_one_a += 1
                    no_hammer_total += 1
                else:
                    one_h_one_a += 1
                    one_hammer_total += 1
            else:
                if hit_metrics.one_hammer_count == 2:
                    two_hammer_total += 1
                elif hit_metrics.no_hammer_count == 2:
                    no_hammer_total += 1
                else:
                    one_hammer_total += 1
                anvils[hit_metrics.phase] += 1
                tekton.anvil_checked = True
            return
        else:
            return
    else:
        return


def hammer_missed():
    tekton.lower_def(int((tekton.defence * .05)))
    adjust_def_integer()
    hit_metrics.no_hammer_count += 1
    return


def spec_hit(instances, status):
    for _ in range(instances):
        defence_roll(True, False, False, status)
        if hit_chancer(True, False, False, False, status):
            damage_val = hit_value_roll(spec_bonus=True, four_tick=False, five_tick=False)
            tekton.lower_hp(damage_val)
            if damage_val > 0:
                tekton.lower_def(int((tekton.defence * .3)))
                adjust_def_integer()
                hit_metrics.one_hammer_count += 1
            else:
                hammer_missed()
        else:
            hammer_missed()
    return


def four_tick_hit(instances, status):
    for _ in range(instances):
        if tekton.hp > 0:
            hit_metrics.four_tick_hit_counter += 1
        else:
            hit_metrics.four_tick_hit_counter += 0
        defence_roll(False, True, False, status)
        if hit_chancer(False, True, False, False, status):
            damage_val = hit_value_roll(spec_bonus=False, four_tick=True, five_tick=False)
            tekton.lower_hp(damage_val)
        else:
            damage_val = 0
            tekton.lower_hp(damage_val)
        tek_check()


def scy_dmg(step_down, status):
    if hit_chancer(False, False, True, False, status):
        damage_val = hit_value_roll(False, four_tick=False, five_tick=True, max_hit_modifier=step_down)
        tekton.lower_hp(damage_val)
    else:
        damage_val = 0
        tekton.lower_hp(damage_val)
    return damage_val


def five_tick_hit(instances, status, fang_spec_pass_var):
    for _ in range(instances):
        defence_roll(False, False, True, status)
        if tekton.hp > 0:
            hit_metrics.five_tick_hit_counter += 1
        else:
            hit_metrics.five_tick_hit_counter += 0
        if fang:
            if fang_spec_pass_var:
                if hit_chancer(False, False, True, fang_spec_pass_var, status):
                    damage_val = hit_value_roll(spec_bonus=False, four_tick=False, five_tick=True, max_hit_modifier=1)
                    tekton.lower_hp(damage_val)
                else:
                    damage_val = 0
                    tekton.lower_hp(damage_val)
            elif hit_chancer(False, False, True, fang_spec_pass_var, status):
                damage_val = hit_value_roll(spec_bonus=False, four_tick=False, five_tick=True, max_hit_modifier=.85)
                tekton.lower_hp(damage_val)
            else:
                damage_val = 0
                tekton.lower_hp(damage_val)
        elif scythe:
            scy_dmg(1, status)
            scy_dmg(.5, status)
            scy_dmg(.25, status)
        else:
            if hit_chancer(False, False, True, False, status):
                damage_val = hit_value_roll(False, four_tick=False, five_tick=True)
                tekton.lower_hp(damage_val)
            else:
                damage_val = 0
                tekton.lower_hp(damage_val)
    tek_check()


def veng_calc():
    if cm:
        if check_var17.get():
            if tekton.veng_count < 2:
                return 65
            else:
                return 70
        else:
            return 70
    else:
        if check_var17.get():
            if tekton.veng_count < 2:
                return 44
            else:
                return 50
        else:
            return 50


def anvil_adjustment(pre_veng, veng_camp):
    if tekton.hp > 0:
        cycle_select = random.randint(3, 6)
        hit_metrics.idle_time += ((cycle_select * 3) + 10)
        if tekton.hp < base_hp:
            tekton.hp += (cycle_select * hp_regen_per_cycle)
        if tekton.defence < base_def:
            tekton.defence += (cycle_select * def_regen_per_cycle)
        if pre_veng:
            tekton.lower_hp(random.randint(1, veng_calc()))
        elif veng_camp:
            for _ in range(2):
                if tekton.veng_count < 4:
                    if hit_metrics.hp_pool > veng_calc():
                        tekton.lower_hp(random.randint(1, veng_calc()))
                    elif hit_metrics.hp_pool > (veng_calc() * 2):
                        tekton.lower_hp(random.randint(1, math.ceil((veng_calc() * .5))))
                    else:
                        return tekton.hp
                    tekton.veng_count += 1
                else:
                    return tekton.hp
        else:
            return tekton.hp
    else:
        return tekton.hp
    return tekton.hp


def min_regen():
    if tekton.hp > 0:
        if tekton.hp < base_hp:
            tekton.hp += 1
            return tekton.hp
        if tekton.defence < base_def:
            tekton.defence += 1
            return tekton.hp
        return tekton.hp
    else:
        return tekton.hp


def time():
    idle_total = hit_metrics.idle_time
    four_total = hit_metrics.four_tick_hit_counter * 4
    five_total = hit_metrics.five_tick_hit_counter * 5
    hit_metrics.time_parameter = (five_total + four_total + idle_total + 12 + 17) * 0.6
    times.append(hit_metrics.time_parameter)
    hit_metrics.time_parameter = (five_total + four_total + idle_total + 12 + 17)
    tick_times.append(hit_metrics.time_parameter)


def pre_anvil():
    if four_and_five:
        spec_hit(2, False)
        four_tick_hit(3, False)
        five_tick_hit(1, False, False)
        four_tick_hit(1, False)
        five_tick_hit(2, False, False)
    else:
        spec_hit(2, False)
        five_tick_hit(6, False, False)
    return


def can_i_spec():
    if lightbearer_equipped:
        hit_metrics.fang_spec_status = True
        return hit_metrics.fang_spec_status
    else:
        if hit_metrics.specced_last_anvil:
            hit_metrics.fang_spec_status = False
            return hit_metrics.fang_spec_status
        else:
            hit_metrics.fang_spec_status = True
            return hit_metrics.fang_spec_status


def post_anvil(fang_lb_spec, spec_alternation):
    hit_metrics.phase += 1
    if four_and_five:
        four_tick_hit(5, True)
        if fang_lb_spec:
            if spec_alternation:
                five_tick_hit(1, False, True)
                hit_metrics.specced_last_anvil = True
                can_i_spec()
            else:
                five_tick_hit(1, False, False)
                hit_metrics.specced_last_anvil = False
                can_i_spec()
            four_tick_hit(6, False)
        else:
            four_tick_hit(6, False)
            five_tick_hit(1, False, False)
        four_tick_hit(2, False)
        five_tick_hit(1, False, False)
    else:
        five_tick_hit(4, True, False)
        if fang_lb_spec:
            if spec_alternation:
                five_tick_hit(1, False, True)
                hit_metrics.specced_last_anvil = True
                can_i_spec()
            else:
                five_tick_hit(1, False, False)
                hit_metrics.specced_last_anvil = False
                can_i_spec()
            five_tick_hit(7, False, False)
        else:
            five_tick_hit(8, False, False)
    return


def defence_roll(spec, four_tick, five_tick, enraged):
    max_def_roll = 0
    test_weapon = ""
    if enraged:
        tekton.stab_def = 280
        tekton.slash_def = 280
        tekton.crush_def = 180
    else:
        tekton.stab_def = 155
        tekton.slash_def = 165
        tekton.crush_def = 105
    if spec or four_tick:
        test_weapon = loadout.static_crush_weapon
    elif five_tick:
        test_weapon = loadout.five_tick_weapon
    if test_weapon == crush:
        max_def_roll = math.ceil((tekton.defence + 9) * (tekton.crush_def + 64))
    elif test_weapon == stab:
        max_def_roll = math.ceil((tekton.defence + 9) * (tekton.stab_def + 64))
    elif test_weapon == slash:
        max_def_roll = math.ceil((tekton.defence + 9) * (tekton.slash_def + 64))
    rolled_def = random.randint(0, max_def_roll)
    return rolled_def


for x in range(trials):
    hit_metrics = Offensive(0, 0, time_parameter=0.0, phase='', idle_time=0, fang_spec_status=True,
                            specced_last_anvil=False, no_hammer_count=0, one_hammer_count=0, two_hammer_count=0, hp_pool=121)
    if cm:
        tekton = NPC(450, 246, 155, 165, 105, alive_status=True, anvil_checked=False, veng_count=0)
        base_hp = 450
        base_def = 246
    else:
        tekton = NPC(300, 205, 155, 165, 105, alive_status=True, anvil_checked=False, veng_count=0)
        base_hp = 300
        base_def = 205
    def_regen_per_cycle = int((base_def * .05) + 1)
    hp_regen_per_cycle = int((base_hp * .01) + 1)
    hit_metrics.no_hammer_count = 0
    hit_metrics.one_hammer_count = 0
    hit_metrics.two_hammer_count = 0
    hit_metrics.phase = 0
    hit_metrics.four_tick_hit_counter = 0
    hit_metrics.five_tick_hit_counter = 0
    veng_count = 0
    if four_and_five:
        vuln_check()
        pre_anvil()
        anvil_adjustment(check_var11.get(), check_var17.get())
        min_regen()
        post_anvil(fang_lb_spec=lightbearer_equipped, spec_alternation=hit_metrics.fang_spec_status)
        anvil_adjustment(check_var11.get(), check_var17.get())
        min_regen()
        while True:
            if tekton.hp > 0:
                post_anvil(fang_lb_spec=lightbearer_equipped, spec_alternation=hit_metrics.fang_spec_status)
                anvil_adjustment(check_var11.get(), check_var17.get())
                min_regen()
                continue
            else:
                time()
                break
    elif five_only:
        vuln_check()
        pre_anvil()
        anvil_adjustment(check_var11.get(), check_var17.get())
        min_regen()
        post_anvil(fang_lb_spec=lightbearer_equipped, spec_alternation=hit_metrics.fang_spec_status)
        anvil_adjustment(check_var11.get(), check_var17.get())
        min_regen()
        while True:
            if tekton.hp > 0:
                post_anvil(fang_lb_spec=lightbearer_equipped, spec_alternation=hit_metrics.fang_spec_status)
                anvil_adjustment(check_var11.get(), check_var17.get())
                min_regen()
                continue
            else:
                time()
                break

p = inflect.engine()

tick_times_raw = tick_times
hist2, bin_edges2 = np.histogram(tick_times_raw, density=True)
cum_cdf_raw = np.cumsum(hist2 * np.diff(bin_edges2))
sub_115 = []
sub_100 = []
sub_115[:] = [x for x in tick_times if x <= 125]
sub_100[:] = [x for x in tick_times if x <= 100]

no_anvil_num = str(anvils[0]) + ', ' + str(round(((anvils[0] / trials) * 100), 2)) + '%'
one_anvil_num = str(anvils[1]) + ', ' + str(round(((anvils[1] / trials) * 100), 2)) + '%'
two_anvil_num = str(anvils[2]) + ', ' + str(round(((anvils[2] / trials) * 100), 2)) + '%'
three_anvil_num = str(np.sum(anvils[3:])) + ', ' + str(round(((np.sum(anvils[3:]) / trials) * 100), 2)) + '%'
temp1 = p.number_to_words(trials)
no_ham_rate_tot = (str(round(((no_h_one_a / trials) * 100), 2)) + '%')
one_ham_rate_tot = (str(round(((one_h_one_a / trials) * 100), 2)) + '%')
two_ham_rate_tot = (str(round(((two_h_one_a / trials) * 100), 2)) + '%')
one_ham_reset = (str(round((((one_h_one_a + two_h_one_a) / (
        one_hammer_total + two_hammer_total)) * 100), 2)) + '%')
two_ham_reset = (str(round(((two_h_one_a / two_hammer_total) * 100), 2)) + '%')
no_ham_rate = (str(no_h_one_a) + ', ' + str(round(((no_h_one_a / anvils[1]) * 100), 2)) + '%')
one_ham_rate = (str(one_h_one_a) + ', ' + str(round(((one_h_one_a / anvils[1]) * 100), 2)) + '%')
two_ham_rate = (str(two_h_one_a) + ', ' + str(round(((two_h_one_a / anvils[1]) * 100), 2)) + '%')
sub_115_df = (str(round((((np.count_nonzero(sub_115)) / anvils[1]) * 100), 2)) + '%')
sub_100_df = (str(round((((np.count_nonzero(sub_100)) / anvils[1]) * 100), 2)) + '%')
table_dataframe = pd.DataFrame({('trials = ' + str(trials)): ['no anvil', 'one anvil', 'two anvil', 'three or more'],
                                'total, % total': [no_anvil_num, one_anvil_num, two_anvil_num, three_anvil_num],
                                'sub 1:15 %': ['N/A', sub_115_df, '0', '0'],
                                'sub 1:00 %': ['N/A', sub_100_df, '0', '0']})
table_dataframe2 = pd.DataFrame({('trials = ' + str(trials)): ['no hammer', 'one hammer', 'two hammer'],
                                 'total, % of 1 anvils': [no_ham_rate, one_ham_rate, two_ham_rate],
                                 '% of total trials': [no_ham_rate_tot, one_ham_rate_tot, two_ham_rate_tot],
                                 ('1 anvil ham. ' + r'$\subset$' + ' total ham.'): ['N/A', (str(one_ham_reset) + ' 1 & 2 Ham.'), (str(two_ham_reset) + ' 2 ham. only')]})
minutes_list = [' 0:45', ' 0:48', ' 0:51', ' 0:54', ' 0:57', ' 1:00', ' 1:03', ' 1:06', ' 1:09', ' 1:12', ' 1:15',
                ' 1:18', ' 1:21', ' 1:24', ' 1:27', ' 1:30', ' 1:33', ' 1:36', ' 1:39', ' 1:42', ' 1:45', ' 1:48',
                ' 1:51', ' 1:54', ' 1:57', ' 2:00', ' 2:03', ' 2:06', ' 2:09', ' 2:12', ' 2:15', ' 2:18', ' 2:21',
                ' 2:24', ' 2:27', ' 2:30', ' 2:33', ' 2:36', ' 2:39', ' 2:42', ' 2:45', ' 2:48']
minutes_list_big_step = [' 0:00', ' 0:15', ' 0:30', ' 0:45', ' 1:00', ' 1:15', ' 1:30', ' 1:45', ' 2:00', ' 2:15',
                         ' 2:30', ' 2:45', ' 3:00', ' 3:15', ' 3:30', ' 3:45', ' 4:00', ' 4:15', ' 4:30', ' 4:45',
                         ' 5:00', ' 5:15', ' 5:30', ' 5:45', ' 6:00', ' 6:15', ' 6:30', ' 6:45', ' 7:00', ' 7:15',
                         ' 7:30', ' 7:45', ' 8:00', ' 8:15', ' 8:30', ' 8:45', ' 9:00', ' 9:15', ' 9:30', ' 9:45',
                         '10:00', '10:15', '10:30', '10:45', '11:00', '11:15', '11:30', '11:45', '12:00', '12:15',
                         '12:30', '12:45', '13:00', '13:15', '13:30', '13:45']
minutes_list_bigger_step = [' 0:00', ' 0:25', ' 0:50', ' 1:15', ' 1:40', ' 2:05', ' 2:30', ' 2:55', ' 3:20', ' 3:45',
                            ' 4:10', ' 4:35', ' 5:00', ' 5:25', ' 5:50', ' 6:15', ' 6:40', ' 7:05', ' 7:30', ' 7:55',
                            ' 8:20', ' 8:45', ' 9:10', ' 9:35', '10:00', '10:25', '10:50', '11:15', '11:40', '12:05',
                            '12:30', '12:55', '13:20', '13:45']


def plot_adjustment():
    plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)
    # plt.subplots_adjust(wspace=.2, hspace=0)


plt.rcParams.update(
    {"lines.color": "silver", "patch.edgecolor": "black", "text.color": "black", "axes.facecolor": "silver",
     "axes.edgecolor": "black", "axes.labelcolor": "black", "xtick.color": "black", "ytick.color": "black",
     "grid.color": "silver", "figure.facecolor": "dimgray", "figure.edgecolor": "dimgray", "axes.titlecolor": "black",
     "savefig.facecolor": "black", "savefig.edgecolor": "black"})

fig = plt.figure()
gs = fig.add_gridspec(3, 2)
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[1, 0])
total_sample_aux_plot = fig.add_subplot(gs[2, 1])
total_sample_main_plot = fig.add_subplot(gs[2, 1])
one_anvil_aux_plot = fig.add_subplot(gs[0, 1])
one_anvil_main_plot = fig.add_subplot(gs[0, 1])
ax4t = fig.add_subplot(gs[2, 0])
ax4 = fig.add_subplot(gs[2, 0])
ax4t.axes.set_visible(False)
xd = ['gray', 'gray', 'gray', 'gray']
colors = [["silver", "silver", "silver", "silver"], ["silver", "silver", "silver", "silver"],
          ["silver", "silver", "silver", "silver"], ["silver", "silver", "silver", "silver"]]
mpl_table = ax1.table(cellText=table_dataframe.values,
                      colLabels=table_dataframe.columns, cellLoc='center', rowLoc='center', loc='upper right',
                      cellColours=colors, colColours=xd)
mpl_table.auto_set_font_size(False)
ax1.axis(False)
mpl_table.set_fontsize(9)

mpl_table2 = ax2.table(cellText=table_dataframe2.values,
                       colLabels=table_dataframe2.columns, cellLoc='center', rowLoc='center', loc='upper right',
                       cellColours=colors[0:3], colColours=xd)
mpl_table2.auto_set_font_size(False)
mpl_table2.set_fontsize(9)
ax2.axis(False)

tick_times_one_anvil[:] = [x for x in tick_times if x <= 150]

n = pd.Series(np.random.randn(trials))
first_q1 = float(np.quantile(n, .25))
first_q3 = float(np.quantile(n, .75))
iqr = first_q3 - first_q1
bin_width = (2 * iqr) / ((len(n)) ** (1. / 3.))
bin_number = int(np.ceil((np.max(n) - np.min(n)) / bin_width))
m = pd.Series(np.random.randn(len(tick_times_one_anvil)))
second_q1 = float(np.quantile(m, .25))
second_q3 = float(np.quantile(m, .75))
iqr_second = second_q3 - second_q1
bin_width_second = (2 * iqr_second) / ((len(m)) ** (1. / 3.))
bin_number_second = int(np.ceil((m.max() - m.min()) / bin_width_second))

cumulative_total_graph = sns.kdeplot(cum_cdf_raw, x=tick_times_raw, cumulative=True, common_norm=False, common_grid=True,
                           legend=True, color='crimson')
empirical_total_graph = sns.ecdfplot(cum_cdf_raw, x=tick_times_raw, legend=True, color='green')
data_x, data_y = cumulative_total_graph.lines[0].get_data()
yi = .99
xi = np.interp(yi, data_y, data_x)
cumulative_total_graph.set(xticks=(np.arange(0, 1400, step=25)), xlim=(0, xi), yticks=(np.arange(0, 1.1, step=.1)), ylim=(0, 1),
                 ylabel='probability of killing tekton', xlabel='time of encounter in ticks',
                 title='cumulative probability of killing tekton')
cumulative_total_graph.set_xticklabels(cumulative_total_graph.get_xticklabels(), rotation=45)
aux_axis_cumulative = cumulative_total_graph.twiny()
sns.kdeplot(ax=aux_axis_cumulative, bins=80)
cumulative_total_graph.legend(labels=('theoretical', 'empirical'), labelcolor='black')
aux_axis_cumulative.set(xticks=(np.arange(0, 840, step=25)), xlim=(0, (xi * .6)), xlabel='time of encounter in seconds')
aux_axis_cumulative.set_xticklabels(minutes_list_bigger_step, rotation=45)
cumulative_total_graph.grid('visible', color='black')

# total histogram graph
n2t, bins2t, pathces2t = total_sample_aux_plot.hist(tick_times, bins=bin_number, density=False, alpha=0)
n2, bins2, pathces2 = total_sample_main_plot.hist(tick_times, bins=bin_number, density=True, edgecolor='black', linewidth=.8)

total_sample_aux_plot.set(ylabel='number of killed tektons in sample')
mu2 = np.mean(tick_times)
sigma2 = statistics.stdev(tick_times)
y2 = ((1 / (np.sqrt(2 * np.pi) * sigma2)) * np.exp(-0.5 * (1 / sigma2 * (bins2 - mu2)) ** 2))
total_sample_main_plot.plot(bins2, y2)
total_sample_main_plot_xticks = (np.arange(75, (np.max(tick_times) + 25), step=25))
total_sample_main_plot.xaxis.set_tick_params(rotation=45)
total_sample_aux_plot.yaxis.tick_right()
total_sample_main_plot_aux_xaxis = total_sample_main_plot.secondary_xaxis('top')
total_sample_aux_plot.xaxis.set_visible(False)
total_sample_aux_plot.spines.top.set_visible(False)
total_sample_main_plot_aux_xaxis.xaxis.set_tick_params(rotation=45)
total_sample_main_plot_aux_xaxis.set(xticks=(np.arange(75, (np.max(tick_times)), step=25)), xlim=(75, (np.max(tick_times))))
total_sample_main_plot_aux_xaxis_labels = np.arange(75, (np.max(tick_times)), step=25)
total_sample_main_plot_aux_xaxis.set_xticklabels(minutes_list_big_step[3:(len(total_sample_main_plot_aux_xaxis_labels) + 3)])
total_sample_main_plot.set(ylabel='probability density', xlabel='time of encounter in ticks',
        title='tekton density histogram of ' + p.number_to_words(trials) + ' trials', xticks=total_sample_main_plot_xticks,
        xlim=(75, (np.max(tick_times))))
total_sample_main_plot.locator_params(nbins=22, axis='y')
total_sample_aux_plot.locator_params(nbins=22, axis='y')
total_sample_aux_plot.yaxis.set_label_position('right')
total_sample_main_plot.xaxis.grid(True, color='black')
total_sample_main_plot.set_axisbelow(True)
total_sample_aux_plot.yaxis.grid(True, color='black')
total_sample_main_plot.set_facecolor((0.0, 0.0, 0.0, 0.0))

# under one anvil graph
n, bins, pathces = one_anvil_main_plot.hist(tick_times_one_anvil, bins=bin_number_second, density=True, edgecolor='black', linewidth=.8)
nt, binst, pathcest = one_anvil_aux_plot.hist(tick_times_one_anvil, bins=bin_number_second, density=False, edgecolor='black',
                                linewidth=.8, alpha=0)

one_anvil_aux_plot.xaxis.set_visible(False)
one_anvil_aux_plot.set(ylabel='number of one anvils')
one_anvil_aux_plot.yaxis.tick_right()
one_anvil_aux_plot.yaxis.set_label_position('right')
mu = np.mean(tick_times_one_anvil)
sigma = statistics.stdev(tick_times_one_anvil)
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu)) ** 2))
one_anvil_main_plot.plot(bins, y)
one_anvil_main_plot_xticks = (np.arange(75, 165, step=5))
one_anvil_main_plot.set(xticks=one_anvil_main_plot_xticks,
        xlim=(75, 160), xlabel='time of encounter in ticks', ylabel='Probability density',
        title='number of tektons under one anvil in ' + p.number_to_words(trials) + ' trials')
one_anvil_main_plot.locator_params(nbins=22, axis='y')
one_anvil_aux_plot.locator_params(nbins=22, axis='y')
one_anvil_main_plot.xaxis.set_tick_params(rotation=45)
one_anvil_main_plot_aux_xaxis = one_anvil_main_plot.secondary_xaxis('top')
one_anvil_aux_plot.spines.top.set_visible(False)
one_anvil_main_plot.spines.top.set_visible(False)
one_anvil_main_plot_aux_xaxis.set(xticks=(np.arange(75, 165, step=5)), xlim=(75, 160))
one_anvil_main_plot_aux_xaxis.set_xticklabels(minutes_list[:18])
one_anvil_main_plot_aux_xaxis.xaxis.set_tick_params(rotation=45)
one_anvil_main_plot.xaxis.grid(True, color='black')
one_anvil_main_plot.set_axisbelow(True)

one_anvil_aux_plot.yaxis.grid(True, color='black')
plt.subplots_adjust(wspace=.25, hspace=0, right=.93, left=0.05, top=.90, bottom=.07)
print('script completed in', datetime.now() - (start_time - initialization_time), 'seconds')
one_anvil_main_plot.set_facecolor((0.0, 0.0, 0.0, 0.0))

plt.show()

# to do list
# fucking leave some comments on the code you degenerate fuck
# optimize backend code
# maybe fix table box margin

# can probably just tack this one onto post anvil adjustment
# def min_regen():
# honestly cba its fine

#update numbers for veng

#dear god the graphs
#idk man graphs are fucked nothing wanted to go into functions seaborn makes me want to choke on broken glass
#did my best

# this is probably a horrible idea that ill regret but could possibly store the booleanvars from buttons into a list would be a lot cleaner
# ok yeah that was a pretty fucking bad idea

# this whole block is kinda a fucking nightmare thanks to fang but uh idk at least the function within the function was clever in a kinda suspic way
# def attack_roll(spec_attack, four_tick, five_tick, multiplier):

# is also bloated but weve tried this before to little success
# def hit_value_roll(spec_bonus, four_tick, five_tick, max_hit_modifier=1.0):

#maybe add short lure option if i can be fucked