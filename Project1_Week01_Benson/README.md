# Week 1 - Project Benson
## Optimizing street placement of non-profit volunteers for outreach effort

## _Team Turnstile Hoppers_. :  Gretta, Shweta, Alex, Steve

This was a team project designed to introduce the students to a "real world"* data science problem, develop knowledge about the Python ```pandas``` database and ```matplotlib``` plotting modules, and foster good habits in communication and in working within a group. Each 4-student team was tasked with helping a hypothetical non-profit organization, Women Tech Women Yes, optimize the placement of their volunteers at subway stations around New York City. The volunteers intend to canvas passersby at the subway entrances to promote an upcoming gala event and to build awareness of their organization. We were instructed to apply our formidable data science skills on a publically available data set from the Metropolitan Transportation Authority (MTA) that provides information about usage of all the NYC subway stations. We were also encouraged to use other sources of data, and any tools we chose as long as we used Python pandas and matplotlib or seaborn. The culimination of the project was a 12-minute presentation describing each team's analytical approach and final results.

My team took the following approach with the data analysis:
1. Focused on the 3 Spring months preceding the Summer gala
2. Transformed turnstile counter values, available for every turnstile unit at every MTA station listed in four-hour periods, into number of people passing through a subway station in the 3-month period.
3. Examined day-of-week trends in the turnstile data.
4. Included information about local technology companies and universities as a proxy for greater percentages of women and tech-involved individuals who may be especially receptive to the WTWY outreach efforts.
5. Included information from WalkScore.com to identify which stations may have larger populations of non-subway riders walking past the subway entrances.
6. Included demographic information from the U.S. Census on local tech-centered companies and residences, as a way to identify affluent zip code regions that might have a larger impact on the WTWY fundraising and outreach efforts.
7. Calculated a final "Benson Score", summing the four normalized scores for the turnstile, technology, walking, and census data.

The final results of our project are detailed in the .pdf file "Benson Project Presentation". In summary, we recommended five subway stations for placing WTWY volunteers: Grand Central at 42nd St, World Trade Center at Cortlandt St, 34th St at Herald Sq., Union Square and 14th St, and Penn Station at 34th St. For future analysis, we suggested a weighting scheme to refine how the four scores were combined to achieve the final score, a better way to report ridership numbers for stations with multiple entrances, employment of more technology companies and schools, and use of more granular demographic data from the Census tables. 


*Attach my putting _real world_ in quotes with as much irony as you'd like.

_Did you know?_  This project was named for Olivia Benson, one of the lead detectives in the hit TV show "Law & Order: Special Victims Unit".
