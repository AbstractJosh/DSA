# DSA210 Project Ulukan Keskin
# Mental State Effects on Gameplay and Strategy

## **Project Goal and Idea**
This project evaluates my gameplay statistics and mental state while playing Valorant. The goal is to analyze trends, identify areas for improvement, and understand the relationship between gameplay performance, mental state, and strategic decisions. The project also logs my improvement over time (if there is any).

## **Dataset**
I have been collecting gameplay footage for 3 years. but since a student's mental state cycles every semester or so, i will be condensing my data set to the last 3-4 months.
##
The dataset includes self-collected video files in the form of mp4 files and additional performance metrics from

**https://tracker.gg/valorant/profile/riot/Akemsss%237421/overview**

as data from my Valorant matches. Key attributes tracked for each game:

- **Performance Metrics**: 
  - Kills
  - Deaths
  - Assists
  - ACS (Average Combat Score)
  - Aggressiveness (First Kills & Deaths in the round)
- **Mental State / Decision Making**: Self-reported indicators such as fatigue, focus, or mood.
  - Aggressiveness (First Kills & Deaths in the round)
  - Willingness to communicate
  - Anger

## **Plan**
1. **Data Collection**: 
   - Utilize recorded gameplay to extract match details and performance metrics.
   - Utilize **tracker.gg** to more easily reach my perfomance metrics.
   - Supplement with self-reported mental state data for a holistic dataset.
2. **Data Processing**: 
   - Process gameplay recordings to ensure accurate data capture.
   - Structure the dataset into a usable format
3. **Analysis and Visualization**:
   - Create performance graphs (e.g., kills, deaths, and assists over time).
   - Analyze agent/map combinations with the highest individual performance.
   - Explore the relationship between subjective mood and gameplay performance.
   - Integrate video analysis to identify patterns, strategies, or errors.
4. **Insights and Recommendations**: 
   - Summarize findings and propose ways to improve gameplay performance and maintain focus.
   - Highlight strategies or agents that optimize performance under specific mental states.

## **Possible Limitations and Future Plans**
### **Limitations**
1. **Self-Reported Mental State Data**: Subjective assessments of mood and focus may not always be accurate and could introduce bias.
2. **Sample Size**: The dataset depends on the number of matches recorded, which may not be large enough for statistically significant results.
3. **Context Dependency**: Other factors (e.g., teammate performance, internet connection quality) that affect gameplay may not be captured.
4. **Manual Data Entry**: Extracting data from recorded gameplay may be time-intensive and prone to human error. Also tracker.gg has protection systems against web-scraping scripts so that is not an option.


### **Future Plans**
1. Automate the extraction of gameplay data using APIs or tools like Blitz or Overwolf.
2. Explore machine learning models to predict performance based on historical data and mental state.
3. Expand the dataset to include different game modes and larger time periods for broader analysis.
4. Develop a dashboard for real-time performance tracking and strategy recommendations.
5. Collaborate with other players to gather diverse datasets and validate findings.

# Findings Over Two Months of Playtime
## **Dataset**
The dataset includes:
- Self-reported mental state metrics (e.g., fatigue, focus, mood) per game.
- Performance statistics retrieved from **tracker.gg** and gameplay footage:
  - **Average Combat Score (ACS)**
  - **Kills/Deaths/Assists (KDA)**
  - **First Kill/First Death Aggressiveness**
  - Other contextual metrics.

The dataset spans two months, ensuring focus on a manageable and relevant period for analysis.

## **Scripts Overview**
### **Skill Level Consistency**
- **acsOverTime.py**
  - Analyzes Average Combat Score (ACS) over time.
  - Demonstrates that ACS remained stable during the experiment, ensuring reliable results.

    ![image](https://github.com/user-attachments/assets/757b489c-1351-4bb2-99df-7aa85df4dbb6)
    
- **kdaOverTime.py**
  - Tracks the Kill/Death/Assist ratio over time.
  - Confirms that there were no significant improvements or declines in skill level.
 
    ![image](https://github.com/user-attachments/assets/f6aa7b62-5d1e-4ad3-afaf-87339988d8a4)
    

### **Findings and Visualizations**
- **ACS_Agression_Scatter.py**
  - Investigates the relationship between player aggression (first kills + first deaths) and ACS.
  - Findings: Aggression positively correlates with ACS, emphasizing the impact of confident decision-making on performance.
    ![image](https://github.com/user-attachments/assets/71a7472a-ae37-4aec-8c89-3451c18a0ad9)
- **mental_firstEngagementViolin.py**
  - Visualizes the success rate of first engagements against mental state scores using violin plots.
  - Findings: Optimal mental states lead to higher first engagement success rates.
 
    ![image](https://github.com/user-attachments/assets/99b738e7-9775-4735-8ea7-1d6074513209)

    
- **mental_scoreHistogram.py**
  - Displays the distribution of mental state scores throughout the experiment.
  - Findings: Most games were played in a medium-to-high mental state range, avoiding outliers.

    ![image](https://github.com/user-attachments/assets/b07f56fb-addc-4c3c-bfaf-fdcda850bda5)
 
- **MentalState_on_Agression.py**
  - Examines how mental state influences aggression levels (first kills + first deaths).
  - Findings: High mental states correlate with increased aggression, suggesting confidence and decisiveness.
  
  ![image](https://github.com/user-attachments/assets/d584eee2-a47f-4cba-9c1b-c2824cb52f27)


## **Insights and Conclusions**
1. **Mental State Consistency**: Mental state is a reliable predictor of gameplay performance, particularly for metrics like aggression and first engagement success.
2. **Optimal Performance Zone**: Players perform best when maintaining a balanced mental state, avoiding extremes of fatigue or overexcitement.
3. **Aggression vs. Performance**: Aggressive playstyles yield better ACS but require a confident and focused mental state.

## **Limitations and Future Work**
### Limitations
1. **Subjectivity**: Self-reported mental state data introduces potential biases.
2. **External Factors**: Gameplay variables like teammate performance and network conditions were not controlled.

### Future Plans
1. Automate data collection using APIs to minimize manual errors.
2. Expand the dataset to include multiple players for more generalized insights.
3. Develop predictive models to provide real-time recommendations for performance improvement.
4. Create a dashboard for tracking gameplay and mental state metrics in real-time.

---

