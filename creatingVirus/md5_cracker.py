import hashlib

def check_md5(md5_hash, password_file):
    with open(password_file, 'r') as file:
        for line in file:
            password = line.strip()
            hashed_password = hashlib.md5(password.encode()).hexdigest()
            if hashed_password == md5_hash:
                return password, hashed_password
    return None, None

if __name__ == "__main__":
    md5_input = input("Enter the MD5 hash: ").strip()
    dictionary_file = input("Enter the path to the password dictionary file: ").strip()

    matched_password, matched_md5 = check_md5(md5_input, dictionary_file)

    if matched_password:
        print(f"Password found: {matched_password}")
        print(f"MD5 hash: {matched_md5}")
    else:
        print("Password not found in the dictionary.")
