import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:


# Create the DataFrame from the 2D list
    df = pd.DataFrame(student_data, columns=['student_id', 'age'])
    return df