from datetime import datetime

selection_time = datetime.now()
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
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
import sys
import os


trials = 10000
root = tk.Tk()
module_time = datetime.now()
initialization_time = module_time - selection_time
root.title('Tekton Sim Version 1.6')
root.geometry('280x240')
five_tick_only_check = tk.BooleanVar()
cm_check = tk.BooleanVar()
inq_check = tk.BooleanVar()
fang_check = tk.BooleanVar()
no_ring = False
b_ring_check = False
brim_check = False
ultor_check = False
feros_check = tk.BooleanVar()
tort_check = tk.BooleanVar()
lightbearer_check = tk.BooleanVar()
check_var10 = tk.BooleanVar()
prevenge_check = tk.BooleanVar()
check_var12 = tk.BooleanVar()
check_var13 = tk.BooleanVar()
vuln_check = tk.BooleanVar()
check_var15 = tk.BooleanVar()
book_of_water_check = tk.BooleanVar()
veng_camp_check = tk.BooleanVar()
sql_import = tk.BooleanVar()
ring_selector = tk.StringVar()

desired_width = 350
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 17)


def abort():
    return sys.exit(0)


def trials_selection():
    global trials
    if check_var10.get():
        trials = 1000
        string_variable.set(f'number of trials: {trials}')
    elif check_var12.get():
        trials = 10000
        string_variable.set(f'number of trials: {trials}')
    elif check_var13.get():
        trials = 100000
        string_variable.set(f'number of trials: {trials}')
    elif check_var15.get():
        trials = 1000000
        string_variable.set(f'number of trials: {trials}')
    else:
        trials = 10000
        string_variable.set(f'number of trials: {trials}')
    return trials


def fang_checker_lb():
    while not fang_check.get():
        return C9.toggle()


def check_correction_new(num):
    while num == '1000':
        C12.deselect()
        C13.deselect()
        C15.deselect()
        return trials_selection()
    while num == '10000':
        C10.deselect()
        C13.deselect()
        C15.deselect()
        return trials_selection()
    while num == '100000':
        C12.deselect()
        C10.deselect()
        C15.deselect()
        return trials_selection()
    while num == '1mil':
        C13.deselect()
        C12.deselect()
        C10.deselect()
        return trials_selection()


def spec_ring():
    if fang_check.get():
        if lightbearer_check.get():
            ring_selector.set('lightbearer')
            ring_menu.config(state='disabled')
        else:
            ring_selector.set('Select Ring')
            ring_menu.config(state='normal')
        return
    else:
        C9.deselect()


def check_correction_veng():
    if prevenge_check.get():
        if veng_camp_check.get():
            return C17.toggle()
        else:
            return


def check_correction_veng2():
    if veng_camp_check.get():
        if prevenge_check.get():
            return C11.toggle()
        else:
            return


def show():
    tk.Label(text=ring_selector.get())


options = ["Select Ring", "b_ring", "brim", "ultor_ring"]

ring_selector.set("Select Ring")

ring_menu = tk.OptionMenu(root, ring_selector, *options)
ring_menu.place(x=175, y=205)

string_variable = tk.StringVar()
C1 = tk.Checkbutton(root, text="five tick only", variable=five_tick_only_check, onvalue=1, offvalue=0)
C1.place(x=25, y=80)
C2 = tk.Checkbutton(root, text="CM", variable=cm_check, onvalue=1, offvalue=0)
C2.place(x=25, y=55)
C2.toggle()
C3 = tk.Checkbutton(root, text="inq", variable=inq_check, onvalue=1, offvalue=0)
C3.place(x=75, y=55)
C3.toggle()
C4 = tk.Checkbutton(root, text="fang", variable=fang_check, onvalue=1, offvalue=0)
C4.place(x=140, y=130)
C7 = tk.Checkbutton(root, text="feros", variable=feros_check, onvalue=1, offvalue=0)
C7.place(x=75, y=130)
C8 = tk.Checkbutton(root, text="tort", variable=tort_check, onvalue=1, offvalue=0)
C8.place(x=25, y=130)
C11 = tk.Checkbutton(root, text="pre veng", variable=prevenge_check, onvalue=1, offvalue=0, command=check_correction_veng)
C11.place(x=120, y=55)
C11.toggle()
C9 = tk.Checkbutton(root, text="lightbearer", variable=lightbearer_check, onvalue=1, offvalue=0, command=spec_ring)
C9.place(x=140, y=155)
C10 = tk.Checkbutton(root, text="1000", variable=check_var10, onvalue=1, offvalue=0, command=lambda: check_correction_new('1000'))
C10.place(x=25, y=30)
C12 = tk.Checkbutton(root, text="10000", variable=check_var12, onvalue=1, offvalue=0, command=lambda: check_correction_new('10000'))
C12.place(x=85, y=30)
trials_selection()
C12.toggle()
C13 = tk.Checkbutton(root, text="100000", variable=check_var13, onvalue=1, offvalue=0, command=lambda: check_correction_new('100000'))
C13.place(x=150, y=30)
C15 = tk.Checkbutton(root, text="1mil", variable=check_var15, onvalue=1, offvalue=0, command=lambda: check_correction_new('1mil'))
C15.place(x=225, y=30)
C14 = tk.Checkbutton(root, text="vuln", variable=vuln_check, onvalue=1, offvalue=0)
C14.place(x=130, y=80)
C14.toggle()
C16 = tk.Checkbutton(root, text="vuln book", variable=book_of_water_check, onvalue=1, offvalue=0)
C16.place(x=190, y=55)
C17 = tk.Checkbutton(root, text="veng camp", variable=veng_camp_check, onvalue=1, offvalue=0, command=check_correction_veng2)
C17.place(x=190, y=80)
C18 = tk.Checkbutton(root, text="import to SQL", variable=sql_import, onvalue=1, offvalue=0)
C18.place(x=180, y=180)


