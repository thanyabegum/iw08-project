import tabula

county_file = "raw/voter_registration_by_county.pdf"
district_file = "raw/voter_registration_by_legislative_district.pdf"

party_by_county = tabula.read_pdf(county_file, pages='1')
party_by_district = tabula.read_pdf(district_file, pages='1')

# print(party_by_county)
# print(party_by_district)

tabula.convert_into(county_file, "output/voter_registration_by_county.csv", output_format="csv", pages='1')
tabula.convert_into(district_file, "output/voter_registration_by_legislative_district.csv", output_format="csv", pages='1')