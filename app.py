
from flask import Flask, render_template, request
import pandas as pd
import json
import plotly
import plotly.express as px

import csv, re, operator
# from textblob import TextBlob

app = Flask(__name__)

person = {
    'first_name': 'Shiyu',
    'last_name' : 'Feng',
    'address' : 'China',
    'job': 'Web developer',
    'tel': '0678282923',
    'email': 'nohossat.tra@yahoo.com',
    'description' : 'Suite à une expérience internationale en développement web et dans le domaine des arts, l’impact de l’intelligence artificielle dans nos vies me surprend de jour en jour. \n Aujourd’hui, je souhaite changer de cap et comprendre les secrets que recèlent nos données. J’aimerais mettre à profit ces découvertes au service des entreprises/associations à dimension sociale.',
    'social_media' : [
        {
            'link': 'https://www.facebook.com/nono',
            'icon' : 'fa-facebook-f'
        },
        {
            'link': 'https://github.com/nono',
            'icon' : 'fa-github'
        },
        {
            'link': 'linkedin.com/in/nono',
            'icon' : 'fa-linkedin-in'
        },
        {
            'link': 'https://twitter.com/nono',
            'icon' : 'fa-twitter'
        }
    ],
    'img': 'img/img_nono.jpg',
    'experiences' : [
        {
            'title' : 'Web Developer',
            'company': 'AZULIK',
            'description' : 'Project manager and lead developer for several AZULIK websites.',
            'timeframe' : 'July 2018 - November 2019'
        },
        {
            'title' : 'Freelance Web Developer',
            'company': 'Independant',
            'description' : 'Create Wordpress websites for small and medium companies. ',
            'timeframe' : 'February 2017 - Present'
        },
        {
            'title' : 'Sharepoint Intern',
            'company': 'ALTEN',
            'description' : 'Help to manage a 600 Sharepoint sites platform (audit, migration to Sharepoint newer versions)',
            'timeframe' : 'October 2015 - October 2016'
        }
    ],
    'education' : [
        {
            'university': 'Paris Diderot',
            'degree': 'Projets informatiques et Startégies d\'entreprise (PISE)',
            'description' : 'Gestion de projets IT, Audit, Programmation',
            'mention' : 'Bien',
            'timeframe' : '2015 - 2016'
        },
        {
            'university': 'Paris Dauphine',
            'degree': 'Master en Management global',
            'description' : 'Fonctions supports (Marketing, Finance, Ressources Humaines, Comptabilité)',
            'mention' : 'Bien',
            'timeframe' : '2015'
        },
        {
            'university': 'Lycée Turgot - Paris Sorbonne',
            'degree': 'CPGE Economie & Gestion',
            'description' : 'Préparation au concours de l\'ENS Cachan, section Economie',
            'mention' : 'N/A',
            'timeframe' : '2010 - 2012'
        }
    ],
    'programming_languages' : {
        'HMTL' : ['fa-html5', '100'], 
        'CSS' : ['fa-css3-alt', '100'], 
        'SASS' : ['fa-sass', '90'], 
        'JS' : ['fa-js-square', '90'],
        'Wordpress' : ['fa-wordpress', '80'],
        'Python': ['fa-python', '70'],
        'Mongo DB' : ['fa-database', '60'],
        'MySQL' : ['fa-database', '60'],
        'NodeJS' : ['fa-node-js', '50']
    },
    'languages' : {'French' : 'Native', 'English' : 'Professional', 'Spanish' : 'Professional', 'Italian' : 'Limited Working Proficiency'},
    'interests' : ['Dance', 'Travel', 'Languages']
}

@app.route('/')
def cv(person=person):
    return render_template('index.html', person=person)




@app.route('/callback', methods=['POST', 'GET'])
def cb():
	return gm(request.args.get('data'))
   
@app.route('/chart')
def index():
	return render_template('chartsajax.html',  graphJSON=gm(),graphJSON1=gm1(),graphJSON2=gm2(),graphJSON3=gm3(),graphJSON4=gm4(),graphJSON5=gm5(),graphJSON6=gm6(),graphJSON7=gm7(),graphJSON8=gm8(),graphJSON9=gm9(),graphJSON10=gm10(),graphJSON11=gm11(),graphJSON12=gm12())

def gm(country='United Kingdom'):
    #1.人均寿命折线图
    df = px.data.gapminder()
    fig = px.line(df[df['country'] == country], x="year", y="gdpPercap")

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON


def gm1():
    iris = px.data.iris()

    fig=px.scatter(iris, x='sepal_width', y='sepal_length',
               color='species', marginal_y='histogram',
               marginal_x='box', trendline='ols')

    graphJSON1 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON1


