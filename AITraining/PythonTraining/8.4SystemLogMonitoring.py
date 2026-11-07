
arr = ["INFO", "DEBUG", "WARNING", "ERROR", "INFO", "CRITICAL", "WARNING"] 

for str in arr:
    if str == "INFO":
        continue
    if str == "CRITICAL":
        break
    if str == "WARNING" or str == "ERROR":
        print(str)
