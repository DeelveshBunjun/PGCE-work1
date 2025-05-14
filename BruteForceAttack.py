import itertools
import string
import time

# Define character set: lowercase + uppercase + digits
charset = string.ascii_lowercase + string.ascii_uppercase + string.digits

# Ask user for a password (up to 5 characters: letters and digits)
password = input("Enter a password (up to 5 characters, letters and numbers only): ").strip()

# Validate input
if not password.isalnum() or len(password) > 5:
    print("Please enter only letters and numbers, max 5 characters.")
    exit()

# Start brute force
start_time = time.time()
tries = 0
found = False

print("\nStarting brute-force attack...")

for length in range(1, 6):  # Try passwords of length 1 to 5
    for guess_tuple in itertools.product(charset, repeat=length):
        guess = ''.join(guess_tuple)
        tries += 1
        print(f"Trying: {guess}")
        if guess == password:
            found = True
            break
    if found:
        break

end_time = time.time()
elapsed = end_time - start_time

# Result
print("\n✅ Password cracked!")
print(f"Password: {guess}")
print(f"Total tries: {tries}")
print(f"Time taken: {elapsed:.4f} seconds")
