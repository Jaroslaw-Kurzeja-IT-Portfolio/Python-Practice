# 2.1. LOGIN SYSTEM v.0.02 — PROJECT DOCUMENTATION

## GENERAL PLAN / PLAN OGÓLNY

I. Next Steps / Następne kroki  
II. Future Plans / Plany na przyszłość  
III. Development Log / Log rozwoju projektu  

---

# ENGLISH

## A. NEXT STEPS

### 1. User Account Expansion  
**(planned for v.0.03)**

- Add information associated with individual user accounts.
- Add the possibility for users to manage their own accounts.

### 2. Migration from TXT to JSON  
**(planned for v.0.03)**

- Replace the current `users.txt` storage with JSON.
- Define the structure of user data in JSON.
- Save users in JSON.
- Load users from JSON.
- Adapt registration and login to the new storage format.

### 3. Account Functionality  
**(planned for v.0.03)**

- Change own password.
- Delete own account.
- Add further functionality related to managing the user's own account.

### 4. User / Administrator Roles  
**(planned for v.0.03)**

Introduce two basic roles:

- `user`
- `admin`

Planned functionality:

- user permissions,
- administrator permissions,
- account management by the administrator,
- changing other users' passwords,
- deleting other users' accounts.

### 5. Modular Project Architecture  
**(planned for v.0.04)**

Divide the application into separate modules as the project grows.

Organize the code according to the responsibilities of individual parts of the application.

Use the Login System as a practical project for learning and implementing a modular Python project structure.

### 6. Frontend – Streamlit  
**(planned for v.1.0)**

Develop a browser-based interface for the Login System.

- interface available through a web browser,
- possibility of making the application available through a link.

### 7. Migration from JSON to SQLite

Replace JSON-based storage with an SQLite database.

Adapt the application to work with database storage.

### 8. API

Introduce an API into the Login System.

Use the API as another stage in the development of the application's architecture and communication with external components or services.

### 9. Migration from SQLite to MySQL

Replace the SQLite database with MySQL.

Adapt the application to work with a MySQL database.

### 10. Further Application Development

Continue expanding the Login System with additional functionality as the project develops.

**The order is orientational. Individual stages may change depending on the development of the project, learning progress and the needs of the application.**

---

## B. FUTURE PLANS

### 1. Login System as a Base Application

Eventually use the Login System as a base application for independently developed Python mini-projects.

The user will log in and then choose from the available programs.

Possible future programs:

- Calculator
- Unit Converter
- Quiz
- Hangman
- Text Processing tools
- other Python mini-projects

Develop and test the mini-projects independently first, then integrate them into the Login System.

### 2. Tkinter

Possible desktop version of the application.

- desktop application interface,
- possibility of creating and sharing a standalone `.exe` file.

### 3. Possible Future Improvements

- more advanced input validation,
- better error handling,
- more secure authentication,
- user-specific data,
- additional user functions,
- additional account functionality,
- additional integrations,
- further development of the application structure.

---

## C. DEVELOPMENT LOG

### 2026-09-19 — Version 0.1

#### Initial Login System

Created the initial working version of the Login System.

Implemented a terminal-based Main Menu.

Added a separate User Menu for logged-in users.

Implemented registration and login using `users.txt`.

Stored users in the `username:password` format.

Added loading and checking of stored user credentials.

Introduced `login_successful` to control the login result.

Implemented separate program and user-session control.

Tested the main program flow and basic login scenarios.

The `w+` file mode was intentionally used at this stage, meaning that the current registration process overwrote the existing file.

#### Current Project Status

The basic Login System was functional.

The main program structure and login/session flow were established.

Further validation, refactoring and additional functionality were planned.

---

### 2026-09-20 — Version 0.2

#### Errors and Debugging

Worked with errors and debugging while developing and restructuring the program.

Used temporary debug output to trace returned `True`/`False` values and locate problems in the program flow.

Resolved a problem related to `session_running` and the control of the user session.

#### Validation

Added validation for Main Menu choices.

Added validation for User Menu choices.

