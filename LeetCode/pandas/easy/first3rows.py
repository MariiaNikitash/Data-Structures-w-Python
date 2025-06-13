import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    df = pd.DataFrame(data = employees)
    return df.head(3)