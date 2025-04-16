import pandas as pd

def calculate_demographic_data(print_data=True):
    # Lecture des données
    df = pd.read_csv("adult.data.csv")

    # 1. Compte des races
    race_count = df['race'].value_counts()

    # 2. Âge moyen des hommes
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Pourcentage de titulaires d’un baccalauréat
    total_people = len(df)
    num_bachelors = df[df['education'] == 'Bachelors'].shape[0]
    percentage_bachelors = round((num_bachelors / total_people) * 100, 1)

    # 4. Pourcentage de >50K avec études avancées
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    higher_edu_rich = round(
        (higher_education[higher_education['salary'] == '>50K'].shape[0] / higher_education.shape[0]) * 100, 1)

    # 5. Pourcentage de >50K sans études avancées
    lower_edu_rich = round(
        (lower_education[lower_education['salary'] == '>50K'].shape[0] / lower_education.shape[0]) * 100, 1)

    # 6. Nombre minimal d’heures travaillées par semaine
    min_work_hours = df['hours-per-week'].min()

    # 7. Pourcentage de >50K chez ceux qui travaillent le minimum
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(
        (num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0]) * 100, 1)

    # 8. Pays avec le plus haut % de >50K
    country_group = df.groupby('native-country')
    rich_by_country = country_group['salary'].apply(lambda x: (x == '>50K').sum() / x.count() * 100)
    highest_earning_country = rich_by_country.idxmax()
    highest_earning_country_percentage = round(rich_by_country.max(), 1)

    # 9. Job le plus populaire en Inde pour >50K
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_rich['occupation'].value_counts().idxmax()

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_edu_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_edu_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_edu_rich,
        'lower_education_rich': lower_edu_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
