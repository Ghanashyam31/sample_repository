from datetime import datetime

dttime=datetime.now().strftime('%Y-%m-%d %H:%M:%S')

print(f"Current date and time: {dttime}")

print("line changed. Now added further comments to test the git commit and push functionality.")


for i in range(14):
    print(f"Iteration {i+1}: Current date and time: {dttime}")
    