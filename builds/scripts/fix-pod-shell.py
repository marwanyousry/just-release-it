# there is an error occurred while archive iOS project and the solution from stackOverFlow to replace  source="$(readlink "${source}")"   with source="$(readlink -f "${source}")"
## there is an -f added so this script should be executed after build and before archive  
def replace():
    file_path = "./../../ios/App/Pods/Target Support Files/Pods-App/Pods-App-frameworks.sh"
    find = 'source="$(readlink "${source}")"'
    replacement = 'source="$(readlink -f "${source}")"'

    with open(file_path) as f:
        s = f.read()
    s = s.replace(find, replacement)
    with open(file_path, "w") as f:
        f.write(s)

replace()