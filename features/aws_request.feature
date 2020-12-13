Feature: Request do serwera Amazon AWS
    Scenario: logowanie
        Given uzytkownik jest zarejestrowany i istnieje
        When loguje sie poprawnym haslem
        Then logowanie konczy sie sukcesem
    Scenario: request do serwera przez requests
        Given serwer działa
        Then otrzymujemy payload w formacie JSON