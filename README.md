<p align="center"><b>BlackBook - персональний помічник для управління адресами та нотатками.</b></p> Ця інструкція надасть вам докладну інформацію щодо того, як встановити та використовувати програму BlackBook.

<p align="center"><b>Для встановлення BlackBook виконайте наступні кроки:</b></p> 

Спершу завантажте код проекту BlackBook на ваш комп'ютер. Ви можете це зробити шляхом клонування репозиторію з GitHub або завантаження ZIP-архіву з репозиторію.

git clone https://github.com/dem-v/goitneo-python-team8-darkcoders/tree/main

Запустіть BlackBook: Тепер ви можете запустити програму BlackBook, використовуючи команду:

```shell
python3 main.py
```

Також запустити програму BlackBook можливо через pip

```shell
pip install -e .
```

Після встановлення, ви можете запустити програму за допомогою наступної команди в консолі:

```shell
BlackBookConsole
```
Використання
BlackBook надає користувачеві можливість керувати адресами та нотатками через командний рядок. Ви можете виконувати різні команди для додавання, редагування, видалення та пошуку контактів та нотаток.

Список підтримуваних команд
Ось список підтримуваних команд BlackBook:

- add - Додати новий контакт.
- delete - Видалити контакт.
- edit - Редагувати інформацію про контакт.
- search - Пошук контактів за різними параметрами.
- addnote - Додати нову нотатку.
- editnote - Редагувати існуючу нотатку.
- removenote - Видалити нотатку.
- getnotes - Пошук нотаток за текстом.
- printcontacts - Вивести список всіх контактів.
- printnotes - Вивести список всіх нотаток.
- getnotesbytag - Використовується для пошуку контактів та нотаток за певними тегами.

Команда "add"
Дозволяє додати новий контакт у книгу адрес. Приклад використання:

```shell
add -n Lyfenko Dmytro -e lyfenko@gmail.com -p 0974045077 -b 18.08.1987 -a Vasylya Stusa 3, Bila Zerkva, Ukraine
```

-n або --name: Ім'я контакту.
-e або --email: Електронна адреса контакту.
-p або --phones: Номер(и) телефону контакту (можливі кілька номерів, розділених комами або пробілами).
-b або --birthday: День народження контакту у форматі "DD.MM.YYYY".
-a або --address: Адреса контакту.

Команда "delete"
Видаляє контакт(и) із книги адрес. Приклад використання:

```shell
delete -n Lyfenko Dmytro
```

-n або --name: Ім'я контакту, яке слід видалити.

Команда "edit"
Редагує існуючий контакт у книзі адрес. Приклад використання:

```shell
edit -q Lyfenko Dmytro -n New Name -e new.email@gmail.com
```

-q або --query: Повне ім'я контакту, яке слід відредагувати.
-n або --name: Нове ім'я контакту.
-e або --email: Нова електронна адреса контакту.
Ви можете також вказати інші параметри, такі як номери телефону, день народження та адресу для редагування.

Команда "search"
Здійснює пошук контактів за певними критеріями. Приклад використання:

```shell
search -n Dmytro
```

-n або --name: Ім'я контакту для пошуку.

Команда "addnote"
Додає нову нотатку до записної книги. Приклад використання:

```shell
addnote -t Important note content Hello World --tags "Hello"
```

-t або --text: Текст нотатки, яку потрібно додати.
--tags Тег нотатки

Команда "editnote"
Редагує існуючу нотатку в записній книзі. Приклад використання:

```shell
editnote -i 1 -t Updated note text --tags Update tag
```

-i або --id: Ідентифікатор нотатки, яку слід відредагувати.
-t або --text: Новий текст нотатки.
--tags: Новий тег

Команда "removenote"
Видаляє нотатку із записної книги. Приклад використання:

```shell
removenote -i 1
```

-i або --id: Ідентифікатор нотатки, яку слід видалити.

Команда "getnotes"
Виводить нотатки, які містять певне ключове слово. Приклад використання:

```shell
getnotes -q important
```

-q або --query: Ключове слово для пошуку в нотатках.

Команда "hello"
Повертає вітання від програми:

```shell
hello
```

Команда "help"
Виводить список підтримуваних команд та короткий опис кожної:

```shell
help
```

Команда "printcontacts"
Виводить список всіх контактів, які зберігаються у книзі адрес:

```shell
printcontacts
```

Команда "printnotes"
Виводить список всіх нотаток, які зберігаються у записній книзі:

```shell
printnotes
```

Команда "getnotesbytag"
Використовується для пошуку нотаток за певними тегами. Приклад використання:

```shell
getnotesbytag --tag "робота"
```

Ця команда виведе всі нотатки, які мають тег "робота". Параметр --tag вказує тег, за яким слід робити пошук.



Команда "close" та "exit"
Завершує роботу з програмою і виходить із неї:

```shell
close
```

або

```shell
exit
```

Ви можете використовувати ці команди для керування програмою BlackBook та взаємодії із нею. Більш докладні інструкції для кожної команди доступні за допомогою флагу --help або -h після кожної команди.