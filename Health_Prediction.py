import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier
import tkinter as tk

file_path = r'D:\7th SEMESTER\ML IBM\health_data_extended_400_rows.xlsx'
data = pd.read_excel(file_path)

X = data[['PH Level', 'Glucose Level', 'Sodium Level']]

le_health_condition = preprocessing.LabelEncoder()
data['Health Condition'] = le_health_condition.fit_transform(data['Health Condition'])
y = data['Health Condition']

health_condition_tree = DecisionTreeClassifier(criterion="entropy", max_depth=4)
health_condition_tree.fit(X, y)

def predict_health_condition_display():
    window = tk.Tk()
    window.title("Know Your Health")
    window.geometry("410x460")

    window.configure(bg="#ADD8E6")
    title_font = ("Membra", 18, "bold")
    label_font = ("Times New Roman", 12, "bold")
    entry_font = ("Times New Roman", 12, "bold")
    button_font = ("Times New Roman", 14, "bold")

    title_label = tk.Label(window, text="KNOW YOUR HEALTH", font=title_font, bg="#003153", fg="white", pady=10)
    title_label.grid(row=0, column=0, columnspan=2)

    input_frame = tk.Frame(window, bg="#F5F5F5", pady=10, padx=10, highlightbackground="black", highlightthickness=1)
    input_frame.grid(row=1, column=0, columnspan=2, pady=10)

    tk.Label(input_frame, text="Name:", font=label_font, bg="#F5F5F5").grid(row=0, column=0, pady=5)
    tk.Label(input_frame, text="Sex:", font=label_font, bg="#F5F5F5").grid(row=1, column=0, pady=5)
    tk.Label(input_frame, text="Age:", font=label_font, bg="#F5F5F5").grid(row=2, column=0, pady=5)

    name_entry = tk.Entry(input_frame, font=entry_font)
    sex_entry = tk.Entry(input_frame, font=entry_font)
    age_entry = tk.Entry(input_frame, font=entry_font)

    name_entry.grid(row=0, column=1, pady=5)
    sex_entry.grid(row=1, column=1, pady=5)
    age_entry.grid(row=2, column=1, pady=5)

    tk.Label(window, text="Enter pH Level (6.8-7.6):", font=label_font, bg="#97b7f7").grid(row=3, column=0, pady=5)
    tk.Label(window, text="Enter Glucose Level (110-130 mg/dL):", font=label_font, bg="#97b7f7").grid(row=4, column=0, pady=5)
    tk.Label(window, text="Enter Sodium Level (130-140 µg/mL):", font=label_font, bg="#97b7f7").grid(row=5, column=0, pady=5)

    ph_entry = tk.Entry(window, font=entry_font)
    glucose_entry = tk.Entry(window, font=entry_font)
    sodium_entry = tk.Entry(window, font=entry_font)

    ph_entry.grid(row=3, column=1, pady=5)
    glucose_entry.grid(row=4, column=1, pady=5)
    sodium_entry.grid(row=5, column=1, pady=5)

    def get_user_input():
        user_info = {
            'Name': name_entry.get(),
            'Sex': sex_entry.get(),
            'Age': age_entry.get()
        }

        ph_level = float(ph_entry.get())
        glucose_level = int(glucose_entry.get())
        sodium_level = int(sodium_entry.get())

        new_data = {
            'PH Level': [ph_level],
            'Glucose Level': [glucose_level],
            'Sodium Level': [sodium_level]
        }

        new_instance = pd.DataFrame(new_data)
        predicted_condition = health_condition_tree.predict(new_instance)

        predicted_condition = le_health_condition.inverse_transform(predicted_condition)[0]

        result_label = tk.Label(window, text=f"Hello {user_info['Name']}, "
                                             f"Predicted Health Condition: {predicted_condition}", font=label_font,
                                fg="#FF0000", pady=10, bg="#ADD8E6")
        result_label.grid(row=7, column=0, columnspan=2)

    predict_button = tk.Button(window, text="Predict", command=get_user_input, bg="#008000", fg="white", font=button_font)
    predict_button.grid(row=6, column=0, columnspan=2, pady=10)

    close_button = tk.Button(window, text="Close", command=window.destroy, bg="#CD5C5C", fg="white", font=button_font)
    close_button.grid(row=8, column=0, columnspan=2, pady=10)

    window.mainloop()

predict_health_condition_display()
