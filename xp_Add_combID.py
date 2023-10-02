import pandas as pd

df = pd.read_csv("Finální data_komplet.csv", index_col=0)

df = df.iloc[:,1:-13]

for idx, column_name in enumerate(df.columns):
    print(f"Column Name: '{column_name}', Index: {idx}")



lower_bound = -10
upper_bound = 10


def pwr_neg(power):
    return power <= -0.051
def pwr_0(power):
    return -0.05 <= power <= 0.05

def pwr_1(power):
    return 0.450 <= power <= 0.550


def pwr_2(power):
    return 0.9 <= power <= 1.1


def pwr_3(power):
    return 1.7 <= power <= 1.9


def pwr_4(power):
    return 2.9 <= power <= 3.1


def pwr_5(power):
    return 4.7 <= power <= 5.3


def rot_0(rot):
    return -1 <= rot <= 1


def rot_300(rot):
    return 297 <= rot <= 303


def rot_vranov_100(rot):
    return 99 <= rot <= 101


def rot_vranov_0(rot):
    return rot <= 1


tolerance_ranges = [
    (350.0, 351.45, 0),
    (348.45, 350.1, 1),
    (347.45, 348.45, 2),
    (346.45, 347.45, 3),
    (345.45, 346.45, 4),
    (344.45, 345.45, 5),
    (343.45, 344.45, 6),
    (342.45, 343.45, 7),
    (341.45, 342.45, 8),
    (340.45, 341.45, 9),
    (339.45, 340.45, 10),
    (338.45, 339.45, 11),
    (337.45, 338.45, 12),
    (336.45, 337.45, 13),
    (335.45, 336.45, 14),
    (334.45, 335.45, 15),
    (333.45, 334.45, 16),
    (332.45, 333.45, 17),
    (331.45, 332.45, 18)
]


def WLevel(Kombinantion):
    value = float(Kombinantion)
    for tolerance_range in tolerance_ranges:
        lower_bound, upper_bound, id_value = tolerance_range
        if lower_bound <= value <= upper_bound:
            return id_value
    # Return None if no tolerance range matches the value
    return None

#
df['NS1'] = df['TG1 - PRŮTOK TURBÍNOU'].apply(lambda x: 0 if x < .5 else 1)
df['TG1_ROT_id'] = df['TG1 - OTÁČKY TURBÍNY'].apply(lambda x: 0 if rot_0(x) else (1 if rot_300(x) else 99))
df['TG1_PW_id'] = df['TG1 - ČINNÝ VÝKON'].apply(lambda x: 0 if pwr_neg(x) else (1 if pwr_0(x) else (2 if pwr_1(x) else (3 if pwr_2(x) else (4 if pwr_3(x) else (5 if pwr_4(x) else (6 if pwr_5(x) else 99)))))))

df['NS2'] = df['TG2 - PRŮTOK TURBÍNOU'].apply(lambda x: 0 if x < .5 else 1)
df['TG2_ROT_id'] = df['TG2 - OTÁČKY TURBÍNY'].apply(lambda x: 0 if rot_0(x) else (1 if rot_300(x) else 99))
df['TG2_PW_id'] = df['TG2 - ČINNÝ VÝKON'].apply(lambda x: 0 if pwr_neg(x) else (1 if pwr_0(x) else (2 if pwr_1(x) else (3 if pwr_2(x) else (4 if pwr_3(x) else (5 if pwr_4(x) else (6 if pwr_5(x) else 99)))))))

df['NS3'] = df['TG3 - PRŮTOK TURBÍNOU'].apply(lambda x: 0 if x < .5 else 1)
df['TG3_ROT_id'] = df['TG3 - OTÁČKY TURBÍNY'].apply(lambda x: 0 if rot_0(x) else (1 if rot_300(x) else 99))
df['TG3_PW_id'] = df['TG3 - ČINNÝ VÝKON'].apply(lambda x: 0 if pwr_neg(x) else (1 if pwr_0(x) else (2 if pwr_1(x) else (3 if pwr_2(x) else (4 if pwr_3(x) else (5 if pwr_4(x) else (6 if pwr_5(x) else 99)))))))

df['Vranov_ROT_id'] = df['VRANOV 2 - OTÁČKY TURBÍNY'].apply(lambda x: 0 if rot_vranov_0(x) else (1 if rot_vranov_100(x) else 99))
df['HH_id'] = df['VRANOV - HORNÍ HLADINA'].apply(lambda x: WLevel(x))

df.to_csv("Fulldata_NewCombID.csv")
