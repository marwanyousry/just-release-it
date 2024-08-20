import fileinput

def replace_line(file_path, old_line, new_line):
    with fileinput.FileInput(file_path, inplace=True, backup='.bak') as file:
        for line in file:
            print(line.replace(old_line, new_line), end='')

if __name__ == "__main__":
    java_file_path = "./../../node_modules/@capacitor/android/capacitor/src/main/java/com/getcapacitor/Bridge.java"
    old_line = "settings.setAppCacheEnabled(true);"
    new_line = "settings.setCacheMode(WebSettings.LOAD_DEFAULT);"

    replace_line(java_file_path, old_line, new_line)
