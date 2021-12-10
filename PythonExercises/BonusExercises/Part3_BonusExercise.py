"""
Bonus exercise for extra practice:
Source - Facebook Interview Question

 # You will be supplied with two data files in CSV format.
 # The first file contains statistics about various dinosaurs.
        Located at: files/dino_race_dataset1.csv
 # The second file contains additional data.
        Located at: files/dino_race_dataset2.csv
 #
 # Given the following formula,
 #
 # speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
 # Where g = 9.8 m/s^2 (gravitational constant)

 # The SQRT can be calculated by using   **0.5

 # Write a program to read in the data files from disk, it must then print the names
 # of only the bipedal dinosaurs from fastest to slowest. Do not print any other information.
"""

g = 9.8

dinosaurs = {}
dataset1 = open("dino_race_dataset1.csv")
dataset2 = open("dino_race_dataset2.csv")

for line in dataset2:
    name, stride, stance = line.split(",")
    if "bipedal" in stance:
        dinosaurs[name] = float(stride)

for line in dataset1:
    name, leg, diet = line.split(",")
    if name in dinosaurs.keys():
        stride = dinosaurs[name]
        dinosaurs[name] = ((stride / float(leg) - 1) * (float(leg) * g) ** 0.5)

# sorted key param?
# https://stackoverflow.com/questions/8966538/syntax-behind-sortedkey-lambda
dinosaurs = dict(sorted(dinosaurs.items(), key=lambda item: item[1], reverse=True))
for k in dinosaurs: print(k)
