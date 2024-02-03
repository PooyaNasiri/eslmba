import tkinter as tk

# make exe file: pyinstaller --onefile --noconsole --icon=milk.ico .\ESLMBA.py


def calculate_sum():
    try:
        num1 = float(entries[0].get())
        num2 = float(entries[1].get())
        num3 = float(entries[2].get())/100
        num4 = float(entries[3].get())
        num5 = float(entries[4].get())/100
        num6 = float(entries[5].get())/100
        num7 = float(entries[6].get())
        num8 = float(entries[7].get())
        num9 = float(entries[8].get())/100
        num10 = float(entries[9].get())
        num11 = float(entries[10].get())


        kgbottle = num2/1000
        AbttlePlasticgr = num2-(num3*num2)
        rPETgr = AbttlePlasticgr*num6
        PETgr = AbttlePlasticgr-rPETgr
        output0 = (num4*num3*kgbottle)+(num8*(PETgr/1000))+(num7*(rPETgr/1000))
        #abw = num1 * num2  # Annual Bottle Weight in kg
        #rpetaw = abw*num7  # rPET-O annual weight in kg
        #petaw = abw*num9  # vPET annual weight in kg
        output1 = (num5 + num9)*100
        output2 = 20000
        output3 = 0.45 * (PETgr/1000)*num1
        output4 = 208.7733333-(16.76*((1-num3)*num6))
        output5 = ((num10*output4)/num11)*num1
        output6 = ((PETgr/1000)*num1*2.15)+((rPETgr/1000)*num1*0.3827)
        output7 = ((PETgr/1000)*num1*2.15)+((rPETgr/1000)*num1*1.075)
        output8 = (output6+output7)/2
        output9 = ((PETgr/1000)*num1*83.8)+((rPETgr/1000)*num1*41.9)
        output10 =((PETgr/1000)*num1*83.8)+((rPETgr/1000)*num1*17.598)
        output11 = (output9+output10)/2
        output12 = ((PETgr/1000)*num1*233.68)+((rPETgr/1000)*num1*23.368)
        output13 = (output0*num1)+output3-output2+output5

        floating = "{:.2f}"
        outputs[0].config(text=floating.format(output0))
        outputs[1].config(text=floating.format(output1))
        outputs[2].config(text=floating.format(output2))
        outputs[3].config(text=floating.format(output3))
        outputs[4].config(text=floating.format(output4))
        outputs[5].config(text=floating.format(output5))
        outputs[6].config(text=floating.format(output6))
        outputs[7].config(text=floating.format(output7))
        outputs[8].config(text=floating.format(output8))
        outputs[9].config(text=floating.format(output9))
        outputs[10].config(text=floating.format(output10))
        outputs[11].config(text=floating.format(output11))
        outputs[12].config(text=floating.format(output12))
        outputs[13].config(text=floating.format(output13))

    except ValueError:
        for i in range(len(outputs)):
            outputs[i].config(text="Invalid input")


def validate_float(value):
    try:
        if value == "":
            return True
        float(value)
        return True
    except ValueError:
        return False


def validate_percent(value):
    try:
        if value == "":
            return True
        float(value)
        if float(value) > 100.0:
            return False
        return True
    except ValueError:
        return False


# Create the main window
root = tk.Tk()
root.title("ESL Milk Bottle Analyser")
root.geometry("1100x550")
root.resizable(width=False, height=False)
# root.iconbitmap('milk.ico')
# root.iconbitmap(default='')
# icon = tk.PhotoImage(file='milk.ico')z
# root.iconphoto(False, 'milk.ico')
# root.config(bg="lightblue")
# image = tk.PhotoImage(file="Screenshot 2024-01-01 184932.png")
# label = tk.Label(root, image=image)
# label.place(x=0, y=0, relwidth=1, relheight=1)

labels_input = []
label_texts_input = ["Bottles Produced", "Bottle Weight",
                     "Masterbatch Content", "Masterbatch Price", "Masterbatch's Titanium Dioxide Content", "rPET-O Content", "rPET-O Price", 
                     "Virgin PET Price", "rPET-O's Titanium Dioxide Risidual", "Electricity Price", "ISBM Machine Production Capacity"]

labels_output = []
label_texts_output = ["Cost of a Bottle", "Total Titanium Dioxide Content", "Tax Credit Value", "Plastic Tax",
                      "Blow Molding Energy Consumption", "Blow Molding Energy Cost", "Minimum Carbon Dioxide Emission",
                      "Maximum Carbon Dioxide Emission", "Average Carbon Dioxide Emission",
                      "Minimum Energy Consumption", "Maximum Energy Consumption",
                      "Average Energy Consumption", "Water Consumption", "Total Cost"]

