import os

def create_project_structure():

    directories = [
        "frontend",
        "data",
        "analysis"
    ]
    
    files = {
        "frontend": ["app.py", "index.html", "result.html"],
        "data": ["housing.csv"],
        "analysis": ["exploration.py", "feature_engineering.py", "imports.py", "model_training.py"],
        "": ["requirements.txt"] 
    }
    

    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        

    for directory, file_list in files.items():
        for file_name in file_list:
            file_path = os.path.join(directory, file_name) if directory else file_name
            with open(file_path, 'w') as f:
                pass  
    
    print("Project structure created successfully!")

if __name__ == "__main__":
    create_project_structure()
