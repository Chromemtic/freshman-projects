from validate_filter import validate_filter

# Receives the input
run_date = str(input("Today's date: "))
run_time = float(input("How long was today's run: "))
type_of_distance = str(input("What type of distance was today's run in: "))
run_distance = float(input("How much distance was today's run: "))
training_type = str(input("What is today's training type: "))

run_date, run_time, type_of_distance, run_distance, training_type, calculated_pace = validate_filter(run_date, run_time, type_of_distance, run_distance, training_type)

#Writes the data logged
print(f"Date: {run_date} | Time ran for: {run_time} | Distance type: {type_of_distance} | Distance: {run_distance} | Pace: {calculated_pace:.2f} | Training type: {training_type}")

with open("training_database.txt", "a") as file:
    file.write(f"Date: {run_date} | Time ran for: {run_time} | Distance type: {type_of_distance} | Distance: {run_distance} | Pace: {calculated_pace:.2f} | Training type: {training_type}\n")

