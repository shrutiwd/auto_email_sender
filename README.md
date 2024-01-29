# Auto Email Sender

This Python project allows you to send emails to multiple recipients using information stored in a CSV file. It provides two versions of the email sender script: one without username customization and another with the ability to replace a placeholder with the recipient's name.

## How to Use

### Email Sender without Username Customization

1. Clone the repository or download the script.

    ```bash
    git clone https://github.com/shrutiwd/auto_email_sender.git
    cd auto_email_sender
    ```

2. Ensure you have Python installed on your system.

3. Update the following parameters in the script:
    - `file_name`: The name of the file containing the email content.
    - `send`: Your email address.
    - `subject`: The subject of the email.

4. Replace the login credentials in the `server.login` method with your own Gmail credentials.

5. Prepare a CSV file named `emailids.csv` with columns 'name' and 'mailid'.

6. Run the script.

    ```bash
    python send_mails_without_usernames.py
    ```

### Enhanced Email Sender with Username Customization

1. Clone the repository or download the script.

    ```bash
    git clone https://github.com/shrutiwd/auto_email_sender.git
    cd auto_email_sender
    ```

2. Ensure you have Python installed on your system.

3. Update the following parameters in the script:
    - `file_name`: The name of the file containing the email content.
    - `send`: Your email address.
    - `subject`: The subject of the email.

4. Replace the login credentials in the `server.login` method with your own Gmail credentials.

5. Prepare a CSV file named `emailids.csv` with columns 'name' and 'mailid'.

6. Customize the email content in the specified file and use the placeholder 'candidate' for the recipient's name.

7. Run the script.

    ```bash
    python sending_emails_from_csv_files_with_username.py
    ```

### Note

- Make sure to allow access to less secure apps in your Gmail account settings.

### Dependencies

This project uses Python's `smtplib` library for email functionality. Ensure to have the required packages installed by running:

```bash
pip install -r requirements.txt
```

Feel free to customize the scripts, CSV file, and email content according to your specific requirements.

Happy emailing!
