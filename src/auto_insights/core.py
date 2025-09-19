from dataclasses import dataclass
import pandas as pd

@dataclass
class Config:
    out_dir: str = "insights_out"
    sample_rows: int | None = 5000

def analyze(df: pd.DataFrame, cfg: Config = Config()):
    # placeholder: just return shape for now
    return {"n_rows": int(len(df)), "n_cols": int(df.shape[1])}
