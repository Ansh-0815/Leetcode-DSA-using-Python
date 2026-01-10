import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    unique=customers.drop_duplicates(subset=['email'],keep='first')
    return unique