def gm2():
    iris = px.data.iris()
    fig = px.scatter(iris, x='sepal_length', y='sepal_width')
    graphJSON2 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON2


def gm3():
    iris = px.data.iris()
    fig = px.scatter_matrix(iris, dimensions=["sepal_width", "sepal_length", "petal_width", "petal_length"],
                                               color="species")
    graphJSON3 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON3


def gm4():
    gapminder = px.data.gapminder()

    fig = px.scatter(gapminder,x="gdpPercap",y="lifeExp",size="pop",size_max=60,color="continent",hover_name="country",animation_frame="year",animation_group="country",log_x=True,range_x=[100,100000],range_y=[25,90],labels=dict(pop="Population",gdpPercap="GDP per Capita",lifeExp="Life Expectancy"))
    graphJSON4 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON4


def gm5():
    iris = px.data.iris()
    fig = px.density_heatmap(iris, x='sepal_width', y='sepal_length')

    graphJSON5 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON5


def gm6():
    tips = px.data.tips()
    fig = px.scatter(tips, x="total_bill", y="tip", facet_row="time", facet_col="day", color="smoker", trendline="ols",
                     category_orders={"day": ["Thur", "Fri", "Sat", "Sun"], "time": ["Lunch", "Dinner"]})
    graphJSON6 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON6


def gm7():
    gapminder = px.data.gapminder()

    fig = px.scatter(gapminder.query('year==2007'), x='gdpPercap', y='lifeExp', size='pop', color='continent',
                     hover_name='country', log_x=True, size_max=60)

    graphJSON7 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON7


def gm8():
    gapminder = px.data.gapminder()
    fig = px.scatter(gapminder, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
                     size="pop", color="continent", hover_name="country", facet_col="continent", log_x=True,
                     size_max=45, range_x=[100, 100000], range_y=[25, 90])
    graphJSON8 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON8


def gm9():
    gapminder = px.data.gapminder()
    fig = px.scatter_geo(gapminder, locations="iso_alpha", color="continent", hover_name="country", size="pop",
                         animation_frame="year", projection="natural earth")
    graphJSON9 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON9


def gm10():
    gapminder = px.data.gapminder()
    fig = px.choropleth(gapminder, locations="iso_alpha", color="lifeExp", hover_name="country", animation_frame="year",
                        range_color=[20, 80])
    graphJSON10 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON10


def gm11():
    election = px.data.election()
    fig = px.scatter_3d(election, x="Joly", y="Coderre", z="Bergeron", color="winner", size="total",
                        hover_name="district",
                        symbol="result", color_discrete_map={"Joly": "blue", "Bergeron": "green", "Coderre": "red"})
    graphJSON11 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON11


def gm12():
    election = px.data.election()
    fig = px.scatter_ternary(election, a="Joly", b="Coderre", c="Bergeron", color="winner", size="total",
                             hover_name="district", size_max=15,
                             color_discrete_map={"Joly": "blue", "Bergeron": "green", "Coderre": "red"})
    graphJSON12 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON12



@app.route('/senti')
def main():
	text = ""
	values = {"positive": 0, "negative": 0, "neutral": 0}

	with open('ask_politics.csv', 'rt') as csvfile:
		reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
		for idx, row in enumerate(reader):
			if idx > 0 and idx % 2000 == 0:
				break
			if  'text' in row:
				nolinkstext = re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', '', row['text'], flags=re.MULTILINE)
				text = nolinkstext

			blob = TextBlob(text)
			for sentence in blob.sentences:
				sentiment_value = sentence.sentiment.polarity
				if sentiment_value >= -0.1 and sentiment_value <= 0.1:
					values['neutral'] += 1
				elif sentiment_value < 0:
					values['negative'] += 1
				elif sentiment_value > 0:
					values['positive'] += 1

	values = sorted(values.items(), key=operator.itemgetter(1))
	top_ten = list(reversed(values))
	if len(top_ten) >= 11:
		top_ten = top_ten[1:11]
	else :
		top_ten = top_ten[0:len(top_ten)]

	top_ten_list_vals = []
	top_ten_list_labels = []
	for language in top_ten:
		top_ten_list_vals.append(language[1])
		top_ten_list_labels.append(language[0])

	graph_values = [{
					'labels': top_ten_list_labels,
					'values': top_ten_list_vals,
					'type': 'pie',
					'insidetextfont': {'color': '#FFFFFF',
										'size': '14',
										},
					'textfont': {'color': '#FFFFFF',
										'size': '14',
								},
					}]

	layout = {'title': '<b>意见挖掘</b>'}

	return render_template('sentiment.html', graph_values=graph_values, layout=layout)


if __name__ == '__main__':
  app.run(debug= True,port=5000,threaded=True)
