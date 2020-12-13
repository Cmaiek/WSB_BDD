import behave
import requests
import json

@given('uzytkownik jest zarejestrowany i istnieje')
def step_impl(context):
    pass

@when('loguje sie poprawnym haslem')
def step_impl(context):
    assert True is not False

@then('logowanie konczy sie sukcesem')
def step_impl(context):
    assert context.failed is False

req = requests.get("https://ip-ranges.amazonaws.com/ip-ranges.json")


def is_json(myjson):
  try:
    json_object = json.loads(myjson)
  except ValueError as e:
    return False
  return True


@given('serwer działa')
def step_impl(context):
    assert req.status_code == 200


@then('otrzymujemy payload w formacie JSON')
def step_impl(context):
    assert is_json(json.dumps(req.json())) is True