import math
import random
import tkinter as tk
import inflect
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import scipy


trials = 10000
root = tk.Tk()
root.title('Tekton Sim Version 1.0')
root.geometry('500x200')

check_var1 = tk.BooleanVar()
check_var2 = tk.BooleanVar()
check_var3 = tk.BooleanVar()
check_var4 = tk.BooleanVar()
check_var5 = tk.BooleanVar()
check_var6 = tk.BooleanVar()
check_var7 = tk.BooleanVar()
check_var8 = tk.BooleanVar()
check_var9 = tk.BooleanVar()


def abort():
    return exit(0)


def trials_selection(amount):
    global trials
    trials = amount
    return trials


def check_correction():
    if check_var5.get():
        if check_var6.get():
            return C6.toggle()
        else:
            return


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


trials_text = tk.Label(root, text="select number of trials")
trials_text.place(x=65, y=5)
trials_button1 = tk.Button(root, text="1000", command=trials_selection(1000))
trials_button1.place(x=60, y=25)
trials_button2 = tk.Button(root, text="10000", command=trials_selection(10000))
trials_button2.place(x=100, y=25)
trials_button3 = tk.Button(root, text="100000", command=trials_selection(100000))
trials_button3.place(x=145, y=25)
exit_button = tk.Button(root, text="Exit", command=abort)
exit_button.pack(pady=10, side=tk.TOP)
button_submit = tk.Button(root, text="Submit", command=root.destroy)
button_submit.pack(side=tk.BOTTOM)
C1 = tk.Checkbutton(root, text="five tick only", variable=check_var1, onvalue=1, offvalue=0)
C1.pack(side=tk.LEFT)
C2 = tk.Checkbutton(root, text="CM", variable=check_var2, onvalue=1, offvalue=0)
C2.pack(side=tk.LEFT)
C3 = tk.Checkbutton(root, text="inq", variable=check_var3, onvalue=1, offvalue=0)
C3.pack(side=tk.LEFT)
C4 = tk.Checkbutton(root, text="fang", variable=check_var4, onvalue=1, offvalue=0)
C4.pack(side=tk.LEFT)
C4.pack()
C5 = tk.Checkbutton(root, text="b ring", variable=check_var5, onvalue=1, offvalue=0, command=check_correction)
C5.pack(side=tk.LEFT)
C5.pack()
C6 = tk.Checkbutton(root, text="brim", variable=check_var6, onvalue=1, offvalue=0, command=check_correction2)
C6.pack(side=tk.LEFT)
C6.pack()
C7 = tk.Checkbutton(root, text="feros", variable=check_var7, onvalue=1, offvalue=0)
C7.pack(side=tk.LEFT)
C7.pack()
C8 = tk.Checkbutton(root, text="tort", variable=check_var8, onvalue=1, offvalue=0)
C8.pack(side=tk.LEFT)
C8.pack()
C9 = tk.Checkbutton(root, text="lightbearer", variable=check_var9, onvalue=1, offvalue=0, command=spec_ring)
C9.pack(side=tk.LEFT)
C9.pack()

root.mainloop()

result_array = ["hit", "miss"]
global max_def_roll
inq = check_var3.get()
cm = check_var2.get()
fang = check_var4.get()
five_only = check_var1.get()
if fang:
    scythe = False
else:
    scythe = True
print('inq:', inq)
print('cm:', cm)
print('fang:', fang)
print('five tick only:', five_only)
print('b ring:', check_var5.get())
print('brim ring:', check_var6.get())
print('tort:', check_var8.get())
print('feros:', check_var7.get())
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
no_h_one_a = 0
one_h_one_a = 0
two_h_one_a = 0
one_hammer = 0
two_hammer = 0
anvils = [0] * 100
times = []
tick_times = []
tick_times_one_anvil = []
no_hammer_total = 0
one_hammer_total = 0
two_hammer_total = 0
lightbearer_equipped = False
crush = 'crush'
slash = 'slash'
stab = 'stab'


class Test:
    def __init__(self, four_tick_hit_counter, five_tick_hit_counter, time_parameter, phase, idle_time, fang_spec_status, specced_last_anvil):
        self.four_tick_hit_counter = four_tick_hit_counter
        self.five_tick_hit_counter = five_tick_hit_counter
        self.time_parameter = time_parameter
        self.phase = phase
        self.idle_time = idle_time
        self.fang_spec_status = fang_spec_status
        self.specced_last_anvil = specced_last_anvil


