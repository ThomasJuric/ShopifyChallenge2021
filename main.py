from images import Images
import os

images = Images()
directory = "images"
current_path = os.getcwd()
path = os.path.join(current_path, directory)

try:
    os.mkdir(path)
    print("Directory '% s' created" % directory)
except OSError:
        print("Directory failed to be created, probably already exists")

while True:
    choice = input("Do you want to add or search an image? (Search, Add, List, Exit): ")
    user_choice = choice[0].lower()
    if user_choice == 's':
        file_to_search = input("What is the title you'd like to search for? ")
        images.search(file_to_search)
    elif user_choice == 'a':
        images.add()
    elif user_choice == 'l':
        images.list(path)
    elif user_choice == 'e':
        break
    else:
        print("Sorry, your input was not recognized")