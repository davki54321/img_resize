
from PIL import Image
import os


def main():

    # Sets the percentage to reduce images
    PERCENT = .4
    NEW_DIR_NAME = "resized"

    # Makes new directory for smaller files
    directory = r'C:/Users/wbrju/Downloads/test'
    path_new = os.path.join(directory, NEW_DIR_NAME)

    make_new_dir(path_new)

    # keeps track of number of files changed and skipped
    change_counter = 0
    skipped_counter = 0

    # Images get open, resized, and saved
    for file in os.listdir(directory):
        if file.endswith(('jpeg', 'png', 'jpg')):
            change_counter += 1
            f_img = directory+"/"+file
            save_location = path_new+"/"+file

            save_location = check_dbl(path_new, directory, file)

            img = Image.open(f_img)
            width, height = img.size
            img = img.resize((int(width * PERCENT), int(height * PERCENT)))
            # print(f"save_location = {save_location}")
            img.save(save_location)
        else:
            skipped_counter += 1

    print_numbers(change_counter, skipped_counter)


# makes new directory for the changed files
def make_new_dir(path):
    try:
        os.mkdir(path)
    except FileExistsError:
        pass


# checks the new directory if a file with the same name already exists
def check_dbl(new_path1, dir, file1, double_counter=""): 
# "new_path1" is location of the new directory
# "dir" is the path where the original files are
# file1 is the name of the file
# "double_counter" is the end number for the new file

    # for first call of function
    if not double_counter:
        # Checks if file with same name exists in the new directory
        new_file = new_path1 + "/" + file1
        if os.path.exists(new_file):
                double_counter = 1
                return check_dbl(new_path1, dir, file1, double_counter)
        # if file with the same name does not exist in the directory
        else:
            return new_file

    # for every call after the first     
    else:
        # checks ending of the file
        if file1.endswith(".jpeg"):
            end = ".jpeg"
        elif file1.endswith(".jpg"):
            end = ".jpg"
        elif file1.endswith(".png"):
            end = ".png"


        # "numbered_file" is the new name with a number appended to the end
        numbered_file = file1.replace(end, f"({double_counter}){end}", 1)
        # "new_file" is the name of the directory and the file together
        new_file = new_path1 + "/" + numbered_file
        
        if os.path.exists(new_file):
            double_counter += 1
            return check_dbl(new_path1, dir, file1, double_counter)
        
        else:  
            return new_file
        

# prints the number of files changed and skipped
def print_numbers(changed, skipped):
    if changed == 1:
        change_end = "file has been changed."
    else:
        change_end = "files have been changed."

    if skipped == 1:
        skipped_end = "file has been skipped."
    else:
        skipped_end = "files have been skipped."

    print("\n= = = = = = = = = = = = = = = ")
    print(f" {changed}  {change_end}")
    print(f" {skipped}  {skipped_end}")
    print("= = = = = = = = = = = = = = = \n")


if __name__=="__main__":
    main()
