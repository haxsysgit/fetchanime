import tkinter as tk
from fetchanime import searcharg # Assuming fetchanime.py contains your command-line functions

# Function to handle button click event
def search_anime():
    keyword = entry_keyword.get()
    results = searcharg(keyword)
    # Display the results in a text area or any other GUI component

# Create the main window
window = tk.Tk()
window.title("GetAnime GUI")

# Create a label and entry for user input
label_keyword = tk.Label(window, text="Enter keyword:")
label_keyword.pack()
entry_keyword = tk.Entry(window)
entry_keyword.pack()

# Create a button to trigger the search
button_search = tk.Button(window, text="Search", command=search_anime)
button_search.pack()

# Run the main event loop
window.mainloop()
