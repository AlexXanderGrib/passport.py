def get_date_of_issue(serial: str, birth_date: str) -> str:
    year_of_issue = serial[2:4]
    date_of_issue = f'{birth_date[0:5]}.20{year_of_issue}'

    return date_of_issue
