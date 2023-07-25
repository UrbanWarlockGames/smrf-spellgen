import os
import random
import tkinter as tk
import tkinterhtml as tkhtml

# Get the directory path of the script
dir_path = os.path.dirname(os.path.abspath(__file__))

def read_words_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        words = file.readlines()
    return [word.strip() for word in words]

def generate_spell(targets, verbs, adverbs, adjectives, magnitude, elements, blasttypes):
    random_choice = random.random()  # Generate a random number between 0 and 1

    if random_choice < 0.5:  # 50% chance for this category
        sub_random_choice = random.random()  # Another random choice within this category

        if sub_random_choice < 0.05:  # 5% chance for magnitude + verb + targets
            random_word = f"{random.choice(magnitude)} {random.choice(verbs).capitalize()} {random.choice(targets)}"
        elif sub_random_choice < 0.40:  # 35% chance for verb + targets
            random_word = f"{random.choice(verbs).capitalize()} {random.choice(targets)}"
        elif sub_random_choice < 0.70:  # 30% chance for adverbs + targets
            random_word = f"{random.choice(adverbs).capitalize()} {random.choice(targets)}"
        else:  # 30% chance for adjectives + targets
            random_word = f"{random.choice(adjectives).capitalize()} {random.choice(targets)}"
    else:  # 50% chance for this category
        sub_random_choice = random.random()  # Another random choice within this category

        if sub_random_choice < 0.25:  # 25% chance for element + blasttype
            random_word = f"{random.choice(elements)} {random.choice(blasttypes)}"
        else:  # 25% chance for adverbs + nouns
            random_word = f"{random.choice(adverbs).capitalize()} {random.choice(targets)}"

    return random_word

def generate_spells(num_results):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    targets_file_path = os.path.join(script_dir, 'targets.txt')
    adjectives_file_path = os.path.join(script_dir, 'adjectives.txt')
    adverbs_file_path = os.path.join(script_dir, 'adverbs.txt')
    verbs_file_path = os.path.join(script_dir, 'verb.txt')
    magnitude_file_path = os.path.join(script_dir, 'magnitude.txt')
    elements_file_path = os.path.join(script_dir, 'elements.txt')
    blasttypes_file_path = os.path.join(script_dir, 'blasttypes.txt')

    # Read words from the files
    targets = read_words_from_file(targets_file_path)
    adjectives = read_words_from_file(adjectives_file_path)
    adverbs = read_words_from_file(adverbs_file_path)
    verbs = read_words_from_file(verbs_file_path)
    magnitude = read_words_from_file(magnitude_file_path)
    elements = read_words_from_file(elements_file_path)
    blasttypes = read_words_from_file(blasttypes_file_path)

    spells = []
    for _ in range(num_results):
        spell = generate_spell(targets, verbs, adverbs, adjectives, magnitude, elements, blasttypes)
        spells.append(spell)
    return spells

# Create a Tkinter window
window = tk.Tk()
window.title("Spell Generator")

# Set the window icon
icon_path = os.path.join(dir_path, "smrf.ico")
window.iconbitmap(icon_path)

# Variable to store the dark mode state
dark_mode = tk.IntVar(value=1)  # Set initial value to 1 for dark mode

# Create a Tkinter Text widget to display the generated spells
text_widget = tk.Text(window, height=15, width=30)
text_widget.grid(row=0, column=0, columnspan=2, sticky=tk.NSEW)  # Grid placement with sticky option

# Create a Tkinter Label and Entry for user input
result_label = tk.Label(window, text="Number of Spells:")
result_label.grid(row=1, column=0, sticky=tk.E)  # Grid placement with sticky option

result_entry = tk.Entry(window)
result_entry.grid(row=1, column=1, sticky=tk.W)  # Grid placement with sticky option
result_entry.insert(tk.END, "100")  # Set the default value to 100

# Create a Tkinter Scrollbar
scrollbar = tk.Scrollbar(window)
scrollbar.grid(row=0, column=2, sticky=tk.NS)  # Grid placement with sticky option

# Configure the Scrollbar to work with the Text widget
scrollbar.config(command=text_widget.yview)
text_widget.config(yscrollcommand=scrollbar.set)

# Function to open the URL in a web browser
def open_url(event):
    import webbrowser
    webbrowser.open("https://spoiledmeat.fandom.com/wiki/Spoiled_Meat,_Rotten_Flesh_Wiki")

