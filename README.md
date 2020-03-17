## COVID-19 DATA API

This package makes **COVID-19** data available through python API. All the data are directy taken from the [CSSEGISandData-covi19](https://github.com/CSSEGISandData/COVID-19#2019-novel-coronavirus-covid-19-2019-ncov-data-repository-by-johns-hopkins-csse) with the below mentioned data sources. There are several methods to extract the statistics and counts for the coutry or province.

## Installation:
#### PyPI:

#### GitHub:
  * Clone this repo.
  * pip install -r requirements.txt
  * pip install covid

## Usage Instructuions:

#### Initialising the instance/api:
```
from covid.main import CovId19Data

api = CovId19Data(force=False)
```
If force = True, every time object is instantiated new data is downloaded. Otherwise data will be refreshed after 24 hrs.

#### Method 1: Get stats:
```
res = api.get_stats()
```
```
{'confirmed': 181546, 'deaths': 7126, 'recovered': 78088}
```
#### Method 2: Get records for all the countries:
```
res = api.get_all_records_by_country()
```
```
{
'aruba': {   'confirmed': 2,
                 'deaths': 0,
                 'label': 'Aruba',
                 'last_updated': '2020-03-16 00:00:00',
                 'lat': '12.5211',
                 'long': '-69.9683',
                 'recovered': 0},
    'australia': {   'confirmed': 377,
                     'deaths': 3,
                     'label': 'Australia',
                     'last_updated': '2020-03-16 00:00:00',
                     'lat': '-33.8688',
                     'long': '151.2093',
                     'recovered': 23},
                     .
                     .
                     .
```

#### Method 3: Get records for all the state/Province:
```
res = api.get_all_records_by_provinces()
```
```
{
'tianjin': {   'confirmed': 136,
                   'country': 'China',
                   'deaths': 3,
                   'label': 'Tianjin',
                   'last_updated': '2020-03-16 00:00:00',
                   'lat': '39.3054',
                   'long': '117.323',
                   'recovered': 133},
    'tibet': {   'confirmed': 1,
                 'country': 'China',
                 'deaths': 0,
                 'label': 'Tibet',
                 'last_updated': '2020-03-16 00:00:00',
                 'lat': '31.6927',
                 'long': '88.0924',
                 'recovered': 1},
                 .
                 .
                 .
```

#### Method 4: Filter by Country:
To find all the countries availabe, plese use show_all_available_countries api.
```
res = api.filter_by_country("ireland")
```
```
{   'confirmed': 169,
    'deaths': 2,
    'label': 'Ireland',
    'last_updated': '2020-03-16 00:00:00',
    'lat': '53.1424',
    'long': '-7.6921',
    'recovered': 0}

```
#### Method 5: Filter by Province/State:
To find all the countries availabe, plese use show_all_available_regions api.
```
res = api.filter_by_province("British Columbia")
```
```
{   'confirmed': 103,
    'country': 'Canada',
    'deaths': 4,
    'label': 'British Columbia',
    'last_updated': '2020-03-16 00:00:00',
    'lat': '49.2827',
    'long': '-123.1207',
    'recovered': 4}

```
#### Method 6: Show all available Countries:
```
res = api.show_available_countries()
```
```
[   'Thailand',
    'Japan',
    'Singapore',
    'Nepal',
    'Malaysia',
    'Canada',
    'Australia',
    .
    .
    .
```

#### Method 7: Show all valiable Province/State:
```
res = api.show_available_regions()
```
```
[   'British Columbia',
    'New South Wales',
    'Victoria',
    'Queensland',
    'South Australia',
    'From Diamond Princess',
    'Western Australia',
    .
    .
    .
```

#### Method 8: Get history data for a given Country:
```
res = api.get_history_by_country("ireland")
```
Shows all the country metrics confirmed, recovered and deaths for the dates till the latest date.

#### Method 9: Get history data for a given State/Province:
```
res = api.get_history_by_province("British Columbia")
```
Shows all the state/province metrics confirmed, recovered and deaths for the dates till the latest date.

## Data Sources:
 
All used data sources [CSSEGISandData-covi19](https://github.com/CSSEGISandData/COVID-19#2019-novel-coronavirus-covid-19-2019-ncov-data-repository-by-johns-hopkins-csse).
  

## Copying and License
##### Terms and conditions of the data provider:
[CSSEGISandData-covi19](https://github.com/CSSEGISandData/COVID-19#2019-novel-coronavirus-covid-19-2019-ncov-data-repository-by-johns-hopkins-csse)

##### Terms and Condition of this repo:
License: [MIT](https://github.com/gtkChop/covid19/blob/master/LICENSE)

## Authors:

 * [gtkChop](https://github.com/gtkChop)
 * [vipin-tech](https://github.com/vipin-tech)

see also [contributors](https://github.com/gtkChop/covid19/graphs/contributors)


