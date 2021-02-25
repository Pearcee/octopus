# octopus
Agile Octopus
    python3 -m venv myvenv
    source myvenv/bin/activate
    pip install -U python-dotenv
    start .env file with
        api_key = "sk_live_......"
        url_tarif = "https://api.octopus.energy/v1/products/AGILE-18-02-21/electricity-tariffs/E-1R-AGILE-18-02-21-N/standard-unit-rates/"
        url_meter = "https://api.octopus.energy/v1/electricity-meter-points/1800020668720/meters/19L3278767/consumption/"


python -m pip freeze > requirements.txt
    python -m pip install -r requirements.txt
