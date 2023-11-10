import csv

header = ['destination', 'pose_x', 'pose_y', 'pose_z']
data = [
    ['Professor_1', 11, 12, 13],
    ['professor_2', 21, 22, 23],
    ['professor_3', 31, 32, 33]
]

with open('data/test.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)
