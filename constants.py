YEAR_START = 1960
YEAR_END = 2021
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

RAW_CSV = "data_raw_year_state.csv"
RAW_CSV_COUNTRY = "data_raw_country.csv"
FEATURES_CSV = "data_features_%s.csv"
