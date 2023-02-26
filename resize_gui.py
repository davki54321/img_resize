
# this program resizes picture files

from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog, ttk


class Window:

    def __init__(self):
        # create root window
        self.root = tk.Tk()
        self.root.geometry("600x500")

        # background color for subframes
        self.bg_color = "#F9F9DD"
        
        # filepath of folder containing files
        self.filepath = None

        # name for new directory to save new files
        self.new_dir_name = "resized"

        # Bool to see if files should be overwritten or not
        self.check_double_bool = False

        self.header()
        self.choose_dir()
        self.resize_options()
        self.save_options()
        self.run_btn()
        # self.start()


    # Initializes directory button
    def start(self):
        self.filepath = None
        self.choose_dir()
        self.resize_options()
        self.save_options()
        self.run_btn()


    # makes header or title of program
    def header(self):
        # Adding weight to row in rootcenters the header label
        # self.root.grid_columnconfigure(0, weight=1)

        header_label = tk.Label(self.root,
                                text="Image Resizer",
                                font=("Helvetica 15 bold underline"))
        # header_label.grid(row=0, column=0, columnspan=2, pady=(15, 10))
        header_label.place(relx = 0.5,
                            rely = 0.07,
                            anchor = "center")


    # frame that allows user to choose directory with photos
    # top left frame
    def choose_dir(self):
        # destroys frame if already created
        try:
            self.dir_frame.destroy()
        except AttributeError:
            pass

        # creates frame for "select directory" button
        self.dir_frame = tk.Frame(self.root,
                                  bg=self.bg_color,
                                  height=140,
                                  width=290,
                                  bd=1,
                                  relief="raised")
        # Creates a frame with fixed sized (will not resize 3ith different number of widgets)
        # Fixed height and width must be entered (line above)
        self.dir_frame.grid_propagate(False)
        self.dir_frame.place(relx = 0.012,
                                rely = 0.14)

        select_btn = tk.Button(self.dir_frame,
                                text="select directory",
                                command=self.select_dir)
        self.dir_frame.grid_columnconfigure(0, weight=1)
        # select_btn.grid(column=0, row=0)
        select_btn.place(relx = 0.5,
                            rely = 0.2,
                            anchor = "center")

        # if directory with photos has been chosen path will be shown in frame
        if self.filepath:
            self.dir_label=tk.Label(self.dir_frame,
                                    text=self.filepath,
                                    font=('Helvetica 11 italic'),
                                    bg=self.bg_color,
                                    wraplength=260, 
                                    justify="center")
            self.dir_label.place(relx = 0.5,
                                    rely = 0.53,
                                    anchor = "center")


    # method used to select directory with photos
    def select_dir(self):
        # get a directory path by user
        self.filepath=filedialog.askdirectory(initialdir=r"C:/",
                                                title="Select Directory")
        self.choose_dir()


    # creates frame with options on where to save the new files
    # top right frame
    def save_options(self):
        # creates frame for save options
        self.save_frame = tk.Frame(self.root,
                                    bg=self.bg_color,
                                    height=140,
                                    width=290,
                                    bd=1,
                                    relief="raised")
        # Creates a frame with fixed sized (will not resize 3ith different number of widgets)
        # Fixed height and width must be entered (line above)
        self.save_frame.grid_propagate(False)
        self.save_frame.place(relx = 0.505,
                                rely = 0.14)

        self.save_label = tk.Label(self.save_frame,
                                    bg=self.bg_color,
                                    text="How do you want to save?",
                                    font=("Helvetica 11 underline"))
        self.save_label.place(relx = 0.2,
                                rely = 0.08)

        # separate frame for radio buttons        
        self.save_btn_frame = tk.Frame(self.save_frame,
                                       bg=self.bg_color,
                                       height=70,
                                       width=70,)
        self.save_btn_frame.place(relx = 0.11,
                                    rely = 0.32)
        
        # creates radio buttons for save options
        OPTIONS = [
            ("Save to new folder", 0),
            ("Save to existing folder and keep old files", 1),
            ("Overwrite existing files", 2)
        ]

        self.save_opt = tk.IntVar(self.save_btn_frame, 0)
        # save_opt.set("0")

        for text, number in OPTIONS:
            tk.Radiobutton(self.save_btn_frame,
                            bg=self.bg_color,
                            text=text, 
                            variable=self.save_opt, 
                            value=number).pack(anchor="w")


    # creates options for how to resize the files
    # bottom frame
    def resize_options(self):
        # creates frame for "select directory" button
        self.resize_frame = tk.Frame(self.root,
                                        bg=self.bg_color,
                                        height=220,
                                        width=585,
                                        bd=1,
                                        relief="raised")
        # Creates a frame with fixed sized (will not resize 3ith different number of widgets)
        # Fixed height and width must be entered (line above)
        self.resize_frame.grid_propagate(False)
        self.resize_frame.place(relx = 0.012,
                                rely = 0.44)
        
        self.resize_label = tk.Label(self.resize_frame,
                                        bg=self.bg_color,
                                        text="How do you want to resize?",
                                        font=("Helvetica 11 underline"))
        self.resize_label.place(relx = 0.35,
                                rely = 0.08)


        # creates frame within "self.resize_frame" for radio button with resize options
        self.resize_radio_frame = tk.Frame(self.resize_frame,
                                            bg=self.bg_color,
                                            height=100,
                                            width=300)
        self.resize_radio_frame.place(relx = 0.1,
                                        rely = 0.25)
        
        # creates radio buttons for save options
        OPTIONS = [
            ("new width (original aspect ratio):", 0),
            ("new height (original aspect ratio):", 1),
            ("percentage:", 2),
            ("new width and height:", 3),
        ]

        self.resize_opt = tk.IntVar(self.resize_radio_frame, 0)

        i = 0
        for text, number in OPTIONS:
            tk.Radiobutton(self.resize_radio_frame,
                            bg=self.bg_color,
                            padx=0,
                            pady=5,
                            text=text, 
                            variable=self.resize_opt,
                            command=self.radio_resize_click, 
                            value=number).grid(column=0, row=i, sticky="w")
            i += 1

        self.radio_resize_click()



        # # creates frame within "self.resize_frame" with input boxes for the different options
        # self.resize_input_frame = tk.Frame(self.resize_frame,
        #                                     bg=self.bg_color,
        #                                     height=155,
        #                                     width=200)
        # self.resize_input_frame.place(relx = 0.5,
        #                                 rely = 0.25)
        
        # # entry widget for width only
        # self.width_only = tk.Entry(self.resize_input_frame, 
        #                             bd=1,
        #                             width=10,
        #                             justify="center",
        #                             relief="raised")
        # self.width_only.grid(column=0, 
        #                      row=0, 
        #                      pady=7, 
        #                      sticky="e")

        # width_label = tk.Label(self.resize_input_frame, 
        #                        text="(number of pixels, i.e. 300)",
        #                        font=("Helvetica 9 italic"),
        #                        padx=7,
        #                        bg=self.bg_color)
        # width_label.grid(column=1, 
        #                  row=0,
        #                  sticky="w")

        # # entry widget for height only
        # self.height_only = tk.Entry(self.resize_input_frame, 
        #                             bd=1,
        #                             width=10,
        #                             justify="center",
        #                             relief="raised")
        # self.height_only.grid(column=0, row=1, pady=7, sticky="e")

        # height_label = tk.Label(self.resize_input_frame, 
        #                        text="(number of pixels, i.e. 300)",
        #                        font=("Helvetica 9 italic"),
        #                        padx=7,
        #                        bg=self.bg_color)
        # height_label.grid(column=1, 
        #                   row=1,
        #                   sticky="w")

        # # entry widget for percent
        # self.percent = tk.Entry(self.resize_input_frame, 
        #                             bd=1,
        #                             width=10,
        #                             justify="center",
        #                             relief="raised")
        # self.percent.grid(column=0, row=2, pady=7, sticky="e")   

        # percent_label = tk.Label(self.resize_input_frame, 
        #                         text="(i.e. 50 will be 50%)",
        #                         font=("Helvetica 9 italic"),
        #                         padx=7,
        #                         bg=self.bg_color)
        # percent_label.grid(column=1, 
        #                    row=2,
        #                    sticky="w")

        # # entry widget for custom width
        # self.custom_width = tk.Entry(self.resize_input_frame, 
        #                                 bd=1,
        #                                 width=10,
        #                                 justify="center",
        #                                 relief="raised")
        # self.custom_width.grid(column=0,
        #                         row=3, 
        #                         pady=7, 
        #                         sticky="e")

        # custom_width_label = tk.Label(self.resize_input_frame, 
        #                                 text="(width)",
        #                                 font=("Helvetica 9 italic"),
        #                                 padx=14,
        #                                 bg=self.bg_color)
        # custom_width_label.grid(column=0, 
        #                          row=4)        

        # # entry widget for custom height
        # self.custom_height = tk.Entry(self.resize_input_frame,
        #                                 bd=1,
        #                                 width=10,
        #                                 justify="center",
        #                                 relief="raised")
        # self.custom_height.grid(column=1,
        #                         row=3, 
        #                         pady=7, 
        #                         padx=10, 
        #                         sticky="w")

        # custom_height_label = tk.Label(self.resize_input_frame, 
        #                                 text="(height)",
        #                                 font=("Helvetica 9 italic"),
        #                                 bg=self.bg_color)
        # custom_height_label.grid(column=1, 
        #                          row=4,
        #                          padx=14,
        #                          sticky="w")


    def radio_resize_click(self):
        # self.user_resize = self.resize_opt.get()
        # if self.user_resize == 0:
        #     pass
        # elif self.user_resize == 1:
        #     pass
        # elif self.user_resize == 2:
        #     pass
        # elif self.user_resize == 3:
        #     pass


        # creates frame within "self.resize_frame" with input boxes for the different options
        self.resize_input_frame = tk.Frame(self.resize_frame,
                                            bg=self.bg_color,
                                            height=155,
                                            width=200)
        self.resize_input_frame.place(relx = 0.5,
                                        rely = 0.25)
        
        # entry widget for width only
        self.width_only = tk.Entry(self.resize_input_frame, 
                                    bd=1,
                                    width=10,
                                    justify="center",
                                    relief="raised")
        self.width_only.grid(column=0, 
                             row=0, 
                             pady=7, 
                             sticky="e")

        width_label = tk.Label(self.resize_input_frame, 
                               text="(number of pixels, i.e. 300)",
                               font=("Helvetica 9 italic"),
                               padx=7,
                               bg=self.bg_color)
        width_label.grid(column=1, 
                         row=0,
                         sticky="w")

        # entry widget for height only
        self.height_only = tk.Entry(self.resize_input_frame, 
                                    bd=1,
                                    width=10,
                                    justify="center",
                                    relief="raised")
        self.height_only.grid(column=0, row=1, pady=7, sticky="e")

        height_label = tk.Label(self.resize_input_frame, 
                               text="(number of pixels, i.e. 300)",
                               font=("Helvetica 9 italic"),
                               padx=7,
                               bg=self.bg_color)
        height_label.grid(column=1, 
                          row=1,
                          sticky="w")

        # entry widget for percent
        self.percent = tk.Entry(self.resize_input_frame, 
                                    bd=1,
                                    width=10,
                                    justify="center",
                                    relief="raised")
        self.percent.grid(column=0, row=2, pady=7, sticky="e")   

        percent_label = tk.Label(self.resize_input_frame, 
                                text="(i.e. 50 will be 50%)",
                                font=("Helvetica 9 italic"),
                                padx=7,
                                bg=self.bg_color)
        percent_label.grid(column=1, 
                           row=2,
                           sticky="w")

        # entry widget for custom width
        self.custom_width = tk.Entry(self.resize_input_frame, 
                                        bd=1,
                                        width=10,
                                        justify="center",
                                        relief="raised")
        self.custom_width.grid(column=0,
                                row=3, 
                                pady=7, 
                                sticky="e")

        custom_width_label = tk.Label(self.resize_input_frame, 
                                        text="(width)",
                                        font=("Helvetica 9 italic"),
                                        padx=14,
                                        bg=self.bg_color)
        custom_width_label.grid(column=0, 
                                 row=4)        

        # entry widget for custom height
        self.custom_height = tk.Entry(self.resize_input_frame,
                                        bd=1,
                                        width=10,
                                        justify="center",
                                        relief="raised")
        self.custom_height.grid(column=1,
                                row=3, 
                                pady=7, 
                                padx=10, 
                                sticky="w")

        custom_height_label = tk.Label(self.resize_input_frame, 
                                        text="(height)",
                                        font=("Helvetica 9 italic"),
                                        bg=self.bg_color)
        custom_height_label.grid(column=1, 
                                 row=4,
                                 padx=14,
                                 sticky="w")


                       
            

    # button at bottom of window to run program
    def run_btn(self):
        self.run_btn = tk.Button(self.root,
                                   text="resize images",
                                   height=1,
                                   width=20,
                                   bg="#BDFFFC",
                                   font=('Helvetica 12'),
                                   command=self.check_dir_resize)
        self.run_btn.place(relx = 0.5,
                                rely = 0.94,
                                anchor = "center")
    

    # runs program after resize button has been clicked
    def check_dir_resize(self):
        # # called by radio_resize_click
        # self.user_resize = self.resize_opt.get()

        # print(f"self.user_resize = {self.user_resize}")
        # print(type(self.user_resize))

        if not self.filepath:
            print("338, self.filepath must be selected")
        
        # if "width only" selected
        elif self.user_resize == 0:
            print("342, resize == 0")
            try:
                self.new_width = int(self.width_only.get())

                if self.new_width < 10 or self.new_width > 3000:
                    raise ValueError
                
                self.check_save_opt()
                
            except ValueError:
                print("352, width value error")
                # self.new_width = int(self.width_only.get())
                # print(f"self.new_width = {self.new_width}")
                # print(type(self.new_width))

                # TODO 
                # pop up window for error

        # if "height only" selected
        elif self.user_resize == 1:
            print("362, resize == 1")
            try:
                self.new_height = int(self.height_only.get())

                # check to see that legitimate values entered
                if self.new_height < 10 or self.new_height > 3000:
                    raise ValueError
                
                self.check_save_opt()

            except ValueError:
                print("373, height value error")
                # TODO
                # pop up window for error

        # if user chose percentage
        elif self.user_resize == 2:
            print("379, resize == 2")
            try:
                self.new_percent = float(self.percent.get())

                # check to see what legitimate value was entered
                if self.new_percent < 1 or self.new_percent > 300:
                    raise ValueError

                self.check_save_opt()
                
            except ValueError:
                print("384, percentage error")
                # TODO
                # pop up window for error

        elif self.user_resize == 3:
            print("395 resize == 3")
            try:
                self.new_width = int(self.custom_width.get())
                self.new_height = int(self.custom_height.get())

                # check to see legitimate values were entered
                if self.new_width < 1:
                    raise ValueError
                if self.new_height < 1:
                    raise ValueError
                
                self.check_save_opt()
                
            except ValueError:
                print("409, height and width error")
                # TODO
                # pop up window for error       


    # checks which save option was chosen
    def check_save_opt(self):

        # get the option for saving selected by user
        user_save = self.save_opt.get()

        # # creates new file path where resized image will be saved
        # self.new_path = os.path.join(self.filepath, self.new_dir_name)
        # print(f"user_save = {user_save}")
        # print(type(user_save))
        # print()

        # "save to new folder" chosen
        if user_save == 0:
            try:
                self.new_path = os.path.join(self.filepath, self.new_dir_name)
                os.mkdir(self.new_path)
            except FileExistsError:
                pass
            self.check_double_bool = True

        # "Save to existing folder and keep old files" chosen
        elif user_save == 1:
            self.new_path = self.filepath
            self.check_double_bool = True

        # "Overwrite existing files" chosen
        elif user_save == 2:
            self.new_path = self.filepath
            self.check_double_bool = False

        self.resize_images()


    # method that actually resizes and sacves the images
    def resize_images(self):

        # keeps track of how many files resized and skipped
        self.change_counter = 0
        self.skipped_counter = 0
    
        # Images get open, resized, and saved
        for file in os.listdir(self.filepath):
            if file.endswith(('jpeg', 'png', 'jpg')):
                self.change_counter += 1

                # used to open file and determine height and width
                f_img = self.filepath+"/"+file
                img = Image.open(f_img)
                img_width, img_height = img.size

                # if "width only" is chosen
                if self.user_resize == 0:
                    print("467, resize_opt == 0")
                    self.new_height = int((img_height * self.new_width) / img_width)

                # if "height only" is chosen
                elif self.user_resize == 1:
                    print("472, resize_opt == 1")
                    self.new_width = int((img_width * self.new_height) / img_height)

                # if percent is chosen
                elif self.user_resize == 2:
                    print("477, resize_opt == 2")
                    self.new_width = int(img_width * (self.new_percent / 100))
                    self.new_height = int(img_height * (self.new_percent / 100))

                # # if new height and new width chosen
                # # (not needed because width and height already defined by user)
                # elif self.user_resize == 3:
                #     pass
                

                print(f"487, self.new_width = {self.new_width}")
                print(f"\tself.new_height = {self.new_height}")
                # stores resized image in variable
                img = img.resize((self.new_width, self.new_height))

                if self.check_double_bool:
                    new_file_path = self.check_double(file)
                else:
                    new_file_path = self.new_path+"/"+file 


                # from resize.cli / / / // / / / ////////////////////
                # save_location = self.new_path+"/"+file
                # save_location = check_dbl(path_new, directory, file)
                # img = Image.open(f_img)
                # width, height = img.size
                # img = img.resize((int(width * PERCENT), int(height * PERCENT)))
                
                # print(f"save_location = {save_location}")
                img.save(new_file_path)

            else:
                self.skipped_counter += 1


    # checks the new directory if a file with the same name already exists
    # file1 is the name of the file
    # "double_counter" is the end number for the new file
    def check_double(self, file1, double_counter=""): 

        # for first call of function
        if not double_counter:
            # Checks if file with same name exists in the new directory
            new_file = self.new_path+"/"+file1
            if os.path.exists(new_file):
                double_counter = 1
                new_file = self.check_double(file1, double_counter)
            # if file with the same name does not exist in the directory
            return new_file
            
        # for every call after the first     
        else:
            print(f"530, double_counter = {double_counter}")
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
            new_file = self.new_path+"/"+numbered_file

            print(f"numbered_file = {numbered_file}")
            print(f"new_file = {new_file}")
            print(f"file1 = {file1}")
            
            if os.path.exists(new_file):
                double_counter += 1
                new_file = self.check_double(file1, double_counter)
            
            return new_file


def main():
    gui = Window()
    gui.root.mainloop()


if __name__=="__main__":
    main()
