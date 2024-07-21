# Tomorrow.io Data Fetcher

This repository contains a workflow and scripts to fetch weekly weather forecast data from Tomorrow.io for the Dedan Kimathi area in Nyeri County and store it in Google Cloud Platform (GCP) and Firebase databases. It  was  a  project  to fetch data  for   a  research in  center  of datascince  `Dkut`. The execution of these scripts is automated using GitHub workflows.

It  is  based on ETL approach  to efficiently fetch, transform and  load  the  weather  data collected.
## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project automates the process of fetching weather forecast data from Tomorrow.io for the Dedan Kimathi area in Nyeri County on a weekly basis. The data is then uploaded to both Firebase and GCP databases. The automation is handled by GitHub workflows, ensuring that the data is fetched and stored without manual intervention and  without  extra  costs  of  running  the  script.

## Features

- Fetches weekly weather forecast data from Tomorrow.io.
- Stores the fetched data in Firebase and GCP databases.
- Automated execution using GitHub workflows.
- Configurable to suit different needs and areas.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have a Tomorrow.io API key.
- You have a Google Cloud Platform account with access to Firestore or another GCP database.
- You have a Firebase project set up.
- You have GitHub Actions enabled for your repository.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/wambugu71/tommorow.io_Data
    cd tommorow.io_Data
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up your cloud service  account  and  download  the credentials.
   i.e the  `json` format.
   In this  case  named
   ```
   dsail-misc-new.json
   weather.json
   ```
   These  are  from my  project, __Note__ : Don't  opensource  your  cloud  credentials.
## Usage

The scripts are designed to be executed automatically by GitHub workflows. However, you can also run them manually for testing purposes.

To fetch and upload data manually, run:

```bash
python maincp.py
```

## Configuration

The repository contains the following key files and directories:

- `maincp.py`: The main script to fetch data from Tomorrow.io and upload it to Firebase and GCP.
- `.github/workflows/`: Contains the GitHub workflow files for automating the execution of the scripts.
- `requirements.txt`: Lists the Python dependencies required for the project.
- `dsail-misc-new.json` for  your  service  account  credentials. Ensure you  have  enabled neecessary  permisions.
### GitHub Workflow

The GitHub workflow is defined in `.github/workflows/main.yml or  ken.yml`. It is set to run the `maincp.py` script on a weekly basis. You can modify the schedule as needed.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

---

Feel free to modify the code further for your needs. If you encounter any issues or have any questions, please open an issue in the repository.

Happy coding!