# Function to handle mouse clicks in the Text widget
def text_widget_click(event):
    index = text_widget.index("@%s,%s" % (event.x, event.y))
    tags = text_widget.tag_names(index)
    if "url" in tags:
        open_url(event)

# Function to handle cursor entering the URL
def text_widget_enter(event):
    index = text_widget.index("@%s,%s" % (event.x, event.y))
    tags = text_widget.tag_names(index)
    if "url" in tags:
        text_widget.config(cursor="hand2")

# Function to handle cursor leaving the URL
def text_widget_leave(event):
    text_widget.config(cursor="")

# Function to generate names based on user input
def generate_names():
    text_widget.delete(1.0, tk.END)  # Clear the text widget
    num_results = result_entry.get()  # Get the user-specified number of results
    
    # Check if the user input is "credits"
    if num_results.lower() == "credits":
        # Display the credits sequence with ASCII art
        ascii_art = r'''
                                                                                                                                                           
                                               *@@@(                                                                                                       
      /%%@@@@@@@@.                             .,,,..%%%%%,            /&@@@@%%*               .(@@@@@&,    /@@@@&,                            &@@@.       
     %@@@,   ,*** .(@@@@@@@@@@&/ ##&@/*#@@@&( #@@##*  %@@@,*##@#**&@@@,*##@#(@@@@@@&/           *@@@@@@%/  #@@@@@&  *##@#**&@@@, ,@@#**&&/  .**&@@@/.      
     *%@@@%(((((((,*@@@@@. *@@@@@@@%*   .@@@@#&@@@@(  %@@@,/@@@(   ,//.(@@@/  &@@@@@#           *@@@@@@@&#@@%(@@@&  /@@@(   ,//.   /(((@@&(.   &@@@.       
     *///.   /&@@@/*@@@@@. *@@@@@@@%*   .@@@& #@@@@(  %@@@,/@@@@&(((/  (@@@/  &@@@@@#           *@@@# (&@@@%*.@@@&  /@@@@@(((/  ,(@@/.(@@@@,   &@@@.       
     %@@@@#***%@#. *@@@@@/%@@%,  (&@@@(*/@%#( #@@@@(  /&@@, .#@@@@(***  .#@@@@@@@##,           ,(@@@#  /###,./@@@&*. .#@@@@(*** (@@@#**&@@@@/  &@@@/.      
                   *@@@#                                                                                                                                   
                                                                                                                                                           
                                                                                                                                                           
         #&&&&&&%.                  .%&&#     (&&&,                                        /&&&&&&&&&&&,                             ,&&&&%.               
      (@@@@&*&@@@@/    ,#######/  /#%@@@@%,,##@@@@%*   *#######*.#####.   (####*            *@@@@@**(@@*./@@@&   .#######(  *#######*  %@@@%#####/         
      (@@@/  &@@@. .#@@@@. ./@@@&.  .@@@&     #@@@* ,@@@%  ,(@@(  %@@@@%/  (@@@/            *@@@@@#(*    .@@@& #@@@*  /&@% %@@@, .//,  %@@@@#//&@@@.       
      (@@@/,@@@&/  *@@@#    .&@@@(, .@@@&     #@@@* ,@@@&/////.   %@@@#%@@(%@@@/            *@@@@&.*(/   .@@@& #@@@#////,  *(((((#@@@% %@@@@/  &@@@.       
      (@@@#, &@@@/.,#@@@@/. .&@@&.  .@@@&     #@@@* .#@@@@(.      %@@@, .##&@@@/            *@@@@&.      .@@@& /&@@@%,     %@&*. ,@@&/ %@@@@/.*&@#         
      *%%%%(  /%%%%(  /%%%%%%%,     .#%%%%,   (%%%%/   *%%%%%%%*  (%%%.    /%%%*            ,%%%%#         (%#   .%%%%%%%( (%%%%%%%.   (%%%. *@@&(         
                                                                                                                                            /&&.           
                                                                                                                                                           
'''
        # Get the width of the text widget
        widget_width = text_widget.winfo_width()

        # Calculate the scaling factor based on the desired width
        scaling_factor = widget_width / 80  # Assuming the original ASCII art has a width of 80 characters

        # Scale the ASCII art based on the scaling factor
        scaled_ascii_art = ""
        for line in ascii_art.splitlines():
            scaled_line = line * int(scaling_factor)
            scaled_ascii_art += line * int(scaling_factor) + "\n"
            centered_line = scaled_line.center(widget_width)  # Center the line based on the text widget width
            scaled_ascii_art += centered_line + "\n"
        text_widget.insert(tk.END, ascii_art + "\n\n")
        text_widget.tag_configure("center", justify="center")
        text_widget.insert(tk.END, "Thanks for trying this program out!\n\n", "center")
        text_widget.insert(tk.END, "Feel free to share, modify, and use it however you wish.\n\n", "center")
        text_widget.insert(tk.END, "You can follow the progress of SMRF at the following link:\n", "center")
        
        # Insert the clickable and styled URL
        url = "https://spoiledmeat.fandom.com/wiki/Spoiled_Meat,_Rotten_Flesh_Wiki"
        text_widget.insert(tk.END, url, "url")
        text_widget.tag_configure("url", underline=True)
        text_widget.tag_add("center", "url.first", "url.last")
        text_widget.tag_configure("center", justify="center")

        text_widget.insert(tk.END, "\n\nCreated by Lucia Chaisson", "center")
        text_widget.insert(tk.END, "\n\nDedicated to: Allister, Christen, Karson, and Kevin", "center")

    elif num_results == "69":  # Check if the number is 69
        # Display the special message for the number 69
        text_widget.insert(tk.END, "Nice!\n")
        text_widget.insert(tk.END, "69 is a magical number in this realm.\n")
        text_widget.insert(tk.END, "May the gods be with you!\n")
        text_widget.insert(tk.END, "---------------------------\n")

        # Generate spells as usual
        try:
            num_results = int(num_results)
            spells = generate_spells(num_results)
            for spell in spells:
                text_widget.insert(tk.END, spell + "\n")
        except ValueError:
            # Invalid input, show an error message
            text_widget.insert(tk.END, "Invalid input. Please enter a valid number.")
    else:
        # Generate spells as usual for any other input
        try:
            num_results = int(num_results)
            spells = generate_spells(num_results)
            for spell in spells:
                text_widget.insert(tk.END, spell + "\n")
        except ValueError:
            # Invalid input, show an error message
            text_widget.insert(tk.END, "Invalid input. Please enter a valid number.")