class Weapon:
    def __init__(self, style_used):
        self.style_used = style_used


static_crush_weapon = Weapon(style_used=crush)
if fang:
    five_tick_weapon = Weapon(style_used=stab)
else:
    if inq:
        five_tick_weapon = Weapon(style_used=crush)
    else:
        five_tick_weapon = Weapon(style_used=slash)


class Gear:
    def __init__(self, dwh_att_bonus, dwh_str_bonus, four_tick_att_bonus, four_tick_str_bonus, fang_att_bonus,
                 fang_str_bonus, scy_att_bonus, scy_str_bonus, gear_multiplier, lightbearer):
        self.lightbearer = lightbearer
        self.dwh_att_bonus = dwh_att_bonus
        self.dwh_str_bonus = dwh_str_bonus
        self.four_tick_att_bonus = four_tick_att_bonus
        self.four_tick_str_bonus = four_tick_str_bonus
        self.fang_att_bonus = fang_att_bonus
        self.fang_str_bonus = fang_str_bonus
        self.scy_att_bonus = scy_att_bonus
        self.scy_str_bonus = scy_str_bonus
        self.gear_multiplier = gear_multiplier


if lightbearer_equipped:
    pass
else:
    pass


def gear_selection():
    if check_var5.get():
        loadout_adjuster(0, 8)
        return loadout
    elif check_var6.get():
        loadout_adjuster(4, 4)
        return loadout
    else:
        loadout_adjuster(0, 0)
        return loadout


def gear_selection_two():
    if check_var8.get():
        loadout_adjuster(5, 2)
        return loadout
    else:
        loadout_adjuster(0, 0)
        return loadout


def gear_selection_three():
    if check_var7.get():
        loadout_adjuster(4, 2)
        return loadout
    else:
        loadout_adjuster(0, 0)
        return loadout


def loadout_adjuster(att_modifier, str_modifier):
    loadout.dwh_str_bonus += str_modifier
    loadout.four_tick_str_bonus += str_modifier
    loadout.fang_str_bonus += str_modifier
    loadout.scy_str_bonus += str_modifier
    loadout.dwh_att_bonus += att_modifier
    loadout.four_tick_att_bonus += att_modifier
    loadout.fang_att_bonus += att_modifier
    loadout.scy_att_bonus += att_modifier
    return


if inq:
    loadout = Gear(dwh_att_bonus=183, dwh_str_bonus=136, four_tick_att_bonus=183, four_tick_str_bonus=140,
                   fang_att_bonus=155, fang_str_bonus=154, scy_att_bonus=90, scy_str_bonus=118, gear_multiplier=1.025,
                   lightbearer=.85)
    gear_selection()
    gear_selection_two()
    gear_selection_three()
    print('loadout bonuses selected: ', loadout.dwh_att_bonus, loadout.dwh_str_bonus, loadout.four_tick_att_bonus,
          loadout.four_tick_str_bonus, loadout.fang_att_bonus, loadout.fang_str_bonus, loadout.scy_att_bonus,
          loadout.scy_str_bonus, loadout.gear_multiplier, loadout.lightbearer)
    print('----------')
else:
    loadout = Gear(dwh_att_bonus=151, dwh_str_bonus=144, four_tick_att_bonus=151, four_tick_str_bonus=148,
                   fang_att_bonus=163, fang_str_bonus=162, scy_att_bonus=138, scy_str_bonus=126, gear_multiplier=1,
                   lightbearer=.85)
    gear_selection()
    gear_selection_two()
    gear_selection_three()
    print('loadout bonuses selected: ', loadout.dwh_att_bonus, loadout.dwh_str_bonus, loadout.four_tick_att_bonus,
          loadout.four_tick_str_bonus, loadout.fang_att_bonus, loadout.fang_str_bonus, loadout.scy_att_bonus,
          loadout.scy_str_bonus, loadout.gear_multiplier, loadout.lightbearer)
    print('----------')


class NPC:
    def __init__(self, hp, defence, stab_def, slash_def, crush_def, max_veng, alive_status=True, anvil_checked=False):
        self.hp = hp
        self.defence = defence
        self.stab_def = stab_def
        self.slash_def = slash_def
        self.crush_def = crush_def
        self.max_veng = max_veng
        self.alive_status = alive_status
        self.anvil_checked = anvil_checked

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


