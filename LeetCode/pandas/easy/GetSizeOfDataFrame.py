import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    df = pd.DataFrame(data = players)
    # converts tuple to a list
    return list(df.shape)