trials_text = tk.Label(root, textvariable=string_variable)
trials_text.place(x=30, y=10)
notif_text = tk.Label(root, text='lb is for fang spec only')
notif_text.place(x=30, y=110)
exit_button = tk.Button(root, text="Exit", command=abort)
exit_button.place(x=230, y=0)
button_submit = tk.Button(root, text="Submit", command=root.destroy)
button_submit.place(x=100, y=210)
root.mainloop()


if ring_selector.get() == 'b_ring':
    b_ring_check = True
elif ring_selector.get() == 'brim':
    brim_check = True
elif ring_selector.get() == 'ultor_ring':
    ultor_check = True
else:
    no_ring = True

checkbuttons_list = [('cm', cm_check.get()), ('inq', inq_check.get()), ('five_tick_only', five_tick_only_check.get()),
                     ('fang', fang_check.get()), ('feros', feros_check.get()), ('tort', tort_check.get()),
                     ('preveng', prevenge_check.get()),
                     ('veng_camp', veng_camp_check.get()), ('vuln', vuln_check.get()),
                     ('book_of_water', book_of_water_check.get())]
ring_list = [('b_ring', b_ring_check), ('brim', brim_check), ('ultor_ring', ultor_check), ('lightbearer', lightbearer_check.get()), ('Select Ring', no_ring)]


start_time = datetime.now()
result_array = ["hit", "miss"]
inq = inq_check.get()
cm = cm_check.get()
fang = fang_check.get()
five_only = five_tick_only_check.get()
if fang:
    scythe = False
else:
    scythe = True


print('inq:', inq)
print('cm:', cm)
print('fang:', fang)
print('five tick only:', five_only)
print('ring selected: ', ring_selector.get())
print('b ring:', b_ring_check)
print('brim ring:', brim_check)
print('ultor ring:', ultor_check)
print('tort:', tort_check.get())
print('feros:', feros_check.get())
print('vuln', vuln_check.get())
print('vuln book', book_of_water_check.get())
print('preveng', prevenge_check.get())
print('veng camp', veng_camp_check.get())
print('lightbearer', lightbearer_check.get())
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
hammer_count_list = []
anvil_count_list = []
times = []
tick_times = []
tick_times_one_anvil = []
hp_check_list = []

crush = 'crush'
slash = 'slash'
stab = 'stab'

if sql_import.get():
    connection_string = r"Driver={ODBC Driver 17 for SQL Server}; Server=DESKTOP-3TJHN4P\MSSQLSERVER01; Database=tekton_sim_data; Trusted_Connection=yes;"
    connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
    engine = create_engine(connection_url)
    conn_id = engine.connect()
    conn = engine.connect()


# These are the metrics that we will be measuring EACH trial and they will reset to initial conditions at the start
class Offensive:
    def __init__(self, four_tick_hit_counter, five_tick_hit_counter, time_parameter, phase, idle_time, fang_spec_status,
                 specced_last_anvil, hammer_missed_count, hammer_hit_count, hp_pool):
        self.four_tick_hit_counter = four_tick_hit_counter
        self.five_tick_hit_counter = five_tick_hit_counter
        self.time_parameter = time_parameter
        self.phase = phase
        self.idle_time = idle_time
        self.fang_spec_status = fang_spec_status
        self.specced_last_anvil = specced_last_anvil
        self.hammer_missed_count = hammer_missed_count
        self.hammer_hit_count = hammer_hit_count
        self.hp_pool = hp_pool


# This is the block where gear is stored this will stay static throughout each trial.
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


