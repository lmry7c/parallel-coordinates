import pandas as pd
df = pd.read_csv("datasets/dataset52.csv")
df.head(0)
x = df.iloc[:,(1)]

group = []

for  names in x:
    print(names + ",")
    if names in ("Argentina", "Antigua and Barbuda", "Aruba", "Barbados", "Belize", "Bolivia", "Brazil", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominica", "Dominican Republic", "Ecuador", "El Salvador", "Grenada", "Guatemala", "Guyana", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "St. Kitts and Nevis", "St. Lucia", "St. Vincent and the Grenadines", "Suriname", "Trinidad and Tobago", "Uruguay", "Republica Bolivariana de Venezuela", "Venezuela, RB", "Bahamas, The"):
        group.append ('Latin America and the Caribbean')
    elif names in ("American Samoa", "Brunei Darussalam", "Cambodia", "China", "Macao SAR, China", "Hong Kong SAR, China", "Fiji", "Indonesia", "Japan", "Kiribati", "Singapore", "Democratic Republic of Korea", "Korea, Dem. People's Rep.", "Korea, Rep.", "Republic of Korea", "Lao People's Democratic Republic", "Lao PDR", "Malaysia", "Marshall Islands", "Federated States of Micronesia", "Mongolia", "Myanmar", "Palau", "Papua New Guinea", "Philippines", "Samoa", "Solomon Islands", "Thailand", "Timor-Leste", "Tonga", "Tuvalu", "Vanuatu", "Vietnam", "Micronesia, Fed. Sts."):
        group.append ('East Asia and Pacific')
    elif names in ("Canada", "The United States", "United States"):
        group.append ('North America')
    elif names in ("Angola" ,  "Benin" ,  "Botswana" ,  "Burkina Faso" ,  "Burundi" ,  "Cameroon" ,  "Cape Verde" ,  "Cote d'Ivoire", "Central African Republic" ,  "Cabo Verde", "Chad" ,  "Commoros" ,  "Democratic Republic of Congo" ,  "Republic of Congo" ,  "Congo, Rep.", "Congo, Dem. Rep.", "Equatorial Guinea" ,  "Eritrea" ,  "Ethiopia" ,  "Gabon" ,  "The Gambia" , "Gambia, The",  "Ghana" ,  "Guinea" ,  "Guinea-Bissau" ,  "Kenya" ,  "Lesotho" ,  "Liberia" ,  "Madagascar" ,  "Malawi" ,  "Mali" ,  "Mauritania" ,  "Mauritius" ,  "Mozambique" ,  "Namibia" ,  "Niger" ,  "Nigeria" ,  "Rwanda" ,  "Senegal" ,  "Seychelles" ,  "Sierra Leone" ,  "Somalia" ,  "South Africa" ,  "South Sudan" ,  "Sudan" ,  "Swaziland" ,  "Tanzania" ,  "Togo" ,  "Sao Tome and Principe", "Uganda" ,  "Zambia" ,  "Zimbabwe"):
        group.append ('Africa')
    elif names in ("Albania", "Armenia", "Azerbaijan", "Belarus", "Bosnia and Herzegovina", "Georgia", "Kazakhstan", "Kosovo", "Kyrgyz Republic", "Former Yugoslav Republic of Macedonia", "Macedonia, FYR", "Moldova", "Montenegro", "Russian Federation", "Slovak Republic", "Serbia", "Tajikistan", "Turkey", "Turkmenistan", "Ukraine", "Uzbekistan"):
        group.append ('Europe and Central Asia')
    elif names in("Algeria", "Djibouti", "Arab Republic of Egypt", "Egypt, Arab Rep.", "Islamic Republic of Iran", "Iran, Islamic Rep.", "Iraq", "Israel", "Jordan", "Kuwait", "Lebanon", "Libya", "Morocco", "Syrian Arab Republic", "Tunisia", "West Bank and Gaza", "the Republic of Yemen", "United Arab Emirates", "Qatar", "Yemen, Rep.", "Bahrain", "Saudi Arabia", "Oman"):
        group.append ('Middle East and North Africa')
    elif names in("Afghanistan", "Bangladesh", "Bhutan", "India", "Maldives", "Nepal", "Pakistan", "Sri Lanka"):
        group.append ('South Asia')
    elif names in("Austria", "Belgium", "Cyprus", "Czech Republic", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Ireland", "Italy", "Luxembourg", "Malta", "Netherlands", "Portugal", "Slovakia", "Slovenia", "Spain", "Switzerland", "Sweden", "United Kingdom", "Norway"):
        group.append ('EU')
    elif names in("Bulgaria", "Croatia", "Poland", "Romania", "Latvia", "Lithuania"):
        group.append ('Europe and Central Asia: Members of EU')
    elif names in("Australia", "New Caledonia", "Nauru", "New Zealand" ):
        group.append ('Oceania')
    else:
        group.append ('Other')

df['group'] = group       

df.to_csv('test.csv', index = False)
