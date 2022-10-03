import sys
import pandas as pd

from datetime import datetime

input_date_format = '%d/%m/%Y'
output_date_format = 'Independent Contractor Services on %B %d, %Y'

worklog = (sys.argv[1:] or [None])[0]

if worklog is None:
    print('No worklog found. Please specify a worklog file.')
    sys.exit(1)

df = pd.read_csv(worklog)

df_work_logs = df[['End Date', 'Duration (decimal)']]

df_work_logs_by_end_date = df_work_logs.groupby('End Date').sum().reset_index()

def reformat_date_string(input_format, output_format):
    def formatter(date_str):
        date_obj = datetime.strptime(date_str, input_format) 
        new_date = date_obj.strftime(output_format)
        
        return new_date
    return formatter

date_formatter = reformat_date_string(
    input_format=input_date_format,
    output_format=output_date_format
)

df_formatted_end_dates = df_work_logs_by_end_date['End Date'].apply(date_formatter)

df_work_logs_by_end_date['End Date'] = df_formatted_end_dates

print(df_work_logs_by_end_date)
print(df_work_logs_by_end_date.groupby('End Date').sum().sum())

df_work_logs_by_end_date.to_csv('worklog.csv', index=False)