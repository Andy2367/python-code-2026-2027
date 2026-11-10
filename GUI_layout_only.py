import tkinter as tk

main= tk.Tk()

main.geometry("250x300")  # sets the main window size
selected_events = tk.Button(text="Selected Events", bg="grey")  # creates the selected events btn which will automaticly filter the results to show only the currently selected events.
selected_events.place(relx= 0.05, rely= 0.05)

filter_btn = tk.Button(text="     Filter     ", bg="grey")  # creates the filter btn which will (currently does not) creat a new window with the filtering options.
filter_btn.place(relx= 0.6, rely= 0.05)

scrollwindow= tk.Canvas(main, bg="light grey")      # creates a canvas which will be used to allow scrolling
scrollwindow.place(relwidth=0.9, relheight=0.75, relx = 0.05, rely=0.2)

scrolbar = tk.Scrollbar(main, orient="vertical", command=scrollwindow.yview) # creates the scrollbar widget on the window
scrolbar.place(relheight=0.75, relwidth=0.1, relx=0.9, rely= 0.2)

scrollwindow.configure(yscrollcommand=scrolbar.set) # sets the position of the slider

frame = tk.Frame(scrollwindow, bg="light grey")      # creates a frame which is the same size as the scrollwindow canvas to allow the addition of widgets to it
scrollwindow.create_window((0, 0), window=frame, anchor="nw")

frame.bind(
    "<Configure>",
    lambda e: scrollwindow.configure(scrollregion=scrollwindow.bbox("all")) # sets the area that can be scrolled to the entire scroll window canvas
)

for i in range(30):
    tk.Button(frame, text=f"Event{i+1}", width=20).pack(pady=5, padx=30,)

main.mainloop() # opens the window and starts the loop to keep it open.