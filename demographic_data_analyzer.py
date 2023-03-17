import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    # columns = df.columns.tolist()
    # print(columns)
  
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()

    # What is the average age of men?
    calc_average_age_men = df[ df["sex"] == "Male" ]["age"].mean()
    average_age_men = round(calc_average_age_men,1)
  
    # What is the percentage of people who have a Bachelor's degree?
    # shape will return dataframe dimention
    calc_percentage_bachelors = 100 * len( df[ df["education"] == "Bachelors" ] ) / len(df)
    percentage_bachelors      = round(calc_percentage_bachelors,1)
    
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    educate         = df[ df['education'].isin( ['Bachelors', 'Masters', 'Doctorate'] )]
    notEducate      = df[~df['education'].isin( ['Bachelors', 'Masters', 'Doctorate'] )]
    rich            = df[ df['salary'] == '>50K' ]
    notRich         = df[ df['salary'] != '>50K' ]
    educateRich     = pd.merge(educate,rich); 
    notEducateRich  = pd.merge(notEducate,rich);

    # percentage with salary >50K
    higher_education_rich = round(100*(educateRich.size / educate.size),1)
    lower_education_rich  = round(100*(notEducateRich.size / notEducate.size),1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df[ ['hours-per-week'] ].min().shape[0]

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    worker_min_h      = df[ df['hours-per-week'] == min_work_hours ]
    rich_worker_min_h = pd.merge( rich, worker_min_h)
    rich_percentage   = round( ( 100*rich_worker_min_h.size ) / worker_min_h.size, 1 )

    # What country has the highest percentage of people that earn >50K?
    all_country  = df["native-country"].value_counts()
    rich_country = ( df[df["salary"] == ">50K"]["native-country"].value_counts() )
    percent_rich_country = ( 100*rich_country / all_country ).sort_values(ascending=False)
    richest_country = percent_rich_country.idxmax()
    richest_percent = percent_rich_country[0]

    highest_earning_country = percent_rich_country.idxmax()
    highest_earning_country_percentage = round(percent_rich_country[0],1)

    # Identify the most popular occupation for those who earn >50K in India.
    all_job = df[ df['native-country'] == 'India' ]["occupation"].value_counts()
    most_popular_job = all_job.idxmax()
    most_popular_value = all_job[0]
  
    top_IN_occupation = most_popular_job

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
