AI-Powered Data Analysis Tool
This Flask web application provides an easy-to-use interface for performing basic data analysis and visualization on uploaded CSV datasets. It leverages popular Python libraries such as Pandas, Seaborn, and Matplotlib to generate visual insights (e.g., heatmaps, bar charts, scatter plots, and line charts) from your data.

Features
File Upload:
Easily upload CSV files via a web interface.

Data Analysis:
The application reads the CSV file into a Pandas DataFrame and provides a basic summary including column names, shape, missing values, data types, and a preview of the data.

Data Visualization:
Generate different types of visualizations based on your dataset:

Heatmap: Displays a correlation heatmap for numeric data.
Bar Chart: Creates a bar chart for the first column’s value counts.
Scatter Plot: Plots a scatter graph using the first two numeric columns.
Line Chart: Generates a line chart using the first two columns.
Static Visualization Storage:
Visualizations are saved to a static folder so they can be served or further processed.

Installation
Requirements
Python 3.7 or higher
Flask
Pandas
Seaborn
Matplotlib
Setup
Clone the repository and navigate into the project folder:

bash
Copy
git clone https://github.com/your_username/your_repository.git
cd your_repository
Create and activate a virtual environment (optional but recommended):

bash
Copy
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
Install the required packages:

You can create a requirements.txt file with the following content:

txt
Copy
Flask
pandas
seaborn
matplotlib
Then run:

bash
Copy
pip install -r requirements.txt
Usage
Run the Flask Application:

In the project directory, execute:

bash
Copy
python <your_main_file>.py
Replace <your_main_file>.py with the filename containing the provided Flask code. The server will start in debug mode by default.

Access the Home Page:

Open your web browser and navigate to http://localhost:5000/. You should see a welcome message.

Upload a CSV File:

Send a POST request to the /upload endpoint with a CSV file and an optional graph_type parameter (supported types: heatmap, bar, scatter, line).
For example, using curl:

bash
Copy
curl -X POST -F "file=@path_to_your_file.csv" -F "graph_type=heatmap" http://localhost:5000/upload
The response will include a summary of the dataset and, if applicable, a path to the generated visualization image stored in the static folder.

Project Structure
php
Copy
ai-powered-data-analysis/
├── static/                     # Folder for storing generated visualizations
├── <your_main_file>.py         # Main Flask application file containing the provided code
├── requirements.txt            # List of required packages
└── README.md                   # This file
API Endpoints
GET /

Description: Home page that displays a welcome message.
Response: "Welcome to the AI-Powered Data Analysis Tool! Upload a dataset to get started."
POST /upload

Description: Upload a CSV file for analysis and visualization.
Parameters:
file: The CSV file to be uploaded.
graph_type (optional): The type of graph to generate (heatmap, bar, scatter, line).
Response: A JSON object containing:
Dataset summary (columns, shape, missing values, data types, and a preview of the first few rows)
The file path of the generated visualization (if successful)
Contributing
Contributions are welcome! Please follow these steps to contribute:

Fork the repository.
Create a new branch: git checkout -b feature/your-feature-name
Commit your changes: git commit -m "Add feature description"
Push your branch: git push origin feature/your-feature-name
Open a pull request describing your changes.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Flask
Pandas
Seaborn
Matplotlib
Feel free to modify and expand this README to best suit your project's needs.
