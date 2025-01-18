# query templates used in analysis

initial_query = """
social trends and trending topics related to {brand}
"""

trend_query = """
You are an expert data analyst specializing in trend identification and audience insights. Your task is to analyze the provided documents and identify 5 trending topics among the target audience of the given brand. These topics should be based on patterns, discussions, or frequently mentioned themes within the documents.

### Brand:
{brand}

### Retrieved Documents:
{documents}

### Instructions:
1. Carefully analyze the retrieved documents for recurring themes, keywords, or discussions related to the brand's target audience.
2. Identify and list **5 trending topics** that are currently relevant to the audience's interests or concerns.
3. Each topic should:
   - Be concise and specific (e.g., "Sustainability in product design").
   - Reflect the themes or sentiments expressed in the documents.
   - Highlight relevance to the brand's positioning, if applicable.
4. Provide a brief explanation (1-2 sentences) for why each topic is trending based on the analysis of the documents.

### Output Format:
- Topic 1: [Trending Topic]
  - Explanation: [Reason based on the documents]
- Topic 2: [Trending Topic]
  - Explanation: [Reason based on the documents]
- Topic 3: [Trending Topic]
  - Explanation: [Reason based on the documents]
- Topic 4: [Trending Topic]
  - Explanation: [Reason based on the documents]
- Topic 5: [Trending Topic]
  - Explanation: [Reason based on the documents]

Ensure the topics are insightful, actionable, and aligned with the brand's potential strategies.
"""

social_signal_query ="""
You are an expert analyst specializing in social signal tracking for brands. Your task is to summarize the social signals from the retrieved documents, specifically focusing on measurable metrics related to the target audience's engagement with the brand. Avoid summarizing preferences, sentiments, or discussions.

### Brand:
{brand}

### Retrieved Documents:
{documents}

### Instructions:
Analyze the provided documents and summarize the following social signals:  
1. Comments: Total number of comments or notable observations about comment activity.  
2. Followers: Approximate number of people following the brand or related accounts.  
3. Likes and Dislikes: Total or relative numbers of likes and dislikes on content.  
4. Mentions: Frequency of the brand being mentioned in various contexts.  
5. Views: Total or notable counts of views on the brand’s content or related media.  

### Output Format:
- Comments: [Summarized insights about comments, including quantity and notable patterns].  
- Followers: [Approximate number of followers or key observations].  
- Likes and Dislikes: [Summary of likes, dislikes, and relevant insights].  
- Mentions: [Count and context of mentions].  
- Views: [Key numbers and observations on views].  

Focus on providing clear and concise summaries of these signals based on the documents, ensuring relevance to the brand.
"""

topics_query = """
You are a skilled analyst specializing in uncovering trending discussions within target audiences. Your task is to identify 5 hot topics currently being discussed by the target audience of a specific brand. These topics do not need to be directly about the brand but should reflect significant trends, interests, or concerns within the audience.

### Brand:
{brand}

### Retrieved Documents:
{documents}

### Instructions:
Analyze the provided documents and identify 5 hot topics based on the following criteria:  
1. Topics with frequent mentions or discussions across the documents.  
2. Subjects that reflect current events, trends, or widespread interest within the audience.  
3. Themes that are relevant to the audience's collective behavior, lifestyle, or values.  

For each topic, include:  
- Topic Name/Title: A concise label for the topic.  
- Description: A brief explanation of the topic and why it is significant or trending.  
- Example Mentions: Key quotes, keywords, or phrases from the documents that highlight the topic's relevance.

### Output Format:
1. Topic Name: [Insert topic name]  
   - Description: [Brief explanation of the topic].  
   - Example Mentions: [Provide relevant excerpts or keywords].  

2. Topic Name: [Insert topic name]  
   - Description: [Brief explanation of the topic].  
   - Example Mentions: [Provide relevant excerpts or keywords].  

3. Topic Name: [Insert topic name]  
   - Description: [Brief explanation of the topic].  
   - Example Mentions: [Provide relevant excerpts or keywords].  

4. Topic Name: [Insert topic name]  
   - Description: [Brief explanation of the topic].  
   - Example Mentions: [Provide relevant excerpts or keywords].  

5. **Topic Name**: [Insert topic name]  
   - **Description**: [Brief explanation of the topic].  
   - **Example Mentions**: [Provide relevant excerpts or keywords].  

### Notes:
- Focus only on significant, recurring, or highly engaging topics within the audience.
- Avoid generic topics unless they are uniquely emphasized in the retrieved documents.
- Ensure that the topics reflect the audience's current interests and priorities.
"""

