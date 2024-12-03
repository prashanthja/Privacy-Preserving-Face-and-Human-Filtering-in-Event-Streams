import pandas as pd
import numpy as np
import glob
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical

# Load event data files
file_paths = glob.glob("/media/lab_user/AIRLab-HDD/FES/train/*.txt")  # Adjust path to your event data files

event_data_list = []
for file in file_paths:
    # Load the event data file
    df = pd.read_csv(file, sep='\s+', header=None, names=["timestamp", "x", "y", "polarity"])    
    print(f"Preview of data from {file}:")
    print(df.head())
    
    # Calculate statistical features
    features = {
        "mean_x": df["x"].mean(),
        "mean_y": df["y"].mean(),
        "mean_polarity": df["polarity"].mean(),
        "std_x": df["x"].std(),
        "std_y": df["y"].std(),
        "std_polarity": df["polarity"].std(),
        "min_x": df["x"].min(),
        "min_y": df["y"].min(),
        "min_polarity": df["polarity"].min(),
        "max_x": df["x"].max(),
        "max_y": df["y"].max(),
        "max_polarity": df["polarity"].max(),
    }
    print(f"Features extracted from {file}: {features}")
    event_data_list.append(features)

# Convert features to a DataFrame
event_features_df = pd.DataFrame(event_data_list)
event_features_df.to_csv("/media/lab_user/AIRLab-HDD/event_features.csv", index=False)
print("Event features summary:")
print(event_features_df.describe())

# Load labels
labels_df = pd.read_csv("/media/lab_user/AIRLab-HDD/FES/train_list.txt", sep='\s+', header=None, names=["filename", "label"])
print("Labels loaded from train_list.txt:")
print(labels_df.head())

# Create a dictionary of labels
labels_dict = dict(zip(labels_df["filename"], labels_df["label"]))

# Match event files with their corresponding labels
event_labels = []
for file in file_paths:
    filename = file.split('/')[-1]  # Extract filename from full path
    label = labels_dict.get(filename, None)
    if label is not None:
        event_labels.append(label)
    else:
        print(f"Warning: No label found for {filename}")
        event_labels.append(None)

# Remove events without labels
valid_indices = [i for i, label in enumerate(event_labels) if label is not None]
event_features_df = event_features_df.iloc[valid_indices]
event_labels = [event_labels[i] for i in valid_indices]

# Encode labels
label_encoder = LabelEncoder()
encoded_labels = label_encoder.fit_transform(event_labels)
encoded_labels.to_csv("/media/lab_user/AIRLab-HDD/labels.csv", index=False)
print(f"Encoded labels: {encoded_labels[:5]}")

# Ensure there are valid labels for categorical conversion
if len(encoded_labels) == 0:
    raise ValueError("Encoded labels are empty, unable to proceed.")

# One-hot encode the labels
y = to_categorical(encoded_labels)
print(f"One-hot encoded labels:\n{y[:5]}")

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(event_features_df, y, test_size=0.2, random_state=42)
print(f"Training dataset shape: {X_train.shape}")
print(f"Test dataset shape: {X_test.shape}")
print(f"Number of classes: {y_train.shape[1]}")

# Build the model
model = Sequential()
model.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(y_train.shape[1], activation='softmax'))

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer=Adam(learning_rate=0.001), metrics=['accuracy'])

# Train the model
print("Training the model...")
history = model.fit(X_train, y_train, epochs=20, batch_size=32, validation_data=(X_test, y_test))

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test Loss: {loss:.4f}")
print(f"Test Accuracy: {accuracy:.4f}")