Initially combined validation with menu handling.

Refactored this approach so that validation is handled separately.

Created dedicated validation functions:

`validate_main_menu_choice()`

`validate_user_menu_choice()`

#### Separation of Responsibilities

Separated validation from menu-choice handling.

Separated Main Menu handling from User Menu handling.

Introduced dedicated functions for menu sessions and menu-choice handling.

Improved the division of responsibilities between functions.

#### Program Organization and Stabilization

Reorganized the program structure and function placement.

Improved function and variable naming.

Clarified the roles of `program_running` and `session_running`.

Improved the flow of information and return values between functions.

Continued restructuring the login process by separating credential collection, user loading and user searching.

Improved terminal readability with spacing and clearer messages.

Replaced temporary menu content with Future Content placeholders.

#### Registration and Login Functionality

Added username validation.

Added password validation.

Added username uniqueness checking during registration.

Added password confirmation during registration.

Changed user storage from `w+` to `a+`, allowing new users to be appended to the existing `users.txt` file.

Refactored the registration process into separate functions:

`get_register_username()`

`get_register_password()`

`save_user()`

`check_username_unique()`

#### ESC Cancellation

Added the possibility to cancel registration and login using the `ESC` key.

Implemented `get_input_or_cancel()` using the `readchar` library.

The function supports:

- text input,
- `Enter`,
- `Backspace`,
- `ESC` cancellation.

`None` is used as the return value when the user cancels the operation.

The cancellation result is handled by the registration and login processes.

#### Current Project Status

Version v.0.02 provides:

- Main Menu,
- User Menu,
- registration,
- login,
- username validation,
- password validation,
- username uniqueness checking,
- password confirmation,
- ESC cancellation,
- logout,
- separate program and user-session control,
- storage of multiple users in `users.txt`.

The project is still incomplete and contains functionality planned for further development.

Version v.0.02 provides a more organized foundation for further development.

---

# POLSKI

## A. NASTĘPNE KROKI

### 1. Rozbudowa kont użytkowników  
**(planowana wersja v.0.03)**

- dodanie informacji przypisanych do poszczególnych kont,
- możliwość zarządzania własnym kontem.

### 2. Przejście z TXT na JSON  
**(planowana wersja v.0.03)**

- zastąpienie obecnego zapisu w `users.txt` formatem JSON,
- określenie struktury danych użytkownika w JSON,
- zapisywanie użytkowników w JSON,
- odczytywanie użytkowników z JSON,
- dostosowanie rejestracji i logowania do nowego sposobu przechowywania danych.

### 3. Funkcjonalności konta  
**(planowana wersja v.0.03)**

- zmiana własnego hasła,
- usunięcie własnego konta,
- dalsze funkcjonalności związane z zarządzaniem własnym kontem.

### 4. Role użytkownika i administratora  
**(planowana wersja v.0.03)**

Wprowadzenie dwóch podstawowych ról:

- `user`,
- `admin`.

Planowane funkcjonalności:

- uprawnienia użytkownika,
- uprawnienia administratora,
- zarządzanie kontami przez administratora,
- zmiana haseł innych użytkowników,
- usuwanie kont innych użytkowników.

### 5. Modułowa architektura projektu  
**(planowana wersja v.0.04)**

Podział aplikacji na osobne moduły wraz z rozwojem projektu.

Uporządkowanie kodu zgodnie z odpowiedzialnością poszczególnych części aplikacji.

Wykorzystanie Login Systemu jako praktycznego projektu do nauki i wdrożenia modułowej struktury projektu Python.

### 6. Frontend – Streamlit  
**(planowana wersja v.1.0)**

Rozbudowa Login Systemu o interfejs dostępny przez przeglądarkę.

- interfejs aplikacji dostępny przez przeglądarkę,
- możliwość udostępnienia aplikacji przez link.

### 7. Przejście z JSON na SQLite

Zastąpienie przechowywania danych w JSON bazą SQLite.

Dostosowanie aplikacji do pracy z bazą danych.

### 8. Wprowadzenie API

