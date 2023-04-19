# Chest X-Ray Disease Detection using ChexNet and Flask

This repository contains the code for a web-based tool that detects and diagnoses 12 chest diseases from X-ray images using the ChexNet model and Flask web framework. By following the provided code and instructions, you can create your own chest disease detection tool.

## Getting Started

To get started, follow these steps:

1. Clone the repository, change to the repository's directory, create a virtual environment, and activate it:

    ```bash
    git clone https://github.com/imad-ict/ChestDiseaseDetection.git
    cd ChestDiseaseDetection
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Download the ChexNet model weight and place the `weights.h5` file in the project's root directory.

4. Run the Flask web app:

    ```bash
    python app.py
    ```

5. Access the web app by opening a browser and navigating to `http://127.0.0.1:5000/`.

## Usage

1. On the main page, click the "Choose File" button to upload a chest X-ray image (in JPEG, PNG, or any other supported format).
2. Click the "Diagnose" button to submit the image.
3. The web app will display a table with the predicted probabilities for each of the 12 chest diseases.

## Customizing the Web App

You can customize the web app by modifying the following files:

- `app.py`: This file contains the Flask web app's main code. You can adjust the routes or add new ones as needed.
- `chexnet.py`: This file contains the ChexNet model implementation. You can modify it to use a different model or change the preprocessing steps.
- `templates/index.html`: This file contains the main page's HTML template. You can customize the layout or add additional input fields.
- `templates/result.html`: This file contains the results page's HTML template. You can customize the layout or add more information about the predictions.
- `static/css/styles.css`: This file contains the CSS styles for the web app. You can modify the styles to change the appearance of the app.

## Contributing

If you would like to contribute to this project, please submit a pull request with your proposed changes. We appreciate your help in improving the ChestDiseaseDetection web app.

## License

This project is licensed under the MIT License. See the (LICENSE) file for details.
