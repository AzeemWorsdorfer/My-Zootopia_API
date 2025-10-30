# Zootopia API 

## Project Description

This project generates a dynamic HTML website displaying animal information. It is an updated version of the original Zootopia project.

Instead of using static files, this application fetches real-time animal data from an external API (API-Ninja) based on user input.

The project uses a modular architecture where data fetching (`data_fetcher.py`) is separate from website generation (`animals_web_generator.py`). The API key is securely managed using a `.env` file and the `python-dotenv` library.

## Usage

### Prerequisites
1.  **Python 3** installed.
2.  An **API Key** from [API Ninja](https://api-ninjas.com/).

### Setup
1.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
2.  **Create a `.env` file** in the root directory and add your API key:
    ```
    API_KEY='YOUR_ACTUAL_API_KEY'
    ```

### Run
Run the main script and follow the prompt to enter an animal name:
```bash
python3 animals_web_generator.py