"""Basic heuristics-based Ensembles."""


from pandas import Series

from h1st.model.oracle.ensemble import Ensemble


class UnanimousFaultPredEnsemble(Ensemble):
    # pylint: disable=too-many-ancestors
    """Unanimous vote between K ("Teacher") & K-Gen ("Student") models."""

    @staticmethod
    def predict(teacher_pred: bool, student_pred: bool) -> bool:
        """Unanimous vote between K ("Teacher") & K-Gen ("Student") models."""
        return teacher_pred and student_pred

    @staticmethod
    def batch_predict(teacher_preds: Series, student_preds: Series) -> Series:
        """Unanimous votes between K ("Teacher") & K-Gen ("Student") models."""
        assert (teacher_preds.index == student_preds.index).all()
        return teacher_preds & student_preds
