def nomni_top(oy):
    nomlar = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    if 1 <= oy <= 12:
        return nomlar[oy - 1]
    else:
        return None

def gregoriy_taqvimi(oy_nomi):
    nomlar = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    oy_raqami = nomlar.index(oy_nomi.capitalize()) + 1
    return oy_raqami

def play():
    print("Enter the month number or name (Type 'stop/done' or press Enter to exit)")
    while True:
        kirish = input(">>> ")
        if kirish.lower() in ['done', 'stop', '']:
            print("The program is finished. Thank you for using!")
            break

        try:
            kirish_raqam = int(kirish)
            oy_nomi = nomni_top(kirish_raqam)

            if oy_nomi is not None:
                print(f"{kirish_raqam}-month is {oy_nomi}!!!")
            else:
                print("Invalid month number.")
        except ValueError:
            try:
                oy_raqami = gregoriy_taqvimi(kirish)
                if oy_raqami != 0:
                    print(f"The month of {kirish.capitalize()} is {oy_raqami}-month!!!")
                else:
                    print("Invalid month name.")
            except ValueError:
                print("Sorry, you entered an invalid value.")
