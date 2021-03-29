The following is copied from the original [README](https://github.com/opportunityinsights/economictracker). 
---

# Overview 

The Opportunity Insights Economic Tracker (https://tracktherecovery.org) combines anonymized data from leading private companies – from credit card processors to payroll firms – to provide a real-time picture of indicators such as employment rates, consumer spending, and job postings across counties, industries, and income groups.

All of the data displayed on the Economic Tracker can be downloaded here. In collaboration with our data partners, we are making this data freely available in order to assist in efforts to inform the public, policymakers, and researchers about the real-time state of the economy and the effects of COVID-19.

Anyone is welcome to use this data; we simply we ask that you attribute our work by citing or linking to [the accompanying paper](https://opportunityinsights.org/wp-content/uploads/2020/05/tracker_paper.pdf) and the Economic Tracker at https://tracktherecovery.org.

> "How Did COVID-19 and Stabilization Policies Aﬀect Spending and Employment? A New Real-Time Economic Tracker Based on Private Sector Data", by Raj Chetty, John Friedman, Nathaniel Hendren, Michael Stepner, and the Opportunity Insights Team. June 2020. Available at: https://opportunityinsights.org/wp-content/uploads/2020/05/tracker_paper.pdf

# Data Dictionary

### Overview

Each data source and level of aggregation has a separate CSV, named using the following convention: *Data source* — *Geographic Level of Aggregation* — *Temporal Level of Aggregation*

Additionally, we have three files, **GeoIDs – State** and **GeoIDs – County** and **GeoIDs - City**, that provide information on geographic crosswalks and aggregation. These can be merged to any file sharing the same geographic level of aggregation using the geographic identifier. Additionally, **GeoIDs – County** indicates the commuting zone (CZ) and state that each county belongs to. The City-level data (listed under "Metro" on the tracker site) associates the largest cities in the United States with a representative county one-to-one (except in the case of New York City which includes the 5 boroughs).

A description of the columns in each file follows.

### GeoID File Descriptions

#### GeoIDs - State.csv

Geographic identifier: `statefips`

- `statename`: The name of the state.
- `stateabbrev`: The 2-letter state abbreviation.
- `state_pop2019`: The population of the state in 2019, from Census Bureau estimates.

#### GeoIDs - County.csv

Geographic identifier: `countyfips`

- `countyname`: The name of the county.
- `cz`: The numeric identifier of the commuting zone (CZ) in which the county is contained.
- `czname`: The name of the commuting zone (CZ) in which the county is contained.
- `statename`: The name of the state in which the county is contained.
- `statefips`: The fips code of the state in which the county is contained.
- `stateabbrev`: The 2-letter abbreviation of the state in which the county is contained.
- `county_pop2019`: The population of the county in 2019, from Census Bureau estimates.

#### GeoIDs - City.csv

Geographic identifier: `cityid`

- `cityname`: The name of the city.
- `stateabbrev`: The 2-letter abbreviation of the state in which the city is contained.
- `statename`: The name of the state in which the city is contained.
- `statefips`: The fips code of the state in which the city is contained.
- `city_pop2019`: The population of the city in 2019.

### ACS Demographic And Housing Estimates - Total Population - 2019

***Not a part of the original dataset.***   

**I added this data as a way to provide further context and comparison at the National level, particularly for demographic data. This data is from Census Bureau estimates.**

* `countrycode`: Foreign Trade country code for the US.
* `total_pop2019`: Total population for the US.
* `sexratio_total_pop2019`: Number of males per 100 females.

### File Descriptions


#### Affinity

Spending data from [Affinity Solutions](https://www.affinity.solutions).

- `spend_all`: Seasonally adjusted credit/debit card spending relative to January 4-31 2020 in all merchant category codes (MCC), 7 day moving average.
- `spend_acf`: Seasonally adjusted credit/debit card spending relative to January 4-31 2020 in accommodation and food service (ACF) MCCs, 7 day moving average, 7 day moving average.
- `spend_aer`: Seasonally adjusted credit/debit card spending relative to January 4-31 2020 in arts, entertainment, and recreation (AER) MCCs, 7 day moving average.
- `spend_apg`: Seasonally adjusted credit/debit card spending relative to January 4-31 2020 in general merchandise stores (GEN) and apparel and accessories (AAP) MCCs, 7 day moving average.
- `spend_grf`: Seasonally adjusted credit/debit card spending relative to January 4-31 2020 in grocery and food store (GRF) MCCs, 7 day moving average.
- `spend_hcs`: Seasonally adjusted credit/debit card spending relative to January 4-31 2020 in health care and social assistance (HCS) MCCs, 7 day moving average.
- `spend_tws`: Seasonally adjusted credit/debit card spending relative to January 4-31 2020 in transportation and warehousing (TWS) MCCs, 7 day moving average.
- `spend_all_inchigh`: Seasonally adjusted credit/debit card spending by consumers living in ZIP codes with high (top quartile) median income, relative to January 4-31 2020 in all merchant category codes (MCC), 7 day moving average.
- `spend_all_incmiddle`: Seasonally adjusted credit/debit card spending by consumers living in ZIP codes with middle (middle two quartiles) median income, relative to January 4-31 2020 in all merchant category codes (MCC), 7 day moving average.
- `spend_all_inclow`: Seasonally adjusted credit/debit card spending by consumers living in ZIP codes with low (bottom quartiles) median income, relative to January 4-31 2020 in all merchant category codes (MCC), 7 day moving average.

#### Burning Glass

Job postings data from [Burning Glass Technologies](https://www.burning-glass.com/).

- `bg_posts`: Average level of job postings relative to January 4-31 2020.
- `bg_posts_ss30`: Average level of job postings relative to January 4-31 2020 in manufacturing (NAICS supersector 30).
- `bg_posts_ss55`: Average level of job postings relative to January 4-31 2020 in financial activities (NAICS supersector 55).
- `bg_posts_ss60`: Average level of job postings relative to January 4-31 2020 in professional and business services (NAICS supersector 60).
- `bg_posts_ss65`: Average level of job postings relative to January 4-31 2020 in education and health services (NAICS supersector 65).
- `bg_posts_ss70`: Average level of job postings relative to January 4-31 2020 in leisure and hospitality (NAICS supersector 70).
- `bg_posts_jz1`: Average level of job postings relative to January 4-31 2020 requiring little/no preparation (ONET jobzone level 1).
- `bg_posts_jz2`: Average level of job postings relative to January 4-31 2020 requiring some preparation (ONET jobzone level 2).
- `bg_posts_jz3`: Average level of job postings relative to January 4-31 2020 requiring medium preparation (ONET jobzone level 3).
- `bg_posts_jz4`: Average level of job postings relative to January 4-31 2020 requiring considerable preparation (ONET jobzone level 4).
- `bg_posts_jz5`: Average level of job postings relative to January 4-31 2020 requiring extensive preparation (ONET jobzone level 5).
- `bg_posts_jzgrp12`: Average level of job postings relative to January 4-31 2020 requiring low preparation (ONET jobzone levels 1 and 2).
- `bg_posts_jzgrp345`: Average level of job postings relative to January 4-31 2020 requiring high preparation (ONET jobzone levels 3, 4 and 5).

#### COVID Cases

COVID case rates from the [New York Times COVID-19 repository](https://github.com/nytimes/covid-19-data).

- `case_rate`: Confirmed COVID-19 cases per 100,000 people, seven day moving average.
- `new_case_rate`: New confirmed COVID-19 cases per 100,000 people, seven day moving average.

#### COVID Deaths

COVID death rates from the [New York Times COVID-19 repository](https://github.com/nytimes/covid-19-data).

- `death_rate`: Confirmed COVID-19 deaths per 100,000 people, seven day moving average.
- `new_death_rate`: New confirmed COVID-19 deaths per 100,000 people, seven day moving average.

#### COVID Tests

COVID test rates from the [COVID Tracking Project](https://covidtracking.com/).

- `test_rate`: Confirmed COVID-19 tests per 100,000 people, seven day moving average.
- `new_test_rate`: New confirmed COVID-19 tests per 100,000 people, seven day moving average.

#### Google Mobility

GPS mobility data indexed to Jan 3-Feb 6 2020 from [Google COVID-19 Community Mobility Reports](https://www.google.com/covid19/mobility/).

- `gps_away_from_home`: Time spent outside of residential locations.
- `gps_retail_and_recreation`: Time spent at retail and recreation locations.
- `gps_grocery_and_pharmacy`: Time spent at grocery and pharmacy locations.
- `gps_parks`: Time spent at parks.
- `gps_transit_stations`: Time at inside transit stations.
- `gps_workplaces`: Time spent at work places.
- `gps_residential`: Time spent at residential locations.

#### Employment

Employment levels relative to Jan 4-31 from [Paychex](https://www.paychex.com/), [Earnin](https://www.earnin.com/), and [Intuit](https://www.intuit.com/).

- `emp_combined`: Employment level for all workers.
- `emp_combined_inclow`: Employment level for workers in the bottom quartile of the income distribution (incomes approximately under $27,000).
- `emp_combined_incmiddle`: Employment level for workers in the middle two quartiles of the income distribution (incomes approximately $27,000 to $60,000).
- `emp_combined_inchigh`: Employment level for workers in the top quartile of the income distribution (incomes approximately over $60,000).
- `emp_combined_ss40`: Employment level for workers in trade, transportation and utilities (NAICS supersector 40).
- `emp_combined_ss60`: Employment level for workers in professional and business services (NAICS supersector 60).
- `emp_combined_ss65`: Employment level for workers in education and health services (NAICS supersector 65).
- `emp_combined_ss70`: Employment level for workers in leisure and hospitality (NAICS supersector 70).

#### UI Claims

Unemployment insurance claims data from the [Department of Labor](https://oui.doleta.gov/unemploy/DataDashboard.asp) (national and state-level) and numerous individual state agencies (county-level).

- `initclaims_rate_regular`: Number of initial claims per 100 people in the 2019 labor force, Regular UI only
  - `initclaims_count_regular`: Count of initial claims, Regular UI only
- `initclaims_rate_pua`: Number of initial claims per 100 people in the 2019 labor force, PUA (Pandemic Unemployment Assistance) only
  - `initclaims_count_pua`: Count of initial claims, PUA (Pandemic Unemployment Assistance) only
- `initclaims_rate_combined`: Number of initial claims per 100 people in the 2019 labor force, combining Regular and PUA claims
  - `initclaims_count_combined`: Count of initial claims, combining Regular and PUA claims
- `contclaims_rate_regular`: Number of continued claims per 100 people in the 2019 labor force, Regular UI only
  - `contclaims_count_regular`: Count of continued claims, Regular UI only
- `contclaims_rate_pua`: Number of continued claims per 100 people in the 2019 labor force, PUA (Pandemic Unemployment Assistance) only
  - `contclaims_count_pua`: Count of continued claims, PUA (Pandemic Unemployment Assistance) only
- `contclaims_rate_peuc`: Number of continued claims per 100 people in the 2019 labor force, PEUC (Pandemic Emergency Unemployment Compensation) only
  - `contclaims_count_peuc`: Count of continued claims, PEUC (Pandemic Emergency Unemployment Compensation) only
- `contclaims_rate_combined`: Number of continued claims per 100 people in the 2019 labor force, combining Regular, PUA and PEUC claims
  - `contclaims_count_combined`: Count of continued claims, combining Regular, PUA and PEUC claims

#### Womply Merchants

Small business openings data from [Womply](https://www.womply.com/).

- `merchants_all`: Percent change in number of small businesses open calculated as a seven-day moving average seasonally adjusted and indexed to January 4-31 2020.
- `merchants_inchigh`: Percent change in number of small businesses open calculated as a seven-day moving average seasonally adjusted and indexed to January 4-31 2020 in high income (quartile 4 of median income) ZIP codes.
- `merchants_incmiddle`: Percent change in number of small businesses open calculated as a seven-day moving average seasonally adjusted and indexed to January 4-31 2020 in middle income (quartiles 2 & 3 of median income) ZIP codes.
- `merchants_inclow`: Percent change in number of small businesses open calculated as a seven-day moving average seasonally adjusted and indexed to January 4-31 2020 in low income (quartile 1 of median income) ZIP codes.
- `merchants_ss40`: Percent change in number of small businesses open calculated as a seven-day moving average seasonally adjusted and indexed to January 4-31 2020 in transportation (NAICS supersector 40).
- `merchants_ss65`: Percent change in number of small businesses open calculated as a seven-day moving average seasonally adjusted and indexed to January 4-31 2020 in education and health services (NAICS supersector 65).
- `merchants_ss70`: Percent change in number of small businesses open calculated as a seven-day moving average seasonally adjusted and indexed to January 4-31 2020 in leisure and hospitality (NAICS supersector 70).

#### Womply Revenue

Small business revenue data from [Womply](https://www.womply.com/).

- `revenue_all`: Percent change in net revenue for small businesses, calculated as a seven-day moving average, seasonally adjusted, and indexed to January 4-31 2020.
- `revenue_inchigh`: Percent change in net revenue for small businesses, calculated as a seven-day moving average, seasonally adjusted, and indexed to January 4-31 2020 in high income (quartile 4 of median income) zipcodes.
- `revenue_inclow`: Percent change in net revenue for small businesses, calculated as a seven-day moving average, seasonally adjusted, and indexed to January 4-31 2020 in low income (quartile 1 of median income) zipcodes.
- `revenue_incmiddle`: Percent change in net revenue for small businesses, calculated as a seven-day moving average, seasonally adjusted, and indexed to January 4-31 2020 in middle income (quartiles 2 & 3 of median income) zipcodes.
- `revenue_ss40`: Percent change in net revenue for small businesses, calculated as a seven-day moving average, seasonally adjusted, and indexed to January 4-31 2020 in transportation (NAICS supersector 40).
- `revenue_ss65`: Percent change in net revenue for small businesses, calculated as a seven-day moving average, seasonally adjusted, and indexed to January 4-31 2020 in education and health services (NAICS supersector 65).
- `revenue_ss70`: Percent change in net revenue for small businesses, calculated as a seven-day moving average, seasonally adjusted, and indexed to January 4-31 2020 in leisure and hospitality (NAICS supersector 70).


#### Zearn

Online math learning data from [Zearn](https://www.zearn.org/).

- `engagement`: Average level of students using platform relative to January 6-February 21 2020.
- `engagement_inclow`: Average level of students using platform relative to January 6-February 21 2020 for schools in the 25% of ZIP codes with the lowest median income.
- `engagement_incmiddle`: Average level of students using platform relative to January 6-February 21 2020 for schools in ZIP codes with median income between the 25th and 75th percentiles.
- `engagement_inchigh`: Average level of students using platform relative to January 6-February 21 2020 for schools in the 25% of ZIP codes with the highest median income.
- `badges`: Average level of students achievements earned (badges) on platform relative to January 6-February 21 2020.
- `badges_inclow`: Average level of students achievements earned (badges) on platform relative to January 6-February 21 2020 for schools in the 25% of ZIP codes with the lowest median income.
- `badges_incmiddle`: Average level of students achievements earned (badges) on platform relative to January 6-February 21 2020 for schools in ZIP codes with median income between the 25th and 75th percentiles.
- `badges_inchigh`: Average level of students achievements earned (badges) on platform relative to January 6-February 21 2020 for schools in the 25% of ZIP codes with the highest median income.

---  
# Data Documentation

### Overview


This document provides an overview of the sources and processing applied to each data series within the [Opportunity Insights Economic Tracker](https://tracktherecovery.org). The documentation is organized sequentially by series in the tracker, then broken down into categories of information describing each series, its source data, and our processing steps.

You can refer to additional documentation published by Opportunity Insights for complementary information:

* The Economic Tracker's **[Data Dictionary](https://github.com/OpportunityInsights/EconomicTracker)** lists each data file and variable available for public use, with short descriptions of the contents of each variable.
* The **[accompanying paper](https://opportunityinsights.org/wp-content/uploads/2020/05/tracker_paper.pdf)** provides detailed information about the methodology used to construct the series.

Please note that both the data and this data documentation is updated regularly and that the following information is subject to change.


# Data Series


## Consumer Spending  



**Summary:** Aggregated and anonymized purchase data from consumer credit and debit card spending. Spending is reported based on the ZIP code where the cardholder lives, not the ZIP code where transactions occurred.


**Data Source:** [Affinity Solutions](https://www.affinity.solutions/dataforgood)

**Update Frequency:** Weekly


**Date Range:** January 13th until the most recent date available.


**Data Frequency:** Data is daily until the final two weeks of the series, and the daily data is presented as a 7 day lookback moving average. For the final two weeks of the series, the data is weekly and presented as weekly data points.


**Index Period:** January 4th - January 31st


**Indexing Type:** Seasonally adjusted change since January 2020. Data is indexed in 2019 and 2020 as the change relative to the January index period. We then seasonally adjust by dividing year-over-year, which represents the difference between the change since January observed in 2020 compared to the change since January observed since 2019. We account for differences in the dates of federal holidays between 2019 and 2020 by shifting the 2019 reference data to align the holidays before performing the year-over-year division.


**Geographies:** National, State, County, Metro


**Breakdowns:**  



* *By Industry*. Industries are constructed by grouping merchant codes that are used by Affinity Solutions to identify the category of merchant and merchant activity.

  - Apparel and General Merchandise
  - Entertainment and Recreation
  - Grocery
  - Health Care
  - Resturants and Hotels
  - Transportation

* *By Consumer Zip Code Income*. Transactions are linked to zip codes where the consumer lives and zip codes are classified into income categories based on measurements of median household income and population provided by the American Community Survey (2014 - 2018).

  - High Income (median household income greater than $78,000 per year)
  - Middle Income (median household income between $46,000 per year and $78,000 per year)
  - Low Income (median household income less than $46,000 per year)


**Notes:** The raw data contains discontinuous breaks caused by entry or exit of credit card providers from the sample. In order to reliably identify and correct these breaks, we require at least 3 weeks of data. The most recent 3 weeks of data are therefore marked 'provisional' and are subject to non-negligible changes as new data is posted. For breaks found prior to the last 3 weeks, we correct for it using a method outlined in the [paper](https://opportunityinsights.org/wp-content/uploads/2020/05/tracker_paper.pdf). Otherwise we substitute the national mean for more recent breaks while we gather enough data to implement the corrections outlined in the [paper](https://opportunityinsights.org/wp-content/uploads/2020/05/tracker_paper.pdf). Additionally, at the county-level when are there more than one structural breaks the data is too noisy to correct for these breaks and counties with multiple breaks are dropped from the sample. Lastly, Affinity Solutions suppresses any cut of the data with fewer than five transactions. For more details refer to the accompanying [paper](https://opportunityinsights.org/wp-content/uploads/2020/05/tracker_paper.pdf).


## Small Business Revenue  



**Summary:** Small business transactions and revenue data aggregated from several credit card processors. Transactions and revenue are reported based on the ZIP code where the business is located.


**Data Source:** [Womply](https://www.womply.com)

**Update Frequency:** Weekly

**Date Range:** January 15th until the most recent date available.


**Data Frequency:** Daily, presented as a 7-day moving average


**Indexing Period:** January 4th - January 31st  



**Indexing Type:** Seasonally adjusted change since January 2020. Data is indexed in 2019 and 2020 as the change relative to the January index period. We then seasonally adjust by dividing year-over-year, which represents the difference between the change since January observed in 2020 compared to the change since January observed since 2019. We account for differences in the dates of federal holidays between 2019 and 2020 by shifting the 2019 reference data to align the holidays before performing the year-over-year division.



**Geographies:** National, State, County, Metro


**Breakdowns:**  



* *Industry*, by [NAICS supersector](https://www.bls.gov/sae/additional-resources/naics-supersectors-for-ces-program.htm).

  - Education and Health Services
  - Leisure and Hospitality
  - Retail and Transportation

* *Business Zip Code Income*. Transactions are linked to ZIP codes where the business is located and ZIP codes are classified into income categories based on measurements of median household income and population provided by the American Community Survey (2014 - 2018).

  - High Income (median household income greater than $78,000 per year)
  - Middle Income (median household income between $46,000 per year and $78,000 per year)
  - Low Income (median household income less than $46,000 per year)



**Notes:**

Small businesses are defined as those with annual revenue below the Small Business Administration's [thresholds](https://www.sba.gov/document/support--table-size-standards). Thresholds vary by 6 digit NAICS code ranging from a maximum number of employees between 100 to 1500 to be considered a small business depending on the industry.

County-level and metro-level data and breakdowns by High/Middle/Low income ZIP codes have been temporarily removed since the August 21st 2020 update due to revisions in the structure of the raw data we receive. We hope to add them back to the OI Economic Tracker soon.




## Small Businesses Open  



**Summary:** Number of small businesses open, as defined by having had at least one transaction in the previous 3 days.



**Data Source:** [Womply](https://www.womply.com)

**Update Frequency:** Weekly


**Date Range:** January 15th until the most recent date available.


**Data Frequency:** Daily, presented as a 7-day moving average


**Indexing Period:** January 4th - January 31st  



**Indexing Type:** Seasonally adjusted change since January 2020. Data is indexed in 2019 and 2020 as the change relative to the January index period. We then seasonally adjust by dividing year-over-year, which represents the difference between the change since January observed in 2020 compared to the change since January observed since 2019. We account for differences in the dates of federal holidays between 2019 and 2020 by shifting the 2019 reference data to align the holidays before performing the year-over-year division.

**Geographies:** National, State, County, Metro

We exclude counties with a total average revenue of less than $250,000 during
the indexing period (January 4-31). Additionally we omit spending categories for a small number of geographies that are extreme positive outliers, and we cap a small number of extreme negative outliers at 0 revenue.


**Breakdowns:**  



* *Industry*, by [NAICS supersector](https://www.bls.gov/sae/additional-resources/naics-supersectors-for-ces-program.htm).

  - Education and Health Services
  - Leisure and Hospitality
  - Retail and Transportation

* *Business Zip Code Income*. Transactions are linked to ZIP codes where the business is located and ZIP codes are classified into income categories based on measurements of median household income and population provided by the American Community Survey (2014 - 2018).

  - High Income (median household income greater than $78,000 per year)
  - Middle Income (median household income between $46,000 per year and $78,000 per year)
  - Low Income (median household income less than $46,000 per year)





**Notes:** Small businesses are defined as those with annual revenue below the Small Business Adminstration's [thresholds](https://www.sba.gov/document/support--table-size-standards). Thresholds vary by 6 digit NAICS code ranging from a maximum number of employees between 100 to 1500 to be considered a small business depending on the industry.

County-level and metro-level data and breakdowns by High/Middle/Low income ZIP codes have been temporarily removed since the August 21st 2020 update due to revisions in the structure of the raw data we receive. We hope to add them back to the OI Economic Tracker soon.


## Job Postings  



**Summary:** Weekly count of new job postings, sourced from over 40,000 online job boards. New job postings are defined as those that have not had a duplicate posting for at least 60 days prior.


**Data Source:** [Burning Glass Technologies](https://www.burning-glass.com)

**Update Frequency:** Weekly


**Date Range:** January 17th until the most recent date available.


**Data Frequency:** Weekly data points, with each week ending on Friday.


**Indexing Period:** January 4th - January 31st  



**Indexing Type:** Change relative to the January 2020 index period, not seasonally adjusted.


**Geographies:** National, State, Metro.


**Breakdowns:**  



* *Industry*, by [NAICS supersector](https://www.bls.gov/sae/additional-resources/naics-supersectors-for-ces-program.htm).

  - Educational and Health Services
  - Financial Activities and Services
  - Leisure and Hospitality
  - Manufactoring
  - Professional and Business Services

* *Education Requirement*, by [ONET Jobzone's Education Requirement Classification](https://www.onetonline.org/help/online/zones).

  - Minimal - Jobzone 1
  - Some - Jobzone 2
  - Moderate - Jobzone 3
  - Considerable - Jobzone 4
  - Extensive - Jobzone 5




## Employment  



**Summary:** Number of active employees, aggregating information from multiple data providers. This series is based on firm-level payroll data from Paychex and Intuit, worker-level data on employment and earnings from Earnin, and firm-level timesheet data from Kronos.  



**Data Source:** [Paychex](https://www.paychex.com/), [Intuit](https://www.intuit.com/), [Earnin](https://www.earnin.com/), [Kronos](https://www.kronos.com/)

**Update Frequency:** Weekly  

**Date Range:** January 15th until the most recent date available. The most recent date available for the full series depends on the combination of Paychex, Intuit and Earnin data. We extend the national trend for the Low Income employment subgroup by using Kronos timecard data to forecast beyond the end of the Paychex, Intuit and Earnin data.


**Data Frequency:** Daily, presented as a 7-day moving average


**Indexing Period:** January 4th - January 31st  



**Indexing Type:** Change relative to the January 2020 index period, not seasonally adjusted.  



**Geographies:** National, State, County, Metro

To prevent the introduction of new Paychex clients from artificially creating noise in the employment series overtime, in the underlying raw data we suppress county x quartile x industry x firm size cells that both (i) experience a large anomalous change in employment and (ii) made up a large share of given wage quartile's total employment at any point in a county in the current year. For more details on the specifics of these thresholds see the appendix of the [accompanying paper](https://opportunityinsights.org/wp-content/uploads/2020/05/tracker_paper.pdf).


**Breakdowns:**  



* *Wage*.

  - High Income (wage greater than $60,000 per year)
  - Middle Income (wage between $27,000 per year and $60,000 per year)
  - Low Income (wage less than $27,000 per year)

* *Industry*, by [NAICS supersector](https://www.bls.gov/sae/additional-resources/naics-supersectors-for-ces-program.htm).

  - Professional and Business Services
  - Education and Health Services
  - Retail and Transportation
  - Leisure and Hospitality



**Notes:**

* For low income workers, the change in employment is calculated using Paychex and Earnin data. For medium and high income workers, the change in employment is calculated using Paychex and Intuit data.

* In order to provide closer to real time data, we forecast the most recent employment measures beyond those available in the combined Earnin, Intuit, and Paychex dataset alone. To do so, we leverage two sources of higher frequency data: Kronos timestamp data and the Paychex weekly pay cycle sample. Using this higher frequency data we forecast more recent changes in employment using a distributed lag model, constructed by regressing a given week’s employment measure on the corresponding week’s Kronos measure, as well as its current and 3 previous lagged weeks’ Paychex weekly pay cycle measure.  For more details, please refer to the appendix of the accompanying [paper](https://opportunityinsights.org/wp-content/uploads/2020/05/tracker_paper.pdf)


## Unemployment Claims


**Summary:** Weekly unimployment insurance claims counts and rates (as a share of the 2019 labor force) for all states, as well as initial unemployment insurance claims for select counties where the data is publicly available.


**Data Source:** State-level and national statistics are reported by the U.S. Department of Labor.

The county-level series is only available for states whose respective state agencies publish county level data:

- Alabama: Alabama Department of Labor
- Arizona: Arizona Commerce Authority
- California: Employment Development Department of California
- Colorado: Colorado Department of Labor and Employment
- Georgia: Georgia Department of Labor
- Hawaii: Hawaii Department of Labor
- Idaho: Idaho Department of Labor
- Illinois: Illinois Department of Employment Security
- Indiana: Indiana Department of Workforce Development
- Iowa: State of Iowa
- Kentucky: Kentucky Center for Statistics
- Maryland: Maryland Department of Labor
- Massachusetts: Massachusetts Department of Unemployment Assistance
- Missouri: State of Missouri
- Nebraska: NEworks (Government of Nebraska)
- Nevada: Nevada Department of Employment; Training and Rehabilitation
- New York: New York State Department of Labor
- Ohio: Ohio Department of Job and Family Services
- Pennsylvania: Government of Pennsylvania
- Washington: Washington State Employment Security Department
- Wisconsin: Wisconsin Department of Workforce Development
- Wyoming: Wyoming Department of Workforce Services  

**Update Frequency:** Weekly (where available, in the case of county-level data)

**Date Range:** January 18th until the most recent date available.


**Data Frequency:** Weekly data points, with each week ending on Saturday.

Note that county-level claims in California, Georgia, Kentucky, and Illinois are reported at the monthly level and imputed to weekly data points for the county-level series. For more information about the imputation methodology, see the **[accompanying paper](https://opportunityinsights.org/wp-content/uploads/2020/05/tracker_paper.pdf)**

**Indexing Period:** No indexing applied, the published numbers directly report quantities.


**Indexing Type:** No indexing applied, the published numbers directly report quantities.


**Geographies:** National, State, County, Metro.


**Breakdowns:**  



* *Initial Claims*

  - Regular Claims
  - PUA Claims
  - Combined Claims

* *Continued Claims*

  - Regular Claims
  - PUA Claims
  - PEUC Claims
  - Combined Claims



**Notes:** Unemployment claims rates are calculated by dividing unemployment claims counts by the Bureau of Labor Statistics labor force estimates from 2019.

Under the CARES Act, all states provide 13 additional weeks of federally funded Pandemic Emergency Unemployment Assistance (PEUC) benefits to people who exhaust their regular state benefits. Under the Act, through the end of 2020, some people who exhaust all these benefits, and others who have lost their jobs for reasons arising from the pandemic but who are not normally eligible for UI in their state, are eligible for Pandemic Unemployment Assistance (PUA). "Combined Claims" are defined as the sum of regular, PUA and PEUC unemployment benefit claims.

## Online Math Participation  



**Summary:** Number of students using an online math curriculum, Zearn Math, among schools that already used Zearn Math in course instruction before the pandemic.


**Data Source:** [Zearn](https://about.zearn.org)  


**Update Frequency:** Weekly, except during summer and winter school breaks.


**Date Range:** January 6th to May 3rd 2020. The data series is not being updated during the summer. Updates will resume during the fall semester.


**Data Frequency:** Weekly data points, with each week ending on Sunday.


**Indexing Period:** January 6th - February 7th


**Indexing Type:** Change relative to the January 2020 index period, not seasonally adjusted.  



**Geographies:** National, States, County, Metro

To ensure privacy, the data we obtain are masked such that any county with fewer than two districts, fewer than three schools, or fewer than 50 students on average using Zearn Math is excluded. Where possible, masked county levels values are replaced by commuting zone means.   


**Breakdowns:**  



* *School Zip Code Income*. Schools are linked back to their ZIP code and ZIP codes are classified into income categories based on measurements of median household income and population provided by the American Community Survey (2014 - 2018).

  - High Income (median household income greater than $78,000 per year)
  - Middle Income (median household income between $46,000 per year and $78,000 per year)
  - Low Income (median household income less than $46,000 per year)





**Notes:** We exclude schools who did not have at least 5 students using Zearn Math for at least one week from January 6 to February 7.

## Student Progress in Math


**Summary:** Number of lessons completed by students each week using Zearn Math, among schools that already used Zearn Math in course instruction before the pandemic.

**Data Source:** [Zearn](https://about.zearn.org)  

**Update Frequency:** Weekly, except during summer and winter school breaks.

**Date Range:** January 6th to May 3rd 2020. The data series is not being updated during the summer. Updates will resume during the fall semester.

**Data Frequency:** Weekly data points, with each week ending on Sunday.

**Indexing Period:** January 6th - February 7th


**Indexing Type:** Change relative to the January 2020 index period, not seasonally adjusted.



**Geographies:** National, States, County, Metro

To ensure privacy, the data we obtain are masked such that any county with fewer than two districts, fewer than three schools, or fewer than 50 students on average using Zearn Math is excluded. Where possible, masked county levels values are replaced by commuting zone means.  



**Breakdowns:**  



* *School Zip Code Income*. Schools are linked back to their ZIP code and ZIP codes are classified into income categories based on measurements of median household income and population provided by the American Community Survey (2014 - 2018).

  - High Income (median household income greater than $78,000 per year)
  - Middle Income (median household income between $46,000 per year and $78,000 per year)
  - Low Income (median household income less than $46,000 per year)



**Notes:** We exclude schools who did not have at least 5 students using Zearn Math for at least one week from January 6 to February 7.


## COVID-19 Cases, Deaths and Tests


**Summary:** The daily count and rate per 100,000 people of confirmed COVID-19 cases, deaths or tests performed.


**Data Source:** [New York Times COVID-19 Data](https://github.com/nytimes/covid-19-data), [The COVID Tracking Project](https://covidtracking.com/).

**Update Frequency:** Daily

**Date Range:** January 22th until the most recent date available.


**Data Frequency:** Daily, presented as a 7-day moving average


**Indexing Period:** No indexing applied, the published numbers directly report quantities.


**Indexing Type:** No indexing applied, the published numbers directly report quantities.


**Geographies:** National, State, Country, Metro

Note that testing counts and rates are only available at the national and state level, not at the county or metro levels.


**Breakdowns:**  


* *New* Cases, Deaths, or Tests (presented as a 7-day moving average)
* *Total* Cases, Deaths, or Tests


## Time Outside Home


**Summary:** Time spent away from home, estimated using cellphone location data from Google users who have enabled the Location History setting.


**Data Source:** [Google COVID-19 Community Mobility Reports](https://www.google.com/covid19/mobility/), [American Time Use Survey](https://www.bls.gov/tus/)

**Update Frequency:** When released by Google, typically every 4-7 days.

**Date Range:** February 24th until the most recent date available.


**Data Frequency:** Daily  



**Indexing Period:** January 3rd to February 5th  



**Indexing Type:** Change relative to the January 2020 index period, not seasonally adjusted.



**Geographies:** National, State, County, Metro


**Breakdowns:**  


* Time Away From Home
* Retail and Restaurants
* Transit
* Parks
* Grocery
* Workplace




**Notes:** Google does not release data for geographies where their internal quality and privacy thresholds are not met. Therefore some geographic areas are omitted from the series for certain finer breakdowns while the release of others can be delayed while under review. When data is missing for 1 or 2 consecutive days we linearly interpolate the missing values and construct the 7 day moving average including these interpolated values. If data is missing for 3 or more consecutive days, the corresponding 7 day moving average is also recorded as missing whenever it overlaps with the missing data.

Time Away From Home is calculated by multiplying the mean time spent inside home from the American Time Use Survey by the percent change in time spent at residential locations reported by Google. For more information about this imputation, see the **[accompanying paper](https://opportunityinsights.org/wp-content/uploads/2020/05/tracker_paper.pdf)**.

## Policy Milestones  

**Summary:** Key state-level policy dates relevant for changes in other series trends and values. Includes start and end of stay at home order dates, public school closure dates, and non-essential business closure and re-opening dates.   

**Data Source(s):** New York Times, MCH Strategic Data, the Institute for Health Metrics and Evaluation, and local news and government sources.

**Update Frequency:** Monthly  

**Geographies:** State

---
# Privacy and Integrity Statement

Opportunity Insights is committed to the rigorous protection of individual and business privacy and fidelity to academic integrity through independent, non-partisan research and policy analysis.

The data reflected in the Opportunity Insights Economic Tracker are aggregated, de-identified, and do not reveal information about specific individuals, transactions, or businesses. Opportunity Insights is a leader in ​[developing privacy protection tools](https://opportunityinsights.org/paper/differential-privacy/)​ and methods, and all data releases follow rigorous protocols to protect individual privacy.

Each external organization that has contributed data to the Economic Tracker has done so with the explicit understanding that Opportunity Insights will use the contributed data in the Economic Tracker without precondition, subject to the data privacy standards set by data providers and any associated regulatory protections.

The Opportunity Insights Economic Tracker is a freely available public good. Opportunity Insights will never sell or monetize data and will not share the underlying data from the Economic Tracker with any third party (including any Opportunity Insights​​ [funder](https://opportunityinsights.org/team/)​).