def defence_roll():
    first_roll = math.ceil(random.randint(0, max_def_roll))
    return first_roll


def hit_chancer(spec, four_tick, five_tick, fang_spec_hit):
    attack_roll_check = 0
    def_roll_check = defence_roll()
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
    vuln = np.random.choice(result_array, 1, replace=True, p=[.62, (1 - .62)])
    if vuln:
        tekton.lower_def(int(tekton.defence * .10))
        adjust_def_integer()
    else:
        tekton.lower_def(0)
    return


def tek_check():
    global one_hammer, two_hammer, no_h_one_a, one_h_one_a, two_h_one_a
    if not tekton.alive_status:
        if not tekton.anvil_checked:
            if hit_metrics.phase == 0:
                anvils[0] += 1
                tekton.anvil_checked = True
            elif hit_metrics.phase == 1:
                anvils[1] += 1
                tekton.anvil_checked = True
                if one_hammer == 1:
                    one_h_one_a += 1
                elif two_hammer == 1:
                    two_h_one_a += 1
                else:
                    no_h_one_a += 1
            else:
                anvils[hit_metrics.phase] += 1
                tekton.anvil_checked = True
            return
        else:
            return
    else:
        return


def spec_hit(instances, status):
    for _ in range(instances):
        global one_hammer, two_hammer, no_hammer_total, one_hammer_total, two_hammer_total
        npc_style_checker(True, False)
        enraged_check(status)
        if hit_chancer(True, False, False, False):
            damage_val = hit_value_roll(spec_bonus=True, four_tick=False, five_tick=False)
            tekton.lower_hp(damage_val)
            if damage_val > 0:
                tekton.lower_def(int((tekton.defence * .3)))
                adjust_def_integer()
                if one_hammer == 0:
                    one_hammer += 1
                    one_hammer_total += 1
                elif one_hammer == 1:
                    one_hammer = 0
                    two_hammer += 1
                    one_hammer_total -= 1
                    two_hammer_total += 1
            else:
                tekton.lower_def(int((tekton.defence * .05)))
                adjust_def_integer()
                if one_hammer == 0:
                    if two_hammer == 0:
                        no_hammer_total += 1
                elif one_hammer == 1:
                    one_hammer_total += 1
        else:
            tekton.lower_hp(0)
            tekton.lower_def(int((tekton.defence * .05)))
            adjust_def_integer()
            if one_hammer == 0:
                if two_hammer == 0:
                    no_hammer_total += 1
            elif one_hammer == 1:
                one_hammer_total += 1
    return


def four_tick_hit(instances, status):
    for _ in range(instances):
        if tekton.hp > 0:
            hit_metrics.four_tick_hit_counter += 1
        else:
            hit_metrics.four_tick_hit_counter += 0
        enraged_check(status)
        npc_style_checker(True, False)
        if hit_chancer(False, True, False, False):
            damage_val = hit_value_roll(spec_bonus=False, four_tick=True, five_tick=False)
            tekton.lower_hp(damage_val)
        else:
            damage_val = 0
            tekton.lower_hp(damage_val)
        tek_check()


def fang_spec(instances, status):
    for _ in range(instances):
        enraged_check(status)
        if fang:
            npc_style_checker(False, True)
            if hit_chancer(False, False, True, True):
                damage_val = hit_value_roll(spec_bonus=False, four_tick=False, five_tick=True, max_hit_modifier=1)
                tekton.lower_hp(damage_val)
            else:
                tekton.lower_hp(0)


def scy_dmg(step_down):
    if hit_chancer(False, False, True, False):
        damage_val = hit_value_roll(False, four_tick=False, five_tick=True, max_hit_modifier=step_down)
        tekton.lower_hp(damage_val)
    else:
        damage_val = 0
        tekton.lower_hp(damage_val)
    return damage_val


