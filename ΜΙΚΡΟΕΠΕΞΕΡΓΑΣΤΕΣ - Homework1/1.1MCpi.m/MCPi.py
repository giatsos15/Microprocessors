# Georgios Giatsos, A.M. 3202

import random

N = 10000
circle_counter = 0
square_counter = 0
pi = 0
a = 1 # h pleura tou tetragwnou


for i in range(N):
    # pairnw tuxaies metablhtes mesa apo to tetragwno
    x = random.uniform(-a, a) 
    y = random.uniform(-a, a)
    # upologizw thn apostash apo to kentro kai an einai mikroterh tou 1 tote exoume shmeio tou kuklou
    distance = (x**2 + y**2)
    if distance <= 1:
        circle_counter=circle_counter+1
    square_counter=square_counter+1
    # to pi isoutai me to logo twn shmeiwn tou kuklou dia ta a shmeia tou tetragwno epi 4
pi = 4 *(circle_counter/square_counter)
print ("Approximate value for pi: ", pi)
print("N = " , N)

