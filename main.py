import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import matplotlib.patches as mpatches

try:
    # Reading the Data into a DataFrame
    file_path = r'.\GrowLocations.csv'
    data = pd.read_csv(file_path)
    print("Data loaded successfully:")
    print(data.head())  # Display the first few rows of the DataFrame to check data loading.

    # Removing Bad Values
    filtered_data = data[
        (data['Latitude'] >= -10.592) & (data['Latitude'] <= 1.6848) &
        (data['Longitude'] >= 50.681) & (data['Longitude'] <= 57.985)
    ]
    print(f"Data filtered: {filtered_data.shape[0]} entries kept")
    print(filtered_data.head())  # Check what data remains after filtering.

    # Plotting the Data Correctly
    map_image_path = r".\map7.png"
    map_image = Image.open(map_image_path)
    plt.figure(figsize=(10, 15))
    plt.imshow(map_image, extent=[-10.592, 1.6848, 50.681, 57.985])
    plt.scatter(filtered_data['Latitude'], filtered_data['Longitude'], color='blue', s=20, edgecolor='blue', label='Sensor Locations')
    plt.title('Plotting Grow Data')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    blue_patch = mpatches.Patch(color='blue')
    plt.grid(True)
    plt.show()

except FileNotFoundError as e:
    print(f"Error: File not found - {e}")
except Exception as e:
    print(f"An error occurred: {e}")
