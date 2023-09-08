# master_pwd = input("What is the Master password? ")

def view(): #functions
    with open('passwords.txt', 'r') as f: # open in read mode
        for line in f.readlines(): # read the txt file line by line
            data = (line.rstrip()) # to remove the blank line after every line with rstrip()
            user, passw = data.split("|") # to split the data whenever there's a |
            print("USER: " , user, ", PASSWORD: ", passw)
def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f: # to open a file and close after execution, a appends the text, w writes and overwrite the file, r reads the file
        f.write(name + "|" + pwd + "\n") #and to go to next line.


while True:
    mode = input("Would you like to add a new password or view existing ones (ADD / VIEW / QUIT): ").lower()
    if mode == "quit":
        break
    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid mode. Try Again !")
        continue

# to encrypt the data install 'pip install cryptography'
# tech with tim