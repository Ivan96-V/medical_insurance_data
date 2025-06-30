import csv


age_row = []
sex_row = []
bmi_row = []
children_row = []
smoker_row = []
region_row = []
charge_row = []

# read csv file and extract rows
with open("insurance.csv", newline="") as insurance_file:
    # print(insurance_file.read())
    data = csv.DictReader(insurance_file)
    for row in data:
        age_row.append(row["age"])
        sex_row.append(row["sex"])
        bmi_row.append(row["bmi"])
        children_row.append(row["children"])
        smoker_row.append(row["smoker"])
        region_row.append(row["region"])
        charge_row.append(row["charges"])

# transform str list on int or float list
age_row_int = [int(age) for age in age_row]
bmi_row_float = [float(bmi) for bmi in bmi_row]
children_row_int = [int(children) for children in children_row]
charge_row_float = [float(charge) for charge in charge_row]

# Transform 2 list in zip dictionary
def transform_list_to_dict(list1, list2):
    lists_zip= zip(list1, list2)
    dict_zip = {key: value for key, value in lists_zip}
    return dict_zip


# Function to calculate AVG age
def avg_calculation(row_list):
    total_sum = 0
    for num in row_list:
        total_sum += num
    avg = total_sum / len(row_list)
    return avg

age_avg = round(avg_calculation(age_row_int))
print(f"Average age is: {age_avg}")

print("*" * 50)
print("\n")

northeast_list = []
northwest_list = []
southeast_list = []
southwest_list = []

# function to count how many resident live on each region
def region_count_function():
    for region in region_row:
        if region == "northeast":
            northeast_list.append(region)
            northeast_len = len(northeast_list)
        elif region == "northwest":
            northwest_list.append(region)
            northwest_len = len(northwest_list)
        elif region == "southeast":
            southeast_list.append(region)
            southeast_len = len(southeast_list)
        elif region == "southwest":
            southwest_list.append(region)
            southwest_len = len(southwest_list)

    return (f"Residents on northeast region has total of {northeast_len}\n"
            f"Residents on northwest region has total of {northwest_len}\n"
            f"Residents on southeast region has total of {southeast_len}\n"
            f"Residents on southwest region has total of {southwest_len}\n")

print(region_count_function())

print("\n")
print("*" * 50)
print("\n")

# Calculation regarding if smokers pay more on insurance cost than non-smokers
def smoker_charges():
    smoker_charge_zip = zip(smoker_row, charge_row)
    dict_smoker_charges = {key:value for key, value in smoker_charge_zip}
    max_smoker = max(dict_smoker_charges.values())
    min_smoker = dict_smoker_charges['no']
    return f"Total charges on residents who smoke is: ${max_smoker} vs non_smokers: ${min_smoker}"

print(smoker_charges())

print("\n")
print("*" * 50)
print("\n")

# Calculation focus on if resident has more or less children insurance cost can increment
def children_cost():
    children_cost_zip = zip(children_row_int, charge_row_float)
    dict_children_charges = {key:value for key, value in children_cost_zip}
    sort_dict = dict(sorted(dict_children_charges.items()))
    print(f"Upon calculation, Residents who doesn't has children pay more on insurance, \n"
          f"this is total charges for residents who has no children: ${max(sort_dict.values())}")

children_cost()

print("\n")
print("*" * 50)
print("\n")

# BMI average for every resident
bmi_avg = round(avg_calculation(bmi_row_float), 2)
print(f"Average BMI is: {bmi_avg}")
print(f"Max BMI: {max(bmi_row_float)}\n"
      f"Min BMI: {min(bmi_row_float)}")

# this is dictionary with key: bmi, and values of sex
sex_bmi = transform_list_to_dict(bmi_row_float, sex_row )

bmi_male = []
bmi_female = []
for bmi in sex_bmi.items():
    if bmi[1] == "male":
        bmi_male.append(bmi[0])
    elif bmi[1] == "female":
        bmi_female.append(bmi[0])

# calculate AVG BMI per sex
total_bmi_male = 0
total_bmi_female = 0

# average BMI for male
for male in bmi_male:
    total_bmi_male += male
avg_bmi_male =round(total_bmi_male / len(bmi_male), 2)

# average BMI for female
for female in bmi_female:
    total_bmi_female += female
avg_bmi_female =round(total_bmi_female / len(bmi_female), 2)
print("Data shown by sex:")
print(f"Male BMI AVG: {avg_bmi_male}")
print(f"Female BMI AVG: {avg_bmi_female}")
print(f"Max BMI for male {max(bmi_male)}")
print(f"Min BMI for male {min(bmi_male)}")
print(f"Max BMI for female {max(bmi_female)}")
print(f"Min BMI for female {min(bmi_female)}")

print("\n")
print("*" * 50)
print("\n")



