# Recipe Finder

A Flask application to find recipes based on ingredients and dietary restrictions.

## Features

- Input multiple ingredients
- Specify dietary restrictions (e.g., vegetarian, vegan, gluten-free)
- Display recipes with:
  - Recipe name
  - Photo
  - Ready in time
  - Missing ingredients
  - Link to full recipe

## Requirements

- Python 3.x
- Flask
- Requests

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/recipe-finder.git
    cd recipe-finder
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Replace `your_actual_spoonacular_api_key` with your Spoonacular API key in `app.py`.

5. Run the application:

    ```bash
    python app.py
    ```

6. Open your web browser and navigate to `http://127.0.0.1:5000`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
