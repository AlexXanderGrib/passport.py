import requests
from datetime import date
from typing import Any


def is_self_employed(inn: str) -> bool:
    "Получает проверяет статус самозанятого по ИНН"

    response = requests.post(url='https://statusnpd.nalog.ru/api/v1/tracker/taxpayer_status', json={
        'inn': inn,
        'requestDate': date.today().isoformat()
    })

    data: dict[str, Any] = response.json()

    if "status" not in data:
        raise Exception(data.get("message"))

    response.raise_for_status()
    return bool(data.get("status"))
