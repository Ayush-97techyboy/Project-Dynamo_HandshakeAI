import json
import os

def test_json_output():
    """Checks if the instruction.md criteria was met: File exists and contains status: success"""
    
    file_path = "/app/report.json"
    
    assert os.path.exists(file_path), "The AI failed to create /app/report.json"
    
    with open(file_path, "r") as f:
        data = json.load(f)
        
    assert "status" in data, "The JSON is missing the 'status' key."
    assert data["status"] == "success", "The status was not set to 'success'."