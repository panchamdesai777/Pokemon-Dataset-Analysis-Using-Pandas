import pandas as pd
#LOADING THE DATASET USING READ_CSV() PANDA FILE OPERATION

filepath = pokemon
df=pd.read_csv(filepath)
print(df.head())

#QUICK EXPLORATION OF DATA


# head of the dataframe
head = df.head(10)
print(head)
# describe the dataframe
describe = df.describe()
print(describe)
# shape of the dataframe
shape = df.shape
print(shape)
# check for null values
null = df.isnull().sum()
print(null)
# check for unique values
unique = df.nunique()
print(unique)



# Create a new column total
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Speed'] + df['Sp. Atk'] + df['Sp. Def']
print(df.head())

#CLEANING OF DATA



# Rename columns 'HP', 'Sp. Atk' and 'Sp. Def' as 'Health Points', 'Attack speed points' and 'Defense speed points'
df.rename(columns={'HP':'Health Points','Sp. Atk':'Attack speed points',
'Sp. Def':'Defense speed points'}, inplace=True)
# Remove the '#' column permanently
df.drop('#',inplace=True,axis=1)
# Set index as names
df.set_index('Name',inplace=True)
# Look at the first 5 observations
print(df.head(5))

#EXPLORING CATEGORICAL DATA

#Total Different variants of `Type 2`
type_two_num = df['Type 2'].nunique()
print('Total Different variants of `Type 2`:', type_two_num)
print('='*50)
#different variants of `Type 2`
type_two = df['Type 2'].unique()
print('variants of type 2:',type_two)
print('='*50)

# Counts for different types of `Type 2`
counts_type_two = df['Type 2'].value_counts()
print('Counts for different types of `Type 2`:', counts_type_two)
print('='*50)

# Number of Pokemons don't have `Type 2`
no_type_two = df['Type 2'].isnull().sum()
print('Number of Pokemons dont have type 2:', no_type_two)


#EXPLORING NUMERICAL DATA


# Which pokemon has the highest 'Health Points'?

healthiest_pokemon = df['Health Points'].idxmax()
print(' Which pokemon has the highest Health Points?:',healthiest_pokemon)
print("="*50)

# Which pokemon has the highest Special Atack points?

special_attack_pokemon = df['Attack speed points'].idxmax()
print('Which pokemon has the highest Special Attack points?:',special_attack_pokemon)
print('='*50)

# Which pokemon has the highest Special Defense points?

special_defense_pokemon = df['Defense speed points'].idxmax()
print('Which pokemon has the highest Special Defense points?:',special_defense_pokemon)
print('='*50)

# Which pokemon has highest Speed?

fastest_pokemon = df['Speed'].idxmax()
print('Which pokemon has highest Speed?:',fastest_pokemon)
print('='*50)