# Function that will modify the gear setup based on selections from the gui prompt
# Now that im looking at it again gear selection and loadout adjuster are probably redundant functions
def gear_selection():
    attack_gear = 0
    strength_gear = 0
    ring_stats = {'Select Ring': (0, 0), 'b_ring': (0, 8), 'brim': (4, 4), 'ultor_ring': (0, 12), 'lightbearer': (0, 0)}
    attack_gear += ring_stats[ring_selector.get()][0]
    strength_gear += ring_stats[ring_selector.get()][1]
    if tort_check.get():
        attack_gear += 5
        strength_gear += 2
    if feros_check.get():
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
    loadout_list = [loadout.dwh_str_bonus, loadout.four_tick_str_bonus, loadout.fang_str_bonus, loadout.scy_str_bonus,
                    loadout.dwh_att_bonus, loadout.four_tick_att_bonus, loadout.fang_att_bonus, loadout.scy_att_bonus]
    loadout_list[:3] = [i + str_modifier for i in loadout_list[:3]]
    loadout_list[4:] = [i + att_modifier for i in loadout_list[4:]]
    (loadout.dwh_str_bonus, loadout.four_tick_str_bonus, loadout.fang_str_bonus, loadout.scy_str_bonus,
     loadout.dwh_att_bonus, loadout.four_tick_att_bonus, loadout.fang_att_bonus, loadout.scy_att_bonus) = loadout_list
    loadout.five_tick_weapon = five_tick_style
    return


# These are the default loadouts that will be selected based on gui selection
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


