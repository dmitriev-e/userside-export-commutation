import json
import os
import requests
import pandas as pd
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

def list_to_string(lst):
    """Convert list to comma-separated string"""
    return ','.join(str(x) for x in lst)

class UsersideAPI:
    def __init__(self):
        self.api_key = os.getenv('USERSIDE_API_KEY')
        self.api_url = os.getenv('USERSIDE_API_URL')
        if not self.api_key or not self.api_url:
            raise ValueError("Please set USERSIDE_API_KEY and USERSIDE_API_URL in .env file")

    def get_commutation_data(self, objects_type):
        """
        Fetch commutation data from Userside API
        
        Returns:
            dict: 
            {
                "Result": "OK",
                "data": {
                    "17099": [                          # object_id
                        {                               # commutation data
                            "object_type": "switch",
                            "object_id": 6918,
                            "direction": 0,
                            "interface": 1,
                            "comment": "",
                            "connect_id": 14175037
                        }
                    ],
                    ....
                }
            }
        """
        try:
            response = requests.get(
                f"{self.api_url}",
                params={
                    'key': self.api_key,
                    'cat': 'commutation',
                    'action': 'get_data',
                    'object_type': objects_type
                }
            )
            response.raise_for_status()
            if response.json().get('Result') == 'OK':   
                return response.json().get('data')
            else:
                print(f"Error fetching data: {response.json().get('Result')}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None

    
        """Fetch device data from Userside API"""
        try:
            response = requests.get(
                f"{self.api_url}",
                params={
                    'key': self.api_key,
                    'cat': 'device',
                    'action': 'get_data',
                    'object_type': str(device_type),
                    'object_id': str(device_id)
                }
            )
            response.raise_for_status()
            if response.json().get('Result') == 'OK':   
                return response.json().get('data')
            else:
                print(f"Error fetching data: {response.json().get('Result')}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Error fetching device data: {e}")
            return None
        
    def get_all_devices_data(self):
        """Fetch all devices data from Userside API and save to cache
        
        Returns:
            dict: 
            {
                "Result": "OK",
                "data": {
                    "8043": {
                        "code": 8043,
                        "devtyper": 4,
                        "skladcode": 31728,
                        "opis": "",
                        "port": 2,
                        "uzelcode": 0,
                        "usercode": 20076,
                        "location": "BILL0008081",
                        "nazv": "Cambium ePMP Force 190 5Ghz",
                        "lastact": "2024-11-01 07:10:53",
                        "dateadd": "2023-12-06",
                        "com_public": "",
                        "com_private": "",
                        "com_login": "",
                        "com_pass": "",
                        "is_peleng": 0,
                        "valuememo": "",
                        "snmpver": 0,
                        "fdpver": 2,
                        "x1": 0,
                        "y1": 0,
                        "upport": "",
                        "onsms": 0,
                        "issmssend": 0,
                        "hash_port2": "YToyOntpOjE7YTo0OntzOjc6ImlmSW5kZXgiO2k6MTtzOjY6ImlmVHlwZSI7aTo2O3M6NjoiaWZOYW1lIjtzOjE1OiJMQU4gaW50ZXJmYWNlIDEiO3M6ODoiaWZOdW1iZXIiO2k6MTt9aToyO2E6NDp7czo3OiJpZkluZGV4IjtpOjI7czo2OiJpZlR5cGUiO2k6NzE7czo2OiJpZk5hbWUiO3M6MTQ6IldMQU4gaW50ZXJmYWNlIjtzOjg6ImlmTnVtYmVyIjtpOjI7fX0=",
                        "onmail": 0,
                        "ismailsend": 0,
                        "proshivka": "",
                        "proshivka_date": null,
                        "cablelen": "",
                        "hostname": "",
                        "basecode": 1227,
                        "_param": "",
                        "rotation": 0,
                        "ipabon": null,
                        "snmp_dontask": 0,
                        "log_status": 1,
                        "dnport": "",
                        "datepeleng": null,
                        "ipport": "",
                        "profile": 0,
                        "azimut": 0,
                        "sectcoord": "",
                        "colcol": "",
                        "flag_custom_coord": 0,
                        "level_max": 0,
                        "level_min": 0,
                        "latitude": null,
                        "longitude": null,
                        "_ip": null,
                        "_mac": "",
                        "snmp_port": 161,
                        "date_cabletest": null,
                        "date_iferr": null,
                        "activity_update_by": 5,
                        "sfp_att_list": "",
                        "custom_iface_list": "a:2:{i:0;a:2:{s:7:\"ifIndex\";s:1:\"2\";s:7:\"caption\";s:0:\"\";}i:1;a:2:{s:7:\"ifIndex\";s:1:\"1\";s:7:\"caption\";s:0:\"\";}}",
                        "options": "",
                        "snmp_v3_security_name": "",
                        "snmp_v3_sec_level": "",
                        "snmp_v3_auth_protocol": "",
                        "snmp_v3_auth_passphrase": "",
                        "snmp_v3_priv_protocol": "",
                        "snmp_v3_priv_passphrase": "",
                        "telnet_enable_password": "",
                        "CODE": 8043,
                        "DEVTYPER": 4,
                        "SKLADCODE": 31728,
                        "OPIS": "",
                        "PORT": 2,
                        "UZELCODE": 0,
                        "USERCODE": 20076,
                        "LOCATION": "BILL0008081",
                        "NAZV": "Cambium ePMP Force 190 5Ghz",
                        "LASTACT": "2024-11-01 07:10:53",
                        "DATEADD": "2023-12-06",
                        "COM_PUBLIC": "",
                        "COM_PRIVATE": "",
                        "COM_LOGIN": "",
                        "COM_PASS": "",
                        "IS_PELENG": 0,
                        "VALUEMEMO": "",
                        "SNMPVER": 0,
                        "FDPVER": 2,
                        "X1": 0,
                        "Y1": 0,
                        "UPPORT": "",
                        "ONSMS": 0,
                        "ISSMSSEND": 0,
                        "HASH_PORT2": "YToyOntpOjE7YTo0OntzOjc6ImlmSW5kZXgiO2k6MTtzOjY6ImlmVHlwZSI7aTo2O3M6NjoiaWZOYW1lIjtzOjE1OiJMQU4gaW50ZXJmYWNlIDEiO3M6ODoiaWZOdW1iZXIiO2k6MTt9aToyO2E6NDp7czo3OiJpZkluZGV4IjtpOjI7czo2OiJpZlR5cGUiO2k6NzE7czo2OiJpZk5hbWUiO3M6MTQ6IldMQU4gaW50ZXJmYWNlIjtzOjg6ImlmTnVtYmVyIjtpOjI7fX0=",
                        "ONMAIL": 0,
                        "ISMAILSEND": 0,
                        "PROSHIVKA": "",
                        "PROSHIVKA_DATE": null,
                        "CABLELEN": "",
                        "HOSTNAME": "",
                        "BASECODE": 1227,
                        "_PARAM": "",
                        "ROTATION": 0,
                        "IPABON": null,
                        "SNMP_DONTASK": 0,
                        "LOG_STATUS": 1,
                        "DNPORT": "",
                        "DATEPELENG": null,
                        "IPPORT": "",
                        "PROFILE": 0,
                        "AZIMUT": 0,
                        "SECTCOORD": "",
                        "COLCOL": "",
                        "FLAG_CUSTOM_COORD": 0,
                        "LEVEL_MAX": 0,
                        "LEVEL_MIN": 0,
                        "LATITUDE": null,
                        "LONGITUDE": null,
                        "_IP": null,
                        "_MAC": "",
                        "SNMP_PORT": 0,
                        "DATE_CABLETEST": null,
                        "DATE_IFERR": null,
                        "ACTIVITY_UPDATE_BY": 5,
                        "SFP_ATT_LIST": "",
                        "CUSTOM_IFACE_LIST": "a:2:{i:0;a:2:{s:7:\"ifIndex\";s:1:\"2\";s:7:\"caption\";s:0:\"\";}i:1;a:2:{s:7:\"ifIndex\";s:1:\"1\";s:7:\"caption\";s:0:\"\";}}",
                        "OPTIONS": "",
                        "SNMP_V3_SECURITY_NAME": "",
                        "SNMP_V3_SEC_LEVEL": "",
                        "SNMP_V3_AUTH_PROTOCOL": "",
                        "SNMP_V3_AUTH_PASSPHRASE": "",
                        "SNMP_V3_PRIV_PROTOCOL": "",
                        "SNMP_V3_PRIV_PASSPHRASE": "",
                        "TELNET_ENABLE_PASSWORD": "",
                        "id": 8043,
                        "ID": 8043,
                        "type_id": 4,
                        "name": "Cambium ePMP Force 190 5Ghz",
                        "entrance": 0,
                        "ip": "178320547",
                        "host": "10.160.244.163",
                        "mac": "0004566139F0",
                        "comment": "",
                        "inventory_id": 31728,
                        "uplink_iface": "",
                        "dnlink_iface": "",
                        "node_id": 0,
                        "interfaces": 2,
                        "podezd": 0,
                        "activity_time": "2024-11-01 07:10:53",
                        "uplink_iface_array": [],
                        "dnlink_iface_array": [],
                        "is_online": 0,
                        "ifaces": {
                            "1": {
                                "ifIndex": 2,
                                "ifType": 71,
                                "ifName": "WLAN interface",
                                "ifNumber": 1
                            },
                            "2": {
                                "ifIndex": 1,
                                "ifType": 6,
                                "ifName": "LAN interface 1",
                                "ifNumber": 2
                            }
                        },
                        "snmp_proto": 2,
                        "snmp_community_ro": "public",
                        "snmp_community_rw": "public",
                        "telnet_login": "admin",
                        "telnet_pass": "admin"
                    },
                    ...
                }
            }
        """
        try:
            response = requests.get(
                f"{self.api_url}",
                params={
                    'key': self.api_key,
                    'cat': 'device',
                    'action': 'get_data',
                    'object_type': 'all'
                }
            )
            response.raise_for_status()
            if response.json().get('Result') == 'OK':
                return response.json().get('data')
            else:
                print(f"Error fetching data: {response.json().get('Result')}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None

    def get_customer_data(self, customers_ids: list):
        """Fetch customer data from Userside API
        
        Returns:
            dict: 
            {
                "Result": "OK",
                "data": {
                    "19448": {
                    "id": 19448,
                    "login": "BILL0007458",
                    "full_name": "Name Surname",
                    "flag_corporate": 0,
                    "balance": "0",
                    "state_id": 0,
                    "agreement": [
                        {
                            "number": "BILL0007458",
                            "date": "2023-03-09 15:47:54"
                        }
                    ],
                    "traffic": {
                        "month": {
                            "up": 0,
                            "down": 0
                        }
                    },
                    "date_create": "2023-03-09 16:03:28",
                    "date_connect": "1970-01-01",
                    "date_activity": "2023-03-10 06:08:46",
                    "date_activity_inet": "2023-03-10 06:08:46",
                    "date_positive_balance": "2025-03-29",
                    "is_disable": 0,
                    "address": [
                        {
                            "type": "connect",
                            "house_id": 13225,
                            "apartment": {
                                "number": "23"
                            }
                        }
                    ],
                    "is_in_billing": 1,
                    "billing_id": "13615",
                    "group": {
                        "51": {
                            "id": 51
                        }
                    },
                    "tariff": {
                        "current": [
                            {
                                "id": "1214"
                            }
                        ]
                    },
                    "account_number": "10013615",
                    "phone": [
                        {
                            "number": "+xxxxxxxxxx",
                            "flag_main": 1
                        },
                        {
                            "number": ""
                        }
                    ],
                    "comment2": ""
                    },
                    ...
                }
            }
        """
        try:
            response = requests.post(
                f"{self.api_url}",
                params={
                    'key': self.api_key,
                    'cat': 'customer',
                    'action': 'get_data'
                },
                data={
                    'customer_id': list_to_string(customers_ids)
                }
            )
            response.raise_for_status()
            if response.json().get('Result') == 'OK':   
                return response.json().get('data')
            else:
                print(f"Error fetching data: {response.json().get('Result')}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Error fetching customer data: {e}")
            return None

    def get_houses_data(self, building_ids: list):
        """Fetch houses data from Userside API
        
        Returns:
            dict:
            {
                "Result": "OK",
                "data": {
                    "18076": {
                        "id": 18076,
                        "name": "9",
                        "parent_ids": [
                            18621,
                            18622,
                            13267,
                            13353
                        ],
                        "parent_id": 13353,
                        "building_id": 13225,
                        "type_id": 1,
                        "floor": 0,
                        "entrance": 0,
                        "apart": 0,
                        "full_name": "Lemesos, Lemesos Municipality, Sotiri Michailidi, 9",
                        "comment": "",
                        "coordinates": [],
                        "exit_comment": "",
                        "task_comment": "",
                        "additional_data": []
                    }
                },
                ...
            } 
        """
        try:
            response = requests.post(
                f"{self.api_url}",
                params={
                    'key': self.api_key,
                    'cat': 'address',
                    'action': 'get_house'
                },
                data={
                    'building_id': list_to_string(building_ids)
                }
            )
            response.raise_for_status()
            if response.json().get('Result') == 'OK':
                return response.json().get('data')
            else:
                print(f"Error fetching data: {response.json().get('Result')}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Error fetching houses data: {e}")
            return None


def export_to_excel(data, filename=None):
    """Export data to Excel file"""
    if not data:
        print("No data to export")
        return

    # Convert data to DataFrame
    df = pd.DataFrame(data)
    
    # Generate filename if not provided
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"commutation_export_{timestamp}.xlsx"
    
    # Export to Excel
    df.to_excel(filename, index=False)
    print(f"Data exported successfully to {filename}")


def transform_houses_data(houses_data):
    """Transform houses data into simplified format"""
    transformed_data = {}
    for house_id, house_info in houses_data.items():
        transformed_data[house_info.get('building_id')] = {
            'house_id': house_id,
            'full_name': house_info.get('full_name')
        }
    return transformed_data

def main():

    try:
        # Initialize API client
        api = UsersideAPI()
        
        # Fetch commutation data
        print("Fetching commutation data...")
        commutation_data = api.get_commutation_data(objects_type='customer')

        # Fetch customer data
        print("Fetching customer data...")
        if commutation_data:
            customer_data = api.get_customer_data(customers_ids=[customer_id for customer_id in commutation_data.keys()])
        else:
            print("No commutation data found")

        # Fetch houses data
        print("Fetching houses data...")
        if commutation_data:
            # make list of building_ids from customer data
            building_ids = [customer_data.get(customer_id).get('address')[0].get('house_id') for customer_id in customer_data.keys()]
            houses_data = api.get_houses_data(building_ids=building_ids)
            if houses_data:
                houses_data = transform_houses_data(houses_data)
            
        else:
            print("No customer data found")

        # Fetch all devices data
        print("Fetching all devices data...")
        if not os.path.exists('devices_data.json'):
            print("No devices data found in cache, fetching from Userside API...")
            all_devices_data = api.get_all_devices_data()
            with open('devices_data.json', 'w') as f:
                json.dump(all_devices_data, f)
        else:
            print("Devices data found in cache, loading from cache...")
            with open('devices_data.json', 'r') as f:
                all_devices_data = json.load(f)
        
        if commutation_data:
            print("Processing commutation data...")
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            data_to_export = []

            # Process each customer's commutation data
            for customer_id, commutation in commutation_data.items():
                print(f"Processing object ID: {customer_id}")

                if isinstance(commutation[0], dict):
                    for commutation in commutation:
                        device_type = commutation.get('object_type')

                        # Check device type, if switch, get device id from commutation data
                        if device_type == 'switch':
                            device_id = commutation.get('object_id')
                        else:
                            continue
                        
                        if device_type and device_id:
                            print(f"Fetching data for device type: {device_type}, id: {device_id}")
                            device_data = all_devices_data.get(str(device_id))

                            # Device Data to export
                            data_to_export.append({
                                'customer_agreement': customer_data.get(customer_id).get('agreement')[0].get('number'),
                                'customer_name': customer_data.get(customer_id).get('full_name'),
                                'customer_address': houses_data.get(customer_data.get(customer_id).get('address')[0].get('house_id')).get('full_name') if customer_data.get(customer_id).get('address')[0].get('house_id') in houses_data else '' + ' ' + customer_data.get(customer_id).get('address')[0].get('apartment').get('number') if customer_data.get(customer_id).get('address')[0].get('apartment').get('number') else '',
                                'device_type': device_type,
                                'location': device_data.get('location'),
                                'hostname': device_data.get('hostname'),
                                'ip': device_data.get('host'),
                                'name': device_data.get('nazv'),
                                'iface_data': device_data.get('ifaces').get(str(commutation.get('interface'))).get('ifName')
                            })

                else:
                    print(f"Unexpected commutation format: {commutation}")

            # Export to Excel
            export_to_excel(data=data_to_export, filename=f"commutation_export_{timestamp}.xlsx")
            
        else:
            print("Failed to fetch commutation data from Userside API")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()