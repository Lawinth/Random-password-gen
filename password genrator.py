import random
import string
def generate_password(length, complexity):
    if complexity == 1:
        characters = string.ascii_lowercase
    elif complexity == 2:
        characters = string.ascii_lowercase + string.ascii_uppercase
    elif complexity == 3:
        characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    elif complexity == 4:
        characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    else:
        raise ValueError("Complexity must be between 1 and 4")

    password = ''.join(random.choice(characters) for i in range(length))
    return password
def main():
    try:
        length = int(input("Enter the  length of the password: "))
        complexity = int(input("Enter the complexity  (1-4):\n1.easy\n2.moderate\n3.hard\n4.very hard\n"))
        password = generate_password(length, complexity)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()
