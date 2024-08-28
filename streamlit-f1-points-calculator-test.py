import streamlit as st

# Initial Points
max_points = 295
lando_points = 225

# Points System for main races
points_system = {
    1: 25,
    2: 18,
    3: 15,
    4: 12,
    5: 10,
    6: 8,
    7: 6,
    8: 4,
    9: 2,
    10: 1
}

# Points System for sprint races
sprint_points_system = {
    1: 8,
    2: 7,
    3: 6,
    4: 5,
    5: 4,
    6: 3,
    7: 2,
    8: 1
}

# Race names including Sprint Races
races = [
    "Italy GP",
    "Azerbaijan GP",
    "Singapore GP",
    "US Sprint Race",
    "US GP",
    "Mexico GP",
    "Brazil Sprint Race",
    "Brazil GP",
    "Las Vegas GP",
    "Qatar Sprint Race",
    "Qatar GP",
    "Abu Dhabi GP"
]

st.title("2024 F1 Championship Fight Points Calculator")

st.write("Select the positions for Max Verstappen and Lando Norris, and choose who got the fastest lap for each race (except Sprint Races):")

# Initialize dictionaries to store race results
max_positions = {}
lando_positions = {}
fastest_lap = {}

# Initialize points for tracking during the race loop
current_max_points = max_points
current_lando_points = lando_points

# Create a table-like interface
for race in races:
    st.subheader(f"{race} Grand Prix")

    # Create two columns for positions
    cols = st.columns(2 if "Sprint" in race else 3)
    with cols[0]:
        max_positions[race] = st.selectbox(f"Max Verstappen's Position", [i for i in range(1, 21)], key=f"max_{race}")
    with cols[1]:
        lando_positions[race] = st.selectbox(f"Lando Norris's Position", [i for i in range(1, 21) if i != max_positions[race]], key=f"lando_{race}")

    # Fastest lap selection only for main races
    if "Sprint" not in race:
        with cols[2]:
            fastest_lap[race] = st.radio("Fastest Lap", ('None', 'Max Verstappen', 'Lando Norris'), key=f"fl_{race}")

    # Determine the points system to use
    if "Sprint" in race:
        points_system_used = sprint_points_system
    else:
        points_system_used = points_system

    # Calculate points for Max
    if max_positions[race] in points_system_used:
        current_max_points += points_system_used[max_positions[race]]
    if "Sprint" not in race and fastest_lap.get(race) == 'Max Verstappen' and max_positions[race] <= 10:
        current_max_points += 1

    # Calculate points for Lando
    if lando_positions[race] in points_system_used:
        current_lando_points += points_system_used[lando_positions[race]]
    if "Sprint" not in race and fastest_lap.get(race) == 'Lando Norris' and lando_positions[race] <= 10:
        current_lando_points += 1

    # Display updated points after each race except Abu Dhabi
    if race != "Abu Dhabi GP":
        st.write(f"**Points after {race}:**")
        st.write(f"Max Verstappen: {current_max_points} points")
        st.write(f"Lando Norris: {current_lando_points} points")

# Final standings after Abu Dhabi GP
st.write(f"**Final Championship Standings after all races entered:**")
st.write(f"Max Verstappen: {current_max_points} points")
st.write(f"Lando Norris: {current_lando_points} points")

# Determine who is leading
if current_max_points > current_lando_points:
    st.success("Max Verstappen is leading the championship!")
elif current_lando_points > current_max_points:
    st.success("Lando Norris is leading the championship!")
else:
    st.info("The championship is tied!")



