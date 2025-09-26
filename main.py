import tkinter as tk
import pygame as pg
import streamlit as st
import json
import re

if st.button("Hi"):

    root = tk.Tk()

    BG = "black"
    FG = "white"
    NT = ("Monospace", 15)

    root.title("Tag'em")
    root.geometry("750x300")
    root.resizable(False, False)
    root.config(bg=BG)

    SF = tk.Frame(root, bg=BG)

    tk.Label(SF, text="Tag'em", fg=FG, bg=BG, font=("Monospace", 30, "underline", "italic", "bold")).pack()
    tk.Label(SF, text="Click One of These Buttons To Get Started!:", fg=FG, bg=BG, font=NT).pack()
    tk.Label(SF, text="", bg=BG).pack()

    def main_page(account, LIF):

        def find_game(MPG):
            MPG.destroy()

            FGF = tk.Frame(root, bg=BG)

            FGF.pack()

        def  make_game(MPG):
            MPG.destroy()

            MGF = tk.Frame()

            MGF.pack()

        LIF.destroy()

        MPF = tk.Frame(root, bg=BG)

        tk.Label(MPF, text="Welcome!", fg=FG, bg=BG, font=("Monospace", 30, "underline", "italic", "bold")).pack()

        tk.Label(MPF, text="", bg=BG)

        tk.Label(MPF, text="Please Select An Option Below, The Creator Of The Game  Will Be The Starting Tagger.",
                fg=FG,
                bg=BG,
                font=NT
                )

        tk.Label(MPF, text="", bg=BG)

        tk.Button(MPF, text="Join A Game", bg="lightgrey", command=lambda: find_game(MPG))

        MPF.pack()

    def log_in():
        SF.destroy()

        LIF = tk.Frame(root, bg=BG)

        tk.Label(LIF, text="Log In", fg=FG, bg=BG, font=("Monospace", 30, "underline", "italic", "bold")).pack()

        tk.Label(LIF, text="", bg=BG).pack()

        UPF = tk.Frame(LIF, bg=BG)

        tk.Label(UPF, text="Enter Your Username: ", fg=FG, bg=BG, font=NT).grid(row=0, column=0)
        USV = tk.StringVar(UPF)
        username = tk.Entry(UPF, textvariable=USV).grid(row=0, column=1)

        tk.Label(UPF, text="Enter Your Password: ",
                fg=FG, bg=BG, font=NT).grid(row=1, column=0)
        global pw
        PSV = tk.StringVar(UPF)
        password = tk.Entry(UPF, textvariable=PSV).grid(row=1, column=1)

        UPF.pack()

        def locate_account(USV, PSV):
            un = USV.get()
            pw = PSV.get()

            with open("accounts.json", "r") as accounts:
                accounts_data = json.load(accounts)

            for a in accounts_data:
                if un in a:

                    account_index = accounts_data.index(a)

                    print(accounts_data[account_index])

                    actual_pw = a.get(un)

                    if actual_pw == pw:
                        cur_account = a
                        main_page(a, LIF)

        tk.Button(LIF, text="Submit", font=NT, command=lambda: locate_account(USV, PSV)).pack()

        LIF.pack()


    def sign_in():
        SF.destroy()

        SIF = tk.Frame(root, bg=BG)

        tk.Label(SIF, text="Sign In", fg=FG, bg=BG, font=("Monospace", 30, "underline", "italic", "bold")).pack()

        UPF = tk.Frame(SIF, bg=BG)

        tk.Label(UPF, text="Enter A Username: ", fg=FG, bg=BG, font=NT).grid(row=0, column=0)
        USV = tk.StringVar(UPF)
        username = tk.Entry(UPF, textvariable=USV).grid(row=0, column=1)

        tk.Label(UPF, text="Enter A Password: ",
                fg=FG, bg=BG, font=NT).grid(row=1, column=0)
        PSV = tk.StringVar(UPF)
        password = tk.Entry(UPF, textvariable=PSV).grid(row=1, column=1)

        UPF.pack()

        def check(PSV, USV):
            global accounts

            errors = []
            pw = PSV.get()
            un = USV.get()

            with open("accounts.json", "r") as accounts:
                accounts_data = json.load(accounts)

            # Minimum 8 characters
            if len(pw) < 8:
                errors.append("Password Needs 7 Or More Characters")

            # At least one uppercase letter
            if not re.search(r"[A-Z]", pw):
                errors.append("Password Has No Uppercase Letter")


            # At least one lowercase letter
            if not re.search(r"[a-z]", pw):
                errors.append("Password Has No Lowercase Letter")

            # At least one digit
            if not re.search(r"\d", pw):
                errors.append("Password Has No Numbers Found")

            # At least one special character
            if not re.search(r"[!@#$%^&*(),.?\":|<>]", pw):
                errors.append("Password Has No Symbols Found")

            if un in accounts_data:
                errors.append("Username Already Exist")

            if not len(un) > 0:
                errors.append("Please Type A Username")

            for a in accounts_data:
                if un in a:
                    errors.append("That Username Has Already Been Taken")


            if len(errors) > 0:
                errors_str =\
                    (
                        str(errors)
                        .replace("[", "")
                        .replace("]", "")
                        .replace('"', "")
                        .replace("'", "")
                        + "."
                    )

                print("Unable To Create Account. Reasons: " + errors_str)

            else:
                with open("accounts.json", "w") as accounts:
                    new_data = {
                        un: pw
                    }
                    accounts_data.append(new_data)
                    json.dump(accounts_data, accounts, indent=4)

                SIF.destroy()
                SIDF = tk.Frame(root, bg=BG)

                tk.Label(SIDF, text="Sign In Done", fg=FG, bg=BG, font=("Monospace", 30, "underline", "italic", "bold")).pack()
                tk.Label(SIDF, text="", bg=BG).pack()
                tk.Label(SIDF, text="You Have Successfuly Created A New Account! Please Press The Button Below To Locate To the Next Page, Where You Can Log In To Your Account!",
                        fg=FG,
                        bg=BG,
                        font=NT,
                        wraplength=750).pack(fill="x")

                tk.Label(SIDF, text="", bg=BG).pack()

                tk.Button(SIDF, text="Continue To Login Page", font=NT, bg="lightgrey", command=lambda: (log_in(), SIDF.destroy())).pack()

                SIDF.pack()

        tk.Button(SIF, text="Submit", command=lambda: check(PSV, USV)).pack()

        SIF.pack()

    ABF = tk.Frame(SF, bg=BG)

    SIB = tk.Button(ABF, text="Sign In To A New Account", bg="lightgrey",  font=NT, command=sign_in)
    ESL = tk.Label(ABF, text="", bg=BG)
    LIB = tk.Button(ABF, text="Log In To An Existing Account", bg="lightgrey", font=NT, command=log_in)

    SIB.grid(row=0, column=0)
    ESL.grid(row=0, column=1)
    LIB.grid(row=0, column=2)

    ABF.pack()

    SF.pack()

    root.mainloop()