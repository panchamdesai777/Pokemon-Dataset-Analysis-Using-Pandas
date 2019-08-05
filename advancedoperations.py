#conditional Filtering Method

#Drop row with Name as nan
df = df[df.index.notnull()]

# Code starts here


# Find out which type of pokemons (use only `Type 1`) have the highest chances of being Legendary

highest_legendary = df[df['Legendary'] == True]['Type 1'].value_counts().idxmax()
single_type_legendary = len(df[df['Type 2'].isnull() & df['Legendary'] == True])
print(highest_legendary)
print(single_type_legendary)

#Apply Functions

# Convert 'Name' to uppercase
df.index = df.index.str.upper()

print('Convert Name to uppercase',df.index)
print("="*50)

# Convert 'Type 1' to lowercase
df['Type 1'] = df['Type 1'].apply(lambda x:x.lower())
print("="*50)

# Convert 'Type 2' to lowercase if present else 
df['Type 2'] = df['Type 2'].apply(lambda x: x.lower() if isinstance(x, str) else None)
print(df['Type 2'])

#Groupby and Sorting

# Determine which type (Type 1) pokemons are the fastest(Speed)
df.groupby(['Type 1','Speed']).groups
fastest_type = df.groupby('Type 1')['Speed'].agg(np.median).sort_values(ascending=False).idxmax()
print(fastest_type)

#Pivot Tables

# mean value of 'Attack speed points' according to 'Generation' and 'Type 1'
pivot = pd.pivot_table(df,index = 'Type 1',columns = 'Generation', values= 'Attack speed points')
print(' mean value of Attack speed points according to Generation and Type:',pivot )



