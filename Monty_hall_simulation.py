import random


TRIALS = int(input("How many trials should be run for not switching? "))
TRIALS2 = int(input("How many trials should be run for switching? "))


def find_host_choice(player_choice, doors):
    if doors == [1, 0, 0]:
        if player_choice == 0:
            return random.randint(1, 2)
        elif player_choice == 1:
            return 2
        else:
            return 1
    if doors == [0, 1, 0]:
        if player_choice == 0:
            return 2
        elif player_choice == 1:
            return random.randint(0, 1) * 2
        else:
            return 0
    if doors == [0, 0, 1]:
        if player_choice == 0:
            return 1
        elif player_choice == 1:
            return 0
        else:
            return random.randint(0, 1)


def make_doors():
    rand = random.randint(0, 2)
    if rand == 0:
        doors = [1, 0, 0]
    elif rand == 1:
        doors = [0, 1, 0]
    else:
        doors = [0, 0, 1]
    return doors


def switch_choice(choice, host_choice):
    arr = [0, 0, 0]
    arr[choice] = 1
    arr[host_choice] = 1

    for i in range(len(arr)):
        if arr[i] == 0:
            return i


# run simulation without changing doors
num_wins_no_change = 0
for no_change_trials in range(TRIALS):
    doors = make_doors()
    choice = random.randint(0, len(doors) - 1)

    if doors[choice] == 1:
        num_wins_no_change += 1

no_change_win_rate = num_wins_no_change / no_change_trials
print("Win rate without switching: " + str(no_change_win_rate))

# run simulation with changing doors
num_wins_with_change = 0
for with_change_trials in range(TRIALS2):
    doors = make_doors()
    choice = random.randint(0, len(doors) - 1)
    host_choice = find_host_choice(choice, doors)

    if doors[switch_choice(choice, host_choice)] == 1:
        num_wins_with_change += 1

with_change_win_rate = num_wins_with_change / with_change_trials
print("Win rate when you switch: " + str(with_change_win_rate))

print("Sum of rates: " + str(with_change_win_rate + no_change_win_rate))