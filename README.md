# evapo Project

## Overview
The evapo project is designed to assist in shutting down machines automatically whenever users log in. This serves as a temporary measure while working on a more permanent solution to prevent ransomware payments.

## Purpose
The primary goal of this project is to enhance security by ensuring that machines are shut down upon user login, thereby minimizing the risk of ransomware attacks.

## Project Structure
```
evapo
├── src
│   ├── main.py          # Entry point of the application
│   └── utils
│       └── shutdown.py  # Contains the shutdown logic
├── requirements.txt     # Lists project dependencies
└── README.md            # Project documentation
```

## Setup Instructions
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies by running:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the application, execute the following command:
```
python src/main.py
```
This will start monitoring user logins and trigger the shutdown process as specified.

## Contributing
Contributions to improve the project are welcome. Please submit a pull request or open an issue for discussion.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.