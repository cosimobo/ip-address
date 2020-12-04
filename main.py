import ip_function
import csv_manager
import databasemanager
import argparse

ip_address = "1.2.3.4"
csv_path = "data/ip_data.csv"
database_path = 'data/databasemanager.db'

databasemanager.db_creation(database_path)

def parse_arguments():
    parser=argparse.ArgumentParser(
            description="IP ADDRESS prject")
    parser.add_argument ("ip_address", type=str,
                         help= "Insert an IP Address",
                         default=None)
    parser.add_argument('-u', help="username name (requires -p)",
                         default=None)
    parser.add_argument('-p', help="username password",
                         default=None)

    group=parser.add_mutually_exclusive_group()
    group.add_argument("-q", "--quiet", action="store_true", help ="print quiet")
    group.add_argument("-v", "--verbose", action="store_true", help="print verbose")
    args = parser.parse_args()

    return args

if __name__ == "__main__":
    args = parse_arguments()
    if databasemanager.check(args.u,args.p):
        city, country = ip_function.get_location(args.ip_address)
        info = str("The IP ADDRESS "+ args.ip_address + " is located in "
                + city + " (" +  country +") ")
        print (info)
        #PARTE DI SCUCCATO
        csv_manager.write_data(csv_path,ip_address,city,country)
