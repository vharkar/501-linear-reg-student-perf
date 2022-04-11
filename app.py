import dash
from dash import dcc,html, dash_table
from dash.dependencies import Input, Output, State

headings = ['Index', 'Education Level']
levels = [['0', 'No HS Diploma'],['1', 'High School Diploma'],['2', 'Bachelors Degree'],['3', 'Masters Degree'],['4', 'Doctoral Degree']]

########### Define your variables ######
myheading1='Predicting Student Performance in Post Covid Semesters'
image1='StudentPerf.jpeg'
tabtitle = 'Student Performance'
sourceurl = 'https://www.kaggle.com/datasets/dylanbollard/covid19-effect-on-grades-constructed-dataset'
githublink = 'https://github.com/vharkar/501-linear-reg-student-perf'


########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading1),
    html.Div([
        html.Img(src=app.get_asset_url(image1), style={'width': '30%', 'height': 'auto'}, className='four columns'),
        html.Div([
                html.H4('Student\'s Test Score is sum of Math, Reading & Writing Scores'),
                html.Div('Student had Covid:'),
                dcc.Input(id='HadCovid', value=0, type='number', min=0, max=1, step=1),
                html.Div('Household Income:'),
                dcc.Input(id='Income', value=60000, type='number', min=0, max=180000, step=10000),
                html.Div('Free Lunch Available:'),
                dcc.Input(id='Lunch', value=1, type='number', min=0, max=1, step=1),
                html.Div('Number of household computers:'),
                dcc.Input(id='Computers', value=1, type='number', min=0, max=5, step=1),
                html.Div('Mothers Education:'),
                dcc.Input(id='Med', value=1, type='number', min=0, max=4, step=1),
                html.Div('Fathers Education:'),
                dcc.Input(id='Fed', value=1, type='number', min=0, max=4, step=1),
                html.Div('Pre-Covid Score:'),
                dcc.Input(id='PreCovid', value=650, type='number', min=150, max=900, step=5),

            ], className='four columns'),
            html.Div([
                html.Button(children='Submit', id='submit-val', n_clicks=0,
                                style={
                                'background-color': 'red',
                                'color': 'white',
                                'margin-left': '5px',
                                'verticalAlign': 'center',
                                'horizontalAlign': 'center'}
                                ),
                html.H3('Predicted Post-Covid Test Score:'),
                html.Div(id='Results')
            ], className='four columns')
        ], className='twelve columns',
    ),
    html.Br(),
    html.Br(),
    html.Br(),
    html.H4('Regression Equation:'),
    html.Div('Predicted Score = (388.9461 Baseline) + (- 19.5318 * HadCovid) + (0.001 * Income) + ( 31.9678 * Lunch) + ( 2.4321 * Computers) + ( 12.1617 * Fed) + ( 10.8461 * Med) + ( 0.1636 * PreCovid)'),
    html.Br(),
    html.H4('Income Levels Table'),
    html.Div([
         html.Div([
           dash_table.DataTable(
              id='data_table',
              columns=[{
                  'name': headings[i],
                  'id': headings[i],
              } for i in range(2)],
              data=[
               {headings[i]: levels[j][i] for i in range(2)}
                for j in range(5)
              ]
           )
         ], className='two columns')
    ]),
    html.Br(),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

######### Define Callback
@app.callback(
    Output(component_id='Results', component_property='children'),
    Input(component_id='submit-val', component_property='n_clicks'),
    State(component_id='HadCovid', component_property='value'),
    State(component_id='Income', component_property='value'),
    State(component_id='Lunch', component_property='value'),
    State(component_id='Computers', component_property='value'),
    State(component_id='Fed', component_property='value'),
    State(component_id='Med', component_property='value'),
    State(component_id='PreCovid', component_property='value')
)
def ames_lr_function(clicks, HadCovid, Income, Lunch, Computers, Fed, Med, PreCovid):
    if clicks==0:
        return "waiting for inputs"
    else:
        y = 388.9461 + (- 19.5318 * HadCovid) + (0.001 * Income) + ( 31.9678 * Lunch) + ( 2.4321 * Computers) + ( 12.1617 * Fed) + ( 10.8461 * Med) + ( 0.1636 * PreCovid)
        return int(y)



############ Deploy
if __name__ == '__main__':
    app.run_server(debug=True)
