import json
data = {"table":"C","currency":"euro","code":"EUR","rates":[{"no":"241/C/NBP/2024","effectiveDate":"2024-12-12","bid":4.2240,"ask":4.3094},{"no":"242/C/NBP/2024","effectiveDate":"2024-12-13","bid":4.2234,"ask":4.3088},{"no":"243/C/NBP/2024","effectiveDate":"2024-12-16","bid":4.2254,"ask":4.3108},{"no":"244/C/NBP/2024","effectiveDate":"2024-12-17","bid":4.2195,"ask":4.3047},{"no":"245/C/NBP/2024","effectiveDate":"2024-12-18","bid":4.2211,"ask":4.3063},{"no":"246/C/NBP/2024","effectiveDate":"2024-12-19","bid":4.2225,"ask":4.3079},{"no":"247/C/NBP/2024","effectiveDate":"2024-12-20","bid":4.2097,"ask":4.2947},{"no":"248/C/NBP/2024","effectiveDate":"2024-12-23","bid":4.2243,"ask":4.3097},{"no":"249/C/NBP/2024","effectiveDate":"2024-12-24","bid":4.2261,"ask":4.3115},{"no":"250/C/NBP/2024","effectiveDate":"2024-12-27","bid":4.2312,"ask":4.3166}]}
filename = "euro.json"
with open(filename, "w") as file:
    json.dump(data, file, indent=4)
    