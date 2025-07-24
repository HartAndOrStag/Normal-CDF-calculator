import normalCDF
import tkinter

def calculate():
    noX = False
    noMu = False
    noSigma = False

    # there is no default x value, an x value must be entered by user
    try:
        x = float(entry_x.get())
    except Exception as exc:
        noX = True

    # if no mu is entered, defaults to 0
    try:
        mu = float(entry_mu.get())
    except Exception as exc:
        mu = 0
        noMu = True
    
    # if no sigma is entered, defaults to 1
    try:
      sigma = float(entry_sigma.get())
    except Exception as exc:
       sigma = 1
       noSigma = True 

    # if no k is entered, defaults to 100
    try:
        k_max = int(entry_kmax.get())
    except Exception as exc:
        k_max = 100
     
    # if no precision is entered, defaults to 100   
    try:
        precision = int(entry_precision.get())
    except Exception as exc:
        precision = 100    
    
    # if no rounding is entered, defaults to 4
    try:
        rounding = int(entry_rounding.get())
    except Exception as exc:
        rounding = 4    

    # ensure it is rounded only to the number of decimal places tracked
    if rounding > precision:
        rounding = precision

    # x must be entered by user
    if noX:
        result_label.config(text="Please enter value for x.")
    # either both mu and sigma must be entered or neither
    elif (noMu and not noSigma) or (noSigma and not noMu):
        result_label.config(text="Please enter values for μ and σ (or leave blank for default 0 and 1).")
    # rounding must be positive integer
    elif rounding < 0:
        result_label.config(text="Error! Ensure all values entered are valid.")
    # final try to excecute function and print result to result label, otherwise show generic error
    else:
        try:
            result = round(normalCDF.Phi(x, mu, sigma, k_max, precision), rounding)
            result_label.config(text=f"Result: {result}")
        except Exception as exc:
            result_label.config(text="Error! Ensure all values entered are valid.")
            

# for GUI

# title window  
root = tkinter.Tk()
root.title("Normal CDF Calculator")

# configure 8 rows (wieght controls how window size affects proportions)
for i in range(6): 
    root.grid_rowconfigure(i, weight=2)

root.grid_rowconfigure(6, weight=1)
root.grid_rowconfigure(7, weight=1)

# configure 2 columns
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=4)

# make entries for each value

# add text label
tkinter.Label(root, text="x:").grid(row=0, column=0)
# add entry 
entry_x = tkinter.Entry(root)
# columnspan=2 means it extends across two columns, sticky=nsew means it expands in all north, south, east, west directions
entry_x.grid(row=0, column=1, columnspan=2, sticky="nsew")

# and so on
tkinter.Label(root, text="μ:").grid(row=1, column=0)
entry_mu = tkinter.Entry(root)
entry_mu.grid(row=1, column=1, columnspan=2, sticky="nsew")

tkinter.Label(root, text="σ:").grid(row=2, column=0)
entry_sigma = tkinter.Entry(root)
entry_sigma.grid(row=2, column=1, columnspan=2, sticky="nsew")

tkinter.Label(root, text="k (Iterations):").grid(row=3, column=0)
entry_kmax = tkinter.Entry(root)
entry_kmax.grid(row=3, column=1, columnspan=2, sticky="nsew")

tkinter.Label(root, text="Tracked Decimal Places:").grid(row=4, column=0)
entry_precision = tkinter.Entry(root)
entry_precision.grid(row=4, column=1, columnspan=2, sticky="nsew")

tkinter.Label(root, text="Rounding (Decimal Places):").grid(row=5, column=0)
entry_rounding = tkinter.Entry(root)
entry_rounding.grid(row=5, column=1, columnspan=2, sticky="nsew")

# add button when clicked, calculate() gets called
calculate_button = tkinter.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=6, columnspan=2)

# add result text
result_label = tkinter.Label(root, text="Result: ")
result_label.grid(row=7, columnspan=2)

# run GUI loop
root.mainloop()