# These are the stats of the npc itself and its active statuses
class NPC:
    def __init__(self, hp, defence, stab_def, slash_def, crush_def, veng_count):
        self.hp = hp
        self.defence = defence
        self.stab_def = stab_def
        self.slash_def = slash_def
        self.crush_def = crush_def
        self.veng_count = veng_count

    def lower_hp(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def lower_def(self, amount):
        self.defence -= amount
        if self.defence < 0:
            self.defence = 0


# This damage value selection based on adjusted gear and whether the hit chance function determines a hit
def hit_value_roll(spec_bonus, four_tick, five_tick, max_hit_modifier=1.0):
    def strength_selector():
        if spec_bonus:
            return loadout.dwh_str_bonus
        elif four_tick:
            return loadout.four_tick_str_bonus
        elif five_tick:
            if fang:
                return loadout.fang_str_bonus
            elif scythe:
                return loadout.scy_str_bonus
        else:
            raise ValueError("Error in strength selector function")


    damage_selection = 0
    if spec_bonus:
        max_hit = int(
            int(0.5 + effective_spec_strength_lvl * ((strength_selector() + 64) / 640)) * 1.5 * loadout.gear_multiplier)
        return int(random.randint(0, max_hit))
    else:
        max_hit = int(int(0.5 + effective_strength_lvl * ((strength_selector() + 64) / 640)) * loadout.gear_multiplier)
        if four_tick:
            return int(random.randint(0, max_hit))
        elif five_tick:
            if fang:
                max_hit = int(((0.5 + effective_strength_lvl * ((strength_selector() + 64) / 640)) * max_hit_modifier))
                min_hit = int((0.5 + effective_strength_lvl * ((strength_selector() + 64) / 640)) * .15)
                return int(random.randint(min_hit, max_hit))
            else:
                return int(random.randint(0, int(max_hit * max_hit_modifier)))
    raise ValueError("Error in hit_value_roll function")


# I forget exactly why I added these but I believe there was some weird rounding error that math.ceiling wasnt fixing
def is_whole(whole):
    return whole % 1 == 0


def adjust_def_integer():
    if not is_whole(tekton.defence):
        tekton.defence = int(tekton.defence) + 1


# Attack roll function that determines the roll that will be used in hit chance based on gear loadout and NPC stats
def attack_roll(spec_attack, four_tick, five_tick, multiplier):
    def attack_selector():
        if spec_attack:
            return loadout.dwh_att_bonus
        elif four_tick:
            return loadout.four_tick_att_bonus
        elif five_tick:
            if fang:
                return loadout.fang_att_bonus
            elif scythe:
                return loadout.scy_att_bonus
        else:
            raise ValueError("Error in attack selector function")

    if spec_attack:
        max_attack_roll_basic = int(effective_spec_attack_lvl * (attack_selector() + 64))
    else:
        max_attack_roll_basic = int(effective_attack_lvl * (attack_selector() + 64))
    if lightbearer_check.get():
        if fang:
            max_attack_roll = int(max_attack_roll_basic * multiplier)
        else:
            max_attack_roll = int(max_attack_roll_basic * loadout.gear_multiplier)
    else:
        max_attack_roll = int(max_attack_roll_basic * loadout.gear_multiplier)
    first_roll = random.randint(0, max_attack_roll)
    return first_roll


# Function that will take the attack roll and defense roll and determine hit or miss of main damage phase
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
            return True if any(i > def_roll_check for i in roll_list) else False
        else:
            attack_roll_check = attack_roll(False, False, True, multiplier=1.0)
    return True if attack_roll_check > def_roll_check else False


# Function that determines whether vulnerability hit which lowers initial tekton defense before any other def. reduction
# I need to add something that lets this be more adjustable based on varying gear
def vuln_applicator():
    if vuln_check.get():
        vuln = np.random.choice(result_array, 1, replace=True, p=[.62, (1 - .62)])
        if book_of_water_check.get():
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


def hammer_check():
    if hit_metrics.hammer_hit_count in [0, 1, 2]:
        hammer_count_list.append(hit_metrics.hammer_hit_count)
    return


def hammer_missed():
    tekton.lower_def(int((tekton.defence * .05)))
    adjust_def_integer()
    hit_metrics.hammer_missed_count += 1
    return


# Function that will take the attack roll and defense roll and determine hit or miss of specs for initial def reduction
def spec_hit(status):
    damage_val = hit_value_roll(spec_bonus=True, four_tick=False, five_tick=False)
    tekton.lower_hp(damage_val)
    tekton.lower_def(int((tekton.defence * .3)))
    adjust_def_integer()
    hit_metrics.hammer_hit_count += 1
    defence_roll(True, False, False, status)
    if hit_chancer(True, False, False, False, status):
        damage_val = hit_value_roll(spec_bonus=True, four_tick=False, five_tick=False)
        tekton.lower_hp(damage_val)
        if damage_val > 0:
            tekton.lower_def(int((tekton.defence * .3)))
            adjust_def_integer()
            hit_metrics.hammer_hit_count += 1
        else:
            hammer_missed()
    else:
        hammer_missed()
    return


# Function that will be called to indicate number of hits in damage phase for mace
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


# Function that will be called to make each scythe hit roll seperately for each of the 3 instances of dmg
def scy_dmg(step_down, status):
    if hit_chancer(False, False, True, False, status):
        damage_val = hit_value_roll(False, four_tick=False, five_tick=True, max_hit_modifier=step_down)
        tekton.lower_hp(damage_val)
    else:
        damage_val = 0
        tekton.lower_hp(damage_val)
    return damage_val


# Function that will be called to indicate number of hits in damage phase for 5 tick weapon
def five_tick_hit(instances, status, fang_spec_pass_var):
    for _ in range(instances):
        defence_roll(False, False, True, status)
        if tekton.hp > 0:
            hit_metrics.five_tick_hit_counter += 1
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
            for i in [1, .5, .25]:
                scy_dmg(i, status)
        else:
            if hit_chancer(False, False, True, False, status):
                damage_val = hit_value_roll(False, four_tick=False, five_tick=True)
                tekton.lower_hp(damage_val)
            else:
                damage_val = 0
                tekton.lower_hp(damage_val)


def veng_calc():
    if cm:
        if veng_camp_check.get():
            if tekton.veng_count < 2:
                return 58
            else:
                return 65
        else:
            return 65
    else:
        if veng_camp_check.get():
            if tekton.veng_count < 2:
                return 39
            else:
                return 44
        else:
            return 44


def veng_applicator(pre_veng, veng_camp):
    if pre_veng:
        tekton.lower_hp(random.randint(1, veng_calc()))
        return tekton.hp
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


def anvil_adjustment():
    if tekton.hp > 0:
        cycle_select = random.randint(3, 6)
        hit_metrics.idle_time += ((cycle_select * 3) + 10)
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
    anvil_count_list.append(hit_metrics.phase)


def pre_anvil():
    if four_and_five:
        spec_hit(False)
        hammer_check()
        # hammer_count_list.append(hit_metrics.hammer_hit_count)
        for four_num, five_num in [(3, 1), (1, 2)]:
            four_tick_hit(four_num, False)
            five_tick_hit(five_num, False, False)
        # four_tick_hit(3, False)
        # five_tick_hit(1, False, False)
        # four_tick_hit(1, False)
        # five_tick_hit(2, False, False)
    else:
        spec_hit(False)
        hammer_check()
        # hammer_count_list.append(hit_metrics.hammer_hit_count)
        five_tick_hit(6, False, False)
    return


def can_i_spec():
    if lightbearer_check.get():
        hit_metrics.fang_spec_status = True
        return hit_metrics.fang_spec_status
    else:
        if hit_metrics.specced_last_anvil:
            hit_metrics.fang_spec_status = False
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
    test_weapon = ""
    if enraged:
        tekton.stab_def, tekton.slash_def, tekton.crush_def = [280, 280, 180]
    else:
        tekton.stab_def, tekton.slash_def, tekton.crush_def = [155, 165, 105]
    if spec or four_tick:
        test_weapon = loadout.static_crush_weapon
    elif five_tick:
        test_weapon = loadout.five_tick_weapon
    def_roll_dict = {'crush': math.ceil((tekton.defence + 9) * (tekton.crush_def + 64)),
                     'stab': math.ceil((tekton.defence + 9) * (tekton.stab_def + 64)),
                     'slash': math.ceil((tekton.defence + 9) * (tekton.slash_def + 64))}
    return random.randint(0, def_roll_dict[test_weapon])


for x in range(trials):
    hit_metrics = Offensive(0, 0, time_parameter=0.0, phase=0, idle_time=0, fang_spec_status=True,
                            specced_last_anvil=False, hammer_missed_count=0, hammer_hit_count=0, hp_pool=121)
    if cm:
        tekton = NPC(450, 246, 155, 165, 105, veng_count=0)
        base_hp, base_def = [450, 246]
    else:
        tekton = NPC(300, 205, 155, 165, 105, veng_count=0)
        base_hp, base_def = [300, 205]

    def_regen_per_cycle = int((base_def * .05) + 1)
    hp_regen_per_cycle = int((base_hp * .01) + 1)
    if four_and_five:
        vuln_applicator()
        pre_anvil()
        veng_applicator(prevenge_check.get(), veng_camp_check.get())
        hp_check_list.append(tekton.hp)
        anvil_adjustment()
        hit_metrics.hp_pool += 44
        min_regen()
        while True:
            if tekton.hp > 0:
                post_anvil(fang_lb_spec=lightbearer_check.get(), spec_alternation=hit_metrics.fang_spec_status)
                veng_applicator(False, veng_camp_check.get())
                anvil_adjustment()
                min_regen()
                continue
            else:
                time()
                break
    elif five_only:
        vuln_applicator()
        pre_anvil()
        veng_applicator(prevenge_check.get(), veng_camp_check.get())
        hp_check_list.append(tekton.hp)
        anvil_adjustment()
        hit_metrics.hp_pool += 44
        min_regen()
        while True:
            if tekton.hp > 0:
                post_anvil(fang_lb_spec=lightbearer_check.get(), spec_alternation=hit_metrics.fang_spec_status)
                veng_applicator(False, veng_camp_check.get())
                anvil_adjustment()
                min_regen()
                continue
            else:
                time()
                break


print(len(anvil_count_list), len(hammer_count_list))
p = inflect.engine()


results_df = pd.DataFrame(list(zip(tick_times, anvil_count_list, hammer_count_list, hp_check_list)),
                          columns=['tick_times', 'anvil_count', 'hammer_count', 'hp_after_pre_anvil'])

for name, gear_val in checkbuttons_list:
    if gear_val:
        results_df[name] = 1
    else:
        results_df[name] = 0
ring_list = [('b_ring', b_ring_check), ('brim', brim_check), ('ultor_ring', ultor_check), ('lightbearer', lightbearer_check.get()), ('Select Ring', no_ring)]
ring_name = ['b_ring', 'brim', 'ultor_ring', 'lightbearer']
for name, gear_val in ring_list:
    if not gear_val:
        continue
    else:
        results_df['ring'] = name

if results_df['ring'].unique() not in ring_name:
    results_df['ring'] = None

print(results_df)
import_df = results_df.copy()
if sql_import.get():
    temp = input('port to sql?')
    if temp == 'y':
        max_id = conn_id.execute(text("""SELECT max(ID)
                        FROM tekton_results""")).first()[0]
        if max_id == None:
            max_id = 0
        conn_id.close()
        import_df.index += max_id + 1
        print(import_df)
        # noinspection PyUnboundLocalVariable
        import_df.to_sql('tekton_results', con=conn, if_exists='append', index_label='ID')

no_anvils = len(results_df[(results_df['anvil_count'] == 0)])
one_anvils = len(results_df[(results_df['anvil_count'] == 1)])
two_anvils = len(results_df[(results_df['anvil_count'] == 2)])
three_or_more_anvils = len(results_df[(results_df['anvil_count'] >= 3)])
no_h_one_a = len(results_df[(results_df['hammer_count'] == 0) & (results_df['anvil_count'] == 1)])
no_hammer_total = len(results_df[(results_df['hammer_count'] == 0)].copy())
one_h_one_a = len(results_df[(results_df['hammer_count'] == 1) & (results_df['anvil_count'] == 1)])
one_hammer_total = len(results_df[(results_df['hammer_count'] == 1)])
two_h_one_a = len(results_df[(results_df['hammer_count'] == 2) & (results_df['anvil_count'] == 1)])
two_hammer_total = len(results_df[(results_df['hammer_count'] == 2)][['hammer_count']])
tick_times_df = results_df.copy()
tick_times_df['completion'] = 1
tick_times_df = tick_times_df[['tick_times', 'completion']]
tick_times_one_anvil = tick_times_df[tick_times_df['tick_times'] <= 150][['tick_times']]
print(len(tick_times_df))
print(len(tick_times_one_anvil))
tick_times_raw = tick_times
hist2, bin_edges2 = np.histogram(tick_times_raw, density=True)
diff_bin_edge = np.diff(bin_edges2)
data_ = hist2 * diff_bin_edge

cum_cdf_raw = np.cumsum(data_, axis=0)
sub_115 = len(results_df[(results_df['tick_times']<=125)])
sub_100 = len(results_df[(results_df['tick_times']<=100)])


def output_formatter(numerator, divisor, long):
    if long:
        return f'{numerator}, {round(((numerator / divisor) * 100), 2)}%'
    else:
        return f'{round(((numerator / divisor) * 100), 2)}%'


no_anvil_num = output_formatter(no_anvils, trials, True)
one_anvil_num = output_formatter(one_anvils, trials, True)
two_anvil_num = output_formatter(two_anvils, trials, True)
three_anvil_num = output_formatter(three_or_more_anvils, trials, True)
no_ham_rate_tot = output_formatter(no_h_one_a, trials, False)
one_ham_rate_tot = output_formatter(one_h_one_a, trials, False)
two_ham_rate_tot = output_formatter(two_h_one_a, trials, False)

one_ham_reset = output_formatter((one_h_one_a + two_h_one_a), (one_hammer_total + two_hammer_total), False)
two_ham_reset = output_formatter(two_h_one_a, two_hammer_total, False)
no_ham_rate = output_formatter(no_h_one_a, one_anvils, True)
one_ham_rate = output_formatter(one_h_one_a, one_anvils, True)
two_ham_rate = output_formatter(two_h_one_a, one_anvils, True)
sub_115_df = output_formatter(sub_115, one_anvils, True)
sub_100_df = output_formatter(sub_100, one_anvils, True)

table_dataframe = pd.DataFrame({f'Trials: {trials}': ['No Anvil', 'One Anvil', 'Two Anvil', 'Three or More'],
                                'Total, % Total': [no_anvil_num, one_anvil_num, two_anvil_num, three_anvil_num],
                                'Total, Sub 1:15 %': ['N/A', sub_115_df, '0', '0'],
                                'Total, Sub 1:00 %': ['N/A', sub_100_df, '0', '0']})
table_dataframe2 = pd.DataFrame({f'Trials: {trials}': ['No Hammer', 'One Hammer', 'Two Hammer'],
                                 'Total, % of One Anvils': [no_ham_rate, one_ham_rate, two_ham_rate],
                                 '% of Total Trials': [no_ham_rate_tot, one_ham_rate_tot, two_ham_rate_tot],
                                 (r"One Anvil Ham. $\subset$ Total Ham."): ['N/A', f'{one_ham_reset} 1 & 2 Ham.', f'{two_ham_reset} 2 Ham. only']})
minutes_list = ['0:45', '0:48', '0:51', '0:54', '0:57', '1:00', '1:03', '1:06', '1:09', '1:12', '1:15',
                '1:18', '1:21', '1:24', '1:27', '1:30', '1:33', '1:36', '1:39', '1:42', '1:45', '1:48',
                '1:51', '1:54', '1:57', '2:00', '2:03', '2:06', '2:09', '2:12', '2:15', '2:18', '2:21',
                '2:24', '2:27', '2:30', '2:33', '2:36', '2:39', '2:42', '2:45', '2:48']
minutes_list_big_step = ['0:00', '0:15', '0:30', '0:45', '1:00', '1:15', '1:30', '1:45', '2:00', '2:15',
                         '2:30', '2:45', '3:00', '3:15', '3:30', '3:45', '4:00', '4:15', '4:30', '4:45',
                         '5:00', '5:15', '5:30', '5:45', '6:00', '6:15', '6:30', '6:45', '7:00', '7:15',
                         '7:30', '7:45', '8:00', '8:15', '8:30', '8:45', '9:00', '9:15', '9:30', '9:45',
                         '10:00', '10:15', '10:30', '10:45', '11:00', '11:15', '11:30', '11:45', '12:00', '12:15',
                         '12:30', '12:45', '13:00', '13:15', '13:30', '13:45']
minutes_list_bigger_step = ['0:00', '0:25', '0:50', '1:15', '1:40', '2:05', '2:30', '2:55', '3:20', '3:45',
                            '4:10', '4:35', '5:00', '5:25', '5:50', '6:15', '6:40', '7:05', '7:30', '7:55',
                            '8:20', '8:45', '9:10', '9:35', '10:00', '10:25', '10:50', '11:15', '11:40', '12:05',
                            '12:30', '12:55', '13:20', '13:45']


plt.rcParams.update({"lines.color": "silver", "patch.edgecolor": "black", "text.color": "black", "axes.facecolor": "silver",
     "axes.edgecolor": "black", "axes.labelcolor": "black", "xtick.color": "black", "ytick.color": "black",
     "grid.color": "silver", "figure.facecolor": "dimgray", "figure.edgecolor": "dimgray", "axes.titlecolor": "black",
     "savefig.facecolor": "black", "savefig.edgecolor": "black"})

fig = plt.figure()
gs = fig.add_gridspec(3, 2)
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[1, 0])
total_sample_main_plot = fig.add_subplot(gs[2, 1])
one_anvil_main_plot = fig.add_subplot(gs[0, 1])
ax4t = fig.add_subplot(gs[2, 0])
ax4 = fig.add_subplot(gs[2, 0])
ax4t.axes.set_visible(False)
col_color = ['gray'] * 4
colors_list = [["silver"] * 4] * 4
mpl_table = ax1.table(cellText=table_dataframe.values,
                      colLabels=table_dataframe.columns, cellLoc='center', rowLoc='center', loc='upper right',
                      cellColours=colors_list, colColours=col_color)
