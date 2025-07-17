# src/preprocessing.py

import pandas as pd
import numpy as np

def convert_timestamps(df: pd.DataFrame) -> pd.DataFrame:
    """
    Converts signup_time and purchase_time to datetime.
    Creates hour_of_day, day_of_week, and time_since_signup features.
    """
    df['signup_time'] = pd.to_datetime(df['signup_time'])
    df['purchase_time'] = pd.to_datetime(df['purchase_time'])

    # Time-based features
    df['hour_of_day'] = df['purchase_time'].dt.hour
    df['day_of_week'] = df['purchase_time'].dt.dayofweek
    df['time_since_signup'] = (df['purchase_time'] - df['signup_time']).dt.total_seconds()

    return df

def ip_to_int(ip_string: str) -> int:
    """
    Converts a dot-decimal IP string to an integer.
    """
    parts = ip_string.split('.')
    return (int(parts[0]) << 24) + (int(parts[1]) << 16) + (int(parts[2]) << 8) + int(parts[3])

def add_country_column(fraud_df: pd.DataFrame, ip_df: pd.DataFrame) -> pd.DataFrame:
    """
    Maps IP addresses to countries using IP range data.
    Adds a new 'country' column to the fraud data.
    """

    # Convert IP addresses in fraud_df to integer
    fraud_df['ip_integer'] = fraud_df['ip_address'].apply(ip_to_int)

    # Prepare IP range data
    ip_df['lower_bound_ip_address'] = ip_df['lower_bound_ip_address'].astype(np.uint32)
    ip_df['upper_bound_ip_address'] = ip_df['upper_bound_ip_address'].astype(np.uint32)

    # Sort for efficient search
    ip_df = ip_df.sort_values('lower_bound_ip_address')

    # Function to map a single IP to a country using the IP range
    def find_country(ip_int):
        match = ip_df[(ip_df['lower_bound_ip_address'] <= ip_int) & (ip_df['upper_bound_ip_address'] >= ip_int)]
        if not match.empty:
            return match.iloc[0]['country']
        else:
            return 'Unknown'

    # Apply mapping
    fraud_df['country'] = fraud_df['ip_integer'].apply(find_country)
    return fraud_df
