def getTiers():
    tiers = [
        'gold', 'silver', 'bronze', 'copper'
    ]

    return tiers

def getDefensePositions():
    positions = {
        'DT': 3,
        'DE': 3,
        'OLB': 2,
        'ILB': 2,
        'CB': 4,
        'SS': 1,
        'FS': 1,
    }

    return positions

def getOffensePositions():
    positions = {
        'WR': 4,
        'TE': 3,
        'T': 2,
        'G': 2,
        'C': 1,
        'QB': 1,
        'FB': 1,
        'HB': 2,
        'K': 1,
        'P': 1
    }

    return positions

def getPoints():
    points = {
        'total_points': 872,
        'gold': 350,
        'silver': 252,
        'bronze': 174,
        'copper': 218
    }

    return points

def playerCost():
    costs = {
        'gold': 60,
        'silver': 24,
        'bronze': 12,
        'copper': 12
    }

    return costs

def attributeOneCost():
    costs = {
        'gold': 11,
        'gold_restricted': 36,
        'silver': 5,
        'silver_restricted': 25,
        'bronze': 3,
        'bronze_restricted': 13,
        'copper': 3,
        'copper_restricted': 10
    }

    return costs

def attributeTwoCost():
    costs = {
        'gold': 12,
        'gold_restricted': 37,
        'silver': 6,
        'silver_restricted': 26,
        'bronze': 4,
        'bronze_restricted': 14,
        'copper': 4,
        'copper_restricted': 11
    }

    return costs

def attributeThreeCost():
    costs = {
        'gold': 13,
        'gold_restricted': 38,
        'silver': 7,
        'silver_restricted': 27,
        'bronze': 5,
        'bronze_restricted': 15,
        'copper': 5,
        'copper_restricted': 12
    }

    return costs

def attributeFourCost():
    costs = {
        'gold': 14,
        'gold_restricted': 39,
        'silver': 8,
        'silver_restricted': 28,
        'bronze': 6,
        'bronze_restricted': 16,
        'copper': 6,
        'copper_restricted': 13
    }

    return costs

def totalAttributeCost():
    costs = {
        1: attributeOneCost(),
        2: attributeTwoCost(),
        3: attributeThreeCost(),
        4: attributeFourCost()
    }

    return costs

def athleticAttributes():
    abilities = {
        'Quick Feet': 0,
        'Speed Burner': 0,
        'Break Away Burst': 0,
        'Cutback Ability': 0,
        'Durability Bonus': 0,
        'Hops': 0,
        'Stamina Bonus': 0,
        'Strength Bonus': 0
    }

    return abilities

def generalIntangibles():
    abilities = {
        'Clutch': 0,
        'Leadership Bonus': 0
    }

    return abilities

def quarterBackAttributes():
    abilities = {
        '4th Quarter Comeback': 0,
        'Deception': 0,
        'Laser Arm': 0,
        'Mobile QB (84 Speed)': 0,
        'Play Fake': 0,
        'Pocket Presence': 0,
        'QB Evade': 0,        
        'Scrambler': 0,
        'Tough as Nails': 0
    }

    return abilities

def quarterBackRestrictedAttributes():
    abilities = {
        'Quick Release': 0,
        'Rocket Arm': 0
    }

    return abilities

def runningBackAttributes():
    abilities = {
        'Ankle Breaker': 0,
        'Arm of Steel': 0,
        'Battering Ram': 0,                
        'Cyclone': 0,
        'Finesse': 0,
        'Finesse and Power': 0,
        'Goalline Dive': 0,
        'Power': 0,        
        'Scissor Kick': 0,
        'Secure Ball Bonus': 0,        
        'Stop on a Dime': 0,
    }

    return abilities

def runningBackRestrictedAttributes():
    abilities = {
        'Branching Tackles': 0,
        'Work Horse': 0
    }

def catchingAttributes():
    abilities = {
        'Acrobatic Catches': 0,
        'Bump Buster': 0,
        'Deep Threat': 0,
        'Magic Feet': 0,
        'Mr. 3rd Down': 0,
        'Possession Receiver': 0,
        'Soft Hands': 0,
        'Tough in the Middle': 0
    }

    return abilities

def catchingRestrictedAttributes():
    abilities = {
        'Route God': 0
    }

    return abilities

def blockingAttributes():
    abilities = {
        'Brick Wall': 0,
        'Bulldozer': 0,
        'Stonewall': 0
    }

    return abilities

def passRushAttributes():
    abilities = {
        'Bull Rush': 0,
        'Club': 0,
       ' Pass Rush Bonus': 0,
        'Rip': 0,
        'Sack Master': 0,
        'Spin': 0,
        'Swim': 0
    }

    return abilities

def runDefenseAttributes():
    abilities = {
        'Reach Tackle': 0,
        'Run Coverage': 0,
        'Run Reader': 0,
        'Ball Strip': 0,
        'Loose Ball Magnet': 0
    }

    return abilities

def passCoverageAttributes():
    abilities = {
        'Ball Hawk': 0,
        'Bump Master': 0,
        'Coverage Bonus': 0,
        'Footsteps': 0
    }

    return abilities

def generalDefenseAttributes():
    abilities = {
        'Big Hit': 0,
        'Closing Speed': 0,
        'High Helmet Tackle': 0,
        'Wrap up Tackler': 0
    }

    return abilities

def specialTeamsAttributes():
    abilities = {
        'Coffin Corner': 0,
        'Kick Accuracy Bonus': 0,
        'Kick Power Bonus': 0,
        'Return Specialist': 0,
        'Special Team Demon': 0
    }

    return abilities

def allAbilities():
    abilities = {
        'qb': quarterBackAttributes(),
        'qb_restricted': quarterBackRestrictedAttributes(),
        'running': runningBackAttributes(),
        'running_restricted': runningBackRestrictedAttributes(),
        'catching': catchingAttributes(),
        'catching_restricted': catchingRestrictedAttributes(),
        'blocking': blockingAttributes(),
        'pass_rush': passRushAttributes(),
        'run_defense': runDefenseAttributes(),
        'pass_coverage': passCoverageAttributes(),
        'general_defense': generalDefenseAttributes(),
        'special_teams': specialTeamsAttributes(),
        'athletic': athleticAttributes()
    }
    
    return abilities
