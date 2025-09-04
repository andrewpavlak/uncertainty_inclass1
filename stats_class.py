class ECDF:
    def __init__(self) -> None:
        pass



# TASK 4: Five-number summary / boxplot stats
def five_number_summary(self) -> dict:
    """
    Returns a dict with the 5-number summary + IQR + whisker fences.
    Keys: min, q1, median, q3, max, iqr, lower_whisker, upper_whisker

    Assumptions about earlier tasks:
    - self.x is a SORTED list of floats (e.g., set in __init__). 
      # CHANGE_IF_DIFFERENT: if your data is stored unsorted or under a different name,
      # replace self.x[0] / self.x[-1] below with min(self.data) / max(self.data) or similar.
    - self.quantile(p) implements the group’s chosen rule (e.g., Type-7).
      # CHANGE_IF_DIFFERENT: if your quantile method is named get_quantile, q, percentile, etc.,
      # replace calls to self.quantile(…) accordingly.
    - self.whiskers() returns Tukey fences (q1 - 1.5*IQR, q3 + 1.5*IQR).
      # CHANGE_IF_DIFFERENT: if your whisker method returns the CLIPPED whisker positions
      # (i.e., the most extreme inlier values), rename or recompute fences here.
    """
    # Quartiles & median using your group's quantile method
    q1 = self.quantile(0.25)      # CHANGE_IF_DIFFERENT: rename if your method differs
    med = self.quantile(0.50)
    q3 = self.quantile(0.75)
    
    # --- IQR
    iqr = q3 - q1

    # --- Whisker *fences* (NOT clipped to data unless your method already clips)
    lw, uw = self.whiskers()      # CHANGE_IF_DIFFERENT: if your whiskers() returns clipped whiskers,
                                  # recompute fences as:
                                  #   lw = q1 - 1.5 * iqr
                                  #   uw = q3 + 1.5 * iqr

    # Min/Max from your stored data
    # Assumes self.x is sorted ascending.
    # CHANGE_IF_DIFFERENT: if your data is self.data and not sorted, use min()/max() instead.
    minimum = self.x[0]
    maximum = self.x[-1]

    return {
        "min": minimum,
        "q1": q1,
        "median": med,
        "q3": q3,
        "max": maximum,
        "iqr": iqr,
        "lower_whisker": lw,
        "upper_whisker": uw,
    }