import os
import shutil
import pandas as pd

# Paths
wav_folder_path = "wavfiles"
csv_file_path = "bird_songs_metadata.csv"
output_folder_path = "audio"

# Read the CSV file
df = pd.read_csv(csv_file_path)

# Loop through each row in the CSV
for index, row in df.iterrows():
    file_id = str(row['id'])  
    species = row['species'] 
    
    # Find the wav file with this ID
    wav_file_name = f"{file_id}.wav"
    wav_file_path = os.path.join(wav_folder_path, wav_file_name)
    
    # Check if the wav file exists
    if os.path.exists(wav_file_path):
        # Create a folder for the species if it doesn't exist
        species_folder_path = os.path.join(output_folder_path, species)
        os.makedirs(species_folder_path, exist_ok=True)
        
        # Move the file to the species folder
        shutil.move(wav_file_path, species_folder_path)
        print(f"Moved: {wav_file_name} to {species_folder_path}")
    else:
        print(f"File not found: {wav_file_name}")

print("Organization complete!")
