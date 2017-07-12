import pandas as pd
df = pd.read_csv("datasets/dataset47.csv")
df.head(0)
x = df.iloc[:,(1)]
last = df.iloc[:,-1]

group = []

regions = {'Latin America and the Caribbean': {"Argentina", "Antigua and Barbuda", "Barbados", "Belize", "Bolivia", "Brazil", "Bermuda", "Cayman Islands", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominica", "Dominican Republic", "Ecuador", "El Salvador", "Grenada", "Guatemala", "Guyana", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "St. Kitts and Nevis", "St. Lucia", "St. Vincent and the Grenadines", "Suriname", "Trinidad and Tobago", "Uruguay", "Republica Bolivariana de Venezuela", "Venezuela, RB", "Bahamas, The", "Virgin Islands (U.S.)"},
           'East Asia and Pacific': {"American Samoa", "Brunei Darussalam", "Cambodia", "China", "Macao SAR, China", "Hong Kong SAR, China", "Fiji", "Indonesia", "Japan", "Kiribati", "Singapore", "Democratic Republic of Korea", "Korea, Dem. People's Rep.", "Korea, Rep.", "Republic of Korea", "Lao People's Democratic Republic", "Lao PDR", "Malaysia", "Marshall Islands", "Federated States of Micronesia", "Mongolia", "Myanmar", "Palau", "Papua New Guinea", "Philippines", "Samoa", "Solomon Islands", "Thailand", "Timor-Leste", "Tonga", "Tuvalu", "Vanuatu", "Vietnam", "Micronesia, Fed. Sts."},
           'North America': {"Canada", "The United States", "United States", "Greenland"},
           'Africa': {"Angola" ,  "Benin" ,  "Botswana" ,  "Burkina Faso" ,  "Burundi" ,  "Cameroon" ,  "Cape Verde" ,  "Cote d'Ivoire", "Central African Republic" ,  "Cabo Verde", "Chad" ,  "Commoros" , "Comoros", "Democratic Republic of Congo" ,  "Republic of Congo" ,  "Congo, Rep.", "Congo, Dem. Rep.", "Equatorial Guinea" ,  "Eritrea" ,  "Ethiopia" ,  "Gabon" ,  "The Gambia" , "Gambia, The",  "Ghana" ,  "Guinea" ,  "Guinea-Bissau" ,  "Kenya" ,  "Lesotho" ,  "Liberia" ,  "Madagascar" ,  "Malawi" ,  "Mali" ,  "Mauritania" ,  "Mauritius" ,  "Mozambique" ,  "Namibia" ,  "Niger" ,  "Nigeria" ,  "Rwanda" ,  "Senegal" ,  "Seychelles" ,  "Sierra Leone" ,  "Somalia" ,  "South Africa" ,  "South Sudan" ,  "Sudan" ,  "Swaziland" ,  "Tanzania" ,  "Togo" ,  "Sao Tome and Principe", "Uganda" ,  "Zambia" ,  "Zimbabwe"},
           'Europe and Central Asia': {"Albania", "Armenia", "Azerbaijan", "Belarus", "Bosnia and Herzegovina", "Georgia", "Kazakhstan", "Kosovo", "Kyrgyz Republic", "Former Yugoslav Republic of Macedonia", "Macedonia, FYR", "Moldova", "Montenegro", "Russian Federation", "Slovak Republic", "Serbia", "Tajikistan", "Turkey", "Turkmenistan", "Ukraine", "Uzbekistan"},
           'Middle East and North Africa': {"Algeria", "Djibouti", "Arab Republic of Egypt", "Egypt, Arab Rep.", "Islamic Republic of Iran", "Iran, Islamic Rep.", "Iraq", "Israel", "Jordan", "Kuwait", "Lebanon", "Libya", "Morocco", "Syrian Arab Republic", "Tunisia", "West Bank and Gaza", "the Republic of Yemen", "United Arab Emirates", "Qatar", "Yemen, Rep.", "Bahrain", "Saudi Arabia", "Oman"},
           'South Asia': {"Afghanistan", "Bangladesh", "Bhutan", "India", "Maldives", "Nepal", "Pakistan", "Sri Lanka"},
           'EU': {"Andorra", "Austria", "Belgium", "Cyprus", "Czech Republic", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Ireland", "Italy", "Luxembourg", "Malta", "Netherlands", "Portugal", "Slovakia", "Slovenia", "Spain", "Switzerland", "Sweden"},
           'Europe and Central Asia: Members of EU': {"Bulgaria", "Croatia", "Poland", "Romania", "Latvia", "Lithuania"},
           'Oceania': {"Australia", "New Caledonia", "Nauru", "New Zealand", "Guam"},
           'Other European Countries': {"Iceland", "United Kingdom", "Liechtenstein",  "Monaco", "San Marino"},
          }

g20 = {"Argentina", "Austria", "Brazil", "China", "Canada", "The United States", "United States", "France", "Germany", "India", "Indonesia", "Japan", "Democratic Republic of Korea", "Korea, Rep.", "Republic of Korea", "Mexico", "Russia", "South Africa", "Turkey", "United Kingdom", "Norway"}

category = regions

for names in x:
    for key in category:
        if names in category[key]:
            group.append(key)
        if len(category[key]) < 1:
            group.append("Other")

print group

df['group'] = group       

df.to_csv('testvariable.csv', index = False)
