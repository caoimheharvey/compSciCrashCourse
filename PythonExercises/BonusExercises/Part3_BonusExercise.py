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

# ds1 = open('C:\\Users\\darks\\Documents\\git\\compSciCrashCourse\\PythonExercises\\files\\dino_race_dataset1.csv', 'r')
# read_ds1 = ds1.read()
# print(read_ds1)
# ds1.close()
#
# ds2 = open('C:\\Users\\darks\\Documents\\git\\compSciCrashCourse\\PythonExercises\\files\\dino_race_dataset2.csv', 'r')
# read_ds2 = ds2.read()
# print(read_ds2)
# ds2.close()

dictdino = {}

with open('C:\\Users\\darks\\Documents\\git\\compSciCrashCourse\\PythonExercises\\files\\dino_race_dataset1.csv', 'r') as file:
    counter = 0
    for line in file:
        NAME, LEG_LENGTH, DIET = line.split(',')
        DIET = DIET.replace('\n', '')
        if counter != 0:
            dictdino[NAME] = {'leg_length': float(LEG_LENGTH), 'diet': DIET}
        counter += 1

# can also be
# with open('..\\files\\csvfile') as file
with open('C:\\Users\\darks\\Documents\\git\\compSciCrashCourse\\PythonExercises\\files\\dino_race_dataset2.csv', 'r') as file:
    counter = 0
    for line in file:
        NAME, STRIDE_LENGTH, STANCE = line.split(',')
        STANCE = STANCE.replace('\n', '')
        if counter != 0:
            dictdino[NAME].update({'stride_length': float(STRIDE_LENGTH), 'stance': STANCE})
        counter += 1

print(dictdino)

for dino in dictdino:
    if 'stride_length' in dictdino[dino] and 'leg_length' in dictdino[dino]:
        SPEED = ((dictdino[dino]['stride_length'] / dictdino[dino]['leg_length']) - 1)\
                * (dictdino[dino]['leg_length'] * 9.8) ** 0.5
        dictdino[dino].update({'speed': SPEED})


print(dictdino)