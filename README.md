
# Autovit Scraper

This project is a Python-based scraper that collects car listings from the Autovit.ro website. The scraper gathers car details, including the link, name, price, year, mileage, fuel type, and location. The data is then saved into a CSV file for further use.

## Features

- Scrapes car listings from Autovit.ro with a price filter.
- Collects key car details such as full name, price, year, mileage, fuel type, and location.
- Supports pagination and will continue scraping new pages until no more pages are available.
- Saves scraped data into a CSV file for easy access and analysis.

## Requirements

To run this project, you'll need the following:

- Python 3.6+ (tested with Python 3.9)
- `requests` library for sending HTTP requests
- `beautifulsoup4` for parsing HTML
- `dataclasses` (Python 3.7+)
- `csv` for writing the data to a CSV file

You can install the necessary libraries with the following command:

```bash
pip install requests beautifulsoup4
```

## Setup

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/supermasina.git
cd supermasina
```

2. **Create a virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scriptsctivate`
```

3. **Install the dependencies:**

```bash
pip install requests beautifulsoup4
```

4. **Run the scraper:**

To start scraping, execute the `scraper.py` script. This will scrape car listings from the first few pages of Autovit.ro and save the results in a CSV file.

```bash
python scraper.py
```

## Scraper Details

- **Autovit Scraper Class**: The main class that interacts with the Autovit website and scrapes the data.
- **Pagination**: The script automatically navigates through all the available pages by checking for the "next" button in the pagination.
- **Car Data**: The scraper collects the following data for each car:
  - Link to the listing
  - Full name of the car
  - Price
  - Year
  - Mileage (km)
  - Fuel type
  - Location

The data is stored in a CSV file (`autovit_cars.csv`).

## Example Output

After running the scraper, you'll get a CSV file (`autovit_cars.csv`) with car listings like this:

```csv
link,full_name,price,year,mileage_km,fuel_type,location
https://www.autovit.ro/example-car,Volkswagen Golf 2021,20000,2021,10000,Gasoline,Bucharest
https://www.autovit.ro/example-car,Mercedes-Benz C-Class 2019,18000,2019,20000,Diesel,Cluj
...
```

## Contributing

Feel free to fork this project and submit pull requests. Contributions are always welcome!

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a new Pull Request.

