2.1. LOGIN SYSTEM v.0.02 — PROJECT DOCUMENTATION

GENERAL PLAN / PLAN OGÓLNY

I. Next Steps / Następne kroki
II. Future Plans / Plany na przyszłość
III. Development Log / Log rozwoju projektu


---

ENGLISH

A. NEXT STEPS

1. Validation

Add username validation.

Add password validation.

Decide what should happen after invalid input.


2. User Menu

Define the actual functions of User Menu options.

Implement User Menu functionality step by step.


3. Data Storage

Replace TXT storage with JSON.

Learn and define the JSON structure.

Save users in JSON.

Load users from JSON.

Adapt registration and login to JSON.


4. Authentication

Add a failed-login attempt limit.

Add password hashing.

Add password-change functionality.


5. Project Structure

Later divide the project into modules.

Improve the organization of the project as functionality grows.



---

B. FUTURE PLANS

1. Login System as a Base Application

Eventually use the Login System as a base application for independently developed Python mini-projects.

Allow the user to log in and then choose from available programs.

Possible future programs:

Calculator

Unit Converter

Quiz

Hangman

Text Processing tools

Other Python mini-projects


Develop and test the mini-projects independently first, then integrate them into the Login System.


2. Possible Future Improvements

More advanced input validation.

Better error handling.

More secure authentication.

User-specific data.

Additional user functions.

Modular project architecture.

Integration of independently developed mini-projects.



---

C. DEVELOPMENT LOG

2026-09-19 — Version 0.1

Initial Login System

Created the initial working version of the Login System.

Implemented a terminal-based Main Menu.

Added a separate User Menu for logged-in users.

Implemented registration and login using users.txt.

Stored users in the username:password format.

Added loading and checking of stored user credentials.

Introduced login_successful to control the login result.

Implemented separate program and user-session control.

Tested the main program flow and basic login scenarios.

The w+ file mode was intentionally used at this stage, meaning that the current registration process overwrites the existing file.


Current Project Status

The basic Login System is functional.

The main program structure and login/session flow are established.

Further validation, refactoring and additional functionality are planned.



---

2026-09-20 — Version 0.2

Errors and Debugging

Worked with errors and debugging while developing and restructuring the program.

Used temporary debug output to trace returned True/False values and locate problems in the program flow.

Resolved a problem related to session_running and the control of the user session.


Validation

Added validation for Main Menu choices.

Added validation for User Menu choices.

Initially combined validation with menu handling.

Refactored this approach so that validation is handled separately.

Created dedicated validation functions:

validate_main_menu_choice()

validate_user_menu_choice()



Separation of Responsibilities

Separated validation from menu-choice handling.

Separated Main Menu handling from User Menu handling.

Introduced dedicated functions for menu sessions and menu-choice handling.

Improved the division of responsibilities between functions.


Program Organization and Stabilization

Reorganized the program structure and function placement.

Improved function and variable naming.

Clarified the roles of program_running and session_running.

Improved the flow of information and return values between functions.

Continued restructuring the login process by separating credential collection, user loading and user searching.

Improved terminal readability with spacing and clearer messages.

Replaced temporary menu content with Future Content placeholders.


Current Project Status

Version v.0.02 runs without errors during normal use and is relatively stable.

The project is still incomplete and contains functions planned for future development.

Version v.0.02 provides a more organized foundation for further development.



---

POLSKI

A. NASTĘPNE KROKI

1. Walidacja

Dodać walidację username.

Dodać walidację password.

Ustalić, co ma się dziać po wprowadzeniu nieprawidłowych danych.


2. User Menu

Określić rzeczywiste funkcje poszczególnych opcji User Menu.

Implementować funkcjonalność User Menu krok po kroku.


3. Przechowywanie danych

Zastąpić zapis w TXT formatem JSON.

Nauczyć się i określić strukturę JSON.

Zapisywać użytkowników w JSON.

Wczytywać użytkowników z JSON.

Dostosować rejestrację i logowanie do JSON.


4. Uwierzytelnianie

Dodać limit nieudanych prób logowania.

Dodać hashowanie haseł.

Dodać możliwość zmiany hasła.


5. Struktura projektu

