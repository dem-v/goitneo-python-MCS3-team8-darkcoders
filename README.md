<p align="center"><b>BlackBook - персональний помічник для управління адресами та нотатками.</b></p> Ця інструкція надасть вам докладну інформацію щодо того, як встановити та використовувати програму BlackBook.

<p align="center"><b>Для встановлення BlackBook виконайте наступні кроки:</b></p> 

Спершу завантажте код проекту BlackBook на ваш комп'ютер. Ви можете це зробити шляхом клонування репозиторію з GitHub або завантаження ZIP-архіву з репозиторію.

git clone https://github.com/dem-v/goitneo-python-team8-darkcoders/tree/main

Запустіть BlackBook: Тепер ви можете запустити програму BlackBook, використовуючи команду:

```shell
python3 main.py
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
- addtag - Дозволяє додати теги до контакту чи нотатки.
- removetag - Видаляє теги із контакту чи нотатки.
- edittag - Дозволяє редагувати існуючі теги для контакту чи нотатки.
- searchtags - Використовується для пошуку контактів та нотаток за певними тегами.
- printtags - Виводить список всіх тегів, які використовуються для контактів та нотаток.

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
addnote -t Important note content Hello World
```

-t або --text: Текст нотатки, яку потрібно додати.

Команда "editnote"
Редагує існуючу нотатку в записній книзі. Приклад використання:

```shell
editnote -i 1 -t Updated note text
```

-i або --id: Ідентифікатор нотатки, яку слід відредагувати.
-t або --text: Новий текст нотатки.

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

Команда "addtag"
Дозволяє додати теги до контакту чи нотатки. Приклад використання:

```shell
addtag -n "Dmytro Lyfenko" -t "робота" "важливо"
```

Ця команда додасть теги "робота" і "важливо" до контакту з іменем "Dmytro Lyfenko". Теги вказуються за допомогою параметра -t або --tags, і можна додавати декілька тегів, розділивши їх пробілами чи комами.

Команда "removetag"
Видаляє теги із контакту чи нотатки. Приклад використання:

```shell
removetag -n "Dmytro Lyfenko" -t "робота"
```

Ця команда видалить тег "робота" з контакту "Dmytro Lyfenko". Тег вказується за допомогою параметра -t або --tag.

Команда "edittag"
Дозволяє редагувати існуючі теги для контакту чи нотатки. Приклад використання:

```shell
edittag -n "Dmytro Lyfenko" -ot "робота" -nt "новий_тег"
```

Ця команда замінить тег "робота" на "новий_тег" для контакту "Dmytro Lyfenko". Параметр -ot або --oldtag вказує старий тег, а -nt або --newtag вказує новий тег.

Команда "searchtags"
Використовується для пошуку контактів та нотаток за певними тегами. Приклад використання:

```shell
searchtags -t "робота"
```

Ця команда виведе всі контакти та нотатки, які мають тег "робота". Параметр -t або --tag вказує тег, за яким слід робити пошук.

Команда "printtags"
Виводить список всіх тегів, які використовуються для контактів та нотаток.

```shell
printtags
```

Ця команда виведе всі доступні теги, які використовуються в програмі.

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