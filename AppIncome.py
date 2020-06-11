# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output
import pandas as pd

import plotly.express as px

data=([
	{'Diplome': 2018,'Formation': 'Universite','Grade': '2-Confirme','Fixe': 49000,'Id': 0,'Remuneration': 53000,'Variable': 4000},
 	{'Diplome': 2017,'Formation': 'ENSAI','Grade': '2-Confirme','Fixe': 49000,'Id': 1,'Remuneration': 54000,'Variable': 5000},
 	{'Diplome': 2018,'Formation': 'Ingenieur','Grade': '2-Confirme','Fixe': 50000,'Id': 2,'Remuneration': 54000,'Variable': 4000},
 	{'Diplome': 2018,'Formation': 'ENSAI','Grade': '2-Confirme','Fixe': 49000,'Id': 3,'Remuneration': 53000,'Variable': 4000},
 	{'Diplome': 2010,'Formation': 'Ingenieur','Grade': '3-Senior','Fixe': 58500,'Id': 4,'Remuneration': 60500,'Variable': 2000},
 	{'Diplome': 2013,'Formation': 'Ingenieur','Grade': '3-Senior','Fixe': 56000,'Id': 5,'Remuneration': 62000,'Variable': 6000},
 	{'Diplome': 2015,'Formation': 'Universite','Grade': '3-Senior','Fixe': 56000,'Id': 6,'Remuneration': 61000,'Variable': 5000},
 	{'Diplome': 2015,'Formation': 'ISFA','Grade': '3-Senior','Fixe': 57000,'Id': 7,'Remuneration': 62000,'Variable': 5000},
 	{'Diplome': 2016,'Formation': 'Universite','Grade': '1-Junior','Fixe': 45000,'Id': 8,'Remuneration': 49300,'Variable': 4300},
 	{'Diplome': 2016,'Formation': 'ENSAI','Grade': '2-Confirme','Fixe': 51000,'Id': 9,'Remuneration': 55000,'Variable': 4000},
 	{'Diplome': 2015,'Formation': 'Ingenieur','Grade': '2-Confirme','Fixe': 56000,'Id': 10,'Remuneration': 61000,'Variable': 5000},
 	{'Diplome': 2017,'Formation': 'Commerce','Grade': '2-Confirme','Fixe': 46000,'Id': 11,'Remuneration': 50000,'Variable': 4000},
 	{'Diplome': 2018,'Formation': 'Universite','Grade': '1-Junior','Fixe': 44000,'Id': 12,'Remuneration': 47000,'Variable': 3000},
 	{'Diplome': 2016,'Formation': 'ENSAI','Grade': '3-Senior','Fixe': 55000,'Id': 13,'Remuneration': 62000,'Variable': 7000},
 	{'Diplome': 2019,'Formation': 'Universite','Grade': '1-Junior','Fixe': 41000,'Id': 14,'Remuneration': 44000,'Variable': 3000},
 	{'Diplome': 2015,'Formation': 'ENSAI','Grade': '3-Senior','Fixe': 65000,'Id': 15,'Remuneration': 70000,'Variable': 5000},
	{'Diplome': 2018,'Formation': 'ENSAI','Grade': '1-Junior','Fixe': 45000,'Id': 16,'Remuneration': 48000,'Variable': 3000}
	])

df=pd.DataFrame(data)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
				html.Div([
					dcc.Dropdown(id='income-dd',options=[{'label':i,'value':i} for i in ['Fixe','Variable','Remuneration']],value='Remuneration'),
					dcc.RadioItems(
					id='radio-formation-or-grade',
		    		options=[{'label': 'Formation', 'value': 'Formation'},{'label': 'Grade', 'value': 'Grade'}],
		    		value='Formation',
		    		labelStyle={'display': 'inline-block','align':'center'})
				],className="rows "),
				html.Div([
					html.Div([dcc.Graph(id='income-scatter-formation')],className='five columns'),
					html.Div([dcc.Graph(id='income-scatter-grade')],className='five columns')
				],className="rows ")
			])

@app.callback(
	Output('income-scatter-formation', 'figure'),
	[Input('income-dd', 'value'),
	Input('radio-formation-or-grade','value')])
def set_scatter(rem,typ):

	figure={
            'data': [
                dict(
                    x=df[df[typ]==i]['Diplome'],
                    y=df[df[typ]==i][rem],
                    text=df[df[typ]==i]['Id'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df[typ].unique()
            ],
            'layout': dict(
                xaxis={'title': 'Année de diplome'},
                yaxis={'title': rem},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
	return figure

@app.callback(
	Output('income-scatter-grade', 'figure'),
	[Input('income-dd', 'value'),
	Input('radio-formation-or-grade','value')])
def set_scatter_grade(rem,typ):
	df1=df.sort_values(by='Grade')
	figure={
            'data': [
                dict(
                    x=df1[df1[typ]==i]['Grade'],
                    y=df1[df1[typ]==i][rem],
                    text=df1[df1[typ]==i]['Id'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df1[typ].unique()
            ],
            'layout': dict(
                xaxis={'title': 'Année de diplome'},
                yaxis={'title': rem},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
	return figure



if __name__ == '__main__':
    app.run_server(debug=True)