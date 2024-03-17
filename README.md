# Near Real Time Air Quality Index (AQI) Finder
These Python scripts make it easier for you to retrieve the air quality status for your Point of Interest (POI) from the nearby CAAQMS that are currently operational. Fundamentally, this is a narrow down step that focuses on making the best use possible of the information from the air quality monitoring station to raise citizen awareness. The output includes the following data about your POI: the overall AQI (value and category), critical pollutants, potential health effects, and concentrations of individual pollutants **(including ozone, carbon monoxide, nitrogen dioxide, and particles with a diameter between 2.5 and 10 micrometres).** AQI and its puprose are covered in more detail in my earlier [writings](https://medium.com/gitconnected/how-bad-is-the-air-pollution-in-your-city-51043d82b321)

**Note:** The AQI calculations in the script usess Indian methodology . So, you may try finding the AQI for place outside India, but the final output dispalyed will be based on India AQI scale.

## Step 1: Clone the repository
Make sure the git is downloaded and installed in your system from [here](https://git-scm.com/downloads).<br /> 
Open the terminal and paste `git clone https://github.com/moorthynair/NRT-AQIfinder.git`

## Step 2: Install the requirements
Move to the directory where the repo is downloaded `cd NRT-AQIfinder` <br />
Install the requirements `pip install -r requirement_aqi.txt`

## Step 2: Knowing the input requirements
Use the help function to know the required inputs `python main.py -h`. The output below must be displayed in your terminal <br />
> <img width="436" alt="Screenshot 2023-06-17 at 3 18 39 PM" src="https://github.com/moorthynair/NRT-AQIfinder/assets/83420459/2f2cc6b0-b241-43a9-acb0-314ad9b365e5"> <br />

| **Inputs** | **Description** |
| --- | --- |
| **API**| Generate your personal API by accessing the AQCIN website [here](https://aqicn.org/data-platform/token/). For more information about the AQI calculation, source, locations, etc you may access the [FAQ](https://aqicn.org/faq/) section of the website. Save this API in a seperate document as this shall be kept confidential and will be used as input everytime you run the script.|
| **Lat** | Input the Latitude in degrees for your Point of Intreset. You may use google maps to find the exact geo-locations of your POI |
| **Lon** | Input the Longitude in degrees for your Point of Intreset. You may use google maps to find the exact geo-locations of your POI |

## Step 3: Execute the script in the terminal
Enter this command in the terminal `python main.py 'Enter API' 'Latitude of your POI' 'Longitude of your POI'` <br />
The output must be on your terminal screen

### Sample run
Provding the command in the terminal: `python main.py dedb######&&&88######1fe 25.607 85.115` <br /> 

#### Output: <br />

> <img width="1323" alt="Screenshot 2023-06-17 at 3 41 07 PM" src="https://github.com/moorthynair/NRT-AQIfinder/assets/83420459/1267a8c4-a02d-47e0-b78b-2ed78c77baea">

## License
Copyright (c) 2023 Moorthy M Nair [MIT License](https://github.com/moorthynair/NRT-AQIfinder/blob/main/LICENSE)

#### Acknowledgment
1. [Central Pollution Control Board](https://cpcb.nic.in/) for providing a) NRT air quality data; b) AQI India scale break point details; c) Potential health impact with respect to individual AQI category
2. [World Air Quality Index](https://waqi.info/)forum for providing API services to retrieve the NRT AQI information worldwide
3. [hangLeQuoc](https://github.com/ThangLeQuoc/aqi-bot) for the USEPA AQI break point details
4. [uk-air.defra.gov.uk](https://uk-air.defra.gov.uk/assets/documents/reports/cat06/0502160851_Conversion_Factors_Between_ppb_and.pdf) for providing ppm/ppb to micrograms per cubicmeters conversion factors for the pollutants
