import ip_function1

if __name__ == "__main__":
    city, country = ip_function1.get_location()
    info = str("The IP address is located in " + city + "(" + country +") ")
    print (info)