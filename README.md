# Human Resources
In this project, I looked at human resources data. My primary goal was to find trends that relate to employee termination. I cleaned the data and created additional variables to use for better exploratory data analysis; I created a data pipeline to transfer the cleaned data to a SQL relational database; I used Pandas, Matplotlib, and Seaborn to conduct my EDA; and I ran the data through a SVC machine learning model to predict employee termination with an accuracy of 0.73%.

General Findings:
- Overall:
  -  Most people tend to be white, single or married, and a US citizen.
  -  Production is by far the most common department.
  -  Indeed and LinkedIn are the most common recruitment channels.
  -  Most people are not assigned 'Special Projects', but if they are assigned any special projects it tends to be for 5-6 times.
  -  There seems to be a strong, positive correlation (0.51) between Salary and Special Projects Count.
  -  There seems to be a strong, negative correlation (-0.59) between Engagement and Days Late Last 30.
  -  The Absences variable shows a Bimodal distribution.

- Pros:
    - Most people Fully Meet their performance requirements.
    - Very few people are below a 3 in employee satisfaction.
    - Most people have not been late in the last 30 days.
    - Simpson's Diversity Index shows that the company has a 56.5% diversity ratio, which is quite good.
  
- Cons:
    - 33.2% of employees are terminated. This number seems to be quite high.
    - There is a relatively high number of people who quit/resign from their position.

More Specific Findings: 
- Low Absence VS High Absence:
  - Low Absent Samples tend to, on average:
    - Have lower salaries.
    - Score lower on EngagementSurvey.
    - Are less satisfied.
    - Conduct more Special Projects.
    - Have been late more often.
   - The performance score of those with high absence appears to be better than those with low absence.
   - High Absence population has higher rates of HispanicLatino and a higher termination rate.
   - Managers Webster Butler, John Smith, and Kelley Spirea have an unusually high number of high absences.

- Voluntary Termination:
  - Tended to have lower Salaries.
  - Were assigned less Special Projects.
  - About 50% of the people that voluntarily terminated did so because they found another position, were unhappy, or wanted more money. The other 50% resigned due to personal reasons unrelated to employee satisfaction.
  - Manager Amy Dunn had a very high number of voluntary terminations.

- Special Projects:
  - Those assigned Special Projects had significantly higher salaries.
  - Most Special Projects were within the IT/IS department.
  - Those assigned Special Projects had better Performance Scores.
  - Those assigned Special Projects scored higher on their Engagement Surveys.
 
Suggestions for Company:
- Taking a close look at Manager Amy Dunn, specifically looking as to why she has a high number of voluntary terminations, could produce valuable insight informing what to avoid to improve employee retention.
- Additionally, looking closer at the Managers that have a high number of Employee Absences could also be useful to optimizing company operations.
- Possibly looking into ways to assign more Special Projects, particularly to departments outside of IT/IS.
  - There appears to be a relationship between being assigned Special Projects and Employee Satisfaction/EngagementScore which, in turn, promotes employee retention.

Interesting Psychology Reading Material:
- This is a literature review looking at factors that have been found to increase employee retention. This review briefly describes 8 factors that contribute to employee retention. This is a great article to get a quick overview on retention strategies. It is also quite good in that you can take a deeper dive into any of the factors by visiting the studies that are referenced.
  - https://www.scirp.org/journal/paperinformation?paperid=66904
- This is another literature review. This one is looking solely at workplace diversity. This is a very in-depth article looking at what diversity does, how to manage diversity, and the future of diversity research. While I am a big advocate for diversity, I know that more diversity does not lead to a better work; this article touches on the good and the bad of diversity and talks about ways to optimize the workplace to get the most good with the least bad. Additionally, the section of future research can also inform possible strategies to improve workplace diversity and optimize its benefits.
  - https://www.annualreviews.org/content/journals/10.1146/annurev-orgpsych-012218-015243
 
Limitations of this Project:
- The dataset was very small. If I had a larger dataset, my EDA could have produced more findings with higher accuracy. I would have also been able to use a different machine learning model for (possibly) more accurate result.
- Not knowing what the company was also produced some limitations. Had I known which industry the data came from, I could have possibly thought of more interesting/targeted ways to look at the data.
