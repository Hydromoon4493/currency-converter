# Currency Converter

A currency converter application that allows users to convert between different currencies using real-time exchange rates. The project supports both a web-based interface and a GUI configuration.

## Features
- Converts between multiple real-world and fictional currencies
- Fetches real-time exchange rates using Open Exchange Rates API
- Supports USD, Euro, Yen, other real currencies in addition to many fictional currencies:
  - Galactic Credit Standard (Star Wars)
  - Imperial Credits (Star Wars)
  - Galleons (Harry Potter)
  - Dracma (Greek Mythology)
- Web-based interface using Flask

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/Hydromoon4493/currency-converter
   cd currency-converter
   ```
2. Install required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Configuration
1. Obtain an API ID from Open Exchange Rates.
2. Add a .env file to your currency-converter dicrectory and enter ```API_ID="your_api_id_here"```

## Running the Application
Run the following command:
```sh
python app.py
```
Then, open `http://127.0.0.1:5000/` in a web browser.

## Exchange Rates
Custom rates for fictional currencies:
- 1 Galactic Credit Standard (GCS) = 1.2 USD
- 1 Imperial Credit = 0.8 GCS
- 1 Galleon = 5 USD
- 1 Dracma = 1 USD

## File Structure
```
/currency-converter
│── app.py              # Python app
│── index.html          # Frontend for the web interface
│── styles.css          # Styling for the web interface
│── requirements.txt    # Python dependencies
│── README.md           # Project documentation
│── .env                # Open Exchange Rate API ID
```
## Acknowledgements
This project was created with assistance of OpenAI's ChatGPT, which helped generate the code, structure, and logic for this project.

## Future Improvements
- Add more fictional and real-world currencies
- Add a tkinter based GUI mode
- Support for historical exchange rates

## License
This project is licensed under the MIT License.

