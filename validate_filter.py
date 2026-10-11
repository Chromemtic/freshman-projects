# Defines the main data cleaning process to clean raw text and calculate the pacing
def validate_filter(run_date, run_time, type_of_distance, run_distance, training_type):

    # Removes spaces and capitalizes written data for the training type and distance type
    training_type = training_type.strip().title()
    type_of_distance = type_of_distance.strip().title()

    # Overwrites the distance to zero and distance type to none for yoga sessions
    if training_type == "Yoga":
        run_distance = 0.0
        type_of_distance = "None"

    # Clears out distance and type of distance for strength training sessions if an invalid or zero distance is entered.
    if training_type == "Strength Conditioning" and run_distance <= 0:
        type_of_distance = "None"
        run_distance = 0.0

    # Displays an error message to the terminal if the duration or distance fall below valid
    if run_time <= 0 or run_distance <= 0:
        print("Value needs to be greater than 0")

    # calculate the pacing if a valid running distance has been entered
    if run_distance > 0:
        calculated_pace = run_time / run_distance
    else:
        calculated_pace = 0.0

    # Sends the finalized, clean data and the calculated pacing back to the main tracking engine
    return run_date, run_time, type_of_distance, run_distance, training_type, calculated_pace