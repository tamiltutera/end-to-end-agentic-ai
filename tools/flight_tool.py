import os
import re
import certifi
import airportsdata
import pycountry
from dotenv import load_dotenv

load_dotenv()

os.environ["SSL_CERT_FILE"] = certifi.where()
os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()

API_KEY = os.environ.get("AVIATIONSTACK_API_KEY")

DEFAULT_ORIGIN_IATA = os.environ.get("DEFAULT_ORIGIN_IATA", "MAA")  # Default to Singapore Changi Airport (SIN)

BASE_URL = "http://api.aviationstack.com/v1/flights"
AIRPORTS = airportsdata.load("IATA")  # Load IATA airport data

COUNTRY_ALIASES = {
    "United States": "USA",
    "United Kingdom": "GBR",
    "South Korea": "KOR",
    "North Korea": "PRK",
    "Russia": "RUS",
    "Iran": "IRN",
    "Vietnam": "VNM",
    "Syria": "SYR",
    "Venezuela": "VEN",
    "Bolivia": "BOL",
    "Brunei": "BRN",
    "Czech Republic": "CZE",
    "Democratic Republic of the Congo": "COD",
    "Republic of the Congo": "COG",
    "Ivory Coast": "CIV",
    "Laos": "LAO",
    "Macedonia": "MKD",
    "Moldova": "MDA",
    "Palestine": "PSE",
    "Saint Kitts and Nevis": "KNA",
    "Saint Lucia": "LCA",
    "Saint Vincent and the Grenadines": "VCT",
    "Sao Tome and Principe": "STP",
    "India": "IND",
    "Taiwan": "TWN",
    "Tanzania": "TZA",
    "Vatican City": "VAT",
    "Venezuela": "VEN",
}