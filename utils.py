from iso8601 import parse_date as iso_parse_date


def parse_date(date: str):
    return iso_parse_date(date)
