import itertools

conf = {
    "1": {
        "files": [
            ["1/input.txt", 365619, 236873508],
            ["okami/day_1/input.txt", 440979, 82498112],
            ["soup/2020_12_01_list", 786811, 199068980],
            ["Vess/input1.txt", 927684, 292093004]
        ],
        "tests": [
            ["Jacob", "1.1"],
            ["Okami", "okami.day_1"],
            ["CatAndDogSoup", "soup.2020_12_01_all"],
            ["Vess", "Vess.advent1"]
        ]
    },
    "2": {
        "files": [
            ["2/input.txt", 422, 451],
            ["okami/day_2/input.txt", 580, 611],
            ["soup/2020_12_02_list", 524, 485],
            ["Vess/input2.txt", 524, 485]
        ],
        "tests": [
            ["Jacob", "2.2"],
            ["CatAndDogSoup", "soup.2020_12_02_all"],
            ["Vess", "Vess.advent2"]
        ]
    },
    "3": {
        "files": [
            ["3/input.txt", 286, 3638606400],
            ["okami/day_3/input.txt", 280, 4355551200],
            ["soup/2020_12_03_list", 247, 2983070376],
            ["Vess/input3.txt", 200, 3737923200]
        ],
        "tests": [
            ["Jacob", "3.3"],
            ["CatAndDogSoup", "soup.2020_12_03_all"],
            ["Vess", "Vess.advent3"]
        ]
    },
    "4": {
        "files": [
            ["4/input.txt", 202, 137],
            ["okami/day_4/input.txt", 256, 198],
            ["Vess/input4.txt", 190, 121]
        ],
        "tests": [
            ["Jacob", "4.4"],
            ["Vess", "Vess.advent4"],
            ["CatAndDogSoup", "soup.2020_12_04_all"]
        ]
    },
    "5": {
        "files": [
            ["5/input.txt", 930, 515],
            ["okami/day_5/input.txt", 980, 607],
            ["Vess/input5.txt", 801, 597]
        ],
        "tests": [
            ["Jacob", "5.5"],
            ["Okami", "okami.day_5.main"],
            ["Vess", "Vess.advent5"]
        ]
    },
    "6": {
        "files": [
            ["6/input.txt", 6273, 3254],
            ["Vess/input6.txt", 6590, 3288],
            ["okami/day_6/input.txt", 6625, 3360]
        ],
        "tests": [
            ["Jacob", "6.6"],
            ["Vess", "Vess.advent6"],
            ["Okami", "okami.day_6.main"],
        ]
    },
    "7": {
        "files": [
            ["7/input.txt", 248, 57281],
            ["Vess/input7.txt", 211, 12414],
            ["okami/day_7/input.txt", 222, 13264]
        ],
        "tests": [
            ["Jacob", "7.7"],
            ["Vess", "Vess.advent7"],
            ["Okami", "okami.day_7.main"],
        ]
    },
    "8": {
        "files": [
            ["8/input.txt", 1766, 1639]
        ],
        "tests": [
            ["Jacob", "8.8"]
        ]
    },
    "9": {
        "files": [
            ["9/input.txt", 530627549, 77730285]
        ],
        "tests": [
            ["Jacob", "9.9"]
        ]
    },
    "10": {
        "files": [],
        "tests": []
    },
    "11": {
        "files": [],
        "tests": []
    },
    "12": {
        "files": [],
        "tests": []
    },
    "13": {
        "files": [],
        "tests": []
    },
    "14": {
        "files": [],
        "tests": []
    },
    "15": {
        "files": [],
        "tests": []
    },
    "16": {
        "files": [],
        "tests": []
    },
    "17": {
        "files": [],
        "tests": []
    },
    "18": {
        "files": [],
        "tests": []
    },
    "19": {
        "files": [],
        "tests": []
    },
    "20": {
        "files": [],
        "tests": []
    },
    "21": {
        "files": [],
        "tests": []
    },
    "22": {
        "files": [],
        "tests": []
    },
    "23": {
        "files": [],
        "tests": []
    },
    "24": {
        "files": [],
        "tests": []
    },
    "25": {
        "files": [],
        "tests": []
    }
}


def idfn(val):
    print(val)
    if isinstance(val, list):
        return val[0]
    if isinstance(val, str):
        return val



def pytest_generate_tests(metafunc):
    to_test = []
    for day in conf:
        for input in conf[day]["files"]:
            for solution in conf[day]["tests"]:
                to_test.append([day, input, solution])

    metafunc.parametrize(f"test_number, file_details, test_details", to_test, ids=idfn)

if __name__ == "__main__":
    for day in conf:
        print(list(itertools.product(conf[day]["files"], conf[day]["tests"])))
