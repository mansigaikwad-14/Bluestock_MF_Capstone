import requests
import pandas as pd

scheme_codes = {
    "HDFC_Top100": "125497",
    "SBI_Bluechip": "119551",
    "ICICI_Bluechip": "120503",
    "Nippon_Large_Cap": "118632",
    "Axis_Bluechip": "119092",
    "Kotak_Bluechip": "120841"
}

for scheme, code in scheme_codes.items():
    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)
    data = response.json()

    nav_df = pd.DataFrame(data["data"])

    nav_df.to_csv(f"{scheme}.csv", index=False)

    print(f"{scheme} downloaded successfully")

print("All NAV files downloaded.")