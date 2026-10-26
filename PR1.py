
# Simple Reflex Agent for Vacuum Cleaner World

def vacuum_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Right"
    else:
        return "Left"


# Environment
location = "A"
room = {"A": "Dirty", "B": "Dirty"}

# Run the agent
for i in range(5):
    print("Location:", location)
    print("Room status:", room)

    action = vacuum_agent(location, room[location])
    print("Action:", action)

    if action == "Suck":
        room[location] = "Clean"
    elif action == "Right":
        location = "B"
    elif action == "Left":
        location = "A"

    print("------------------")


# Simple Reflex Agent for the Vacuum Cleaner World

# def simple_reflex_agent(location, status):
#     if status == 'Dirty':
#         return 'Suck'
#     elif location == 'A':
#         return 'Right'
#     else:
#         return 'Left'


# def run_vacuum_world(location, world, steps=6):
#     performance = 0

#     for t in range(steps):
#         status = world[location]
#         action = simple_reflex_agent(location, status)

#         print(f"t={t} loc={location} status={status} action={action}")

#         if action == 'Suck':
#             world[location] = 'Clean'
#         elif action == 'Right':
#             location = 'B'
#         elif action == 'Left':
#             location = 'A'

#         # Count how many rooms are clean
#         performance += sum(state == 'Clean' for state in world.values())

#     return performance


# # Initial state of the world
# world = {
#     'A': 'Dirty',
#     'B': 'Dirty'
# }

# # Run the simulation
# total = run_vacuum_world('A', world)

# print("\nFinal World State:", world)
# print("Total Performance:", total)
