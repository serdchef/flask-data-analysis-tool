from flask import Flask, request, jsonify
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Matplotlib backend
import matplotlib
matplotlib.use('Agg')  # Non-GUI backend

# Initialize the Flask application
app = Flask(__name__)

# Ensure static folder exists
if not os.path.exists('static'):
    os.makedirs('static')

# Route for the home page
@app.route('/')
def home():
    return "Welcome to the AI-Powered Data Analysis Tool! Upload a dataset to get started."

# Route to handle file upload, basic analysis, and visualization
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    if not file.filename.endswith('.csv'):
        return jsonify({"error": "Unsupported file type. Please upload a CSV file."}), 400

    graph_type = request.form.get('graph_type', None)  # Optional graph_type parameter

    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file)

        # Perform basic analysis
        summary = {
            "columns": list(df.columns),
            "shape": df.shape,
            "missing_values": df.isnull().sum().to_dict(),
            "data_types": df.dtypes.apply(str).to_dict(),
            "head": df.head().to_dict()
        }

        save_path = os.path.join(app.root_path, 'static', 'visualization.png')

        # Generate graphs based on graph_type
        if graph_type is None or graph_type == 'heatmap':
            numeric_df = df.select_dtypes(include=['number'])
            if not numeric_df.empty:
                plt.figure(figsize=(10, 6))
                sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
                plt.title('Correlation Heatmap')
                plt.tight_layout()
                plt.savefig(save_path)
                plt.close()
                summary["visualization"] = "static/visualization.png"
            else:
                summary["visualization"] = "No numeric data available for correlation heatmap."

        elif graph_type == 'bar':
            if len(df.columns) < 1:
                return jsonify({"error": "Not enough columns for bar chart"}), 400

            plt.figure(figsize=(10, 6))
            df[df.columns[0]].value_counts().plot(kind='bar')
            plt.title(f'Bar Chart for {df.columns[0]}')
            plt.xlabel(df.columns[0])
            plt.ylabel('Counts')
            plt.tight_layout()
            plt.savefig(save_path)
            plt.close()
            summary["visualization"] = "static/visualization.png"

        elif graph_type == 'scatter':
            numeric_df = df.select_dtypes(include=['number'])
            if numeric_df.shape[1] < 2:
                return jsonify({"error": "Not enough numeric columns for scatter plot"}), 400

            plt.figure(figsize=(10, 6))
            plt.scatter(numeric_df.iloc[:, 0], numeric_df.iloc[:, 1])
            plt.title('Scatter Plot')
            plt.xlabel(numeric_df.columns[0])
            plt.ylabel(numeric_df.columns[1])
            plt.tight_layout()
            plt.savefig(save_path)
            plt.close()
            summary["visualization"] = "static/visualization.png"

        elif graph_type == 'line':
            if len(df.columns) < 2:
                return jsonify({"error": "Not enough columns for line chart"}), 400

            plt.figure(figsize=(10, 6))
            plt.plot(df[df.columns[0]], df[df.columns[1]])
            plt.title('Line Chart')
            plt.xlabel(df.columns[0])
            plt.ylabel(df.columns[1])
            plt.tight_layout()
            plt.savefig(save_path)
            plt.close()
            summary["visualization"] = "static/visualization.png"

        else:
            return jsonify({"error": f"Unsupported graph type: {graph_type}. Supported types are: heatmap, bar, scatter, line"}), 400

        return jsonify(summary)

    except Exception as e:
        return jsonify({"error": f"Failed to process the file. Details: {str(e)}"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
