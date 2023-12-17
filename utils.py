import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
from soccerplots.radar_chart import Radar
from prc import process_data
from features_meaning import dict_metric, type_of_stats
import plotly.subplots as sp
import plotly.graph_objects as go

stats_to_compare = {'FW': ['Gls', 'xG', 'xA', 'SCA', 'Sh', 'PassProg', 'AttPen', 'KP', 'PPA', 'Succ%', 'CPA', 'TacklesAtt3rd', 'Press'],
                    'WB': ['CrsPA', 'xA', 'SCA', 'PassAtt', 'Cmp%', 'PassProg', 'ProgCarries', 'Succ%', 'Tkl', 'TklW', 'Int', 'Blocks', 'Clr'],
                    'RB': ['CrsPA', 'xA', 'SCA', 'PassAtt', 'Cmp%', 'PassProg', 'ProgCarries', 'Succ%', 'Tkl', 'TklW', 'Int', 'Blocks', 'Clr'],
                    'LB': ['CrsPA', 'xA', 'SCA', 'PassAtt', 'Cmp%', 'PassProg', 'ProgCarries', 'Succ%', 'Tkl', 'TklW', 'Int', 'Blocks', 'Clr'],
                    'CB': ['PassAtt', 'Cmp%', 'PassProg', 'ProgCarries', 'Cmp%.3', 'Tkl', 'TklW', 'Int', 'Blocks', 'Clr'],
                    'DM': ['PassAtt', 'Cmp%', 'PassProg', 'PassFinThird', 'KP', 'ProgCarries', 'Tkl', 'TklW', 'Int', 'Blocks', 'Clr'],
                    'CM': ['npxG', 'xA', 'SCA', 'Sh', 'PassAtt', 'Cmp%', 'PassProg', 'PassFinThird', 'KP', 'ProgCarries', 'Succ%', 'CPA', 'Int', 'TklW', 'Blocks', 'TacklesMid3rd'],
                    'AM': ['Gls', 'xG', 'xA', 'SCA', 'Sh', 'PassAtt', 'Cmp%', 'PassProg', 'KP', 'ProgCarries', 'PPA', 'Succ%', 'CPA', 'AttPen', 'TacklesAtt3rd', 'Press'],
                    'LM': ['Gls', 'xG', 'xA', 'SCA', 'Sh', 'CrsPA', 'PassAtt', 'Cmp%', 'KP', 'ProgCarries', 'PPA', 'Succ%', 'CPA', 'Att', 'TacklesAtt3rd', 'Press'],
                    'RM': ['Gls', 'xG', 'xA', 'SCA', 'Sh', 'CrsPA', 'PassAtt', 'Cmp%', 'KP', 'ProgCarries', 'PPA', 'Succ%', 'CPA', 'Att', 'TacklesAtt3rd', 'Press'],
                    'RW': ['Gls', 'xG', 'xA', 'SCA', 'Sh', 'CrsPA', 'PassAtt', 'Cmp%', 'KP', 'ProgCarries', 'PPA', 'Succ%', 'CPA', 'Att', 'TacklesAtt3rd', 'Press'],
                    'LW': ['Gls', 'xG', 'xA', 'SCA', 'Sh', 'CrsPA', 'PassAtt', 'Cmp%', 'KP', 'ProgCarries', 'PPA', 'Succ%', 'CPA', 'Att', 'TacklesAtt3rd', 'Press']}


@st.cache_data
def load_data():
    # df = pd.read_csv('all_processed.csv')
    df = process_data()

    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    numerical_cols = numerical_cols[numerical_cols != 'Min']

    scaler = StandardScaler()
    scaled_df = df.copy()
    scaled_df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

    vector_embeddings = scaled_df[numerical_cols].values

    similarity_matrix = cosine_similarity(vector_embeddings)

    similarity_df = pd.DataFrame(similarity_matrix, index=scaled_df['Name'], columns=scaled_df['Name'])

    return df, scaled_df, similarity_df

def get_similar_players_cosine(df, similarity_df, player_name, top_n=10):
    similarity_scores = similarity_df[player_name]
    most_similar_players = similarity_scores.sort_values(ascending=False).head(top_n + 1)
    most_similar_players = most_similar_players[most_similar_players.index != player_name]

    similar_players_df = pd.DataFrame(most_similar_players).join(df.set_index('Name')[['Pos', 'Squad']])
    similar_players_df.reset_index(inplace=True)
    similar_players_df.columns = ['Name', 'Similarity', 'Position', 'Squad']
    similar_players_df.sort_values(by='Similarity', ascending=False, inplace=True)
    similar_players_df.reset_index(drop=True, inplace=True) 
    similar_players_df.index += 1

    return similar_players_df

def get_similar_players_knn(df, player_name, top_n=10):
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    numerical_cols = numerical_cols[numerical_cols != 'Min']

    scaler = StandardScaler()
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

    knn = NearestNeighbors(n_neighbors=top_n + 1, metric='euclidean')
    knn.fit(df[numerical_cols])

    player_index = df[df['Name'] == player_name].index[0]
    _, indices = knn.kneighbors(df.iloc[player_index][numerical_cols].values.reshape(1, -1))

    similar_players_df = df.iloc[indices[0][1:top_n+1]][['Name', 'Pos', 'Squad']]

    similar_players_df.reset_index(drop=True, inplace=True)

    similar_players_df.index += 1

    similar_players_df.columns = ['Name', 'Position', 'Squad']

    return similar_players_df

