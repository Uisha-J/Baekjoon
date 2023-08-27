n, start_money, salary, num_golden_keys = map(int, input().split())
golden_key_cards = []
owned_lands = [False] * (4 * n - 4)

for _ in range(num_golden_keys):
    card_info = input().split()
    card_type = int(card_info[0])
    value = int(card_info[1])
    golden_key_cards.append((card_type, value))

land_prices = []
for i in range(4 * n - 4):
    if i == 0:
        land_prices.append(('start', 0))
        owned_lands[i] = True
    elif i == n - 1:
        land_prices.append(('jail', 0))
        owned_lands[i] = True
    elif i == 2 * n - 2:
        land_prices.append(('tax', 0))
        owned_lands[i] = True
    elif i == 3 * n - 3:
        land_prices.append(('trip', 0))
        owned_lands[i] = True
    else:
        line = input().split()
        if line[0] == 'G':
            land_prices.append('G')
            owned_lands[i] = True
        else:
            land_prices.append(('L', int(line[1])))

num_rolls = int(input())
dice_rolls = []

for i in range(num_rolls):
    dice_rolls.append(tuple(map(int, input().split())))

player_money = start_money
current_position = 0
in_jail = False
on_space = False
golden_key_index = 0
collected_tax = 0


for roll in dice_rolls:
    if in_jail:
        if roll[0] == roll[1]:
            in_jail = False
            continue
        else:
            jail_counter += 1
            if jail_counter == 3:
                in_jail = False
                continue

    elif on_space:
        current_position = (0)
        player_money += salary
        on_space = False
        move = roll[0] + roll[1]
        current_position = (current_position + move) % (4 * n - 4)
    else:
        move = roll[0] + roll[1]
        current_position = (current_position + move) % (4 * n - 4)

    if current_position == 0 or current_position + move >= (4 * n - 4):
        player_money += salary

    land_type = land_prices[current_position][0]
    if land_type == 'L':
        price = land_prices[current_position][1]
        if not owned_lands[current_position] and player_money >= price:
            player_money -= price
            owned_lands[current_position] = True

    if land_prices[current_position][0] == 'G':
        card_type, value = golden_key_cards[golden_key_index]
        golden_key_index = (golden_key_index + 1) % num_golden_keys

        if card_type == 1:
            player_money += value
        elif card_type == 2:
            player_money -= value
            if player_money < 0:
                print('LOSE')
                exit()
        elif card_type == 3:
            player_money -= value
            collected_tax += value
            if player_money < 0:
                print('LOSE')
                exit()
        elif card_type == 4:
            current_position = (current_position + value) % (4 * n - 4)
            if current_position == 0 or current_position + value >= (4 * n - 4):
                player_money += salary
            land_type, price = land_prices[current_position][0], land_prices[current_position][1]
            if land_type == 'L':
                if not owned_lands[current_position] and player_money >= price:
                    player_money -= price
                    owned_lands[current_position] = True
            if land_type == 'trip':
                on_space = True
            if land_type == 'tax':
                player_money += collected_tax
                collected_tax = 0
            if land_type == 'jail':
                in_jail = True
                jail_counter = 0

print(player_money, current_position)

if player_money < 0:
    print('LOSE')
    exit()

if False in owned_lands:
    print('LOSE')
    exit()

print('WIN')