mpl_table.auto_set_font_size(False)
ax1.axis(False)
mpl_table.set_fontsize(9)

mpl_table2 = ax2.table(cellText=table_dataframe2.values,
                       colLabels=table_dataframe2.columns, cellLoc='center', rowLoc='center', loc='upper right',
                       cellColours=colors_list[0:3], colColours=col_color)
mpl_table2.auto_set_font_size(False)
mpl_table2.set_fontsize(9)
ax2.axis(False)


n = pd.Series(np.random.randn(trials))
iqr = float(np.quantile(n, .75)) - float(np.quantile(n, .25))
bin_width = (2 * iqr) / ((len(n)) ** (1. / 3.))
bin_number = int(np.ceil((np.max(n) - np.min(n)) / bin_width))
m = pd.Series(np.random.randn(len(tick_times_one_anvil)))
iqr_second = float(np.quantile(m, .75)) - float(np.quantile(m, .25))
bin_width_second = (2 * iqr_second) / ((len(m)) ** (1. / 3.))
bin_number_second = int(np.ceil((m.max() - m.min()) / bin_width_second))


cumulative_total_graph = sns.kdeplot(tick_times_df, x='tick_times', cumulative=True, common_norm=False,
                                     common_grid=True, legend=True, color='crimson')
empirical_total_graph = sns.ecdfplot(tick_times_df, x='tick_times', legend=True, color='green')
data_x, data_y = cumulative_total_graph.lines[0].get_data()
yi = .99
xi = np.interp(yi, data_y, data_x)
cumulative_total_graph.set(xticks=(np.arange(0, 1400, step=25)), xlim=(0, xi), yticks=(np.arange(0, 1.1, step=.1)),
                           ylim=(0, 1), ylabel='Probability of Completing Tekton', xlabel='Time of Encounter in Ticks',
                           title='Cumulative Probability of Completing Tekton')
