# Program for testing around with case numbers for project
# Case Numbers are defined as: YYYY-CourtAcronym-SixDigitNumber-OptionalLetter
# It *seems* that only cases with the 'CA' acronym require an optional letter. Code reflects this.
# The dashes in the case number are not necessary

# Importing current date for default end year in generator.
from datetime import date
current_year = date.today().year

# Court acronyms for the majority of cases (prior to Oct. 31, 2022).
court_acronyms_old = ('CA', 'CA1', 'CA2',  # This 'CA' I add due to seeing cases with it, but not in documentation.
                      'CA3', 'CAA', 'CAB',
                      'CAC', 'CAD', 'CAE',
                      'CAF', 'CAH', 'CAL',
                      'CAM', 'CAO', 'CAP',
                      'CAR', 'CAS', 'CAT',
                      'LTB', 'SC1', 'SC2',
                      'SC3', 'SCB', 'SCJ',
                      'FEP', 'ADM', 'DIS',
                      'LIT', 'SEB', 'CVT', 'WIL')

# Court acronyms for newer cases for on or after Oct. 31, 2022.
court_acronyms_new = ('AA', 'AP', 'CAAF', 'CACC', 'CACL', 'CACO',
                      'CAED', 'CAFJ', 'CAFS', 'CAH', 'CAIFJ', 'CAM',
                      'CAQT', 'CAR', 'CARF', 'CAS', 'CAST', 'CAT', 'CATA',
                      'CAVF', 'CTO', 'GC', 'MFLC', 'NCVRA', 'LTNT',
                      'LTR', 'LTPS', 'LTC', 'MFLC', 'COL', 'CTC', 'ED',
                      'FJU', 'INS', 'LTD', 'MAL', 'MFLC', 'PDCTL', 'TOR',
                      'UAA', 'FEP', 'ADM', 'AMC', 'AMF', 'AMP', 'AMS',
                      'AMT', 'NRT', 'DIS', 'LIT', 'SEB', 'CVT', 'WIL')

# Certified optional letters (by observation) include B, C, M, and L(RB)
optional_letters = ('B', 'C', 'M', 'L(RB)')  # TODO: Need to confirm these are all the possible optional letters.

# Depending on scope of scraper, need to implement new acronyms for scraping post-10/31/22
# Case number generator; for now, simply prints all possible combinations.


def generate_court_codes(initial_year=1900, end_year=current_year):  # 1900 is the earliest possible year to search.
    for year in range(initial_year, end_year + 1):
        for court in court_acronyms_old:
            for num in range(0, 1000000):
                code = str(num)
                while len(code) < 6:
                    code = '0' + code
                if court == 'CA':
                    for letter in optional_letters:
                        print(str(year) + court + code + letter)
                else:
                    print(str(year) + court + code)


print(generate_court_codes(2012))
