import pandas as pd
import matplotlib.pyplot as plt

# Load the Iris dataset
file_path = 'Iris.csv'  # Replace with the path to your CSV file
iris = pd.read_csv(file_path)

# Drop the 'Id' column as it's not needed for analysis
iris = iris.drop(columns=['Id'])

# Grouping the data by species to calculate the mean for each measurement
species_avg = iris.groupby("Species").mean()

# Step 1: Plotting Basics - Create a line plot of the average measurements for each species
plt.figure(figsize=(10, 6))  # Step 2: Figure and Axes

# Line plot for each feature's average value across species
plt.plot(species_avg.index, species_avg['SepalLengthCm'], label='Sepal Length', marker='o')
plt.plot(species_avg.index, species_avg['SepalWidthCm'], label='Sepal Width', marker='o')
plt.plot(species_avg.index, species_avg['PetalLengthCm'], label='Petal Length', marker='o')
plt.plot(species_avg.index, species_avg['PetalWidthCm'], label='Petal Width', marker='o')

# Step 3: Title, Labels, and Legends
plt.title("Average Measurements of Iris Species")
plt.xlabel("Species")
plt.ylabel("Average Measurement (cm)")
plt.legend()  # Adds a legend to the plot
plt.grid(True)  # Adding grid for better readability

# Display the plot
plt.show()
# Display the plot
plt.show()