def five_tick_hit(instances, status):
    for _ in range(instances):
        enraged_check(status)
        npc_style_checker(False, True)
        if tekton.hp > 0:
            hit_metrics.five_tick_hit_counter += 1
        else:
            hit_metrics.five_tick_hit_counter += 0
        if fang:
            if hit_chancer(False, False, True, False):
                damage_val = hit_value_roll(spec_bonus=False, four_tick=False, five_tick=True, max_hit_modifier=.85)
                tekton.lower_hp(damage_val)
            else:
                damage_val = 0
                tekton.lower_hp(damage_val)
        elif scythe:
            scy_dmg(1)
            scy_dmg(.5)
            scy_dmg(.25)
        else:
            if hit_chancer(False, False, True, False):
                damage_val = hit_value_roll(False, four_tick=False, five_tick=True)
                tekton.lower_hp(damage_val)
            else:
                damage_val = 0
                tekton.lower_hp(damage_val)
        tek_check()


def anvil_adjustment(veng):
    if tekton.hp > 0:
        cycle_select = random.randint(3, 6)
        hit_metrics.idle_time += ((cycle_select * 3) + 10)
        if tekton.hp < base_hp:
            tekton.hp += (cycle_select * hp_regen_per_cycle)
        if tekton.defence < base_def:
            tekton.defence += (cycle_select * def_regen_per_cycle)
        if veng:
            tekton.lower_hp(random.randint(1, tekton.max_veng))
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
        five_tick_hit(1, False)
        four_tick_hit(1, False)
        five_tick_hit(2, False)
    else:
        spec_hit(2, False)
        five_tick_hit(6, False)
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
                fang_spec(1, False)
                four_tick_hit(6, False)
                hit_metrics.specced_last_anvil = True
                can_i_spec()
            else:
                five_tick_hit(1, False)
                four_tick_hit(6, False)
                hit_metrics.specced_last_anvil = False
                can_i_spec()
        else:
            four_tick_hit(6, False)
            five_tick_hit(1, False)
        four_tick_hit(2, False)
        five_tick_hit(1, False)
    else:
        five_tick_hit(4, True)
        if fang_lb_spec:
            if spec_alternation:
                fang_spec(1, False)
                five_tick_hit(7, False)
                hit_metrics.specced_last_anvil = True
                can_i_spec()
            else:
                five_tick_hit(8, False)
                hit_metrics.specced_last_anvil = False
                can_i_spec()
        else:
            five_tick_hit(8, False)
    return


def enraged_check(enraged):
    if enraged:
        tekton.stab_def = 280
        tekton.slash_def = 280
        tekton.crush_def = 180
    else:
        tekton.stab_def = 155
        tekton.slash_def = 165
        tekton.crush_def = 105
    return tekton.stab_def, tekton.slash_def, tekton.crush_def


def npc_style_checker(spec_or_four_tick, five_tick):
    global max_def_roll
    max_def_roll = 0
    test_weapon = ""
    if spec_or_four_tick:
        test_weapon = static_crush_weapon.style_used
    elif five_tick:
        test_weapon = five_tick_weapon.style_used
    if test_weapon == crush:
        max_def_roll = math.ceil((tekton.defence + 9) * (tekton.crush_def + 64))
    elif test_weapon == stab:
        max_def_roll = math.ceil((tekton.defence + 9) * (tekton.stab_def + 64))
    elif test_weapon == slash:
        max_def_roll = math.ceil((tekton.defence + 9) * (tekton.slash_def + 64))
    return max_def_roll


for x in range(trials):
    hit_metrics = Test(0, 0, time_parameter=0.0, phase='', idle_time=0, fang_spec_status=True, specced_last_anvil=False)
    if cm:
        tekton = NPC(450, 246, 155, 165, 105, 65, alive_status=True, anvil_checked=False)
        base_hp = 450
        base_def = 246
    else:
        tekton = NPC(300, 205, 155, 165, 105, 44, alive_status=True, anvil_checked=False)
        base_hp = 300
        base_def = 205
    def_regen_per_cycle = int((base_def * .05) + 1)
    hp_regen_per_cycle = int((base_hp * .01) + 1)

    if four_and_five:
        hit_metrics.phase = 0
        hit_metrics.four_tick_hit_counter = 0
        hit_metrics.five_tick_hit_counter = 0
        vuln_check()
        pre_anvil()
        anvil_adjustment(True)
        min_regen()
        post_anvil(fang_lb_spec=lightbearer_equipped, spec_alternation=hit_metrics.fang_spec_status)
        anvil_adjustment(False)
        min_regen()
        one_hammer = 0
        two_hammer = 0
        while True:
            if tekton.hp > 0:
                post_anvil(fang_lb_spec=lightbearer_equipped, spec_alternation=hit_metrics.fang_spec_status)
                anvil_adjustment(False)
                min_regen()
                continue
            else:
                time()
                break

    elif five_only:
        hit_metrics.phase = 0
        hit_metrics.four_tick_hit_counter = 0
        hit_metrics.five_tick_hit_counter = 0
        vuln_check()
        pre_anvil()
        anvil_adjustment(True)
        min_regen()
        post_anvil(fang_lb_spec=lightbearer_equipped, spec_alternation=hit_metrics.fang_spec_status)
        anvil_adjustment(False)
        one_hammer = 0
        two_hammer = 0
        while True:
            if tekton.hp > 0:
                post_anvil(fang_lb_spec=lightbearer_equipped, spec_alternation=hit_metrics.fang_spec_status)
                anvil_adjustment(False)
                min_regen()
                continue
            else:
                time()
                break

