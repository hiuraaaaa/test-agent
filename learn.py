import json
import sys
import os

MEMORY_FILE = "xena_memory.json"

def learn(issue, solution):
    if not os.path.exists(MEMORY_FILE):
        data = {"lessons_learned": []}
    else:
        with open(MEMORY_FILE, "r") as f:
            data = json.load(f)
    
    data["lessons_learned"].append({
        "issue": issue,
        "solution": solution
    })
    
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)
    print(f"✅ Pelajaran baru dicatat: {issue}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 learn.py 'masalah' 'solusi'")
    else:
        learn(sys.argv[1], sys.argv[2])