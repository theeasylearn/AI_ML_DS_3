import re 
text = """
Dear Customer,

Please verify the following details submitted in the application.

Applicant 1:
Name: Rahul Sharma
Mobile: 9876543210
Alternate Contact: +91 9123456789
Address: 12 Green Park, New Delhi - 110016
Aadhaar Number: 1234 5678 9012
PAN Number: ABCDE1234F

Applicant 2:
Name: Priya Patel
Phone: 7984561230
Office Contact: +91-9825012345
Address: 45 River View Society, Bhavnagar, Gujarat - 364001
Aadhaar: 5678 1234 9876
PAN: FGHIJ5678K

Applicant 3:
Name: Amit Verma
Mobile No: 8765432109
Address: MG Road, Bengaluru - 560001
Aadhaar Card Number: 4321 8765 2109
PAN Card: KLMNO4321P

Applicant 4:
Name: Neha Singh
Contact: 7012345678
Address: Sector 22, Chandigarh - 160022
Aadhaar: 9876 5432 1098
PAN Number: PQRST9876R

Applicant 5:
Name: Vikram Joshi
Phone: +91 8899776655
Address: Pune, Maharashtra - 411001
Aadhaar Number: 3456 7890 1234
PAN: UVWXY3456Z

Reference Numbers:
Order ID: ORD123456
Employee ID: EMP98765
Invoice Number: INV2026001

Thank you."""

#extract mobile from text
mobiles = re.findall(r'[0-9]{10}',text) #find string with only numbers size 10
print(mobiles)
#extract pincodes from text 
pincodes = re.findall(r'\s[0-9]{6}\n',text) #find string with only numbers size 6
print(pincodes)

#extract aadharcard numbers from text
aadhar_cards = re.findall(r'[0-9]{4} [0-9]{4} [0-9]{4}',text)
print(aadhar_cards)

#extract pancard numbers from text 
pan_cards = re.findall(r'[A-Z]{5}[0-9]{4}[A-Z]{1}',text)
print(pan_cards)