import os
import pandas as pd
from datetime import datetime
from pathlib import Path

def save_to_excel(data_cards, custom_columns=None):
    """
    Accepts the array of processed extraction data cards and structures them 
    into a pristine Excel matrix, mapping the columns dynamically based on GitHub rules.
    """
    if not data_cards:
        return "No Data"

    # --- UPDATED: Added Email ID and completely removed Google Plus Code ---
    columns_structure = custom_columns if custom_columns else [
        "Business Name",
        "Google Rating",
        "Complete Address",
        "Operating Hours Matrix",
        "Website Link",
        "Email ID",
        "Phone Number",
        "Facebook Handle",
        "Instagram Handle",
        "LinkedIn Handle",
        "Twitter/X Handle"
    ]

    # Re-map the dictionaries into dynamically structured rows
    rows = []
    for card in data_cards:
        row_data = {col: card.get(col, "Not Provided") for col in columns_structure}
        rows.append(row_data)

    df = pd.DataFrame(rows, columns=columns_structure)

    # CROSS-PLATFORM SAVE LOCATION PATH DETECTOR
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"timevehicle1.0_Export_{timestamp}.xlsx"
    
    desktop_dir = Path.home() / "Desktop"
    
    if desktop_dir.exists():
        output_filepath = desktop_dir / filename
    else:
        output_filepath = Path.home() / filename
    
    try:
        df.to_excel(str(output_filepath), index=False)
        return os.path.abspath(str(output_filepath))
    except Exception as e:
        print(f"❌ Excel engine generation error: {str(e)}")
        try:
            df.to_excel(filename, index=False)
            return os.path.abspath(filename)
        except:
            return "Generation Error"

def save_to_word(data_cards):
    """
    Optional fallback documentation generator. Appends social anchors 
    neatly at the bottom of each structural text section.
    """
    pass
