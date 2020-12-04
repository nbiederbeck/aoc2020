"""Friday, 4 Dec"""
from puzzles import get_puzzle

puzzle = get_puzzle(4)


def test():
    example = [
        "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
        "byr:1937 iyr:2017 cid:147 hgt:183cm",
        "",
        "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
        "hcl:#cfa07d byr:1929",
        "",
        "hcl:#ae17e1 iyr:2013",
        "eyr:2024",
        "ecl:brn pid:760753108 byr:1931",
        "hgt:179cm",
        "",
        "hcl:#cfa07d eyr:2025 pid:166559648",
        "iyr:2011 ecl:brn hgt:59in",
    ]

    assert one(example) == 2

    # --- part two ---
    invalid_examples = [
        "eyr:1972 cid:100",
        "hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926",
        "",
        "iyr:2019",
        "hcl:#602927 eyr:1967 hgt:170cm",
        "ecl:grn pid:012533040 byr:1946",
        "",
        "hcl:dab227 iyr:2012",
        "ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277",
        "",
        "hgt:59cm ecl:zzz",
        "eyr:2038 hcl:74454a iyr:2023",
        "pid:3556412378 byr:2007",
    ]
    for passport in list_to_passports(invalid_examples):
        assert not is_valid(passport)

    valid_examples = [
        "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980",
        "hcl:#623a2f",
        "",
        "eyr:2029 ecl:blu cid:129 byr:1989",
        "iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm",
        "",
        "hcl:#888785",
        "hgt:164cm byr:2001 iyr:2015 cid:88",
        "pid:545766238 ecl:hzl",
        "eyr:2022",
        "",
        "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719",
    ]
    for passport in list_to_passports(valid_examples):
        assert is_valid(passport), to_dict(passport)


def list_to_passports(puzzle: list) -> list:
    passports = []

    p = ""
    for line in puzzle:
        if line != "":
            p += line + " "
        else:
            passports.append(p)
            p = ""

    return passports


def has_required_fields(passport: str) -> bool:
    fields = [
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
    ]
    passport = to_dict(passport)
    for key in fields:
        if key not in passport:
            return False

    return True


def to_dict(passport: str) -> dict:
    passdict = dict()
    for keyvalue in passport.split():
        key, value = keyvalue.split(':')
        passdict[key] = value

    return passdict


def is_valid(passport: str) -> bool:
    if not has_required_fields(passport):
        return False

    passdict = to_dict(passport)

    try:
        byr = int(passdict['byr'])
        if byr < 1920 or byr > 2002:
            return False
    except ValueError:
        return False

    try:
        iyr = int(passdict['iyr'])
        if iyr < 2010 or iyr > 2020:
            return False
    except ValueError:
        return False

    try:
        eyr = int(passdict['eyr'])
        if eyr < 2020 or eyr > 2030:
            return False
    except ValueError:
        return False

    hgt = passdict['hgt']
    try:
        h = int(hgt[:-2])
    except ValueError:
        return False
    u = hgt[-2:]
    if u == 'cm':
        if h < 150 or h > 193:
            return False
    elif u == 'in':
        if h < 59 or h > 76:
            return False
    else:
        return False

    hcl = passdict['hcl']
    if hcl[0] != "#":
        return False
    for char in hcl[1:]:
        if char not in "0123456789abcdef":
            return False

    ecl = passdict['ecl']
    if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False

    pid = passdict['pid']
    if len(pid) != 9:
        return False
    for c in pid:
        try:
            int(c)
        except ValueError:
            return False

    return True


def one(puzzle: list) -> int:
    passports = list_to_passports(puzzle)

    valid = 0
    for p in passports:
        if has_required_fields(p):
            valid += 1

    return valid


def two(puzzle: list) -> int:
    passports = list_to_passports(puzzle)

    valid = 0
    for p in passports:
        if is_valid(p):
            valid += 1

    return valid


if __name__ == "__main__":
    test()
    print(one(puzzle))
    print(two(puzzle))