def compare_players(df, player1, player2):
    # positions_set = ast.literal_eval(df[df['Name'] == player1]['Pos'].values[0])
    # position = list(positions_set)[0]

    position = df[df['Name'] == player1]['Pos'].values[0][0]

    if position not in stats_to_compare:
        print(f"Position '{position}' is not available for comparison.")
        return None

    value1 = df[df['Name'] == player1][stats_to_compare[position]].values
    value2 = df[df['Name'] == player2][stats_to_compare[position]].values

    values = [value1[0], value2[0]]

    ranges = []
    for col in stats_to_compare[position]:
        # ranges.append([df[col].min(), df[col].max()])
        ranges.append([df[df['Pos'].str[0] == position][col].min(), df[df['Pos'].str[0] == position][col].max()])
        
    title = dict(
        title_name=player1 + ' - ' + position,
        title_color='#B6282F',
        subtitle_name=df[df['Name'] == player1]['Squad'].values[0],
        subtitle_color='#B6282F',
        title_name_2=player2 + ' - ' + position,
        title_color_2='#344D94',
        subtitle_name_2=df[df['Name'] == player2]['Squad'].values[0],
        subtitle_color_2='#344D94',
        title_fontsize=18,
        subtitle_fontsize=15,
    )

    radar = Radar()

    fig, ax = radar.plot_radar(ranges=ranges, params=stats_to_compare[position], values=values, 
                            radar_color=['#B6282F', '#344D94'], 
                            title=title,
                            compare=True)

    return fig

def plot_percentiles(df, player_name='Harry Kane'):

    player_row = df[df['Name'] == player_name]
    player_position = player_row['Pos'].values[0][0]
    same_position_players = df[df['Pos'].apply(lambda x: player_position in x)]

    df_temp = same_position_players.copy()

    # position = df[df['Name'] == player_name]['Pos'].values[0][0]
    lst_cols_pr = [col for col in df.columns if df[col].dtype == 'float64' and col != 'Min']

    for col in lst_cols_pr:
        df_temp[col] = df_temp[col].rank(pct=True)

    df_player_pr = df_temp[(df_temp['Name'] == player_name)]

    df_player_pr = df_player_pr[lst_cols_pr]

    df_player_pr_t = df_player_pr.T

    df_player_pr_t = df_player_pr_t.reset_index(drop=False)

    df_player_pr_t.columns = ['Stats', 'PR']

    dict_metrics = {k: dict_metric[k] for k in lst_cols_pr}

    df_player_pr_t['Metric'] = df_player_pr_t['Stats'].map(dict_metrics)

    df_player_pr_t

    passing_stats = type_of_stats['Passing']
    goal_stats = type_of_stats['Goal and Shot Creation']
    defensive_stats = type_of_stats['Defensive Actions']
    possession_stats = type_of_stats['Possession']
    summary_stats = type_of_stats['Summary']

    # Filter the DataFrame for each major type
    passing_df = df_player_pr_t[df_player_pr_t['Stats'].isin(passing_stats)]
    goal_df = df_player_pr_t[df_player_pr_t['Stats'].isin(goal_stats)]
    defensive_df = df_player_pr_t[df_player_pr_t['Stats'].isin(defensive_stats)]
    possession_df = df_player_pr_t[df_player_pr_t['Stats'].isin(possession_stats)]
    summary_df = df_player_pr_t[df_player_pr_t['Stats'].isin(summary_stats)]

    # Calculate the maximum number of features among all subplots
    # max_features = max(len(summary_stats), len(passing_stats), len(goal_stats), len(defensive_stats), len(possession_stats))

    # Calculate the width of the bars based on the maximum number of features
    bar_width = 0.03

    # row_heights=[0.5, 0.8, 0.8, 0.7, 0.8]

    # Add the subplots to the big plot with updated row_heights
    fig = sp.make_subplots(rows=5, cols=1, shared_xaxes=True, vertical_spacing=0.02, subplot_titles=('Summary Stats', 'Passing Stats', 'Goal and Shot Creation Stats', 'Defensive Action Stats', 'Possession Stats'))

    # Add the subplots to the big plot
    fig.add_trace(go.Bar(x=summary_df['PR'], y=summary_df['Metric'], orientation='h',
                        width=bar_width*len(summary_stats),
                        marker=dict(color=summary_df['PR'], coloraxis='coloraxis')), row=1, col=1)
    fig.add_trace(go.Bar(x=passing_df['PR'], y=passing_df['Metric'], orientation='h',
                        width=bar_width*len(passing_stats),
                        marker=dict(color=passing_df['PR'], coloraxis='coloraxis')), row=2, col=1)
    fig.add_trace(go.Bar(x=goal_df['PR'], y=goal_df['Metric'], orientation='h',
                        width=bar_width*len(goal_stats),
                        marker=dict(color=goal_df['PR'], coloraxis='coloraxis')), row=3, col=1)
    fig.add_trace(go.Bar(x=defensive_df['PR'], y=defensive_df['Metric'], orientation='h',
                        width=bar_width*len(defensive_stats),
                        marker=dict(color=defensive_df['PR'], coloraxis='coloraxis')), row=4, col=1)
    fig.add_trace(go.Bar(x=possession_df['PR'], y=possession_df['Metric'], orientation='h',
                        width=bar_width*len(possession_stats),
                        marker=dict(color=possession_df['PR'], coloraxis='coloraxis')), row=5, col=1)

    # Update the layout of the big plot
    fig.update_layout(
        height=3000,
        width=1000,
        coloraxis=dict(colorscale='RdYlGn', colorbar=dict(title='Percentile Rank')),
        bargap=0.05,
        bargroupgap=0.05,
        font=dict(
            family="Arial",
            size=14,
            color="black"
        )
    )

    for trace in fig['data']: 
        trace['showlegend'] = False

    fig.update_yaxes(automargin='left+right')

    return fig