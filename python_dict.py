import pandas as pd
df = pd.read_csv("datasets/dataset57.csv")
df.head(0)
countries = df.iloc[:,(1)]
last = df.iloc[:,-1]

group = []

regions = {'Latin America and the Caribbean': {"Argentina", "Antigua and Barbuda", "Aruba", "Barbados", "Belize", "Bolivia", "Brazil", "Bermuda", "Cayman Islands", "Chile", "Colombia", "Costa Rica", "Cuba", "Dominica", "Dominican Republic", "Ecuador", "El Salvador", "Grenada", "Guatemala", "Guyana", "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", "Puerto Rico", "St. Kitts and Nevis", "St. Lucia", "St. Vincent and the Grenadines", "Suriname", "Trinidad and Tobago", "Uruguay", "Republica Bolivariana de Venezuela", "Venezuela, RB", "Bahamas, The", "Virgin Islands (U.S.)"},
           'East Asia and Pacific': {"American Samoa", "Brunei Darussalam", "Cambodia", "China", "Macao SAR, China", "Hong Kong SAR, China", "Fiji", "Indonesia", "Japan", "Kiribati", "Singapore", "Democratic Republic of Korea", "Korea, Dem. People's Rep.", "Korea, Rep.", "Republic of Korea", "Lao People's Democratic Republic", "Lao PDR", "Malaysia", "Marshall Islands", "Federated States of Micronesia", "Mongolia", "Myanmar", "Palau", "Papua New Guinea", "Philippines", "Samoa", "Solomon Islands", "Thailand", "Timor-Leste", "Tonga", "Tuvalu", "Vanuatu", "Vietnam", "Micronesia, Fed. Sts."},
           'North America': {"Canada", "The United States", "United States"},
           'Sub-Saharan Africa': {"Angola" ,  "Benin" ,  "Botswana" ,  "Burkina Faso" ,  "Burundi" ,  "Cameroon" ,  "Cape Verde" ,  "Cote d'Ivoire", "Central African Republic" ,  "Cabo Verde", "Chad" ,  "Commoros" , "Comoros", "Democratic Republic of Congo" ,  "Republic of Congo" ,  "Congo, Rep.", "Congo, Dem. Rep.", "Equatorial Guinea" ,  "Eritrea" ,  "Ethiopia" ,  "Gabon" ,  "Gambia", "The Gambia" , "Gambia, The",  "Ghana" ,  "Guinea" ,  "Guinea-Bissau" ,  "Kenya" ,  "Lesotho" ,  "Liberia" ,  "Madagascar" ,  "Malawi" ,  "Mali" ,  "Mauritania" ,  "Mauritius" ,  "Mozambique" ,  "Namibia" ,  "Niger" ,  "Nigeria" ,  "Rwanda" ,  "Senegal" ,  "Seychelles" ,  "Sierra Leone" ,  "Somalia" ,  "South Africa" ,  "South Sudan" ,  "Sudan" ,  "Swaziland" ,  "Tanzania" ,  "Togo" ,  "Sao Tome and Principe", "Uganda" ,  "Zambia" ,  "Zimbabwe"},
           'Europe and Central Asia': {"Albania", "Armenia", "Azerbaijan", "Belarus", "Bosnia and Herzegovina", "Georgia", "Kazakhstan", "Kosovo", "Kyrgyz Republic", "Former Yugoslav Republic of Macedonia", "Macedonia, FYR", "Moldova", "Montenegro", "Russian Federation", "Slovak Republic", "Serbia", "Tajikistan", "Turkey", "Turkmenistan", "Ukraine", "Uzbekistan", "Iceland", "United Kingdom", "Liechtenstein",  "Monaco", "San Marino", "Greenland", "Andorra", "Austria", "Belgium", "Cyprus", "Czech Republic", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Ireland", "Italy", "Luxembourg", "Malta", "Netherlands", "Portugal", "Slovakia", "Slovenia", "Spain", "Switzerland", "Sweden", "Bulgaria", "Croatia", "Poland", "Romania", "Latvia", "Lithuania"},
           'Middle East and North Africa': {"Algeria", "Djibouti", "Arab Republic of Egypt", "Egypt, Arab Rep.", "Islamic Republic of Iran", "Iran, Islamic Rep.", "Iraq", "Israel", "Jordan", "Kuwait", "Lebanon", "Libya", "Morocco", "Syrian Arab Republic", "Tunisia", "West Bank and Gaza", "the Republic of Yemen", "United Arab Emirates", "Qatar", "Yemen, Rep.", "Bahrain", "Saudi Arabia", "Oman"},
           'South Asia': {"Afghanistan", "Bangladesh", "Bhutan", "India", "Maldives", "Nepal", "Pakistan", "Sri Lanka"},
           'Oceania': {"Australia", "New Caledonia", "Nauru", "New Zealand", "Guam"}
          }

g20 = {'G20 Member': {"Argentina", "Austria", "Brazil", "China", "Canada", "The United States", "United States", "France", "Germany", "India", "Indonesia", "Japan", "Democratic Republic of Korea", "Korea, Rep.", "Republic of Korea", "Mexico", "Russia", "South Africa", "Turkey", "United Kingdom", "Norway"},
        'G20 permanent guests': {"Spain", "Norway", "Singapore", "Vietnam", "Sengal", "Netherlands", "Guinea"}
        }
        
regionalOrgs = {'ASEAN Member': {"Brunei Darussalam", "Cambodia", "Indonesia","Lao People's Democratic Republic", "Lao PDR", "Malaysia", "Myanmar", "Philippines", "Singapore", "Thailand", "Vietnam"},
                'ASEAN Observers': {"Papua New Guinea", "Timor-Leste"},
                'EU': {"Andorra", "Austria", "Belgium", "Cyprus", "Czech Republic", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Ireland", "Italy", "Luxembourg", "Malta", "Netherlands", "Portugal", "Slovakia", "Slovenia", "Spain", "Switzerland", "Sweden", "Bulgaria", "Croatia", "Poland", "Romania", "Latvia", "Lithuania"},
        }

income = {'Low-Income Economies': {"Afghanistan", "Guinea", "Rwanda", "Benin", "Guinea-Bissau", "Senegal", "Burkina Faso", "Haiti", "Sierra Leone", "Burundi", "Korea, Dem. People's Rep.", "Somalia", "Democratic Republic of Korea", "Central African Republic", "Liberia", "South Sudan", "Chad", "Madagascar", "Tanzania", "Comoros", "Malawi", "Togo", "Congo, Dem. Rep", "Mali", "Uganda", "Eritrea", "Mozambique", "Zimbabwe", "Ethiopia", "Nepal", "Gambia", "The Niger"},
          'Lower-Middle-Income Economies': {},
          'Upper-Middle-Income Economies': {},
          'High-Income Economies': {}
         }

category = regions

for country_name in countries:
    # print(country_name)
    matched_region = 'Other'
    for region in category.keys():
        # print(region)
        if country_name in category[region]:
            matched_region = region
            break
    # print('Result: '+matched_region)
    group.append(matched_region)

'''for names in x[0:2]:
    print(names)
    for key in category.keys():
        print(key)
        if names in category[key]:
            print("match_found!")
            group.append(key)
            break
        group.append("Other")
        print('no match')

print len(group)
print len(x)
'''

'''for country_name in countries:
    #print(country_name)
    region = 'TBD'
    while region == 'TBD':
        for key in category.keys():
            #print(key)
            if country_name in category[key]:
                region = key
                #print("match_found!")
                break
        region = 'Other'
    group.append(region)
            
        #group.append("Other")
        #print('no match')

print len(group)
print len(countries)'''
        


'''            test = key
            if pd.isnull(group)
                group.append("Other")'''


'''        if len(str(category[key])) < 1:
            group.append("Other")'''

df['group'] = group       

df.to_csv('testvariableHope.csv', index = False)
