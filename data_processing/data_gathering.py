import pandas as pd
from pybaseball import statcast
import time

def clean_to_csv():
    
    selected_columns = [
        'game_date', 'player_name', 'release_speed', 'release_pos_x', 'release_pos_z', 'pitcher',
        'description', 'pfx_x', 'pfx_z', 'effective_speed', 'release_extension', 'release_spin_rate',
        'estimated_woba_using_speedangle'
    ]

    for year in range(2015, 2026):
        print(f"Pulling data for {year}...")
        
        # Season dates
        start_date = f"{year}-03-01"
        end_date = f"{year}-11-15"
        
        try:
            year_data = statcast(start_dt=start_date, end_dt=end_date)
            
            if not year_data.empty:
                # Filter to only selected columns (only keep columns that exist)
                available_cols = [col for col in selected_columns if col in year_data.columns]
                filtered_data = year_data[available_cols]
                
                # Save to CSV with year in filename
                filename = f"statcast_{year}.csv"
                filtered_data.to_csv(filename, index=False)
                print(f"Saved {len(filtered_data)} records ({len(available_cols)} columns) to '{filename}'")
            else:
                print(f"No data found for {year}")
            
        except Exception as e:
            print(f"Error for {year}: {e}")
        
        # Pause between years
        time.sleep(2)
    
    print("\nAll seasons saved as separate CSV files!")

# Run it
clean_to_csv()