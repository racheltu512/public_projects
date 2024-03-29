# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def run_script():
    gender = input("Please input the patient's gender. Enter m or f: ")
    while gender != "m" and gender != "f":

        gender = input("That was not a valid input. Please input the patient's gender. Enter m or f: ")

    while True:
        try:
            age = int(input("Please input the patient's age. Please enter a non-negative number: "))
            if age >= 0:
                break
            else:
                print("That was not a valid input. Age cannot be a negative number.")
        except ValueError:
            print("That was not a valid input. Please enter a non-negative number.")

    HBV = input("Is the patient HBeAG+ or HBeAG-. Enter + or -: ")
    while HBV != "+" and HBV != "-":
        HBV = input("That is not an appropriate answer. Is the patient HBeAG+ or HBeAG-. Enter + or -: ")
    if HBV == "+":
        print("You have entered that the patient is HBeAG+")

        ALT = input("Is the patient's ALT score lower than their ULN score: Enter yes or no: ")
        while ALT != "yes" and ALT != "no":
            ALT = input("Is the patient's ALT score lower than their ULN score: Enter yes or no: ")

        if ALT == 'yes':
            if age > 40:
                if gender == "m":
                    risk = "10-15"
                else:
                    risk = "8-13"
                print(f"Recommendation is Biopsy/Therapy + HCC survailence. Risk score is {risk}")
            else:
                if gender == "m":
                    risk = "8-10"
                else:
                    risk = "6-8"
                print(f"Recommendation is 3 month follow up. Risk score of {risk}")
        else:

            ULN = input("Is the patient's ALT score greater than twice than their ULN score: Enter yes or no: ")
            while ULN != "yes" and ULN!= "no":
                ULN = input("That is not a valid input. Is the patient's ALT score greater than twice than their ULN score: Enter yes or no: ")

            if ULN == "yes":
                if gender == "m":
                    risk = "10-16"
                else:
                    risk = "8-14"
                print(f"User has persistently HBeAg(+) and elevated ALT. Recommendation is Antiviral treatment. Risk score of {risk}")
            else:
                if age > 40:
                    if gender == "m":
                        risk = "12-16"
                    else:
                        risk = "10-14"
                    print(f"Recommendation is Biopsy/Therapy + HCC survailence. Risk score is {risk}")
                else:
                    if gender == "m":
                        risk = "10-11"
                    else:
                        risk = "8-9"
                    print(f"Recommendation is 1-3 month follow up. Risk score of {risk}")

    else:
        print("You have entered that the patient is HBeAG-")

        HBV = input("Is the patient's HBV-DNA score lower than two times ten to the three IU/mL: Enter yes or no: ")
        while HBV != "yes" and HBV != "no":
            HBV = input("That is not a valid input. Is the patient's HBV-DNA score lower than two times ten to the three IU/mL: Enter yes or no: ")

        if HBV == "yes":
            ULN = input("Is the patient's ALT score lower than their ULN score: Enter yes or no: ")
            while ULN != "yes" and ULN != "no":
                ULN = input("That is not a valid input. Is the patient's ALT score lower than their ULN score: Enter yes or no: ")

            if ULN == "yes":
                if gender == "m":
                    if age > 40:
                        risk = "4-10"
                        print(f"Recommendation is HCC survailence. Risk score is {risk}")
                    else:
                        risk = "2-5"
                        print(f"User has negative HBeAg(-). Recommendation is 6 month follow up. Risk score of {risk}")
                else:
                    if age > 40:
                        risk = "2-8"
                        print(f"Recommendation is HCC survailence. Risk score is {risk}")
                    else:
                        risk = "0-3"
                        print(f"User has negative HBeAg(-). Recommendation is 6 month follow up. Risk score of {risk}")
            else:
                if gender == "m":
                    if age > 40:
                        risk = "6-11"
                        print(f"Recommendation is HCC survailence. Risk score is {risk}")
                    else:
                        risk = "4-6"
                        print(f"User has negative HBeAg(-). Recommendation is 6 month follow up. Risk score of {risk}")
                else:
                    if age > 40:
                        risk = "4-9"
                        print(f"Recommendation is HCC survailence. Risk score is {risk}")
                    else:
                        risk = "2-4"
                        print(f"User has negative HBeAg(-). Recommendation is 6 month follow up. Risk score of {risk}")
        else:
            print("You have entered that the patient's HBV-DNA score is not lower than two times ten to the three IU/mL")

            ULN = input("Is the patient's ALT score lower than their ULN score: Enter yes or no: ")
            while ULN != "yes" and ULN != "no":
                ULN = input("That is not a valid input. Is the patient's ALT score lower than their ULN score: Enter yes or no: ")

            if ULN == "yes":
                if gender == "m":
                    if age > 40:
                        risk = "7-15"
                        print(f"Recommendation is Biopsy/therapy + HCC surveillance. Risk score is {risk}")
                    else:
                        risk = "5-9"
                        print(f"User has negative HBeAg(-). Recommendation is 3 month follow up. Risk score of {risk}")
                else:
                    if age > 40:
                        risk = "5-12"
                        print(f"Recommendation is Biopsy/therapy + HCC surveillance. Risk score is {risk}")
                    else:
                        risk = "3-7"
                        print(f"User has negative HBeAg(-). Recommendation is 3 month follow up. Risk score of {risk}")
            if ULN == "no":
                ULN = input("Is the patient's ALT score greater than twice than their ULN score: Enter yes or no: ")
                while ULN != "yes" and ULN != "no":
                    ULN = input("That is not a valid input. Is the patient's ALT score greater than two times their ULN score: Enter yes or no: ")
                if ULN == "yes":
                    if gender == "m":
                        risk = "7-15"
                        print(f"User has negative HBeAg(-) and has persistantly high HBV DNA level and elevated ALT. Recommendation is antiviral treatment. Risk score of {risk}")
                    else:
                        risk = "5-13"
                        print(f"User has negative HBeAg(-) and has persistantly high HBV DNA level and elevated ALT. Recommendation is antiviral treatment. Risk score of {risk}")
                else:
                    if ULN == "no":
                        if gender == "m":
                            if age > 40:
                                risk = "9-15"
                                print(f"Recommendation is Biopsy/therapy + HCC survailence. Risk score is {risk}")
                            else:
                                risk = "7-10"
                                print(f"User has negative HBeAg(-). Recommendation is 1-3 month follow up. Risk score of {risk}")
                        else:
                            if age > 40:
                                risk = "7-13"
                                print(f"Recommendation is Biopsy/therapy + HCC survailence. Risk score is {risk}")
                            else:
                                risk = "5-8"
                                print(f"User has negative HBeAg(-). Recommendation is 1-3 month follow up. Risk score of {risk}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_script()