p = inflect.engine()

tick_times_raw = tick_times
hist, bin_edges = np.histogram(tick_times, density=True)
cum_cdf = np.cumsum(hist * np.diff(bin_edges))
hist2, bin_edges2 = np.histogram(tick_times_raw, density=True)
cum_cdf_raw = np.cumsum(hist2 * np.diff(bin_edges2))
sub_115 = []
sub_100 = []
sub_115[:] = [x for x in times if x <= 125]
sub_100[:] = [x for x in times if x <= 100]

no_anvil_num = str(anvils[0]) + ', ' + str(round(((anvils[0] / trials) * 100), 2)) + '%'
one_anvil_num = str(anvils[1]) + ', ' + str(round(((anvils[1] / trials) * 100), 2)) + '%'
two_anvil_num = str(anvils[2]) + ', ' + str(round(((anvils[2] / trials) * 100), 2)) + '%'
three_anvil_num = str(anvils[3]) + ', ' + str(round(((anvils[3] / trials) * 100), 2)) + '%'
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
                                 'reset chance': ['N/A', one_ham_rate, two_ham_rate]})
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

plt.subplot(3, 2, 1)
font_size = 10
mpl_table = plt.table(cellText=table_dataframe.values, rowLabels=table_dataframe.index,
                      colLabels=table_dataframe.columns, cellLoc='center', rowLoc='center', loc='upper right')
mpl_table.auto_set_font_size(False)
mpl_table.set_fontsize(font_size)
sns.despine(bottom=True, left=True)
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)
plt.subplots_adjust(wspace=.2)
plt.subplots_adjust(hspace=0)

plt.subplot(3, 2, 3)
font_size = 10
mpl_table2 = plt.table(cellText=table_dataframe2.values, rowLabels=table_dataframe2.index,
                       colLabels=table_dataframe2.columns, cellLoc='center', rowLoc='center', loc='upper right')
mpl_table2.auto_set_font_size(False)
mpl_table2.set_fontsize(font_size)
sns.despine(bottom=True, left=True)
plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)
plt.subplots_adjust(wspace=.2)
plt.subplots_adjust(hspace=0)
plt.gcf().set_size_inches(18, 10)

plt.subplot(3, 2, 2)
fourth_graph = sns.kdeplot(cum_cdf_raw, x=tick_times_raw, cumulative=True, common_norm=False, common_grid=True,
                           legend=True)
fourth_empirical_graph = sns.ecdfplot(cum_cdf_raw, x=tick_times_raw, legend=True)
data_x, data_y = fourth_graph.lines[0].get_data()
data_x2, data_y2 = fourth_empirical_graph.lines[0].get_data()
yi = .99  # coordinate where to find th
xi = np.interp(yi, data_y, data_x)
yi2 = .99
xi2 = np.interp(yi2, data_y2, data_x2)
fourth_graph.set_title('cumulative probability of killing tekton')
fourth_graph.set(xticks=(np.arange(0, 1400, step=25)), xlim=(0, xi))
fourth_graph.set_xticklabels(fourth_graph.get_xticklabels(), rotation=45)
fourth_graph.set(xlabel='time of encounter in ticks')
aux_axis_fourth = fourth_graph.twiny()
sns.kdeplot(ax=aux_axis_fourth, bins=80)
fourth_graph.legend(labels=('theoretical', 'empirical'))
fourth_graph.set(ylabel='probability of killing tekton')
fourth_graph.set(yticks=(np.arange(0, 1.1, step=.1)), ylim=(0, 1))
aux_axis_fourth.set(xticks=(np.arange(0, 840, step=25)), xlim=(0, (xi * .6)),
                    xlabel='time of encounter in minutes and seconds')
