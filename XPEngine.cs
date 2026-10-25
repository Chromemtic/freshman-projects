// This engine only functions with cross_country_run_tracker.py and requires the dotnet run method to execute

// Loads the stanard toolsets of c#
using System;

// Enables file management from the computer you are on
using System.IO;

// Keeps the backend tracker running without crashing
using System.Runtime.ConstrainedExecution;

class TrackXPEngine
{
    static void Main()
    {
        // Reads the logged traning files and counts the total lines to find where the data ends
        string[] allLines = File.ReadAllLines("training_database.txt");
        int lastIndex = allLines.Length - 1;
        while (lastIndex >= 0 && string.IsNullOrWhiteSpace(allLines[lastIndex]))
        {
            lastIndex--;
        }
        string pythonData = allLines[lastIndex];
       
        string[] workoutField = pythonData.Split('|');

        string date = workoutField[0].Replace("Date: ","").Trim();
        string trainingType = workoutField[5].Replace(" Training type: ","").Trim();
        string rawTime = workoutField[1].Replace(" Time ran for: ","").Trim();
        double timeSpent = double.Parse(rawTime);

        double baseXp_PerMinute = 10;
        double multiplier = 1.0d;

        if (trainingType == "Strength Conditioning")
        {
            multiplier = 2.0d;
        }
        else if (trainingType == "5K Race")
        {
            multiplier = 1.5d;
        }

        double FinalXPEarned = timeSpent * baseXp_PerMinute * multiplier;

        Console.WriteLine(date);
        Console.WriteLine(FinalXPEarned);

        string saveLogExp = date + " | " + trainingType + " | Earned: +" + FinalXPEarned + " Xp\n";
        File.AppendAllText("player_progression_log.txt", saveLogExp);
    }
}
