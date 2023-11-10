import tkinter

root = tkinter.Tk()
root.title("BODY MASS INDEX CALCI")

#Creating Function
def calculate_bmi():
    kg = float(entry_Kilogram.get())
    height = float(entry_Height.get())
    bmi = kg / (height ** 2)
    label_result['text'] = f"BMI: {bmi}"




#Creating GUI
label_Kilogram = tkinter.Label(root, text="KG: ")
label_Kilogram.grid(column=0, row=0)

entry_Kilogram = tkinter.Entry(root)
entry_Kilogram.grid(column=1, row=0)

label_Height = tkinter.Label(root, text="HEIGHT: ")
label_Height.grid(column=0, row=1)

entry_Height = tkinter.Entry(root)
entry_Height.grid(column=1, row=1)

button_Calculate = tkinter.Button(root, text = "Calculate", command=calculate_bmi)
button_Calculate.grid(column=0, row=2)

label_result = tkinter.Label(root, text="BMI: ")
label_result.grid(column=1, row=2)

root.mainloop()