import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.DataFrame(pd.read_csv("adult.data.csv"))
    print(df.head())

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = pd.Series(df["race"].value_counts(), index=["White", "Black", "Asian-Pac-Islander",
                                                             "Amer-Indian-Eskimo", "Other"])

    # What is the average age of men?
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)
    #print(average_age_men)

    # What is the percentage of people who have a Bachelor's degree?
    #percentage_bachelors = df[df["education"] == "Bachelors"].shape[0] / df.shape[0] * 100
    percentage_bachelors = round(len(df[df["education"] == "Bachelors"]) / len(df["education"]) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df["education"].isin(["Bachelors", "Masters", "Doctorate"])]

    #print(higher_education)

    lower_education = df[~df["education"].isin(["Bachelors", "Masters", "Doctorate"])]
    #print(lower_education)

    # percentage with salary >50K
    higher_education_rich = round(len(higher_education[higher_education["salary"] == ">50K"]) / len(higher_education) * 100, 1)
    #print(higher_education_rich)

    lower_education_rich = round(len(lower_education[lower_education["salary"] == ">50K"]) / len(lower_education) * 100, 1)
    #print(lower_education_rich)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()
    #print(min_work_hours)

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    a = df[df["hours-per-week"] == 1]
    num_min_workers = df[df["hours-per-week"] == 1]['hours-per-week'].count()
    #print(num_min_workers)

    rich_percentage = len(a[a["salary"] == ">50K"]) / len(a) * 100
    ## TODO JUNTO
    b = df[(df['hours-per-week'] == 1) & (df['salary'] == '>50K')].shape[0] / num_min_workers * 100

    #print(rich_percentage)
    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = df[df["salary"] == ">50K"]["native-country"].value_counts().index[0]


    c = df[df["salary"] == ">50K"]["native-country"].value_counts()
    #print(c)
    highest_earning_country_percentage = int(round(\
        (len(df[(df["salary"] == ">50K") & (df["native-country"] == "United-States")])) / len(df["salary"] == ">50K") * 100,1))
    #highest_earning_country_percentage = round(highest_earning_country_percentage, 1)
    #print(highest_earning_country_percentage)

    #round(highest_earning_country_percentage)
    #print(highest_earning_country_percentage)


     #b = df[(df['hours-per-week'] == 1) & (df['salary'] == '>50K')].shape[0] / num_min_workers * 100
# Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df["salary"] == ">50K") & (df["native-country"] == "India")]["occupation"].value_counts().index[0]
    print(top_IN_occupation)

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
        'highest_earning_country_percentage': highest_earning_country_percentage,

        'top_IN_occupation': top_IN_occupation
    }


calculate_demographic_data()