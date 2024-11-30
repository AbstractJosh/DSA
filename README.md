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
  - Aggressiveness (First Bloods)
- **Mental State / Decision Making**: Self-reported indicators such as fatigue, focus, or mood.
  - Aggressiveness (First Bloods)
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
4. **Manual Data Entry**: Extracting data from recorded gameplay may be time-intensive and prone to human error.

### **Future Plans**
1. Automate the extraction of gameplay data using APIs or tools like Blitz or Overwolf.
2. Explore machine learning models to predict performance based on historical data and mental state.
3. Expand the dataset to include different game modes and larger time periods for broader analysis.
4. Develop a dashboard for real-time performance tracking and strategy recommendations.
5. Collaborate with other players to gather diverse datasets and validate findings.
