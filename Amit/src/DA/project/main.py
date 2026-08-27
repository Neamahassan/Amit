from config.config import RAW_DATA_PATH, COLUMNS_TO_DROP
from preprocessing import(
read_data_file,
drop_unnecessary_features,
check_data_type
)
def main():
    # 1) Read The data
    df = read_data_file(RAW_DATA_PATH)
    # check if the data was loaded successfully
    if df is None:
        print("program stopped because data loading failed.")
        return
    # 2) Drop unnecessary columns based on the config
    df = drop_unnecessary_features(df,COLUMNS_TO_DROP)
    # 3) Check data quality
    quality_report = check_data_type(df)
    # Display the Data Quality Report
    print("\n--- Data Quality Report ---")
    print(quality_report)

if __name__ == "__main__":
    main()

        