import random
import numpy as np

FILE_NAME = "patients.txt"


class Patient:

    def __init__(self, patient_id, name, age, gender, disease, doctor):

        self.__patient_id = patient_id
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__disease = disease
        self.__doctor = doctor

    def get_patient_id(self):
        return self.__patient_id

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_gender(self):
        return self.__gender

    def get_disease(self):
        return self.__disease

    def get_doctor(self):
        return self.__doctor

    def set_disease(self, disease):
        self.__disease = disease

    def set_doctor(self, doctor):
        self.__doctor = doctor

    def display(self):

        print("\n----------------------------")
        print("Patient ID :", self.__patient_id)
        print("Name       :", self.__name)
        print("Age        :", self.__age)
        print("Gender     :", self.__gender)
        print("Disease    :", self.__disease)
        print("Doctor     :", self.__doctor)
        print("----------------------------")

    def save_to_file(self):

        file = open(FILE_NAME, "a")

        file.write(
            self.__patient_id + "," +
            self.__name + "," +
            str(self.__age) + "," +
            self.__gender + "," +
            self.__disease + "," +
            self.__doctor + "\n"
        )

        file.close()


class Doctor:

    def __init__(self, doctor_name, fees):

        self.doctor_name = doctor_name
        self.fees = fees

    def display_doctor(self):

        print("\nDoctor Name :", self.doctor_name)
        print("Doctor Fees :", self.fees)


class Bill:

    def __init__(self, room_charge, medicine_charge, doctor_fee):

        self.room_charge = room_charge
        self.medicine_charge = medicine_charge
        self.doctor_fee = doctor_fee

    def generate_bill(self):

        charges = np.array([
            self.room_charge,
            self.medicine_charge,
            self.doctor_fee
        ])

        total_bill = np.sum(charges)

        print("\n========= HOSPITAL BILL =========")
        print("Room Charge  :", self.room_charge)
        print("Doctor Fee   :", self.doctor_fee)
        print("Medicine Fee :", self.medicine_charge)
        print("---------------------------------")
        print("Total Bill   :", total_bill)
        print("=================================")


class Hospital:

    def add_patient(self):

        print("\n--- Add Patient ---")

        try:

            name = input("Enter Patient Name: ")
            age = input("Enter Age: ")
            gender = input("Enter Gender: ")
            disease = input("Enter Disease: ")
            doctor = input("Enter Doctor Name: ")

            if (
                name == "" or
                age == "" or
                gender == "" or
                disease == "" or
                doctor == ""
            ):

                print("All fields are required!")
                return

            if not age.isdigit():

                print("Age must be numeric!")
                return

            patient_id = "P" + str(
                random.randint(1000, 9999)
            )

            patient = Patient(
                patient_id,
                name,
                int(age),
                gender,
                disease,
                doctor
            )

            patient.save_to_file()

            print("\nPatient Added Successfully!")
            print("Generated Patient ID :", patient_id)

        except Exception as e:

            print("Error:", e)

    def view_patients(self):

        print("\n--- All Patients ---")

        try:

            file = open(FILE_NAME, "r")

            data = file.readlines()

            file.close()

            if len(data) == 0:

                print("No Records Found!")
                return

            for line in data:

                patient_data = line.strip().split(",")

                patient = Patient(
                    patient_data[0],
                    patient_data[1],
                    patient_data[2],
                    patient_data[3],
                    patient_data[4],
                    patient_data[5]
                )

                patient.display()

        except FileNotFoundError:

            print("No Patient Records Found!")

    def search_patient(self):

        print("\n--- Search Patient ---")

        search_id = input("Enter Patient ID: ")

        found = False

        try:

            file = open(FILE_NAME, "r")

            data = file.readlines()

            file.close()

            for line in data:

                patient_data = line.strip().split(",")

                if search_id == patient_data[0]:

                    patient = Patient(
                        patient_data[0],
                        patient_data[1],
                        patient_data[2],
                        patient_data[3],
                        patient_data[4],
                        patient_data[5]
                    )

                    print("\nPatient Found!")

                    patient.display()

                    found = True
                    break

            if found == False:

                print("Patient Not Found!")

        except FileNotFoundError:

            print("No Patient Records Found!")

    def update_patient(self):

        print("\n--- Update Patient ---")

        update_id = input("Enter Patient ID: ")

        found = False

        try:

            file = open(FILE_NAME, "r")

            data = file.readlines()

            file.close()

            file = open(FILE_NAME, "w")

            for line in data:

                patient_data = line.strip().split(",")

                if update_id == patient_data[0]:

                    found = True

                    print("\n1. Update Disease")
                    print("2. Update Doctor")

                    choice = input("Enter Choice: ")

                    if choice == "1":

                        patient_data[4] = input(
                            "Enter New Disease: "
                        )

                    elif choice == "2":

                        patient_data[5] = input(
                            "Enter New Doctor: "
                        )

                    else:

                        print("Invalid Choice!")

                updated_line = ",".join(patient_data)

                file.write(updated_line + "\n")

            file.close()

            if found:

                print("Patient Updated Successfully!")

            else:

                print("Patient Not Found!")

        except FileNotFoundError:

            print("No Patient Records Found!")

    def generate_bill(self):

        print("\n--- Generate Bill ---")

        try:

            patient_id = input("Enter Patient ID: ")

            days = input("Enter Number of Days: ")

            if not days.isdigit():

                print("Days must be numeric!")
                return

            days = int(days)

            room_charge = days * 500
            doctor_fee = 2000
            medicine_fee = 1000

            doctor = Doctor(
                "Hospital Doctor",
                doctor_fee
            )

            doctor.display_doctor()

            bill = Bill(
                room_charge,
                medicine_fee,
                doctor_fee
            )

            bill.generate_bill()

        except Exception as e:

            print("Error:", e)

    def menu(self):

        print("\n========== HOSPITAL MANAGEMENT SYSTEM ==========")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Search Patient by ID")
        print("4. Update Patient")
        print("5. Generate Bill")
        print("6. Exit")


hospital = Hospital()

print("Welcome to Hospital Management System")

while True:

    hospital.menu()

    choice = input("\nEnter Your Choice: ")

    if choice == "1":

        hospital.add_patient()

    elif choice == "2":

        hospital.view_patients()

    elif choice == "3":

        hospital.search_patient()

    elif choice == "4":

        hospital.update_patient()

    elif choice == "5":

        hospital.generate_bill()

    elif choice == "6":

        print("\nThank You!")
        print("Exiting Program...")
        break

    else:

        print("Invalid Choice! Please Try Again.")