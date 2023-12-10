import pandas as pd


def generate_car_matrix(df)->pd.DataFrame:
    """
    Creates a DataFrame  for id combinations.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values, 
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
    # Write your logic here
    import pandas as pd
    df = pd.read_csv("dataset-1.csv")
    df
    # Extract unique 'id_1' and 'id_2' values
    unique_id_1 = df['id_1'].unique()
    unique_id_1.sort()

    unique_id_2 = df['id_2'].unique()
    unique_id_2.sort()

    df = df.sort_values('car')

    # Create an empty DataFrame with 'id_1' as index and 'id_2' as columns
    car_matrix = pd.DataFrame(index=unique_id_1, columns=unique_id_2)

    # Fill the matrix with 'car' values from the DataFrame

    for index, row in df.iterrows():
        car_matrix.at[row['id_1'], row['id_2']] = row['car']

    # Fill NaN values with 0 or any default value if needed
    car_matrix = car_matrix.fillna(0)

    car_matrix




def get_type_count(df)->dict:
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    # Write your logic here
    # Use value_counts() to count occurrences of each car type
    car_counts = df['car'].value_counts().to_dict()

    car_counts



def get_bus_indexes(df)->list:
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
    # Write your logic here
    # Calculate the mean of 'bus' values
    bus_mean = df['bus'].mean()

    # Find indexes where 'bus' values exceed twice the mean
    bus_indexes = df[df['bus'] > 2 * bus_mean].index.tolist()

    bus_indexes




def filter_routes(df)->list:
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    # Write your logic here
    # Group by 'route' and calculate the mean of 'truck' values for each route
    route_means = df.groupby('route')['truck'].mean()

    # Filter routes with average 'truck' values greater than 7
    selected_routes = route_means[route_means > 7].index.tolist()

    selected_routes

    


def multiply_matrix(matrix)->pd.DataFrame:
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
    # Write your logic here

    return matrix


def time_check(df)->pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here

    return pd.Series()