Wprowadzenie API do Login Systemu.

Wykorzystanie API jako kolejnego etapu rozwoju architektury aplikacji oraz komunikacji z zewnętrznymi komponentami lub usługami.

### 9. Przejście ze SQLite na MySQL

Zastąpienie bazy SQLite bazą MySQL.

Dostosowanie aplikacji do pracy z MySQL.

### 10. Dalsza rozbudowa aplikacji

Dalszy rozwój Login Systemu i dodawanie kolejnych funkcjonalności wraz z rozwojem projektu.

**Kolejność jest orientacyjna. Poszczególne etapy mogą się zmieniać zależnie od rozwoju projektu, postępów w nauce i potrzeb aplikacji.**

---

## B. PLANY NA PRZYSZŁOŚĆ

### 1. Login System jako aplikacja bazowa

Docelowo wykorzystać Login System jako aplikację bazową dla niezależnie tworzonych mini-projektów w Pythonie.

Użytkownik będzie się logował, a następnie wybierał dostępny program.

Możliwe przyszłe programy:

- Calculator,
- Unit Converter,
- Quiz,
- Hangman,
- narzędzia do przetwarzania tekstu,
- inne mini-projekty w Pythonie.

Najpierw rozwijać i testować mini-projekty niezależnie, a następnie integrować je z Login Systemem.

### 2. Tkinter

Możliwa desktopowa wersja aplikacji.

- interfejs aplikacji desktopowej,
- możliwość utworzenia i udostępnienia samodzielnego pliku `.exe`.

### 3. Możliwe przyszłe usprawnienia

- bardziej zaawansowana walidacja danych,
- lepsza obsługa błędów,
- bezpieczniejsze uwierzytelnianie,
- dane przypisane do konkretnych użytkowników,
- dodatkowe funkcje użytkownika,
- dodatkowe funkcjonalności kont,
- dodatkowe integracje,
- dalszy rozwój struktury aplikacji.

---

## C. LOG ROZWOJU

### 19.09.2026 — Wersja 0.1

#### Początkowa wersja Login System

Utworzono pierwszą działającą wersję Login System.

Zaimplementowano terminalowe Main Menu.

Dodano osobne User Menu dla zalogowanego użytkownika.

Zaimplementowano rejestrację i logowanie z wykorzystaniem `users.txt`.

Użytkownicy są zapisywani w formacie `username:password`.

Dodano wczytywanie i sprawdzanie zapisanych danych użytkowników.

Wprowadzono `login_successful` do kontroli wyniku logowania.

Zaimplementowano osobne sterowanie programem i sesją użytkownika.

Przetestowano główny przepływ programu oraz podstawowe scenariusze logowania.

Na tym etapie celowo zastosowano tryb pliku `w+`, przez co obecny sposób rejestracji nadpisywał istniejący plik.

#### Aktualny stan projektu

Podstawowa wersja Login System działała.

Ustalono główną strukturę programu oraz przepływ logowania i sesji użytkownika.

Zaplanowano dalszą walidację, refaktoryzację i rozwój funkcjonalności.

---

### 20.09.2026 — Wersja 0.2

#### Błędy i debugowanie

Pracowano z błędami i debugowaniem podczas rozwijania oraz przebudowy programu.

Wykorzystano tymczasowe komunikaty debugujące do śledzenia zwracanych wartości `True`/`False` i lokalizowania problemów w przepływie programu.

Rozwiązano problem związany z `session_running` i kontrolą sesji użytkownika.

#### Walidacja

Dodano walidację wyborów w Main Menu.

Dodano walidację wyborów w User Menu.

Początkowo walidacja była połączona z obsługą wyboru.

Następnie rozdzielono walidację od obsługi wyboru.

Utworzono osobne funkcje:

`validate_main_menu_choice()`

`validate_user_menu_choice()`

#### Rozdzielenie odpowiedzialności

Oddzielono walidację od obsługi wyboru.

Oddzielono obsługę Main Menu od obsługi User Menu.

Wprowadzono osobne funkcje odpowiedzialne za sesje menu i obsługę ich wyborów.