entries = []

for i in range(len(label_texts_input)):
    label = tk.Label(root, text=str(i+1) + ") " + label_texts_input[i])
    label.grid(row=i, column=0, padx=5, pady=5, sticky='w')
    labels_input.append(label)
    entry = tk.Entry(root, width=10, validate="key",
                     validatecommand=(root.register(validate_float), "%P"))
    entry.grid(row=i, column=1, padx=5, pady=5, sticky='w')
    entries.append(entry)
    entries[i].insert(0, "0")

tk.Label(root, text="number/year").grid(row=0,
                                        column=2, padx=5, pady=5, sticky='w')
tk.Label(root, text="g").grid(row=1, column=2, padx=5, pady=5, sticky='w')
tk.Label(root, text="%/total bottle weight").grid(row=2, column=2, padx=5, pady=5, sticky='w')
tk.Label(root, text="€/kg").grid(row=3, column=2, padx=5, pady=5, sticky='w')
tk.Label(root, text="%/total bottle weight").grid(row=4, column=2, padx=5, pady=5, sticky='w')
tk.Label(root, text="%/total PET weight").grid(row=5, column=2, padx=5, pady=5, sticky='w')
tk.Label(root, text="€/kg").grid(row=6, column=2, padx=5, pady=5, sticky='w')
tk.Label(root, text="€/kg").grid(row=7, column=2, padx=5, pady=5, sticky='w')
tk.Label(root, text="%/total bottle weight").grid(row=8, column=2, padx=5, pady=5, sticky='w')
tk.Label(root, text="€/kWh").grid(row=9, column=2, padx=5, pady=5, sticky='w')
tk.Label(root, text="bottle/hour").grid(row=10,
                                        column=2, padx=5, pady=5, sticky='w')

outputs = []
for i in range(len(label_texts_output)):
    labels_output.append(
        tk.Label(root, text="\t\t"+str(i+1) + ") "+label_texts_output[i]+":"))
    labels_output[i].grid(row=i, column=3, padx=5, pady=5, sticky='w')
    outputs.append(tk.Label(root, text="0"))
    outputs[i].grid(row=i, column=4, padx=5, pady=5, sticky='w')

tk.Label(root, text="€/bottle").grid(row=0,
                                     column=5, padx=5, pady=5, sticky='w')
tk.Label(root, text="%/bottle").grid(row=1,
                                     column=5, padx=5, pady=5, sticky='w')
tk.Label(root, text="€/year").grid(row=2, column=5, padx=5, pady=5, sticky='w')
tk.Label(root, text="€/year").grid(row=3, column=5, padx=5, pady=5, sticky='w')
tk.Label(root, text="kWh").grid(row=4,
                                     column=5, padx=5, pady=5, sticky='w')
tk.Label(root, text="€/year").grid(row=5, column=5, padx=5, pady=5, sticky='w')
tk.Label(root, text="kg CO2/PET kg/year").grid(row=6,
                                               column=5, padx=5, pady=5, sticky='w')
tk.Label(root, text="kg CO2/PET kg/year").grid(row=7,
                                               column=5, padx=5, pady=5, sticky='w')
tk.Label(root, text="kg CO2/PET kg/year").grid(row=8,
                                               column=5, padx=5, pady=5, sticky='w')
tk.Label(root, text="MJ/PET kg/year").grid(row=9,
                                           column=5, padx=5, pady=5, sticky='w')
tk.Label(root, text="MJ/PET kg/year").grid(row=10,
                                           column=5, padx=5, pady=5, sticky='w')
tk.Label(root, text="MJ/PET kg/year").grid(row=11,
                                           column=5, padx=5, pady=5, sticky='w')
tk.Label(root, text="L/PET kg/year").grid(row=12,
                                          column=5, padx=5, pady=5, sticky='w')
tk.Label(root, text="€/Year").grid(row=13,
                                   column=5, padx=5, pady=5, sticky='w')

# Apply validation to only some of the entries
entries[2].config(validatecommand=(root.register(validate_percent), "%P"))
entries[4].config(validatecommand=(root.register(validate_percent), "%P"))
entries[6].config(validatecommand=(root.register(validate_percent), "%P"))
entries[9].config(validatecommand=(root.register(validate_percent), "%P"))


# Create a button to calculate the sum
root.grid_rowconfigure(30, weight=1)
calculate_button = tk.Button(
    root, text="\tCalculate\t", command=calculate_sum).grid(row=30, column=0, padx=5)


# Start the main loop
root.mainloop()
