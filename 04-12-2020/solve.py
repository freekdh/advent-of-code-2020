from dataclasses import dataclass
import re


def get_input_data():
    with open("04-12-2020/input.txt") as input_file:
        return list(
            map(lambda s: s.replace("\n", " "), input_file.read().split(sep="\n\n"))
        )


class distance:
    def __init__(self, meters):
        self._meters = meters

    def __repr__(self):
        return f"{self._meters:.2f} meters"

    @classmethod
    def from_centimeters(cls, centimeters):
        return cls(meters=centimeters * 0.01)

    @classmethod
    def from_inches(cls, inches):
        return cls(meters=inches / 39.37)

    def get_centimeters(self):
        return self._meters * 100

    def get_inches(self):
        return self._meters * 39.37


@dataclass(frozen=True)
class Passport:
    birth_year: int = None
    issue_year: int = None
    expiration_year: int = None
    height: distance = None
    hair_color: str = None
    eye_color: str = None
    passport_id: int = None
    country_id: int = None

    def is_valid(self):
        return None not in (
            self.birth_year,
            self.issue_year,
            self.expiration_year,
            self.height,
            self.hair_color,
            self.eye_color,
            self.passport_id,
        )


def get_group(pattern, data, dtype):
    match = re.search(re.compile(pattern=pattern), data)
    if match:
        return dtype(match.groups()[0])
    else:
        return None


def get_groups(pattern, data):
    match = re.search(re.compile(pattern=pattern), data)
    if match:
        return match.groups()
    else:
        return None


def parse_data(passport_data):
    birth_year = get_group(pattern="byr:([^ ]+)", data=passport_data, dtype=int)
    issue_year = get_group(pattern="iyr:([^ ]+)", data=passport_data, dtype=int)
    expiration_year = get_group(pattern="eyr:([^ ]+)", data=passport_data, dtype=int)
    height = get_group(pattern="hgt:([^ ]+)", data=passport_data, dtype=str)
    hair_color = get_group(pattern="hcl:([^ ]+)", data=passport_data, dtype=str)
    eye_color = get_group(pattern="ecl:([^ ]+)", data=passport_data, dtype=str)
    passport_id = get_group(pattern="pid:([^ ]+)", data=passport_data, dtype=str)
    country_id = get_group(pattern="cid:([^ ]+)", data=passport_data, dtype=int)

    return {
        "birth_year": birth_year,
        "issue_year": issue_year,
        "expiration_year": expiration_year,
        "height": height,
        "hair_color": hair_color,
        "eye_color": eye_color,
        "passport_id": passport_id,
        "country_id": country_id,
    }


def main():
    input_data = get_input_data()

    passports = []
    for passport_data in input_data:
        passport_fields = parse_data(passport_data)
        passports.append(Passport(**passport_fields))

    valid_passports = sum(passport.is_valid() for passport in passports)

    print(
        f"Part1: there are {valid_passports} valid passports out of {len(passports)} passports"
    )


if __name__ == "__main__":
    main()