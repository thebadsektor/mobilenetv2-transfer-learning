import os
import shutil
import random

# Set the seed to ensure consistent results across runs
random.seed(42)

# Set the source directory and output directories
source_dir = 'data/dump/chair'
output_dirs = {
    'train': 'data/train/chair',
    'validation': 'data/validation/chair',
    'test': 'data/test/chair'
}

# Create output directories if they don't exist
for output_dir in output_dirs.values():
    os.makedirs(output_dir, exist_ok=True)

# Get a list of all the image files in the source directory
image_files = [f for f in os.listdir(source_dir) if f.lower().endswith(('.jpg', '.jpeg'))]

# Shuffle the image files
random.shuffle(image_files)

# Define the split ratios
train_ratio = 0.7
validation_ratio = 0.2
test_ratio = 0.1

# Calculate the number of images for each split
total_images = len(image_files)
train_count = int(total_images * train_ratio)
validation_count = int(total_images * validation_ratio)
test_count = total_images - train_count - validation_count

# Split the images
train_files = image_files[:train_count]
validation_files = image_files[train_count:train_count + validation_count]
test_files = image_files[train_count + validation_count:]

# Copy the images to their respective directories
for file in train_files:
    shutil.copy(os.path.join(source_dir, file), os.path.join(output_dirs['train'], file))

for file in validation_files:
    shutil.copy(os.path.join(source_dir, file), os.path.join(output_dirs['validation'], file))

for file in test_files:
    shutil.copy(os.path.join(source_dir, file), os.path.join(output_dirs['test'], file))

print(f'Split completed: {train_count} train, {validation_count} validation, {test_count} test images.')
