# This is a test

import random
import numpy as np


def reselect():
    x = 0
    base = 136.3 * 0.5774
    mge = 1
    rge = 2
    t = 0
    u = 0
    c = 0
    z = 0
    r_prob_hit_new = 1 - (pow(base, z) / 100)
    l_prob_hit_new = (pow(base, z) / 100)
    choice_initial = np.array([1, 2])
    print('test')
    while c == 0:
        initial_result = np.random.choice(choice_initial, p=[0.50, 0.50])
        print(initial_result)
        if initial_result.any() < 2:
            t += 1
            c += 1
            z += 1
            print('magetest')
        elif initial_result > 1:
            u += 1
            c += 1
            z += 1
            print('rangetest')

        for z in range(1, 30):
            if u > 0:
                post_result = np.random.choice(choice_initial, p=[l_prob_hit_new, r_prob_hit_new])
                print(post_result)
                print('success')
                u += 1
                z = u
                x += 1
            elif t > 0:
                post_result = np.random.choice(choice_initial, p=[r_prob_hit_new, l_prob_hit_new])
                print(post_result)
                print('success2')
                t += 1
                z = t
                x += 1


reselect()
