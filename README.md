# Near Real Time Air Quality Index Finder
These python script will facilitate you in fetching the air quality status for your Point of Intereset (POI)from the neareby operating CAAQMS. Bascially, this is narrow down step to get into ground level specific to POI as a part of citizen awareness. The outputs intended in the scripts include, the overall AQI (value and category), critical pollutant, potential health impacts, concentration of indivudal pollutants (Particulate Matter of size 2.5 and 10 micrometeres, Nitrogen Dioxide, Sulphur Dioxide, Carbon Monoxide and Ozone) and their AQI. 

**Note:** The AQI calculations in the script usess Indian methodology . So, you may try finding the AQI for place outside India, but the final output dispalyed will be based on India AQI scale.

## Step 1: Clone the repository
Make sure the git is downloaded and installed in your system from [here](https://git-scm.com/downloads).<br /> 
Open the terminal and paste `git clone https://github.com/moorthynair/NRT-AQIfinder.git`

## Step 2: Install the requirements
Move to the directory where the repo is downloaded `cd NRT-AQIfinder` <br />
Install the requirements `pip install requirement_aqi.txt`

## Step 2: Knowing the input requirements
Use the help function to know the required inputs `python main.py -h`. The output below must be displayed in your terminal <br />
> <img width="436" alt="Screenshot 2023-06-17 at 3 18 39 PM" src="https://github.com/moorthynair/NRT-AQIfinder/assets/83420459/2f2cc6b0-b241-43a9-acb0-314ad9b365e5"> <br />

| **Inputs** | **Description** |
| --- | --- |
| **API**| Generate your personal API by accessing the AQCIN website [here](https://aqicn.org/data-platform/token/). For more information about the AQI calculation, source, locations, etc you may access the [FAQ](https://aqicn.org/faq/) section of the website. Save this API in a seperate document as this shall be kept confidential and will be used as input everytime you run the script.|
| **Lat** | Input the Latitude in degrees for your Point of Intreset. You may use google maps to find the exact geo-locations of your POI |
| **Lon** | Input the Longitude in degrees for your Point of Intreset. You may use google maps to find the exact geo-locations of your POI |

## Step 3: Run the script on your terminal
Enter this command in the terminal `python main.py 'Enter API' 'Latitude of your POI' 'Longitude of your POI'` <br />
Thr output must be on your terminal screen

### Sample run on the terminal

Provding the command in the terminal: `python main.py dedb######&&&88######1fe 25.607 85.115` <br /> 

and the output as below: <br />

> <img width="1323" alt="Screenshot 2023-06-17 at 3 41 07 PM" src="https://github.com/moorthynair/NRT-AQIfinder/assets/83420459/1267a8c4-a02d-47e0-b78b-2ed78c77baea">

