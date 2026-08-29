def validate_filter(run_date, run_time, type_of_distance, run_distance, training_type):

    training_type = training_type.strip().title()
    type_of_distance = type_of_distance.strip().title()

    if training_type == "Yoga" or training_type == "Strength Conditioning":
        run_distance = 0.0
        type_of_distance = "None"

    if run_time <= 0 or run_distance <= 0:
        print("Value needs to be greater than 0")

    if run_distance > 0:
        calculated_pace = run_time / run_distance
    else:
        calculated_pace = 0.0

    return run_date, run_time, type_of_distance, run_distance, training_type, calculated_pace