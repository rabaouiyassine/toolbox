def missing_values_table(train_df):
    """
    Function to calculate missing values by column
    
    params:
    -------
    train_df : data frame 
    the data frame to analyze 
    
    
    output : 
    -------
    mis_val_table_ren_columns : dataframe
    the missing values 
    """
    # Total missing values
    mis_val = train_df.isnull().sum()

    # Percentage of missing values
    mis_val_percent = 100 * train_df.isnull().sum()/len(train_df)

    # Make a table with the results
    mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)

    # Rename the columns
    mis_val_table_ren_columns = mis_val_table.rename(columns = {0: 'Missing Values', 1: '% of Total Values'})

    # Sort the table by percentage of missing descending
    mis_val_table_ren_columns = mis_val_table_ren_columns[mis_val_table_ren_columns.iloc[:,1]!=0].sort_values(
    '% of Total Values', ascending=False).round(1)

    #Print some summary information
    print(
        (
            (
                f'Your selected dataframe has{str(train_df.shape[1])}'
                + "columns.\n"
                "There are"
            )
            + str(mis_val_table_ren_columns.shape[0])
            + "columns that have missing values."
        )
    )

    # Return the dataframe with missing information
    return mis_val_table_ren_columns