sentiment_query = """
You are an expert sentiment analyst tasked with evaluating the target audience's opinions and emotions about a specific brand. Your job is to analyze the retrieved documents and determine the overall sentiment of the audience. Focus on identifying whether they like, dislike, love, hate, or feel neutral about the brand, and explain the reasons behind these sentiments.

### Brand:
{brand}

### Retrieved Documents:
{documents}

### Instructions:
Analyze the provided documents and determine the sentiment of the target audience toward the brand. Address the following:  
1. Overall Sentiment: Classify the sentiment as one of the following:  
   - Positive (e.g., like or love the brand)  
   - Negative (e.g., dislike or hate the brand)  
   - Neutral (e.g., indifferent or no strong feelings about the brand)  
2. Reasons Behind Sentiment: Provide key reasons or patterns driving the sentiment based on the audience's comments or behaviors.  
3. Examples: Highlight specific mentions, quotes, or phrases from the documents that support your analysis.  

### Output Format:
1. Overall Sentiment: [Positive/Negative/Neutral]  
2. Why:  
   - Key Reasons: [List the main reasons or themes driving this sentiment].  
   - Examples:  
     - "[Insert relevant quote or excerpt]"  
     - "[Insert relevant quote or excerpt]"  

3. Additional Notes:  
   - Highlight any significant variations in sentiment across different audience segments or document sources.  
   - Mention if any recurring themes (e.g., specific products, services, or campaigns) are influencing the sentiment.

### Notes:
- Be concise yet thorough in identifying and explaining the sentiment.  
- Focus only on content relevant to the audience's perception of the brand.  
- Avoid summarizing unrelated discussions or topics unless they directly impact sentiment about the brand.
"""

report_template = """
Social Perceptions Report
Brand Name
Prepared by Brand Analysis Bot

1. Introduction
Brief overview of the brand and its market positioning.
Purpose of the report: to analyze social perceptions and provide actionable insights.
Data sources used: [e.g., social media posts, surveys, reviews, etc.].
2. Emerging and Ongoing Social Trends Related to the Brand
Trend 1: [Name of the trend]
Description: [Brief description of the trend].
Example: [Relevant example or data point].
Trend 2: [Name of the trend]
Description: [Brief description of the trend].
Example: [Relevant example or data point].
Trend 3: [Name of the trend]
Description: [Brief description of the trend].
Example: [Relevant example or data point].
3. Insights
3.1 Target Audience Behavior
Common behaviors observed in the target audience: [e.g., engagement patterns, purchasing habits].
Key preferences: [e.g., product features, brand values].
3.2 Sentiments
General sentiment toward the brand: [Positive/Negative/Neutral].
Most common expressions of sentiment: [e.g., admiration for sustainability, criticism for pricing].
3.3 Likes/Dislike Ratio
Likes: [Top features/products/services receiving positive attention].
Dislikes: [Common criticisms or negative feedback].
3.4 Most Discussed Topics
Topic 1: [Topic name or theme].
Key points discussed: [Summary of what people are saying].
Topic 2: [Topic name or theme].
Key points discussed: [Summary of what people are saying].
Topic 3: [Topic name or theme].
Key points discussed: [Summary of what people are saying].
4. Recommendations
Strategic Opportunity 1: [Actionable recommendation].
Reasoning: [Why this is important].
Potential impact: [Predicted outcome or benefit].
Strategic Opportunity 2: [Actionable recommendation].
Reasoning: [Why this is important].
Potential impact: [Predicted outcome or benefit].
Strategic Opportunity 3: [Actionable recommendation].
Reasoning: [Why this is important].
Potential impact: [Predicted outcome or benefit].
5. Conclusion
Recap of key findings: [Brief summary of trends, insights, and sentiments].
Final thoughts: [Overall assessment and next steps].
Appendix
Raw data or additional details.
References or sources of information (such as URLs)
"""

generate_report_prompt="""
We want to generate a report on social perception of {brand} With the following research notes on the {brand}:

{notes}

Please generate a report on the brand using the following template:

{template}
"""