# Userside Commutation Export

This script exports commutation data from Userside to Excel format, including customer information, device details, and house addresses.

UPD: 29/03/2025 - it works only with Commutations with Device Type - switch

## Features

- Fetches commutation data for customers
- Retrieves customer information
- Gets house address details
- Caches device data locally
- Exports all data to Excel format

## Prerequisites

- Python 3.6+
- Userside API access
- Required Python packages (see requirements.txt)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd userside-export-commutation
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root with your Userside API credentials:
```
USERSIDE_API_KEY=your_api_key_here
USERSIDE_API_URL=https://your-userside-instance.com/api
```

## Usage

Run the script:
```bash
python export_commutation.py
```

The script will:
1. Fetch commutation data for all customers
2. Get customer information
3. Retrieve house address details
4. Load or fetch device data
5. Export all data to an Excel file named `commutation_export_YYYYMMDD_HHMMSS.xlsx`

## Output Format

The Excel file will contain the following columns:
- customer_agreement: Customer's agreement number
- customer_name: Customer's full name
- customer_address: Customer's full address
- device_type: Type of device (e.g., 'switch')
- location: Device location
- hostname: Device hostname
- ip: Device IP address
- name: Device name
- iface_data: Interface information

## Caching

Device data is cached in `devices_data.json` to improve performance on subsequent runs. The cache is automatically updated if the file is missing.

## Error Handling

The script includes error handling for:
- API connection issues
- Invalid data formats
- Missing required data
- File operations

## Dependencies

- python-dotenv==1.0.0
- requests==2.31.0
- pandas==2.1.4
- openpyxl==3.1.2