cumulative_total_graph.set_xticklabels(cumulative_total_graph.get_xticklabels(), rotation=45)
aux_axis_cumulative = cumulative_total_graph.twiny()
sns.kdeplot(ax=aux_axis_cumulative, bins=80)
cumulative_total_graph.legend(labels=('Theoretical', 'Empirical'), labelcolor='black')
aux_axis_cumulative.set(xticks=(np.arange(0, 840, step=25)), xlim=(0, (xi * .6)), xlabel='Time of Encounter in Seconds')
aux_axis_cumulative.set_xticklabels(minutes_list_bigger_step, rotation=45)
cumulative_total_graph.grid('visible', color='black')


# total histogram graph
with sns.axes_style(style='ticks', rc={'ytick.left': True}):
    sns.histplot(tick_times, bins=bin_number, ax=total_sample_main_plot, color='orange', alpha=1, edgecolor='k', linewidth=1)

total_sample_main_plot_aux_axis = total_sample_main_plot.twinx()

sns.kdeplot(tick_times,  ax=total_sample_main_plot_aux_axis, color='crimson')

total_sample_main_plot_xticks = (np.arange(75, (np.max(tick_times) + 25), step=25))
total_sample_main_plot.xaxis.set_tick_params(rotation=45)
total_sample_main_plot_aux_axis.set(ylabel='Probability Density')
total_sample_main_plot.set(ylabel='Number of Tektons in Sample')
total_sample_main_plot_aux_xaxis = total_sample_main_plot.secondary_xaxis('top')
total_sample_main_plot_aux_xaxis.xaxis.set_tick_params(rotation=45)
total_sample_main_plot_aux_xaxis.set(xticks=(np.arange(75, (np.max(tick_times)), step=25)), xlim=(75, (np.max(tick_times))))
total_sample_main_plot_aux_xaxis_labels = np.arange(75, (np.max(tick_times)), step=25)
total_sample_main_plot_aux_xaxis.set_xticklabels(minutes_list_big_step[3:(len(total_sample_main_plot_aux_xaxis_labels) + 3)])
total_sample_main_plot.set(title=f'Tekton Density Histogram of {p.number_to_words(trials).title()} Trials',
                           xticks=total_sample_main_plot_xticks, xlim=(75, (np.max(tick_times))))
