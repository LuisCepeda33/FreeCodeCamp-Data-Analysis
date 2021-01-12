import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.DataFrame(pd.read_csv("medical_examination.csv"))
pd.set_option('display.max_columns', None)
#print(df)


# Add 'overweight' column

df["height"] = df["height"] / 100
df['overweight'] = df["weight"] / (df["height"]**2)
# print(df.head())
df['overweight'] = [1 if x > 25 else 0 for x in df['overweight']]
#print(df.head())
# print(df.dtypes)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the
# value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = [0 if x == 1 else 1 for x in df['cholesterol']]
df['gluc'] = [0 if x == 1 else 1 for x in df['gluc']]
#print(df.head())


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco',
    # 'active', and 'overweight'.
    df_cat = df.melt(id_vars="cardio", value_vars=["cholesterol", "gluc",	"smoke", "alco", "active", "overweight"])
    #print(df_cat.head())
    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one
    # of the collumns for the catplot to work correctly.
    df_cat = pd.DataFrame(df_cat.groupby(["cardio",	"variable", "value"])["value"].count())
    df_cat.rename(columns={"value":"total"},inplace=True)
    df_cat.reset_index(inplace=True)
    #print(df_cat.head())

    # Draw the catplot with 'sns.catplot()'

    fig = sns.catplot(x="variable", y="total", data=df_cat, hue="value", kind="bar", col="cardio").fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))]
#    print(df_heat.head())
    # Calculate the correlation matrix
    corr = df_heat.corr(method="pearson")

    # Generate a mask for the upper triangle
    mask = np.triu(corr)
    print(mask)



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 12))

    # Draw the heatmap with 'sns.heatmap()'

    sns.heatmap(corr, linewidths=1, annot=True, square=True, mask=mask, fmt=".1f",  center=0.08, cbar_kws={"shrink": 0.5})

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig


draw_cat_plot()
draw_heat_map()