aux_axis_fourth.set_xticklabels(minutes_list_bigger_step, rotation=45)
fourth_graph.grid('visible')
tick_times_one_anvil[:] = [x for x in tick_times if x <= 150]
np.mean(tick_times)

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
if trials == 1000:
    tick_mod = 100
elif trials == 10000:
    tick_mod = 200
else:
    tick_mod = 400

xd = []
for each in np.arange(45, 170, step=5):
    xd.append(str(each))
step_increment = int(trials / tick_mod)
plt.subplot(3, 2, 5)
first_graph = sns.histplot(tick_times, kde=True, bins=bin_number, color='darkblue', legend=False)
ymax_array1, bin_edges1 = np.histogram(tick_times, bins=bin_number, density=False)
y_max1 = np.max(ymax_array1)
remainder1 = divmod(y_max1, step_increment)
adjusted_ymax1 = remainder1[0] + 1
first_graph.set(yticks=(np.arange(0, (adjusted_ymax1 * (2 * step_increment)), step=step_increment)),
                ylim=(0, (adjusted_ymax1 * step_increment)))
first_graph.set(ylabel='number of killed tektons in sample')
first_graph.set_title('tekton density histogram of ' + str(trials) + ' trials')
plt.xlabel('time of encounter in ticks')
first_graph_xticks = (np.arange(75, 620, step=25))
first_graph.set(xticks=first_graph_xticks, xlim=(75, 600))
first_graph.set_xticklabels(first_graph_xticks, rotation=45)
second_axis = first_graph.twiny()
sns.histplot(ax=second_axis, bins=80)
second_axis_xticks = (np.arange(45, 400, step=15))
second_axis.set(xticks=second_axis_xticks, xlim=(45, 360), xlabel='time of encounter in minutes and seconds')
second_axis.set_xticklabels(minutes_list_big_step[3:27], rotation=45)
first_graph.grid('visible')
if trials == 100000:
    step_increment_second = trials / 1000
else:
    step_increment_second = trials / 500
plt.subplot(3, 2, 6)

second_graph = sns.histplot(tick_times_one_anvil, kde=True, bins=bin_number_second, color='darkblue')
ymax_array, bin_edges = np.histogram(tick_times_one_anvil, bins=bin_number_second, density=False)
y_max = np.max(ymax_array)
remainder = divmod(y_max, step_increment_second)
adjusted_ymax = remainder[0] + 1
second_graph.set(yticks=(np.arange(0, (adjusted_ymax * (2 * step_increment_second)), step=step_increment_second)), ylim=(0, (adjusted_ymax * step_increment_second)))
second_graph.set(ylabel='number of one anvils')
second_graph_xticks = (np.arange(45, 170, step=5))
second_graph.set(xticks=second_graph_xticks, xlim=(75, 160), xlabel='time of encounter in ticks')
second_graph.set_xticklabels(second_graph_xticks, rotation=45)
second_graph.set_title('number of tektons under one anvil in ' + str(trials) + ' trials')
aux_axis = second_graph.twiny()
sns.histplot(ax=aux_axis, bins=80)
aux_axis.set(xticks=(np.arange(45, 100, step=3)), xlim=(45, 96), xlabel='time of encounter in minutes and seconds')
aux_axis.set_xticklabels(minutes_list[0:19], rotation=45)
second_graph.legend(labels=('kde', (str((anvils[1] + anvils[0])) + ' total one anvils + no anvils')))
second_graph.grid('visible')
plt.subplots_adjust(wspace=.2)
plt.subplots_adjust(hspace=0)
plt.gcf().set_size_inches(18, 13)
plt.show()

# to do list
# either user input trials or buttons like 1k, 10k, 100k, 1m
# checkbox redundancy
# cfg saved defaults?
# optimize backend code
# make sure fang spec function works properly
# maybe fix table box margin
# maybe set default margins in a dataframe
# adaptive step function based on
