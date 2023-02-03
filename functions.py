import re


def name_normalization(rows):
    result = [
        " ".join(employee[0:3]).split(" ")[0:3] + employee[3:7] for employee in rows
    ]
    return result


def remove_duplicates(correct_name_list):
    no_duplicates = []
    for compared in correct_name_list:
        for employee in correct_name_list:
            if compared[0:2] == employee[0:2]:
                list_employee = compared
                compared = list_employee[0:2]
                for i in range(2, 7):
                    if list_employee[i] == "":
                        compared.append(employee[i])
                    else:
                        compared.append(list_employee[i])
        if compared not in no_duplicates:
            no_duplicates.append(compared)

    return no_duplicates


def change_phone(pattern, substitution, text):
    new_format = re.sub(pattern, substitution, text)
    result = new_format.split(",")
    return result


def change_name(pattern, substitution, text):
    new_format = re.sub(pattern, substitution, text)
    result = new_format.split(",")
    return result
