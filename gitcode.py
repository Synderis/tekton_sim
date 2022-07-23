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
    r_prob_hit_new = 1 - pow(base, auto_count)
    l_prob_hit_new = pow(base, auto_count)
    choice_initial = np.array([1, 2])
    while initial_qualifier == 0:
        initial_result = np.random.choice(choice_initial, 2, p=[0.50, 0.50])
        print(initial_result)
        if initial_result.any < 2:
            mage_count += 1
            initial_qualifier += 1
            auto_count += 1
            print('magetest')
        elif initial_result > 1:
            range_count += 1
            initial_qualifier += 1
            auto_count += 1
            print('rangetest')
        else:
            continue
##think there probably needs to be another function here
        for x in range(1, 30):
            if range_count > 0:
                post_result = np.random.choice(choice_initial, 2, p=[l_prob_hit_new, r_prob_hit_new])
                print(post_result)
                range_count += 1
                auto_count = range_count
                x += 1

            elif mage_count > 0:
                post_result = np.random.choice(choice_initial, 2, p=[l_prob_hit_new, r_prob_hit_new])
                print(post_result)
                mage_count += 1
                auto_count = mage_count
                x += 1
reselect()