W późniejszym etapie podzielić projekt na moduły.

Usprawniać organizację projektu wraz z rozwojem funkcjonalności.



---

B. PLANY NA PRZYSZŁOŚĆ

1. Login System jako aplikacja bazowa

Docelowo wykorzystać Login System jako aplikację bazową dla niezależnie tworzonych mini-projektów w Pythonie.

Użytkownik będzie się logował, a następnie wybierał dostępny program.

Możliwe przyszłe programy:

Calculator

Unit Converter

Quiz

Hangman

narzędzia do przetwarzania tekstu

inne mini-projekty w Pythonie


Najpierw rozwijać i testować mini-projekty niezależnie, a następnie integrować je z Login System.


2. Możliwe przyszłe usprawnienia

Bardziej zaawansowana walidacja danych wejściowych.

Lepsza obsługa błędów.

Bezpieczniejsze uwierzytelnianie.

Dane przypisane do konkretnych użytkowników.

Dodatkowe funkcje użytkownika.

Modułowa architektura projektu.

Integracja niezależnie rozwijanych mini-projektów.



---

C. LOG ROZWOJU

2026-09-19 — Wersja 0.1

Początkowa wersja Login System

Utworzono pierwszą działającą wersję Login System.

Zaimplementowano terminalowe Main Menu.

Dodano osobne User Menu dla zalogowanego użytkownika.

Zaimplementowano rejestrację i logowanie z wykorzystaniem users.txt.

Użytkownicy są zapisywani w formacie username:password.

Dodano wczytywanie i sprawdzanie zapisanych danych użytkowników.

Wprowadzono login_successful do kontroli wyniku logowania.

Zaimplementowano osobne sterowanie programem i sesją użytkownika.

Przetestowano główny przepływ programu oraz podstawowe scenariusze logowania.

Na tym etapie celowo zastosowano tryb pliku w+, przez co obecny sposób rejestracji nadpisuje istniejący plik.


Aktualny stan projektu

Podstawowa wersja Login System działa.

Ustalono główną strukturę programu oraz przepływ logowania i sesji użytkownika.

Zaplanowano dalszą walidację, refaktoryzację i rozwój funkcjonalności.



---

2026-09-20 — Wersja 0.2

Błędy i debugowanie

Pracowano z błędami i debugowaniem podczas rozwijania oraz przebudowy programu.

Wykorzystano tymczasowe komunikaty debugujące do śledzenia zwracanych wartości True/False i lokalizowania problemów w przepływie programu.

Rozwiązano problem związany z session_running i kontrolą sesji użytkownika.


Walidacja

Dodano walidację wyborów w Main Menu.

Dodano walidację wyborów w User Menu.

Początkowo walidacja była połączona z obsługą wyboru.

Następnie rozdzielono walidację od obsługi wyboru.

Utworzono osobne funkcje:

validate_main_menu_choice()

validate_user_menu_choice()



Rozdzielenie odpowiedzialności

Oddzielono walidację od obsługi wyboru.

Oddzielono obsługę Main Menu od obsługi User Menu.

Wprowadzono osobne funkcje odpowiedzialne za sesje menu i obsługę ich wyborów.

Uporządkowano podział odpowiedzialności pomiędzy funkcjami.


Porządkowanie programu i stabilizacja

Uporządkowano strukturę programu oraz rozmieszczenie funkcji.

Poprawiono nazewnictwo funkcji i zmiennych.

Doprecyzowano role program_running i session_running.

Uporządkowano przepływ danych i wartości zwracanych przez funkcje.

Kontynuowano przebudowę procesu logowania poprzez rozdzielenie pobierania danych, wczytywania użytkowników i wyszukiwania użytkownika.

Poprawiono czytelność terminala poprzez odstępy i bardziej przejrzyste komunikaty.

Tymczasową zawartość menu zastąpiono oznaczeniami Future Content.


Aktualny stan projektu

Wersja v.0.02 działa bez błędów podczas normalnego użytkowania i jest względnie stabilna.

Projekt jest nadal nieukończony i zawiera funkcje zaplanowane do dalszego rozwoju.

Wersja v.0.02 stanowi bardziej uporządkowaną podstawę do dalszej pracy.