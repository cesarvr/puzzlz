def load_from_db():
    inventory = {}
    game_db = open('./game_db.txt').read()
    game_db = game_db.split('\n')
    current_gear = ''

    for line in game_db:
        print('line: ', line)
        if ':' in line or not line:
            if 'Weapons:' in line:
                current_gear = 'weapon'
            if 'Armor:' in line:
                current_gear = 'armor'
            if 'Rings:' in line:
                current_gear = 'rings'
            continue

        if '+' in line:
            record = line.split(' ')
            record[0] = record[0] + record.pop(1)
        else:
            record = line.split(' ')
        record = list(filter(lambda n: n, record))

        record[1] = int(record[1])
        record[2] = int(record[2])
        record[3] = int(record[3])
        if current_gear not in inventory:
            inventory[current_gear] = []

        inventory[current_gear].append(record)

    return inventory


def simulate(hero, monster):
    monster_health = monster[0]
    monster_attack_power = monster[1]
    monster_defense = monster[2]

    hero_health = hero[0]
    hero_attack_power = hero[1]
    hero_defense = hero[2]

    turn = 0
    while True:
        if monster_health <= 0:
            return True

        if hero_health <= 0:
            return False

        if turn == 0 and hero_attack_power > 0:
            attack_power = hero_attack_power - monster_defense
            attack_power = attack_power if attack_power > 0 else 1
            monster_health = monster_health - attack_power

            print(f'Hero attack!! with {attack_power} power')
            print(f'Monster health {monster_health}')

        if turn == 1:
            attack_power = monster_attack_power - hero_defense
            attack_power = attack_power if attack_power > 0 else 1

            hero_health = hero_health - attack_power

            print(f'Monster attack!! with {attack_power} power')
            print(f'Hero health {hero_health}')

        if turn == 1:
            turn = 0
        else:
            turn += 1


def compute_hero_stats_and_costs(hero, weapon=['', 0, 0, 0], armor=['', 0, 0, 0], ring=['', 0, 0, 0]):
    cost = weapon[1] + armor[1] + ring[1]
    new_hero = [hero[0],0,0]
    new_hero[1] = new_hero[1] + (weapon[2] + ring[2])
    new_hero[2] = new_hero[2] + (armor[3] + ring[3])
    return cost, new_hero


def run_simulation_part_two(best_cost, hero, monster, weapon=['No Weapon', 0, 0, 0], armor=['No Armor', 0, 0, 0], ring=['Ringless', 0, 0, 0]):
    cost, hero_stats = compute_hero_stats_and_costs(hero, weapon, armor, ring)

    if cost >= 282 and not simulate(hero_stats, monster):
            print('bug!')

    victory = simulate(hero_stats, monster)

    if not victory:
        # print(f'monster is victorious: cost: {cost} -> hero stats: {hero}, monster stats: {monster}')
        return max(best_cost, cost)
    else:
        return best_cost


def run_simulation_solver_1(best_cost, hero, monster, weapon=['', 0, 0, 0], armor=['', 0, 0, 0], ring=['', 0, 0, 0]):
    cost, hero_stats = compute_hero_stats_and_costs(hero, weapon, armor, ring)
    victory = simulate(hero_stats, monster)

    if victory:
        print(f'victory!!: cost: {cost} -> hero stats: {hero}, monster stats: {monster}')
        return min(best_cost, cost)
    else:
        return best_cost


def solve_1(_inventory, _hero, _monster, current_cost=100000, run_sim=run_simulation_solver_1):
    rings = _inventory['rings']

    for weapon in _inventory['weapon']:
        current_cost = run_sim(current_cost, _hero.copy(), _monster.copy(), weapon)

        for armor in _inventory['armor']:
            current_cost = run_sim(current_cost, _hero.copy(), _monster.copy(), armor=armor)
            current_cost = run_sim(current_cost, _hero.copy(), _monster.copy(), weapon=weapon)
            current_cost = run_sim(current_cost, _hero.copy(), _monster.copy(), weapon=weapon, armor=armor)

            for r1 in range(len(rings)):
                ring1 = rings[r1]

                current_cost = run_sim(current_cost, _hero.copy(), _monster.copy(), weapon=weapon, ring=ring1)
                current_cost = run_sim(current_cost, _hero.copy(), _monster.copy(), weapon=weapon, armor=armor,
                                       ring=ring1)

                for r2 in range(r1 + 1, len(rings)):
                    ring2 = rings[r2]
                    ring_new = ['', 0, 0, 0]
                    ring_new[0] = ring1[0] + " and " + ring2[0]
                    ring_new[1] = ring1[1] + ring2[1]
                    ring_new[2] = ring1[2] + ring2[2]
                    ring_new[3] = ring1[3] + ring2[3]

                    print(f"permutation rings: {ring_new[0]}")


                    current_cost = run_sim(current_cost, _hero.copy(), _monster.copy(), weapon=weapon, ring=ring_new)
                    current_cost = run_sim(current_cost, _hero.copy(), _monster.copy(), weapon=weapon, armor=armor,
                                           ring=ring_new)

    return current_cost


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    hero = [8, 5, 5]
    monster = [12, 7, 2]

    hero_p = [100, 0, 0]
    monster_p = [103, 9, 2]

    inventory = load_from_db()
    solution_1 = solve_1(inventory, hero_p, monster_p)

    solution_2 = solve_1(inventory, hero_p, monster_p, current_cost=-1, run_sim=run_simulation_part_two)

    print('inventory: ', inventory)
    print('total cost solution 1: ', solution_1)
    print('total cost solution 2: ', solution_2)
