import re

def request_data(request_data, title="Introduce values as requested:\n"):
    """Request data from the user from standar input
    
    Parameters
    ----------
    request_data : list containing tuples (i.e. (string, regexp )) with a "string" 
    corresponding to value requested and the "regexp" corresponding to the regular 
    expresion that will be used to validate the data

    Return
    ------
    input_data : a list with the values gathered from the user. In the same order as the
    request_data and properly validated

    """

    patients = []
    value = None
    print(title)
    request_data = list(request_data)
    while True:
        patient = []
        try:
            for idx in range(len(request_data)):
                var_name = request_data[idx][0]
                regexp = request_data[idx][1]
                data_type = request_data[idx][2]

                matcher = re.compile(regexp)
                
                while True:
                    value = input(var_name)
                    match = matcher.match(value)

                    if match:
                        if data_type is int:
                            value = int(value)
                        elif data_type is str:
                            value = str(value)
                        patient.append((var_name, value))
                        break
                    else:
                        print("The value", value, "does not fulfill the requirements (regular expresion) ", regexp)
            
            patients.append(patient)

            add_patient = input("Add new patient[y|n]?: ")
            if  add_patient.lower() == "n" or add_patient.lower() == "no":
                break
        except EOFError as err:
            print("\nProgram finished ... bye")
            break
    
    return patients


def print_patients(patients):
    """Print on screen the list of participants passed in 'participants'
    
    Parameters
    ----------
    participants: list of the information of the participants organized on a list
    
    """

    for idx, patient in enumerate(patients):
        print("Participant ", idx)
        for var_name, value in patient:
            print("\t", var_name, value)