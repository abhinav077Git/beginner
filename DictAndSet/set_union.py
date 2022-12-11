from prescription_data import adverse_interactions

meds_to_watch = set()

# for interaction in adverse_interactions:
#     meds_to_watch = meds_to_watch.union(interaction)
#     # meds_to_watch = meds_to_watch | interaction
#     # meds_to_watch.update(interaction) # update the set without the need to create new set everytime
#     meds_to_watch |= interaction

meds_to_watch.update(*adverse_interactions)  # unpack list and provide all as argument as update to list
print(sorted(meds_to_watch))
print(*sorted(meds_to_watch), sep="\n")

# farm_animals = {"sheep", "hen", "cow", "horse", "goat"}
# wild_animals = {"lion", "elephant", "tiger", "goat", "panther", "horse"}
#
# all_animals_1 = farm_animals.union(wild_animals)
# print(all_animals_1)
#
# all_animals_2 = wild_animals.union(farm_animals)
# print(all_animals_2)
#
# all_animals_3 = wild_animals | farm_animals
# print(all_animals_3)

