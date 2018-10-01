# Week 1 - Project Benson
## Optimizing street placement of non-profit volunteers for outreach effort

## _Team Turnstile Hoppers_. :  Gretta, Shweta, Alex, Steve
_Start Date: September 24, 2018_ &emsp; _Due Date: October 01, 2018_

This was a team project designed to introduce the students to exploring a real world data set, develop knowledge about the Python ```pandas``` database and ```matplotlib``` plotting modules, and foster good habits in communication and in working within a group. Each 4-student team was tasked with helping a hypothetical non-profit organization, Women Tech Women Yes, optimize the placement of their volunteers at subway stations around New York City. The volunteers intend to canvas passersby at the subway entrances to promote an upcoming gala event and to build awareness of their organization. We were instructed to apply our new but formidable data science skills on a publically available data set from the Metropolitan Transportation Authority (MTA) that provides information about usage of all the NYC subway stations. We were also encouraged to use other sources of data and other tools as long as we used Python pandas and matplotlib or seaborn. The culimination of the project was a 12-minute presentation describing each team's analytical approach and final recommendations for placement of the WTWY volunteers.

My team took the following approach with the data analysis:
1. Focused on the 3 spring months of 2018, as next year's gala will be in early summer. Our assumption was that 
2. Transformed turnstile counter values, available for every turnstile unit at every MTA station listed in four-hour periods, into number of people passing through a subway station in the 3-month period.
3. Examined day-of-week trends in the turnstile data.
4. Included information about local technology companies and universities as a proxy for greater percentages of women and tech-involved individuals who may be especially receptive to the WTWY outreach efforts.
5. Included information from WalkScore.com to identify which stations may have larger populations of non-subway riders walking past the subway entrances.
6. Included demographic information from the U.S. Census on local tech-centered companies and residences, as a way to identify affluent zip code regions that might have a larger impact on the WTWY fundraising and outreach efforts.
7. Calculated a final "Benson Score", summing the four normalized scores for the turnstile, technology, walking, and census data.

The repository Python code for these analytical steps, written by the respective team members but attributed to the team as a whole, can be found within the following Jupyter notebooks: [Turnstile Score]('Benson_pt1_TurnstileScore.ipynb'), [Tech Score](Benson_pt2_TechScore.ipynb), [Census Score](Benson_pt3_CensusScore.ipynb), [Walk Score](Benson_pt4_WalkScore.ipynb). These notebooks include annotations and graphical output documenting the analyses, and describe the specific data sets and tools utilized.

The final results of our project are described in [Benson Project Presentation.pdf](Project1_Week01_Benson/Benson Project Presentation.pdf). In summary, we recommended five subway stations for placing WTWY volunteers: Grand Central at 42nd St, World Trade Center at Cortlandt St, 34th St at Herald Sq., Union Square and 14th St, and Penn Station at 34th St.

![Total "Benson Score"](supporting_files/Total_Benson_Score.png')

For future analysis, we suggested a weighting scheme to refine how the four scores were combined to achieve the final score, a better way to report ridership numbers for stations with multiple entrances, employment of more technology companies and schools, and use of more granular demographic data from the Census tables. 


_Did you know?_  This project was named for Olivia Benson, one of the lead detectives in the hit TV show "Law & Order: Special Victims Unit".
