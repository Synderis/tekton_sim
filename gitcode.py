#This is a test 

import random
import numpy as np
def reselect():

    x = 0
    base = 136.3 * 0.5774
    mge = "mage"
    rge = "range"
    t = 0
    u = 0
    c = 0
    z = 0
    r_prob_hit_new = 100 - pow(base, c)
    l_prob_hit_new = pow(base, c)
    choice_initial = ['mge', 'rge']
    while c == 0:
        initial_result = np.random.choice(choice_initial, 2, p=[0.50, 0.50])
        print(initial_result)
        if initial_result == mge:
            t += 1
            c += 1
            z += 1
            print('magetest')
        elif initial_result == rge:
            u += 1
            c += 1
            z += 1
            print('rangetest')
        else:
            continue

        for z in range(1, 30):
            if u > 0:
                post_result = np.random.choice(choice_initial, 2, p=[l_prob_hit_new, r_prob_hit_new])
                print(post_result)
                u += 1
                z = u

            elif t > 0:
                post_result = np.random.choice(choice_initial, 2, p=[l_prob_hit_new, r_prob_hit_new])
                print(post_result)
                t += 1
                z = t
