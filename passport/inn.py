import requests
from typing import Any


def get_inn(fio: str, birth_date: str, passport: str) -> str:
    """
    Получает ИНН по паспортным данным

    ДР в формате: `DD.MM.YYYY`
    Паспорт в формате: `XX XX XXXXXX`
    """

    [family_name, first_name, father_name] = fio.split(' ')

    response = requests.post(url='https://service.nalog.ru/inn-proc.do', data={
        'c': "innMy",
        'captcha': '',
        'captchaToken': '',
        'fam': family_name,
        'nam': first_name,
        'otch': father_name,
        'bdate': birth_date,
        'bplace': '',
        'doctype': 21,
        'docno': passport,
        'docdt': ''
    })

    response.raise_for_status()
    data: dict[str, Any] = response.json()
    return data.get("inn", "")
