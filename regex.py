import csv
from functions import name_normalization, remove_duplicates, change_phone, change_name

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ

correct_name_list = name_normalization(contacts_list)
no_duplicates_list = remove_duplicates(correct_name_list)

pattern_phone = r"(\+7|8)\s*\(*(\d{3})\)*[-\s]*(\d{3})[-\s]*(\d{2})[-\s]*(\d{2})\s*\(*([доб.]{0,4})\s*(\d{4})*\)*"
substitution_phone = r"+7(\2)-\3-\4-\5 \6\7"

pattern_name = r"^(\w+)(\s*)(\,?)(\w+)(\s*)(\,?)(\w*)(\,?)(\,?)(\,?)"
substitution_name = r"\1\3\10\4\6\9\7\8"

new_list = []
for row in no_duplicates_list:
    make_str = ",".join(row)
    new_list.append(change_phone(pattern_phone, substitution_phone, make_str))

new_list_2 = []
for row in new_list:
    make_str = ",".join(row)
    new_list_2.append(change_name(pattern_name, substitution_name, make_str))

# TODO 2: сохраните получившиеся данные в другой файл

if __name__ == "__main__":
    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=",")
        datawriter.writerows(new_list_2)
