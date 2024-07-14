''' Given a set of men’s and women’s preference list. 
Design and implement Gale-Shapley algorithm to determine 
the stable set of marriages among them. Comment on the time complexity of the same.
Assumptions: Men propose first according to their preference list. 
Women can choose a better partner based on the preference.
Men’s preference list
A: V W X
B: W V X
C: V W X
Women’s preference list
V: A B C
W: B C A
X: C A B
'''
def stable_marriage(n, men_pref, women_pref):
    free_men = list(range(n))
    woman_partner = [-1] * n
    proposals = [0] * n

    while free_men:
        m = free_men[0]  # Take the first free man
        w = men_pref[m][proposals[m]]  # The woman m is proposing to
        proposals[m] += 1

        if woman_partner[w] == -1:  # If the woman is free
            woman_partner[w] = m  # Engage them
            free_men.pop(0)
        else:  # If the woman is already engaged
            m_current = woman_partner[w]
            # Check if she prefers this new man over her current partner
            if women_pref[w].index(m) < women_pref[w].index(m_current):
                woman_partner[w] = m  # Engage her with the new man
                free_men.pop(0)
                free_men.append(m_current)  # The previous partner becomes free

    # Convert to pairs (man, woman)
    return [(woman_partner[w], w) for w in range(n)]

def get_preferences(identifiers, entities, is_man=True):
    preferences = []
    for i in identifiers:
        pref = input(f"Enter the preference list for {'man' if is_man else 'woman'} {i}: ").split()
        preferences.append([entities.index(p) for p in pref])
    return preferences

# Number of men and women
n = int(input("Enter the number of men/women: "))

# Input man and woman identifiers
men = input("Enter the identifiers for men (e.g., A B C): ").split()
women = input("Enter the identifiers for women (e.g., V W X): ").split()

print("Enter the men's preference lists:")
men_pref = get_preferences(men, women, is_man=True)
print("Enter the women's preference lists:")
women_pref = get_preferences(women, men, is_man=False)

pairs = stable_marriage(n, men_pref, women_pref)
for m, w in pairs:
    print(f"Man {men[m]} is engaged to Woman {women[w]}")
