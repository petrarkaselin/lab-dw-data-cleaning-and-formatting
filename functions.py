#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

def load_data(url):
    # Load the CSV file into a dataframe
    df = pd.read_csv(url)
    return df

def lowercase_column_names(df):
    # Convert column names to lowercase
    new_cols = [col.lower() for col in df.columns]
    return new_cols

def display_column_names(df):
    # Identifying any column names that need to be modified
    cols = df.columns
    column_names = pd.DataFrame(columns=cols)
    print('Current column names:')
    display(column_names.T)

def convert_to_lowercase(df):
    # Convert column names to lowercase
    new_cols = [col.lower() for col in df.columns]
    return new_cols

def replace_and_display(df, old_char, new_char):
    # Replace specified character in all column names
    new_cols = [col.replace(old_char, new_char) for col in df.columns]
    df.columns = new_cols
    
    # Create a DataFrame with modified column names
    modified_column_names_df = pd.DataFrame(columns=new_cols)
    
    # Display the modified column names
    print('Modified column names:')
    display(pd.DataFrame(columns=new_cols).T)

def replace_column_name(df, old_name, new_name):
    # Replace a specific column name with a new name
    df = df.rename(columns={old_name: new_name})
    return df

def display_unique_values(df, columns_to_display):
    # Display unique values for specified columns
    for column in columns_to_display:
        unique_values = df[column].unique()
        print(f"\nUnique values for {column}:\n{unique_values}")

def standardize_values(df, column, value_mapping):
    # Replace specified values in the specified column
    #valu_mapping can ba a dictionary
    df[column] = df[column].replace(value_mapping)
    
def transform_to_numeric_and_display(df: pd.DataFrame, column_name: str) -> None:
   
    # Transform the specified column to numeric
    df[column_name] = pd.to_numeric(df[column_name], errors='coerce')

    # Display the data type of the transformed column
    print(f"Data type of '{column_name}': {df.dtypes[column_name]}")

def fix_number_of_open_complaints_format_and_display(df: pd.DataFrame, column_name: str) -> None:
  
    # Fix the format of the specified column
    df[column_name] = df[column_name].apply(lambda x: int(str(x).split('/')[1]) if '/' in str(x) else x)

    # Display unique values after fixing the format
    unique_values = df[column_name].unique()
    print(f"Unique values for '{column_name}':\n{unique_values}")

def identify_and_count_null_values(df: pd.DataFrame) -> None:

    # Count null values in each column
    null_counts = df.isnull().sum()

    # Display columns with null values and their respective counts
    print("Columns with Null Values:")
    print(null_counts)

def drop_rows_with_nulls_and_display_null_counts(df: pd.DataFrame) -> pd.DataFrame:

    # Drop rows with null values
    df_dropped = df.dropna(how='all')

    # Display null counts after dropping rows
    null_counts_after_drop = df_dropped.isnull().sum()
    print("Null counts after dropping rows with null values:")
    print(null_counts_after_drop)

    return df_dropped

def display_rows_with_null_values(df: pd.DataFrame, column_name: str) -> None:

    # Display rows where the specified column has null values
    rows_with_nulls = df[df[column_name].isnull()]

    # Print the resulting dataframe
    print(f"Rows with null values in '{column_name}':")
    display(rows_with_nulls)

def drop_row_by_index_and_display(df: pd.DataFrame, index_to_drop: int) -> pd.DataFrame:

    # Drop the specified row by index
    df_dropped_row = df.drop(index_to_drop)

    # Display the resulting dataframe
    print(f"DataFrame after dropping row with index {index_to_drop}:")
    display(df_dropped_row)

    return df_dropped_row

def fill_null_values_with_mean_and_display(df: pd.DataFrame, column_name: str) -> None:
 
    # Calculate the mean value of the specified column
    mean_value = df[column_name].mean()

    # Fill null values in the specified column with the mean
    df[column_name].fillna(mean_value, inplace=True)

    # Display rows with null values after filling with the mean
    rows_with_nulls = df[df[column_name].isnull()]
    print(f"Rows with null values in '{column_name}' after filling with mean:")
    display(rows_with_nulls)

def fill_null_values_with_default_and_display(df: pd.DataFrame, column_name: str, default_value: str) -> None:

    # Fill null values in the specified column with the default value
    df[column_name].fillna(default_value, inplace=True)

    # Display null counts after filling with the default value
    null_counts_after_fill = df.isnull().sum()
    print(f"Null counts after filling '{column_name}' with '{default_value}':")
    display(null_counts_after_fill)



# In[ ]:




