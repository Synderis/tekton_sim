import random
import numpy as np
##hgj
def reselect():

    x = 0
    base = 136.3 * 0.5774
    mge = "mage"
    rge = "range"
    mage_count = 0
    range_count = 0
    initial_qualifier = 0
    auto_count = 0
    r_prob_hit_new = 100 - pow(base, auto_count)
    l_prob_hit_new = pow(base, auto_count)
    choice_initial = ['mge', 'rge']
    while initial_qualifier == 0:
        initial_result = np.random.choice(choice_initial, 2, p=[0.50, 0.50])
        print(initial_result)
        if initial_result == mge:
            mage_count += 1
            initial_qualifier += 1
            auto_count += 1
            print('magetest')
        elif initial_result == rge:
            range_count += 1
            initial_qualifier += 1
            auto_count += 1
            print('rangetest')
        else:
            continue
##think there probably needs to be another function here
        for z in range(1, 30):
            if range_count > 0:
                post_result = np.random.choice(choice_initial, 2, p=[l_prob_hit_new, r_prob_hit_new])
                print(post_result)
                range_count += 1
                z = range_count

            elif mage_count > 0:
                post_result = np.random.choice(choice_initial, 2, p=[l_prob_hit_new, r_prob_hit_new])
                print(post_result)
                mage_count += 1
                z = mage_count
