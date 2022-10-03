# Requirements
- Python 3.x

# Installation

```
pip install -r requirements.txt
```

## Usage

Replace test_worklog with your worklog csv file from Clockify Reports (Summary)

```
python cia.py test_worklog.csv
```

The script will then produce a `worklog.csv` file which you can easily copy pasta to your invoice report.

```
End                                               Date  Duration (decimal)
0   Independent Contractor Services on September 0...                6.58
1   Independent Contractor Services on September 0...                8.84
2   Independent Contractor Services on September 0...                6.83
3   Independent Contractor Services on September 0...                1.64
4   Independent Contractor Services on September 0...                6.39
5   Independent Contractor Services on September 0...                7.17
6   Independent Contractor Services on September 0...                8.63
7   Independent Contractor Services on September 0...                7.85
8   Independent Contractor Services on September 1...                5.85
9   Independent Contractor Services on September 1...                8.22
10  Independent Contractor Services on September 1...                9.01
11  Independent Contractor Services on September 1...                9.18
12  Independent Contractor Services on September 1...                8.01
13  Independent Contractor Services on September 1...                5.89
14  Independent Contractor Services on September 2...                9.30
15  Independent Contractor Services on September 2...                6.22
16  Independent Contractor Services on September 2...               10.46
17  Independent Contractor Services on September 2...                8.18
18  Independent Contractor Services on September 2...                6.03
19  Independent Contractor Services on September 2...               10.06
20  Independent Contractor Services on September 2...                7.25
21  Independent Contractor Services on September 3...                8.95
Duration (decimal)    166.54
```
