browser = str(input("Enter the browser name\n"))
browser = browser.lower()

match browser:
    case "chrome":
        print("Chrome is executed!")
    case "firefox":
        print("firefox browser is executed!")
    case _:
        print("No browser found")
