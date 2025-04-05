import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tabulate import tabulate

def select_players(team1_data, team2_data):
    # Concatenate data of both teams
    all_teams_data = pd.concat([team1_data, team2_data])

    # Calculate average points for each player across matches
    if not all_teams_data.empty:  # Check if DataFrame is not empty
        all_teams_data['Average_Points'] = all_teams_data.iloc[:, 5:].mean(axis=1)

        # Filter players based on roles
        batsmen = all_teams_data[all_teams_data['Role'] == 'BAT']
        bowlers = all_teams_data[all_teams_data['Role'] == 'BALL']
        allrounders = all_teams_data[all_teams_data['Role'] == 'ALL']
        wicket_keepers = all_teams_data[all_teams_data['Role'] == 'WK']

        # Select top 4 batsmen, 4 bowlers, 2 all-rounders, and 1 wicket-keeper based on average points
        selected_batsmen = batsmen.nlargest(4, 'Average_Points')[['Player', 'Role', 'Team', 'Average_Points']]
        selected_bowlers = bowlers.nlargest(4, 'Average_Points')[['Player', 'Role', 'Team', 'Average_Points']]
        selected_allrounders = allrounders.nlargest(2, 'Average_Points')[['Player', 'Role', 'Team', 'Average_Points']]
        selected_wk = wicket_keepers.nlargest(1, 'Average_Points')[['Player', 'Role', 'Team', 'Average_Points']]

        # Combine all selected players
        selected_players = pd.concat([selected_batsmen, selected_bowlers, selected_allrounders, selected_wk])

        # Select captain based on the highest average points
        captain = all_teams_data.loc[all_teams_data['Average_Points'].idxmax(), 'Player']

        # Select vice-captain based on the second-highest average points
        vice_captain = all_teams_data.sort_values('Average_Points', ascending=False).iloc[1]['Player']

        return selected_players, captain, vice_captain
    else:
        return pd.DataFrame(), None, None


def generate_team():
    team1 = team1_var.get()
    team2 = team2_var.get()
        
    if team1 == "" or team2 == "":
        messagebox.showerror("Error", "Please select both teams")
        return
    
    team1_data = data[data['Team'] == team1]
    team2_data = data[data['Team'] == team2]
    selected_players, captain, vice_captain = select_players(team1_data, team2_data)
    result_text.config(state='normal')
    result_text.delete('1.0', tk.END)
    result_text.insert(tk.END, "Selected Players:\n")
    result_text.insert(tk.END, tabulate(selected_players, headers='keys', tablefmt='fancy_grid', showindex=False, floatfmt=(".4f"))) # type: ignore
    result_text.insert(tk.END, f"\n\nCaptain: {captain}\n")
    result_text.insert(tk.END, f"Vice-Captain: {vice_captain}\n")
    result_text.config(state='disabled')

# Load the dataset
data = pd.read_csv('D:\\IT & Tools\\Codes\\Project 1\\your_dataset.csv')

# Create the main window
root = tk.Tk()
root.title("TeamCraft")
root.geometry("600x660")

# Team selection labels and dropdowns
team1_label = ttk.Label(root, text="Select Team 1:")
team1_label.pack(pady=10)
team1_var = tk.StringVar()
# Remove inverted commas from team names
team1_values = [team.replace("'", "") for team in data['Team'].unique()]
team1_dropdown = ttk.Combobox(root, textvariable=team1_var, values=team1_values)
team1_dropdown.pack()

team2_label = ttk.Label(root, text="Select Team 2:")
team2_label.pack(pady=10)
team2_var = tk.StringVar()
# Remove inverted commas from team names
team2_values = [team.replace("'", "") for team in data['Team'].unique()]
team2_dropdown = ttk.Combobox(root, textvariable=team2_var, values=team2_values)
team2_dropdown.pack()

# Generate button
generate_button = ttk.Button(root, text="Generate Team", command=generate_team)
generate_button.pack(pady=10)

# Result display text
result_text = tk.Text(root, height=30, width=60)
result_text.pack(pady=10)
result_text.config(state='disabled')

root.mainloop()