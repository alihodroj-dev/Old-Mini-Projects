# imports

# Starting statements
print("Separate your password into 3 parts!!!")

# Variables
part1 = input("Enter part1: ")
part2 = input("Enter part2: ")
part3 = input("Enter part3: ")
key = ["ijed4", "k3de2"]
arrayed_pass = [part1, part2, part3]
encrypted_pass = ""

# Functions
def encrypt():
    arrayed_pass.insert(1, key[0])
    arrayed_pass.append(key[1])

def decrypt():
    arrayed_pass.remove(arrayed_pass[1])
    arrayed_pass.remove(arrayed_pass[len(arrayed_pass) - 1])

# Encryption Process
encrypt()
for word in arrayed_pass:
    encrypted_pass += word

# Printing Encrypted password
print("Encrypting password ...")
print("Your encrypted password is " + encrypted_pass)

# Restoring Values
encrypted_pass = ""

# Decryption Process
decrypt()
for word in arrayed_pass:
    encrypted_pass += word

# Printing Encrypted password
print("Decrypting password ...")
print("Yor original password is " + encrypted_pass)