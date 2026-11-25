Experiment 7: Regular Expressions (Regex) - Pattern matching
Find email patterns in a given text using Python's re module.
"""

import re

EMAIL_PATTERN = r"[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,4}"


def find_emails(text):
    """Return a list of all email addresses found in the text."""
    return re.findall(EMAIL_PATTERN, text)


def first_email(text):
    """Return the first email found (Match object) or None."""
    return re.search(EMAIL_PATTERN, text)


def mask_emails(text):
    #Om Kutwal Sy-12 Roll no. 70
    """Replace every email in the text with [HIDDEN] using re.sub."""
    return re.sub(EMAIL_PATTERN, "[HIDDEN]", text)


def split_on_emails(text):
    """Split the text at every email using re.split."""
    return re.split(EMAIL_PATTERN, text)


def print_menu():
    print("\n===== REGEX - EMAIL PATTERN FINDER =====")
    print("1. Find all emails in a text (findall)")
    print("2. Find the first email with its position (search)")
    print("3. Hide all emails in a text (sub)")
    print("4. Split a text at emails (split)")
    print("5. Run built-in example")
    print("6. Exit")
    print("=========================================")


def main():
    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            text = input("Enter the text: ")
            emails = find_emails(text)
            if emails:
                print(f"\nTotal emails found: {len(emails)}")
                for i, mail in enumerate(emails, 1):
                    print(f"{i}. {mail}")
            else:
                print("No email addresses found.")

        elif choice == "2":
            text = input("Enter the text: ")
            match = first_email(text)
            if match:
                print(f"\nFirst email : {match.group()}")
                print(f"Position    : {match.span()}")
            else:
                print("No email address found.")

        elif choice == "3":
            text = input("Enter the text: ")
            print("\nText after hiding emails:")
            print(mask_emails(text))

        elif choice == "4":
            text = input("Enter the text: ")
            print("\nParts of text between emails:")
            print(split_on_emails(text))

        elif choice == "5":
            text = ("Contact us at support@mitadt.edu.in or admin_office@mitadt.com. "
                    "Personal: om.kutwal-70@gmail.com, invalid@@mail, test@site.org")
            print("\nText:", text)
            print("Emails found:", find_emails(text))

        elif choice == "6":
            print("Exiting the Regex Program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
