#!/bin/bash

# Configuration
INPUT="data_list.txt"
COLOR="#10b981" # Default PharmaGO Emerald

echo "--- Batch Generating Customized QRs ---"

while IFS= read -r line; do
    if [[ -z "$line" ]]; then continue; fi
    
    # Create a safe filename
    clean_name=$(echo "$line" | sed 's/[^a-zA-Z0-9]/_/g')
    
    # Call the python script with the custom color
    PYTHONPATH=src uv run python src/qr_service.py "$line" "$clean_name" "$COLOR"
    
done < "$INPUT"

echo "Check the /qrs folder for your customized files."