from datetime import datetime, timedelta


def get_date_of_issue(serial: str, birth_date: str) -> str:
    year_of_issue = serial[2:4]
    date_of_issue = f'{birth_date[0:5]}.{year_of_issue}'

    date = datetime.strptime(date_of_issue, "%d.%m.%y") + timedelta(days=20)

    return date.strftime("%d.%m.%Y")