total_sample_main_plot.locator_params(nbins=22, axis='y')
total_sample_main_plot_aux_axis.locator_params(nbins=22, axis='y')
total_sample_main_plot.set_xlabel('Time of Encounter in Ticks')
total_sample_main_plot_aux_xaxis.set_xlabel('Time of Encounter in Minutes and Seconds')
total_sample_main_plot.grid(True, color='black')
total_sample_main_plot.set_axisbelow(True)
# total_sample_main_plot.set_facecolor((0.0, 0.0, 0.0, 0.0))

# under one anvil graph
with sns.axes_style(style='ticks', rc={'ytick.left': True}):
    sns.histplot(tick_times_one_anvil, bins=bin_number_second, ax=one_anvil_main_plot, palette=['orange'], alpha=1, legend=False, edgecolor='k', linewidth=1)

one_anvil_main_plot_aux_axis = one_anvil_main_plot.twinx()
sns.kdeplot(tick_times_one_anvil, palette=['r'],  ax=one_anvil_main_plot_aux_axis, legend=False)

one_anvil_main_plot.xaxis.set_tick_params(rotation=45)
one_anvil_main_plot_aux_axis.set(ylabel='Probability Density')
one_anvil_main_plot.set(ylabel='Number of Tektons in Sample')
one_anvil_main_plot_aux_xaxis = one_anvil_main_plot.secondary_xaxis('top')
one_anvil_main_plot_aux_xaxis.xaxis.set_tick_params(rotation=45)

