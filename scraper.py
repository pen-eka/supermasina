import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass, asdict
from typing import List
import csv

@dataclass
class Car:
    link: str
    full_name: str
    price: str
    year: str
    mileage_km: str
    fuel_type: str
    location: str

class AutovitScraper:
    def __init__(self, max_price: int) -> None:
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        }
        self.max_price = max_price
        self.website = "https://www.autovit.ro/autoturisme"

    def scrape_all_pages(self) -> List[Car]:
        cars = []
        page_number = 1  # Start from page 1
        while True:
            print(f"Scraping page {page_number}...")
            current_website = f"{self.website}?search%5Bfilter_float_price%3Ato%5D={self.max_price}&search%5Badvanced_search_expanded%5D=true&page={page_number}"
            new_cars = self.scrape_cars_from_current_page(current_website)
            if new_cars:
                cars += new_cars
                page_number += 1  # Move to the next page
            else:
                # If no cars are found, check if the "Next" button exists.
                print("No cars found on this page or pagination reached the end.")
                break
        return cars

    def scrape_cars_from_current_page(self, current_website: str) -> List[Car]:
        try:
            response = requests.get(current_website, headers=self.headers).text
            soup = BeautifulSoup(response, "html.parser")
            cars = self.extract_cars_from_page(soup)
            return cars
        except Exception as e:
            print(f"Problem with scraping website: {current_website}, reason: {e}")
            return []

    def extract_cars_from_page(self, soup: BeautifulSoup) -> List[Car]:
        cars_list = soup.find_all("article", class_="ooa-1yux8sr e15xeixv0")
        list_of_cars = []
        for car in cars_list:
            try:
                link = car.find("a", class_="ooa-mtc8pf")["href"]
                full_name = car.find("p", class_="e2z61p70").text.strip() if car.find("p", class_="e2z61p70") else "N/A"
                price = car.find("h3", class_="e6r213i1").text.strip() if car.find("h3", class_="e6r213i1") else "N/A"
                
                # Safely extracting year, mileage, fuel type, and engine capacity
                year = car.find("dd", {"data-parameter": "year"}).text.strip() if car.find("dd", {"data-parameter": "year"}) else "N/A"
                mileage_km = car.find("dd", {"data-parameter": "mileage"}).text.strip() if car.find("dd", {"data-parameter": "mileage"}) else "N/A"
                fuel_type = car.find("dd", {"data-parameter": "fuel_type"}).text.strip() if car.find("dd", {"data-parameter": "fuel_type"}) else "N/A"
                
                # Extract location (if available)
                location = car.find("p", class_="ooa-gmxnzj").text.strip() if car.find("p", class_="ooa-gmxnzj") else "N/A"

                list_of_cars.append(
                    Car(
                        link=link,
                        full_name=full_name,
                        price=price,
                        year=year,
                        mileage_km=mileage_km,
                        fuel_type=fuel_type,
                        location=location
                    )
                )
            except Exception as e:
                print(f"Error msg: {e}")
        return list_of_cars

    def is_next_page_available(self, soup: BeautifulSoup) -> bool:
        """ Check if the next page exists by looking for the "Next" button in pagination. """
        next_button = soup.find("li", class_="next")
        return next_button is not None

def write_to_csv(cars: List[Car]) -> None:
    with open("autovit_cars.csv", mode="w", newline="") as f:
        fieldnames = [
            "link",
            "full_name",
            "price",
            "year",
            "mileage_km",
            "fuel_type",
            "location"
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for car in cars:
            writer.writerow(asdict(car))

def scrape_autovit() -> None:
    max_price = 20000  # Set max price for cars
    scraper = AutovitScraper(max_price)
    cars = scraper.scrape_all_pages()  # Scrape all pages dynamically
    write_to_csv(cars)

if __name__ == "__main__":
    scrape_autovit()
