#! /urs/bin/env python
import utils

def main():
    """This program register information patients into a list validating some
      input values and computing others
      """
    
    name_regexp = "^[a-zA-Záéíóúñ ]{3,}$"
    age_regexp = "^100$|^1[89]$|^[2-9][0-9]$"
    email_regexp = "^[a-z1-9._]+@(gmail|hotmail|yahoo|outlook)(\.com|\.mx|\.edu)$"

    data = ["Name:", "Age:", "Email:"]
    regexp = [name_regexp, age_regexp, email_regexp]
    data_types = [str, int, str]
    
    requested_data = zip(data, regexp, data_types)
    
    input_data = utils.request_data(requested_data)
    utils.print_patients(input_data)

if __name__ == "__main__":
    main()
