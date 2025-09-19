import pandas as pd
from auto_insights.core import analyze, Config

def test_analyze_runs(tmp_path):
    df = pd.DataFrame({"a":[1,2,3]})
    out = analyze(df, Config(out_dir=str(tmp_path)))
    assert out["n_rows"] == 3
