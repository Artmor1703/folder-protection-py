#### РУС

В папке предоставлен проект реализованный на **Python** с использованием  **pywin32**.

Проект представляет из себя программу, вызываемую через командную строку. Манипуляции происходят с папкой указанной в самом коде. <br>
При введении правильного пароля (111) пользователю представится возможность совершить 4 действия.

1.	 Открыть доступ к файлам, указанным в "template.tbl".
2.	 Закрыть доступ к файлам, указанным в "template.tbl".

Под закрытием доступа стоит подразумевать полное отсутствие возможности совершения любых операций с файлом (редактирование, выполнение, чтение, удаление, перетаскивание и так далее). <br>
Работа происходит с файлами находящимися в той же папке, что и сама программа. <br>
В самом файле "template" необходимо указать имя файлов без расширения ("txt" по умолчанию), отделяя их пробелом.  По умолчанию "template" будет иметь ограниченный доступ, чтобы внести в него изменение, необходимо вызвать третью команду.

3.	Открыть доступ к "template".

После того как доступ откроется, программа запросит уведомление об окончании редактирования (нажатие любой клавиши). После редактирования доступ к "template" закроется. <br>
Последняя команда:

4.	Начать отслеживание изменений в папке.

Во время этого режима, блокируется возможность создания файлов с именами указанными в "template". Те, что были созданы до начала сканирования остаются неизменными. Для отключения режима достаточно ввести любой символ. <br>
После вызова одной из команд программа предложит продолжить, если пользователь соглашается, ему предоставляется совершить все те же 4 действия, в обратном случае программа завершается.

___
#### ENG

The file contains project implemented in **Python** using **pywin32**

A project is a command line program. Manipulations are performed with the folder specified in the code itself.<br>
After entering the correct password (111), the user will have the opportunity to perform 4 actions.

1. Open access to the files specified in "template.tbl".
2. Close access to files specified in "template.tbl".

Closing access means the complete inability to perform any operations with the file (editing, executing, reading, deleting, dragging and dropping, and so on). <br>
The program interacts with files located in the same folder as the program itself. <br>
In the file "template" itself, you must specify the name of the files ("txt" default), separating them with a space.

3.	Open access to the "template".

After the access opens, the program will ask for a notification about the end of editing (release any keys). <br>
After editing, access to the template will be closed.

4. Start tracking changes in the folder.

During this mode, the ability to create files with the names specified in "template" is blocked.
Those that were created before the start of the scan remain unchanged. <br>
To disable the mode, just enter any character.<br>
After calling one of the commands, the program will offer to continue, if the user agrees, he is given to perform all the same 4 actions, otherwise the program ends.
