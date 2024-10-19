import re

pattern = "was"
text = '''Madagascar was unexpectedly hit by Cyclone Gamane as it veered into the island country’s northern district of Vohemar during the early hours of Wednesday, resulting in at least 11 deaths.

The storm was expected to skim the coast, but it changed course and went into the island causing disruption to 7,000 people with hundreds of homes destroyed. The slow-moving nature of the storm exacerbated its impact, with persistent rainfall and prolonged strong winds causing devastation to infrastructure and significant flooding. The cyclone moved across the island with an average wind speed of 93mph (150km/h) while gusts of up to 130mph were recorded, making it a category 1 storm on the Saffir-Simpson scale. Cyclone Gamane has since weakened to a tropical storm and is expected to clear the island on Friday.

In the same week, significant flash floods and a landslide in Indonesia left at least 19 people dead with seven others missing. Mud, rocks and uprooted trees crashed down a mountainside on the island of Sumatra, engulfing villages in the western Pesisier Selatan district late last Friday after torrential rains. Rescue operations were disrupted by power cuts as more than 80,000 people fled to temporary government shelters.'''

match = re.search (pattern , text )
print(match)