### CrowdFund Console App

The CrowdFund Console App is a robust crowdfunding platform designed to empower users to raise funds for their projects with ease. With an intuitive interface and essential features, this console application simplifies the fundraising process, making it accessible to a wide range of users.

#### Key Features

1. **Authentication System**
   - **Registration**: Users can sign up for an account by providing their first name, last name, email, password, confirmed password, and mobile phone number. The phone number validation ensures that only Egyptian phone numbers are accepted.
   - **Login**: Registered users can securely log in to their accounts using their email and password.

2. **Project Management**
   - **Create Projects**: Users can create projects with essential details such as title, description, total target amount, and start/end dates for the campaign. The application validates the date formula to ensure accurate scheduling.
   - **View Projects**: Users have the ability to browse through all active projects on the platform.
   - **Edit Projects**: Project creators can modify the details of their campaigns, allowing them to make updates or adjustments as needed.
   - **Delete Projects**: Users retain control over their projects and can choose to remove them from the platform if necessary.
   - **Search Functionality**: Users are able to find specific projects based on their start or end dates, enhancing usability and facilitating project discovery.

#### Dependencies

This project relies on the following Python libraries:
- **re**: This library is used for regular expression operations, particularly for validating the format of inputs such as email addresses and phone numbers.
- **maskpass**: This library provides functionality for securely masking password input, enhancing user privacy and security during authentication.
- **json**: This library facilitates the parsing and manipulation of JSON data, which may be utilized for storing and managing project information within the application.

#### Modular Structure

The application is organized into the following modules:
- **Registration**: Handles user registration functionality.
- **Login**: Manages user authentication and login processes.
- **Projects**: Implements project management features, including creation, viewing, editing, and deletion.
- **Main**: The main module orchestrates the interaction between the various components of the application.

#### Usage

1. **Installation**: Clone the repository to your local machine.
2. **Setup**: Ensure you have Python installed. Navigate to the project directory and install the required dependencies using `pip install re maskpass json`.
3. **Run**: Execute the main application file to start the CrowdFund Console App.

#### Contribution

Contributions to this project are welcome. Feel free to fork the repository, make improvements, and submit pull requests.
