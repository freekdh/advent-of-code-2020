from dataclasses import dataclass
import re


def get_input_data(path_to_data):
    with open(path_to_data) as input_file:
        return list(
            map(lambda s: s.replace("\n", " "), input_file.read().split(sep="\n\n"))
        )


@dataclass(frozen=True)
class RawDataPassport:
    birth_year: str = None
    issue_year: str = None
    expiration_year: str = None
    height: str = None
    hair_color: str = None
    eye_color: str = None
    passport_id: str = None
    country_id: str = None

    def get_required_fields(self):
        return {
            key: value for key, value in self.__dict__.items() if key != "country_id"
        }

    def required_fields_are_present(self):
        return None not in self.get_required_fields().values()

    def required_fields_are_valid(self):
        return all(self.is_valid(key) for key in self.get_required_fields())

    def is_valid(self, key):
        if self.__dict__[key] is None:
            return False

        if key == "birth_year":
            return self._is_birth_year_valid()
        elif key == "issue_year":
            return self._is_issue_year_valid()
        elif key == "expiration_year":
            return self._is_expiration_year_valid()
        elif key == "height":
            return self._is_height_valid()
        elif key == "hair_color":
            return self._is_hair_color_valid()
        elif key == "eye_color":
            return self._is_eye_color_valid()
        elif key == "passport_id":
            return self._is_passport_id_valid()
        elif key == "country_id":
            return self._is_country_id_valid()
        else:
            raise Exception("can't find key: {key}")

    def _is_birth_year_valid(self):
        try:
            return 1920 <= int(self.birth_year) <= 2002
        except ValueError:
            return False

    def _is_issue_year_valid(self):
        try:
            return 2010 <= int(self.issue_year) <= 2020
        except ValueError:
            return False

    def _is_expiration_year_valid(self):
        try:
            return 2020 <= int(self.expiration_year) <= 2030
        except ValueError:
            return False

    def _is_height_valid(self):
        pattern = re.compile(pattern="(\d+)(in|cm)")
        match = re.match(pattern, self.height)
        if match:
            try:
                value, unit = match.groups()
                if unit == "cm":
                    return 150 <= int(value) <= 193
                else:
                    return 59 <= int(value) <= 76
            except ValueError:
                return False
        else:
            return False

    def _is_hair_color_valid(self):
        pattern = re.compile(pattern="#([0-9a-f]{6})")
        match = re.match(pattern, self.hair_color)
        return True if match else False

    def _is_eye_color_valid(self):
        return self.eye_color in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

    def _is_passport_id_valid(self):
        pattern = re.compile(pattern="(\d{9})")
        match = re.fullmatch(pattern, self.passport_id)
        return True if match else False


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
    birth_year = get_group(pattern="byr:([^ ]+)", data=passport_data, dtype=str)
    issue_year = get_group(pattern="iyr:([^ ]+)", data=passport_data, dtype=str)
    expiration_year = get_group(pattern="eyr:([^ ]+)", data=passport_data, dtype=str)
    height = get_group(pattern="hgt:([^ ]+)", data=passport_data, dtype=str)
    hair_color = get_group(pattern="hcl:([^ ]+)", data=passport_data, dtype=str)
    eye_color = get_group(pattern="ecl:([^ ]+)", data=passport_data, dtype=str)
    passport_id = get_group(pattern="pid:([^ ]+)", data=passport_data, dtype=str)
    country_id = get_group(pattern="cid:([^ ]+)", data=passport_data, dtype=str)

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


def get_passports(input_data):
    passports = []
    for passport_data in input_data:
        passport_fields = parse_data(passport_data)
        passports.append(RawDataPassport(**passport_fields))
    return passports


def main():
    input_data = get_input_data("advent_of_code_2020/day4/input.txt")

    # Part 1
    passports = get_passports(input_data)

    valid_passports_part_1 = sum(
        passport.required_fields_are_present() for passport in passports
    )

    print(
        f"Part1: there are {valid_passports_part_1} valid passports out of {len(passports)} passports"
    )

    # Part 2
    valid_passports_part_2 = sum(
        (
            passport.required_fields_are_present()
            and passport.required_fields_are_valid()
        )
        for passport in passports
    )

    print(
        f"Part2: there are {valid_passports_part_2} valid passports out of {len(passports)} passports"
    )


if __name__ == "__main__":
    main()