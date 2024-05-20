days = int(input())
doctors = 7
treated_patients = 0
untreated_patients = 0

for i in range(0, days):
    patients = int(input())
    if ((i + 1) % 3 == 0) and untreated_patients > treated_patients:
        doctors += 1
    if patients <= doctors:
       treated_patients += patients
    else:
       treated_patients += doctors
       untreated_patients += (patients - doctors)


print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