one_anvil_main_plot_xticks = (np.arange(75, 165, step=5))
one_anvil_main_plot.set(xticks=one_anvil_main_plot_xticks, xlim=(75, 160),
                        title=f'Number of Tektons Within One Anvil in {p.number_to_words(trials).title()} Trials')
one_anvil_main_plot.locator_params(nbins=22, axis='y')
one_anvil_main_plot.set_xlabel('Time of Encounter in Ticks')
one_anvil_main_plot_aux_xaxis.set_xlabel('Time of Encounter in Minutes and Seconds')
one_anvil_main_plot_aux_axis.locator_params(nbins=22, axis='y')
one_anvil_main_plot.xaxis.set_tick_params(rotation=45)


one_anvil_main_plot_aux_xaxis.set(xticks=(np.arange(75, 165, step=5)), xlim=(75, 160))
one_anvil_main_plot_aux_xaxis.set_xticklabels(minutes_list[:18])
one_anvil_main_plot_aux_xaxis.xaxis.set_tick_params(rotation=45)
one_anvil_main_plot.grid(True, color='black')
one_anvil_main_plot.set_axisbelow(True)


plt.subplots_adjust(wspace=.25, hspace=0, right=.93, left=0.05, top=.90, bottom=.07)
print('script completed in', datetime.now() - (start_time - initialization_time), 'seconds')
# one_anvil_main_plot.set_facecolor((0.0, 0.0, 0.0, 0.0))

plt.show()

# to do list
# leave some comments on the code
# optimize calculation code

# can probably just tack this one onto post anvil adjustment
# def min_regen():
# honestly cba its fine

#update numbers for veng

#dear god the graphs
#idk man graphs are f nothing wanted to go into functions seaborn is painful
#did my best

# this is probably a horrible idea that ill regret but could possibly store the booleanvars from buttons into a list would be a lot cleaner
# ok yeah that was a pretty bad idea

# this whole block is kinda a nightmare thanks to fang but uh idk at least the function within the function was clever in a kinda suspic way
# def attack_roll(spec_attack, four_tick, five_tick, multiplier):

# is also bloated but tried before with little success
# def hit_value_roll(spec_bonus, four_tick, five_tick, max_hit_modifier=1.0):


#find likelihood of one anvil based on hp value using ML library

#maybe add short lure option
