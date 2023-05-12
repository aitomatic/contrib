"""Time Series Analyzer (TSA)."""


from pandas.core.frame import DataFrame
from pandasai import PandasAI
from pandasai.llm.base import LLM


class TimeSeriesAnalyzer:  # pylint: disable=too-few-public-methods
    """Time Series Analyzer (TSA)."""

    def __init__(self, llm: LLM):
        """Initialize TSA."""
        self.pandas_ai: PandasAI = PandasAI(llm=llm,
                                            conversational=True,
                                            verbose=False,
                                            enforce_privacy=False)

    def __call__(self, df: DataFrame, /, prompt: str):
        """Analyze tabular/time-series data frame."""
        return self.pandas_ai.run(data_frame=df, prompt=prompt)
