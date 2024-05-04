import pandas as pd
import requests
import json 
import googlemaps
import streamlit as st

API_KEY = "AIzaSyDIpQcxrp3T6FKD9yBj1hHLZLIajGHGv5A"
MAPS_API_URL = "https://maps.googleapis.com/maps/api/distancematrix/json"

def read_csv_with_specific_columns (file_path, columns):
    data = pd.read_csv(file_path, usecols=columns)
    return data

food_file_path = "Food_Display_Table.csv"
food_columns = ["Display_Name", "Portion_Display_Name", "Calories"]
food_data = read_csv_with_specific_columns(food_file_path, food_columns)

exercise_file_path = "exercise_dataset.csv"
exercise_columns = ["Activity, Exercise or Sport (1 hour)", "Calories per kg"]
exercise_data = read_csv_with_specific_columns(exercise_file_path, exercise_columns)

class Food_Calories:
    @staticmethod
    def get_food(data=food_data):
        food_list = data['Display_Name'].unique().tolist()
        return food_list

    @staticmethod
    def filter_and_display_portion_names (food, data=food_data):
        filtered_data = data[data["Display_Name"] == food]
        portions = filtered_data["Portion_Display_Name"].unique()
        return portions

    @staticmethod
    def get_calories_by_portion (food, portion, data=food_data):
        filter_data = data[(data["Display_Name"] == food) & (data["Portion_Display_Name"] == portion)]
        calories = filter_data["Calories"].iloc[0]
        return calories
    
    @staticmethod
    def calculate_calories_for_item(food, portion, no_of_portions=1):
        calories = Food_Calories.get_calories_by_portion(food, portion)
        # total_calories = no_of_portions*calories
        return calories

    def calculate_total_intake_calories(food_list):
        total_calories = 0
        for food_item in food_list:
            total_calories = total_calories + Food_Calories.get_calories_by_portion(food_item["food_name"], food_item["food_portion"])
        return total_calories

class Calories_Burnt:

    @staticmethod
    def get_excercises(data=exercise_data):
        excercise_list = data['Activity, Exercise or Sport (1 hour)'].unique().tolist()
        return excercise_list
    
    @staticmethod
    def calories_burnt_per_excercise(time, weight, excercise, excercise_data=exercise_data):
        filter_excercise_data = excercise_data[(excercise_data["Activity, Exercise or Sport (1 hour)"] == excercise)]
        calories_burnt_per_kg = filter_excercise_data["Calories per kg"].iloc[0]
        calories_burnt_per_hour = calories_burnt_per_kg*weight
        calories_burnt = (calories_burnt_per_hour/60)*time
        return calories_burnt

    @staticmethod
    def calculate_total_calories_burnt(excercise_list, weight):
        total_calories_burnt = 0
        for excercise in excercise_list:
            total_calories_burnt = total_calories_burnt + Calories_Burnt.calories_burnt_per_excercise(excercise["exercise_duration"], weight, excercise["exercise_name"])
        return total_calories_burnt
    
    @staticmethod
    def get_remaining_calories(intake_calories, calories_burnt, calories_burnt_goal):
        intake_calories = intake_calories.item()
        calories_burnt = calories_burnt.item()
        remaining_calories = intake_calories - calories_burnt
        # remaining_calories = remaining_calories.item()
        calories_achieved = calories_burnt_goal - remaining_calories
        remaining_calories_percentage = ((calories_achieved)/remaining_calories)*100
        return calories_achieved, remaining_calories_percentage

class Map_Calories_Burnt:
    @staticmethod
    def convert_to_minutes(time_string):
        hours = 0
        minutes = 0
        parts = time_string.split()
        for ind in range(len(parts)):
            if parts[ind] == "hours":
                hours = int(parts[ind-1])
            elif parts[ind] == "mins":
                minutes = int(parts[ind-1])
        total_minutes = hours*60 + minutes
        return total_minutes

    @staticmethod
    def maps_calorie_calculator(duration, mode, weight):
        cycling_calorie_per_kg = 1.750729719
        walking_calorie_per_kg = 0.679710997
        if mode == "bicycling":
            calories_burnt = cycling_calorie_per_kg*weight
        elif mode == "walking":
            calories_burnt = walking_calorie_per_kg*weight
        minutes = Map_Calories_Burnt.convert_to_minutes(duration)
        actual_calories_burnt = (calories_burnt/60) * minutes
        return actual_calories_burnt

    @staticmethod
    def maps_distance_calculator(weight, source, destination, mode):
        gmaps = googlemaps.Client(key=API_KEY)
        response = gmaps.distance_matrix(source, destination, mode=mode)["rows"][0]["elements"][0]
        print("respone: ",response)
        # distance = response["distance"]["text"]
        duration = response["duration"]["text"]
        actual_calories_burnt = Map_Calories_Burnt.maps_calorie_calculator(duration, mode, weight)
        return actual_calories_burnt


if __name__ == "__main__":
    # food_file_path = "C:\\Users\\Ryanc\\OneDrive\\Desktop\\FatFinisher\\Food_Display_Table.csv"
    # food_columns = ["Display_Name", "Portion_Display_Name", "Calories"]
    # food_data = read_csv_with_specific_columns(food_file_path, food_columns)
    # number_of_food_items = int(input("Please Enter The Number of Food Items You Ate "))
    # count = 0
    # total_calories = 0.0
    # while count < number_of_food_items:
    #     food_calories = calculate_total_calories_for_item(food_data)
    #     total_calories = total_calories + food_calories
    #     count = count + 1
    # print("Total Calories For The Food = ", total_calories)

    # exercise_file_path = "C:\\Users\\Ryanc\\OneDrive\\Desktop\\FatFinisher\\exercise_dataset.csv"
    # exercise_columns = ["Activity, Exercise or Sport (1 hour)", "Calories per kg"]
    # exercise_data = read_csv_with_specific_columns(exercise_file_path, exercise_columns)
    # number_of_exercises =  int(input("Please Enter The Amount of Exercices That You Have Done "))
    # weight = float(input("Please Enter Your Weight in KGs "))
    # exercise_count = 0
    # total_calories_burnt = 0.0
    # while excercise_count < number_of_exercises:
    #     calories_burnt = calculate_total_calories_burnt_per_excercise(excercise_data, weight)
    #     total_calories_burnt = total_calories_burnt + calories_burnt
    #     exercise_count = excercise_count + 1
    
    # print("Total Calories For All Excercises ", total_calories_burnt)

    # calories_burnt_goal = float(input("What Is Your Goal of Calories To Be Burnt? "))
    # calories_achieved, remaining_calories_percentage = get_remaining_calories(total_calories, total_calories_burnt, calories_burnt_goal)
    # if calories_achieved < 0:
    #     print("You Have Exceeded Your Calorie Count ", abs(calories_achieved))
    # else:
    #     print("The Calories You Have Achieved Are ", calories_achieved)
    #     print("The Percentage Of Remaining Calories Are ", remaining_calories_percentage)
    # weight = 65
    # actual_calories_burnt = maps_distance_calculator(weight)
    print("hah")