speeds = [48,47,54,50,42,68,39,46]

speed_too_high = list(filter(lambda x:x>50, speeds))



print(f"Speed to high: {speed_too_high}")