import win32security
import ntsecuritycon as con
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

def b():
    userx = win32security.LookupAccountName("", "USER")


    FILENAME = r"C:\Users\USER\PycharmProjects\pythonProject\pythonProject\template.tbl"

    sd = win32security.GetFileSecurity(FILENAME, win32security.DACL_SECURITY_INFORMATION)
    dacl = win32security.ACL()

    dacl.AddAccessAllowedAce(win32security.ACL_REVISION, con.FILE_ALL_ACCESS, userx[0])
    sd.SetSecurityDescriptorDacl(1, dacl, 0)  # may not be necessary
    win32security.SetFileSecurity(FILENAME, win32security.DACL_SECURITY_INFORMATION, sd)

    handle = open("template.tbl", "r")

    b = handle.read()
    b = str(b).split(" ")
    handle.close()
    dacl.AddAccessDeniedAce(win32security.ACL_REVISION, con.FILE_ALL_ACCESS, userx[0])
    sd.SetSecurityDescriptorDacl(1, dacl, 0)  # may not be necessary
    win32security.SetFileSecurity(FILENAME, win32security.DACL_SECURITY_INFORMATION, sd)

    return b
class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        for filename in os.listdir(r"C:\Users\USER\PycharmProjects\pythonProject\pythonProject"):
            a = filename[:filename.index(".")]
            pyti = event.src_path[58:event.src_path.find(".")]
            if (a in b()) and (a == pyti):
                 c = str(a) + '.txt'
                 os.remove(c)


pas = input("Введите пароль: ")
if pas != "111":
    print("Пароль неверный!")
    exit()

def qwe():
    print("Добро пожаловать! Выберите, что вам нужно")
    print("1. Открыть доступ к файлам указанным в template")
    print("2. Закрыть доступ к файлам указанным в template")
    print("3. Открыть доступ к template")
    print("4. Начать отслеживание изменений в папке")
    choise = int(input())

    Folder = os.listdir(r"C:\Users\USER\PycharmProjects\pythonProject\pythonProject")
    if (choise == 1 or choise == 2):
        for a in b():
            if (a + ".txt" not in Folder):
                continue
            FILENAME = r"C:\Users\USER\PycharmProjects\pythonProject\pythonProject\{}.txt".format(a)

            userx = win32security.LookupAccountName("", "USER")

            sd = win32security.GetFileSecurity(FILENAME, win32security.DACL_SECURITY_INFORMATION)
            dacl = win32security.ACL()
            if (choise == 1):
                dacl.AddAccessAllowedAce(win32security.ACL_REVISION, con.FILE_ALL_ACCESS, userx[0])
            if (choise == 2):
                dacl.AddAccessDeniedAce(win32security.ACL_REVISION, con.FILE_ALL_ACCESS, userx[0])
            sd.SetSecurityDescriptorDacl(1, dacl, 0)  # may not be necessary
            win32security.SetFileSecurity(FILENAME, win32security.DACL_SECURITY_INFORMATION, sd)

    elif (choise == 3):
        userx = win32security.LookupAccountName("", "USER")

        FILENAME = r"C:\Users\USER\PycharmProjects\pythonProject\pythonProject\template.tbl"

        sd = win32security.GetFileSecurity(FILENAME, win32security.DACL_SECURITY_INFORMATION)
        dacl = win32security.ACL()

        dacl.AddAccessAllowedAce(win32security.ACL_REVISION, con.FILE_ALL_ACCESS, userx[0])
        sd.SetSecurityDescriptorDacl(1, dacl, 0)  # may not be necessary
        win32security.SetFileSecurity(FILENAME, win32security.DACL_SECURITY_INFORMATION, sd)

        input("Когда закончите редактирование нажмите на любую клавишу: ")
        dacl.AddAccessDeniedAce(win32security.ACL_REVISION, con.FILE_ALL_ACCESS, userx[0])
        sd.SetSecurityDescriptorDacl(1, dacl, 0)  # may not be necessary
        win32security.SetFileSecurity(FILENAME, win32security.DACL_SECURITY_INFORMATION, sd)

    elif (choise == 4):
        event_handler = MyHandler()
        observer = Observer()
        observer.schedule(event_handler, path=r"C:\Users\USER\PycharmProjects\pythonProject\pythonProject",
                          recursive=False)
        observer.start()
        while True:
            try:
                input("Для выхода нажмите любую кнопку:")
                break
                pass
            except KeyboardInterrupt:
                observer.stop()
    quest = input("Хотите продолжить? (y/n): ")
    if (quest == "y"):
        qwe()
    else:
        print("До свидания!")
        exit()
qwe()