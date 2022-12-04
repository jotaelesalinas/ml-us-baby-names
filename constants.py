YEAR_START = 1960   # if you change YEAR_START or YEAR_END,
YEAR_END = 2021     # remove all CSV files except CSV_RAW

COMPUTE_YEARS_BACKWARDS = 5
YEARS_NO_TRAINING = 5

STATES = ('AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL',
          'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME',
          'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH',
          'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI',
          'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI',
          'WY')

URL_YEAR_COUNTRY = 'https://www.ssa.gov/cgi-bin/popularnames.cgi'
URL_YEAR_STATE = 'https://www.ssa.gov/cgi-bin/namesbystate.cgi'

CSV_RAW = "data_raw.csv"

CSV_COUNTRY = "data_country.csv"
CSV_FEATURES_CURRENT = "data_features_1_current.csv"
CSV_FEATURES_PAST = "data_features_2_past.csv"
CSV_FEATURES_LABEL = "data_features_3_label.csv"