# Create a Tkinter button to generate spells
generate_button = tk.Button(window, text="Generate Spells", command=generate_names)
generate_button.grid(row=2, column=0, columnspan=2, sticky=tk.NSEW)  # Grid placement with sticky option
text_widget.bind("<Button-1>", text_widget_click)  # Bind mouse click event to the Text widget
text_widget.tag_bind("url", "<Enter>", text_widget_enter)  # Bind mouse enter event to the URL tag
text_widget.tag_bind("url", "<Leave>", text_widget_leave)  # Bind mouse leave event to the URL tag

# Create a Tkinter Scrollbar
scrollbar = tk.Scrollbar(window)
scrollbar.grid(row=0, column=2, sticky=tk.NS)  # Grid placement with sticky option

# Configure the Scrollbar to work with the Text widget
scrollbar.config(command=text_widget.yview)
text_widget.config(yscrollcommand=scrollbar.set)

# Function to toggle dark mode
def toggle_dark_mode():
    if dark_mode.get() == 1:
        window.config(bg="#333333")  # Set background color
        text_widget.config(bg="#111111", fg="#ffffff")  # Set text widget colors
        generate_button.config(bg="#444444", fg="#ffffff")  # Set generate button colors
        result_label.config(bg="#333333", fg="#ffffff")  # Set label colors
        result_entry.config(bg="#555555", fg="#ffffff")  # Set entry field colors
        dark_mode_button.config(bg="#333333", fg="#ffffff", selectcolor="#333333")  # Set dark mode button colors
    else:
        window.config(bg="white")  # Set background color
        text_widget.config(bg="white", fg="black")  # Set text widget colors
        generate_button.config(bg="lightgray", fg="black")  # Set generate button colors
        result_label.config(bg="white", fg="black")  # Set label colors
        result_entry.config(bg="white", fg="black")  # Set entry field colors
        dark_mode_button.config(bg="white", fg="black", selectcolor="white")  # Set dark mode button colors

# Create a checkmark button for dark mode
dark_mode_button = tk.Checkbutton(window, text="Dark Mode", variable=dark_mode, command=toggle_dark_mode)
dark_mode_button.grid(row=3, column=1, sticky=tk.SE)  # Grid placement with sticky option

# Configure row and column weights to maintain size and placement
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

# Call the toggle_dark_mode() function to set the GUI to dark mode initially
toggle_dark_mode()

# Set the window state to maximized
window.state('zoomed')

# Start the Tkinter event loop
window.mainloop()