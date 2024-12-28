import json
with open("euro.json", "r") as file:
    rates = json.load(file)

def displayer(rates):
    rate_read = []
    for item in rates["rates"]:
        info = {}
        info["Date"] = item["effectiveDate"]
        info["Buying Rate"] = item["ask"]
        info["Selling Rate"] = item["bid"]
        rate_read.append(info)
    print(rate_read)
    result_string = f"""Date                   Buying Rate    Selling Rate
==================================================
                        """
    print(result_string)
    for item in rate_read:
        print(f"{item["Date"]}             {item["Buying Rate"]}         {item["Selling Rate"]}")

  

print(displayer(rates))