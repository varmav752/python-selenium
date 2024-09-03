#!/bin/bash

# Step 1: Install Python packages
echo "Installing Python dependencies..."
pip3 install selenium behave behave-html-formatter

# Step 2: Download ChromeDriver
echo "Downloading ChromeDriver..."
curl -O https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip

# Step 3: Unzip ChromeDriver
echo "Unzipping ChromeDriver..."
unzip chromedriver_linux64.zip

# Step 4: Set ChromeDriver path
echo "Setting up ChromeDriver path..."
export PATH=$PATH:$(pwd)

# Step 5: Run behave tests
echo "Running Behave tests..."
behave

# Keep the shell window open after running
exec $SHELL
