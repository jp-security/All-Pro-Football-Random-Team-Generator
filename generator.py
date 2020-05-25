# Python Imports
import collections
import random

# Internal Imports
from configuration import (
    getPoints, getDefensePositions, getOffensePositions, playerCost,
    totalAttributeCost, getTiers, allAbilities, abilityCount
)


class TeamBuilder:
    def __init__(self):
        self.Player = collections.namedtuple(
            'Player', [
                'tier', 'side', 'position', 'attribute_one',
                'attribute_two', 'attribute_three', 'attribute_four',
                'player_cost'
            ]
        )
        self.team = []
        self.points = getPoints()
        self.player_cost = playerCost()
        self.ability_costs = totalAttributeCost()
        self.tiers = getTiers()
        self.offense_positions = getOffensePositions()
        self.defense_positions = getDefensePositions()
        self.player_attributes = allAbilities()
        self.ability_count = abilityCount()

    def _tierSetup(self):
        number_of_gold_players = random.randint(2, 5)
        max_silver = 8

        if number_of_gold_players == 4:
            max_silver = 7

        if number_of_gold_players == 5:
            max_silver = 6

        number_of_silver_players = random.randint(3, max_silver)
        number_of_bronze_players = 11 - number_of_gold_players - number_of_silver_players
        number_of_copper_players = 9

        self.points['total_points'] -= (
            (self.player_cost['gold'] * number_of_gold_players)
            + (self.player_cost['silver'] * number_of_silver_players)
            + (self.player_cost['bronze'] * number_of_bronze_players)
            + (self.player_cost['copper'] * number_of_copper_players)
        )

        self.points['gold'] -= (self.player_cost['gold'] * number_of_gold_players)
        self.points['silver'] -= (self.player_cost['silver'] * number_of_silver_players)
        self.points['bronze'] -= (self.player_cost['bronze'] * number_of_bronze_players)
        self.points['copper'] -= (self.player_cost['copper'] * number_of_copper_players)

        players_at_each_tier = {
            'gold': number_of_gold_players,
            'silver': number_of_silver_players,
            'bronze': number_of_bronze_players,
            'copper': number_of_copper_players
        }

        return players_at_each_tier

    def _positionValidation(self, side, positions):
        validated = True

        if side == 'offense':
            search_dict = self.offense_positions

        if side == 'defense':
            search_dict = self.defense_positions

        for position in positions:            
            if search_dict[position] == 0:
                validated = False
                return validated

        for position in positions:
            search_dict[position] -= 1

        return validated
        
    def _abilityValidation(self, tier, abilities):
        validated = True

        if len(abilities) == 1:
            cost = self.ability_costs[1][tier]

        if len(abilities) == 2:
            cost = self.ability_costs[1][tier] + self.ability_costs[2][tier]

        if len(abilities) == 3:
            cost = self.ability_costs[1][tier] + self.ability_costs[2][tier] + self.ability_costs[3][tier]

        if len(abilities) == 4:
            cost = self.ability_costs[1][tier] + self.ability_costs[2][tier] + self.ability_costs[3][tier] + self.ability_costs[4][tier]

        if not self.points['total_points'] - cost <= 0 and self.points[tier] - cost <= 0:
            validated = False
            return validated

        for ability in abilities:
            if self.ability_count[ability] > 3:
                validated = False
                return validated

        self.points['total_points'] -= cost
        self.points[tier] -= cost

        return validated

    def _playerCost(self, tier, abilities):
        if len(abilities) == 0:
            cost = 0

        if len(abilities) == 1:
            cost = self.ability_costs[1][tier]

        if len(abilities) == 2:
            cost = self.ability_costs[1][tier] + self.ability_costs[2][tier]

        if len(abilities) == 3:
            cost = self.ability_costs[1][tier] + self.ability_costs[2][tier] + self.ability_costs[3][tier]

        if len(abilities) == 4:
            cost = self.ability_costs[1][tier] + self.ability_costs[2][tier] + self.ability_costs[3][tier] + self.ability_costs[4][tier]

        cost += self.player_cost[tier]

        return cost

    def _playerBuilder(self, side, tier, position):
        validated = False

        while True:            
            number_of_attributes = random.randint(0, 4)

            if number_of_attributes == 0:
                validated = True
                abilities = []
                cost = self._playerCost(tier, abilities)

            if number_of_attributes > 0:
                abilities = random.sample(list(self.player_attributes[position]), number_of_attributes)
                validated = self._abilityValidation(tier, abilities)

                if validated:
                    cost = self._playerCost(tier, position)

            if validated:
                break

        if abilities == []:
            player = self.Player(tier, side, position, None, None, None, None, cost)

        if len(abilities) == 1:
            player = self.Player(tier, side, position, abilities[0], None, None, None, cost)

        if len(abilities) == 2:
            player = self.Player(tier, side, position, abilities[0], abilities[1], None, None, cost)

        if len(abilities) == 3:
            player = self.Player(tier, side, position, abilities[0], abilities[1], abilities[2], None, cost)

        if len(abilities) == 4:
            player = self.Player(tier, side, position, abilities[0], abilities[1], abilities[2], abilities[3], cost)

        self.team.append(player)

        return validated

    def buildTeam(self):
        players_at_tier = self._tierSetup()

        for tier in self.tiers:
            players = players_at_tier[tier]
            
            if players != 0:
                if players == 1:
                    offense = random.randint(1, players)
                
                if players != 1:
                    offense = random.randint(1, players - 1)

                defense = players - offense

                while True:
                    validated = False

                    offense_positions = random.sample(list(self.offense_positions), offense)
                    validated = self._positionValidation('offense', offense_positions)

                    if validated == True:
                        break
                
                while True:
                    validated = False

                    defense_positions = random.sample(list(self.defense_positions), defense)
                    validated = self._positionValidation('defense', defense_positions)

                    if validated == True:
                        break
                
                for position in offense_positions:
                    validated = False
                    while True:
                        validated = self._playerBuilder('offense', tier, position)

                        if validated:
                            break

                for position in defense_positions:
                    validated = False
                    while True:
                        validated = self._playerBuilder('defense', tier, position)

                        if validated:
                            break

        for player in self.team:
            print(f'{player}')

        print(f'{self.points}')