Uporządkowano podział odpowiedzialności pomiędzy funkcjami.

#### Porządkowanie programu i stabilizacja

Uporządkowano strukturę programu oraz rozmieszczenie funkcji.

Poprawiono nazewnictwo funkcji i zmiennych.

Doprecyzowano role `program_running` i `session_running`.

Uporządkowano przepływ danych i wartości zwracanych przez funkcje.

Kontynuowano przebudowę procesu logowania poprzez rozdzielenie pobierania danych, wczytywania użytkowników i wyszukiwania użytkownika.

Poprawiono czytelność terminala poprzez odstępy i bardziej przejrzyste komunikaty.

Tymczasową zawartość menu zastąpiono oznaczeniami Future Content.

#### Aktualny stan projektu

Wersja v.0.02 stanowi bardziej uporządkowaną podstawę do dalszej pracy.

Projekt jest nadal nieukończony i zawiera funkcjonalności zaplanowane do dalszego rozwoju.

---

### 28–29.09.2026 — Wersja 0.2

#### Walidacja danych użytkownika

Dodano walidację `username` podczas rejestracji.

Dodano walidację `password` podczas rejestracji.

Dodano walidację `username` podczas logowania.

Dodano walidację `password` podczas logowania.

Walidacja obejmuje m.in. długość danych oraz dozwolone znaki.

#### Funkcjonalności rejestracji i wielu użytkowników

Dodano sprawdzanie unikalności `username` podczas rejestracji.

Dodano obsługę wielu użytkowników.

Zmieniono sposób zapisu użytkowników z `w+` na `a+`, dzięki czemu nowi użytkownicy są dopisywani do istniejącego pliku `users.txt` zamiast nadpisywać wcześniejsze dane.

Przebudowano proces rejestracji, dzieląc go na osobne funkcje:

`get_register_username()`

`get_register_password()`

`save_user()`

`check_username_unique()`

#### Data Flow i odpowiedzialność funkcji

Kontynuowano pracę nad przepływem danych pomiędzy funkcjami.

Pracowano nad wywoływaniem jednej funkcji przez inną oraz przekazywaniem danych i wyników pomiędzy funkcjami.

Analizowano różne możliwe wartości zwracane przez funkcje, w tym `True`, `False`, `None` oraz dane typu `str`.

Pracowano ze zwracaniem kilku danych jednocześnie, np. `(username, password)`.

Uporządkowano sposób, w jaki wyniki jednej funkcji są wykorzystywane przez kolejne funkcje.

Kontynuowano rozdzielanie odpowiedzialności pomiędzy funkcjami.

Rozwijano strukturę procesu logowania i sposób przekazywania danych pomiędzy `login()`, `check_login()` oraz pozostałymi funkcjami.

#### Anulowanie rejestracji i logowania przez ESC

Dodano możliwość anulowania rejestracji i logowania za pomocą klawisza `ESC`.

Zaimplementowano funkcję `get_input_or_cancel()` z wykorzystaniem biblioteki `readchar`.

Funkcja obsługuje:

- wprowadzanie tekstu,
- `Enter`,
- `Backspace`,
- anulowanie przez `ESC`.

Wartość `None` jest wykorzystywana jako informacja o anulowaniu operacji.

Wynik anulowania jest przekazywany przez kolejne funkcje rejestracji i logowania.

Dodano potwierdzenie hasła podczas rejestracji.

Kontynuowano pracę nad odpowiedzialnością funkcji oraz Data Flow.

#### Aktualny stan projektu

Wersja v.0.02 zawiera:

- Main Menu,
- User Menu,
- rejestrację,
- logowanie,
- walidację username,
- walidację password,
- sprawdzanie unikalności username,
- potwierdzenie hasła,
- anulowanie przez ESC,
- wylogowanie,
- osobne sterowanie programem i sesją użytkownika,
- przechowywanie wielu użytkowników w `users.txt`.

Projekt jest nadal nieukończony i zawiera funkcjonalności zaplanowane do dalszego rozwoju.


