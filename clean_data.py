import pandas as pd

# 1. Load the original dataset
file_path = '/Users/ambareeshlankipalli/Downloads/data.csv'
df = pd.read_csv(file_path, sep=';')

# 2. Build the Translation Dictionaries for Marital Status and Course
marital_map = {
    1: 'Single',
    2: 'Married',
    3: 'Widower',
    4: 'Divorced',
    5: 'Facto Union',
    6: 'Legally Separated'
}

course_map = {
    33: 'Biofuel Production Technologies',
    171: 'Animation and Multimedia Design',
    8014: 'Social Service (evening attendance)',
    9003: 'Agronomy',
    9070: 'Communication Design',
    9085: 'Veterinary Nursing',
    9119: 'Informatics Engineering',
    9130: 'Equinculture',
    9147: 'Management',
    9238: 'Social Service',
    9254: 'Tourism',
    9500: 'Nursing',
    9556: 'Oral Hygiene',
    9670: 'Advertising and Marketing Management',
    9773: 'Journalism and Communication',
    9853: 'Basic Education',
    9991: 'Management (evening attendance)'
}

# 3. Apply the translations using .map()
df['Marital status'] = df['Marital status'].map(marital_map)
df['Course'] = df['Course'].map(course_map)

# 4. Save the cleanly translated data into a brand new file
output_path = '/Users/ambareeshlankipalli/Downloads/cleaned_student_data.csv'
df.to_csv(output_path, sep=';', index=False)

# 5. Print a success message and a preview of the newly cleaned data
print(f"\n🎉 SUCCESS! Cleaned dataset permanently saved to:\n👉 {output_path}\n")
print("--- Here is a sneak peek at your new human-readable columns: ---")
print(df[['Marital status', 'Course']].head())