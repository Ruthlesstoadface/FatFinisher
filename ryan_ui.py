import streamlit as st
from collections import defaultdict
from ryan_app import Food_Calories, Calories_Burnt, Map_Calories_Burnt

def main_page_ui():
    st.title("Fat Finisher")
    st.subheader("Track Calories and Excercises")
    st.divider()
    selecting_option = st.selectbox("Choose a Feature ", ["Calorie Tracker", "Exercise Tracker", "Distance and Calorie Tracker via Maps"])
    if selecting_option == "Calorie Tracker":
        st.header("Calorie Tracker")
        # food_data = {
        #     "Apple": {"calories": 95, "portion_sizes": {"Small": 100, "Medium": 180, "Large": 250}},
        #     "Banana": {"calories": 105, "portion_sizes": {"Small": 118, "Medium": 131, "Large": 169}},
        # }
        food_items = []
        num_food_items = st.number_input("Enter the Number of Food Items ", min_value = 1)
        for foodnumber in range(num_food_items):
            value = {}
            # food_name = st.selectbox(f"Food Item {foodnumber+1}", list(food_data.keys()), key = f"food_name_{foodnumber+1}" )
            food_name = st.selectbox(f"Food Item {foodnumber+1}", Food_Calories.get_food(), key = f"food_name_{foodnumber+1}" )
            food_portion = st.selectbox(f"Portion for {food_name}", list(Food_Calories.filter_and_display_portion_names (food_name)), key = f"food_portion_{foodnumber+1}" )
            value["food_name"]=food_name
            value["food_portion"]=food_portion
            food_items.append(value)
        if st.button("Calculate Calories"):
            total_calories = Food_Calories.calculate_total_intake_calories(food_items)
            print("f",food_items)
            st.success("Total Intake Calories are " + str(total_calories))
    elif selecting_option == "Exercise Tracker":
        st.header("Exercise Tracker")
        # exercise_data = {"Running": {"calories_per_minute": 10}, "Swimming": {"calories_per_minute": 8}, "Cycling": {"calories_per_minute": 7}}
        weight = st.number_input("Enter Your Weight in kg ", min_value = 1)
        num_exercises = st.number_input("Enter the Amount of Exercises ", min_value = 1)
        exercise_details = []
        for exercisenumber in range(num_exercises):
            temp_value = {}
            exercise_name = st.selectbox(f"Select Excercise {exercisenumber + 1}", Calories_Burnt.get_excercises(), key = f"exerise_name_{exercisenumber+1}")
            exercise_duration = st.number_input(f"Enter the Amount of Time Exercising in Minutes ", min_value = 0, key = f"exercise_duration_{exercisenumber+1}")
            temp_value["exercise_name"] = exercise_name
            temp_value["exercise_duration"] = exercise_duration
            exercise_details.append(temp_value)
        if st.button("Calculate Total Calories Burnt"):
            total_burnt_calories = Calories_Burnt.calculate_total_calories_burnt(exercise_details, weight)
            print("exercise_details", exercise_details)
            st.success("Total Burnt Calories are " + str(total_burnt_calories))
    elif selecting_option == "Distance and Calorie Tracker via Maps":
        st.header("Distance and Calorie Tracker via Maps")
        weight = st.number_input("Enter Your Weight in kg ", min_value = 1)
        source = st.text_input("Please Enter the Starting Location ")
        destination = st.text_input("Please Enter the Ending Location ") 
        map_modes = ["bicycling", "walking"]
        selected_mode = st.radio("Which Method of Travelling Did You Use? ", map_modes, key = "selected_mode", index = 0)
        # Map_Calories_Burnt.show_map_with_calories(source, destination, selected_mode, weight)
        if st.button("Calculate Calories Burnt"):
            map_burnt_calories = Map_Calories_Burnt.maps_distance_calculator(weight, source, destination, selected_mode)
            st.success("Total Calories Burnt while " + selected_mode + " are " + str(map_burnt_calories))
    with st.sidebar:
        st.title("Fat Finisher")
        st.subheader("Faster not Fatter")
        st.markdown(
            """Hi, my name is Ryan Clark and I am the creator of this application, Fat Finisher. I am 16 years old, and I am in 10th grade right now. I’ve always had a passion pertaining to coding and game designing. I wanted to create an app tackling the problems with obesity, and allow those people help losing weight along with tracking their diet plans. This app helps track weight loss and weight gain by calculating meal plans and exercise plans."""
        )


    # Footer content (HTML for styling)
    footer_html = """
    <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #000000;
            color: white;
            text-align: center;
            padding: 10px;
        }
    </style>
    <div class="footer">
        <p>© 2024 - Made with Streamlit</p>
    </div>
    """

    st.markdown(footer_html, unsafe_allow_html=True)

    # Ensure content is displayed above the footer
    st.write(" ")  # Add an empty space to push content up


if __name__ == "__main__":
    main_page_ui()