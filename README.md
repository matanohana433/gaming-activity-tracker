# 🎮 Gaming Activity Tracker

## 🌟 Overview

The Gaming Activity Tracker is a Python application that uses the Pixela API to track and visualize gaming habits. Users can log gaming hours daily, update their data, and view trends over time using a visual graph.

## 🛠 Features
* **User Creation:** Automatically creates a user account on Pixela.
* **Graph Creation:** Sets up a customizable graph for tracking gaming hours.
* **Daily Logging:** Allows users to log the number of hours they played each day.
* **Data Updates:** Enables users to update the logged hours for any specific date.
* **Data Deletion:** Deletes logged data for specific dates.

## 📂 Project Structure


    .
    ├── main.py                 # Main Python script for interacting with Pixela API
    ├── requirements.txt        # Project dependencies 
    ├── README.md               # Project documentation
## 🔧 Setup Guide

**Prerequisites**

* Python 3.x installed.
* A Pixela account (or the app will create one for you).

**Installation**

1. Clone this repository:


        git clone https://github.com/matanohana433/gaming-activity-tracker.git
        cd gaming-activity-tracker
2. Create and activate a virtual environment (optional but recommended):

**Windows:**

    python -m venv venv
    venv\Scripts\activate
**macOS/Linux:**

    python3 -m venv venv
    source venv/bin/activate
3. Install dependencies:


        pip install -r requirements.txt
4. Set environment variables:

   * Create a .env file or set the variables manually:


            USERNAME=your_pixela_username
            TOKEN=your_pixela_token
## 🚀 Usage

1. **Create a Pixela User:** Uncomment and run the following code in main.py:


        response = requests.post(url=pixela_endpoint, json=user_params)
        print(response.text)
2. **Create a Graph:** Uncomment and run the graph creation code in main.py:


        graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
        print(graph_response.text)
3. **Add Daily Data:**

* Input the number of hours played when prompted:


      How many hours did you play today? 3.5

* The data will be added to the graph.

4. **Update Existing Data:** Uncomment and run the update pixel code in main.py:


        edit_pixel_response = requests.put(url=edit_pixel_endpoint, json=edit_pixel_params, headers=headers)
        print(edit_pixel_response.text)
5. **Delete Specific Data:** Uncomment and run the delete pixel code in main.py:


        delete_pixel_response = requests.delete(url=delete_pixel_endpoint, headers=headers)
        print(delete_pixel_response.text)
## 🌟 Key Features

1. **Dynamic Date Handling:**
   * Automatically logs today’s date for pixel creation.
   * Allows updates and deletions for specific dates.
2. **Customizable Graph:**
   * Choose graph name, unit, type, and color during setup.
3. **Easy Integration:**
   * Uses environment variables for secure and flexible authentication.

## 🚀 Future Enhancements

1. Add a user-friendly CLI or web interface.
2. Support multiple graph types for tracking different activities.
3. Integrate notifications or reminders for logging daily activity.

## 📬 Contact

For questions or collaboration:

* **Email:** matanohana433@gmail.com
* **GitHub:** matanohana433
